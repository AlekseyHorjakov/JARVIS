# JARVIS Main Workflow

## Назначение

Основной workflow проекта JARVIS.

Обеспечивает полный цикл обработки пользовательского запроса — от получения сообщения до формирования ответа и сохранения новой информации в долговременную память.

---

## Основные задачи

- получение сообщений из Telegram;
- преобразование входящих данных в единый внутренний формат;
- определение сценария обработки запроса;
- поиск релевантной информации в долговременной памяти;
- загрузка ядра JARVIS;
- формирование полного контекста;
- вызов необходимых инструментов;
- генерация ответа языковой моделью;
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

---

## Используемые компоненты

### Интерфейс

- Telegram Trigger

### Маршрутизация

- Input Gateway
- Intent Router

### Long-Term Memory

- Memory Classifier
- Resolve Ontology
- Generate Memory Embedding
- Save Memory
- Forget Memory
- Keyword Recall
- Vector Recall
- Merge Recall
- Smart Recall Filter

### AI Core

- Load JARVIS Core
- Build Context
- OpenAI Chat Model
- AI Agent

### Tools

- Memory Tool
- SearXNG Tool
- Docker Tool
- SSH Tool

### Инфраструктура

- PostgreSQL 17
- pgvector
- OpenAI API
- n8n

---

## Статус

🟢 Актуально для **JARVIS Core v1** с архитектурой **Long-Term Memory v2** и поддержкой **Tool Calling**.
