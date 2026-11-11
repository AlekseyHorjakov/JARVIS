# JARVIS

Персональный AI-ассистент с долговременной памятью, модульной архитектурой и инструментами для выполнения задач.

JARVIS — портфельный проект на базе **n8n, PostgreSQL, pgvector и OpenAI API**. Он демонстрирует практический подход к созданию AI-продукта: объединение модели, данных, памяти, контекста и подключаемых инструментов в единую систему.

> **Статус:** JARVIS Core v1 реализован и проверен в работе через Telegram. Постоянно развёрнутая демо-версия сейчас не поддерживается: для неё требуется отдельный VPS.

## Что реализовано

- Telegram-интерфейс.
- Долговременная память с классификацией и атомарным хранением фактов.
- Семантическая онтология памяти и разрешение синонимов.
- Гибридный поиск: ключевые слова + embeddings + pgvector.
- Smart Recall Filter и автоматическая сборка контекста.
- AI Agent с Tool Calling.
- Инструменты: SearXNG, Docker Tool, SSH Tool.
- Модульная структура для расширения Skills.

## Архитектура обработки запроса

```text
Telegram
   │
   ▼
Input Gateway
   │
   ▼
Intent Router
   │
   ▼
Recall Memory
 ├── Keyword Search
 └── Vector Search
   │
   ▼
Merge Recall
   │
   ▼
Smart Recall Filter
   │
   ├────────────► Load JARVIS Core
   │
   ▼
Build Context
   │
   ▼
AI Agent
 ├── Memory Tool
 ├── SearXNG Tool
 ├── Docker Tool
 └── SSH Tool
   │
   ▼
Telegram Reply
```

## Стек

- **AI:** OpenAI API, GPT-4.1 Mini, OpenAI Embeddings
- **Автоматизация:** n8n
- **Данные:** PostgreSQL 17, pgvector
- **Интерфейс:** Telegram Bot API
- **Инфраструктура:** Docker, Caddy, Ubuntu Server
- **Инструменты:** SearXNG, Docker Tool, SSH Tool

## Структура репозитория

```text
JARVIS/
├── architecture/              # описание модулей
├── assets/screenshots/        # скриншоты
├── automation/n8n/workflows/  # экспорт workflow
├── core/                      # Identity, Principles, Response Style, System Prompt
├── docs/                      # архитектура, roadmap, соглашения
├── scripts/                   # служебные скрипты
├── skills/                    # описания Skills
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Запуск

1. Импортировать `automation/n8n/workflows/jarvis-core-v1.json` в n8n.
2. Создать в n8n собственные credentials:
   - Telegram Bot API;
   - OpenAI API;
   - PostgreSQL;
   - SearXNG;
   - HTTP Bearer Auth для embeddings.
3. Назначить credentials соответствующим узлам workflow.
4. Подготовить PostgreSQL, включить расширение `pgvector` и создать таблицы памяти.
5. Заполнить `jarvis_config` через `scripts/deploy_core.py`, указав параметры подключения через переменные окружения.

Пример переменных окружения — в `.env.example`.

## Безопасность

- В публичном workflow удалены credentials, webhook ID и служебные метаданные n8n.
- В репозитории нет API-ключей, паролей и токенов.
- Скрипт развёртывания читает параметры БД из переменных окружения.
- Перед публикацией своих изменений проверяйте экспорт workflow на наличие credentials и внутренних адресов.

## Ограничения

- Проект не является готовым SaaS-продуктом.
- Workflow требует собственной инфраструктуры и настройки credentials.
- Часть инструментов зависит от внешних сервисов и доступности сети.
- Постоянная демо-версия не поддерживается без отдельного VPS.

## Автор

**Алексей Хорьяков** — AI-инженер / инженер по AI-автоматизации.

GitHub: [AlekseyHorjakov](https://github.com/AlekseyHorjakov)

## Скриншоты

![Общий workflow](assets/screenshots/workflow-overview.png)

![Система памяти](assets/screenshots/memory-system.png)

![Telegram](assets/screenshots/telegram-demo.png)
