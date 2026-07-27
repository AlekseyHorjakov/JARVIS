from pathlib import Path
import psycopg

BASE_DIR = Path(__file__).parent
CORE_DIR = BASE_DIR / "core"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "n8n",
    "user": "n8n",
    "password": ""
}

FILES = {
    "identity": "identity.md",
    "principles": "principles.md",
    "response_style": "response_style.md",
    "system_prompt": "system_prompt.md",
}


def deploy():

    conn = psycopg.connect(**DB_CONFIG)

    with conn:

        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS jarvis_config (
                    id SERIAL PRIMARY KEY,
                    config_key TEXT UNIQUE NOT NULL,
                    config_value TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT NOW()
                );
            """)

            for key, filename in FILES.items():

                path = CORE_DIR / filename

                if not path.exists():
                    print(f"❌ {filename} not found")
                    continue

                text = path.read_text(encoding="utf-8")

                cur.execute("""
                    INSERT INTO jarvis_config(config_key, config_value)
                    VALUES (%s,%s)
                    ON CONFLICT(config_key)
                    DO UPDATE SET
                        config_value = EXCLUDED.config_value,
                        updated_at = NOW();
                """, (key, text))

                print(f"✔ {key}")

    conn.close()

    print("\nDone.")


if __name__ == "__main__":
    deploy()