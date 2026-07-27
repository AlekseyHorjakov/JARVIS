# JARVIS Main Workflow

## Назначение

Основной workflow проекта JARVIS.

Отвечает за полный цикл обработки сообщений пользователя:

- получение сообщений из Telegram;
- поиск релевантной памяти;
- загрузку ядра JARVIS;
- формирование общего контекста;
- генерацию ответа;
- сохранение новой памяти.

---

## Файл

```text
automation/n8n/workflows/jarvis-core-v1.json
```

---

## Архитектура

```text
Telegram
      │
      ▼
Generate Embedding
      │
      ▼
Recall Memory
      │
      ▼
Smart Recall Filter
      ├────────────► Load JARVIS Core
      │
      ▼
     Merge
      │
      ▼
 Build Context
      │
      ▼
 OpenAI Agent
      │
      ▼
Telegram Reply
```

---

## Используемые компоненты

- Telegram Trigger
- OpenAI Embeddings
- PostgreSQL + pgvector
- Smart Recall
- Load JARVIS Core
- Merge
- Build Context
- OpenAI Chat Model
- AI Agent
- Memory Classifier
- Save Memory

---

## Статус

🟢 Актуально для **JARVIS Core v1**.