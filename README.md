# JARVIS

> Модульная AI-платформа для создания персонального интеллектуального ассистента с долговременной памятью, собственной личностью и расширяемой архитектурой.

---

# О проекте

JARVIS — мой основной pet-проект, в котором я изучаю и применяю современные технологии искусственного интеллекта на практике.

Главная цель проекта — создать персонального AI-напарника, который способен:

- помнить пользователя;
- понимать контекст;
- обучаться новой информации;
- автоматизировать повседневные задачи;
- масштабироваться за счёт модульной архитектуры.

JARVIS разрабатывается как долгосрочный проект с прицелом на постоянное развитие новых модулей.

---

# Реализовано

## JARVIS Core v1

- собственная личность ассистента (Identity)
- набор принципов работы (Principles)
- стиль общения (Response Style)
- системное ядро (System Prompt)
- хранение ядра в PostgreSQL
- автоматическая загрузка ядра при каждом запросе

---

## Долговременная память

- сохранение новой информации
- AI-классификация памяти
- удаление воспоминаний
- семантический поиск (pgvector)
- релевантный Recall
- контекстные ответы с использованием памяти

---

## Автоматизация

- Telegram-интерфейс
- n8n Workflow
- PostgreSQL
- OpenAI API
- Docker

---

# Архитектура обработки запроса

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
        ├──────────────► Load JARVIS Core
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

# Скриншоты

## Общий Workflow

![Workflow](assets/screenshots/workflow-overview.png)

---

## Система долговременной памяти

![Memory](assets/screenshots/memory-system.png)

---

## Telegram

![Telegram](assets/screenshots/telegram-demo.png)

---

## PostgreSQL

![Database](assets/screenshots/user-memory.png)

---

# Используемые технологии

| Категория | Технологии |
|-----------|------------|
| AI | OpenAI GPT-4.1 Mini |
| Workflow | n8n |
| Векторная БД | PostgreSQL 17 + pgvector |
| Backend | JavaScript |
| Контейнеризация | Docker |
| Сервер | Ubuntu Server 24.04 |
| Reverse Proxy | Caddy |
| Контроль версий | Git + GitHub |

---

# Структура проекта

```text
JARVIS/

├── architecture/
├── assets/
├── automation/
│   └── n8n/
│       └── workflows/
├── config/
├── context/
├── core/
├── docker/
├── docs/
├── logs/
├── memory/
├── prompts/
├── scripts/
├── skills/
├── src/
├── storage/
├── tests/
└── tools/
```

---

# Roadmap

## Core

- [x] Personality
- [x] Long-term Memory
- [x] Semantic Recall
- [x] PostgreSQL Core
- [x] Telegram

## Следующие этапы

- Voice
- Vision
- MCP
- Web UI
- Multi-Agent
- AI Health
- AI Business
- Local LLM (Ollama)

---

# Статус проекта

🟢 **JARVIS Core v1 завершён.**

В настоящий момент проект включает:

- собственное AI-ядро;
- долговременную память;
- семантический поиск;
- хранение личности в PostgreSQL;
- автоматическую сборку контекста;
- Telegram-интерфейс.

Следующий этап разработки — расширение возможностей ассистента новыми модулями.

---

# Автор

**Алексей Хорьяков**

Системный администратор, развивающийся в направлении AI Engineering, автоматизации и разработки интеллектуальных ассистентов.