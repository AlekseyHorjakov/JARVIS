# Changelog

Все заметные изменения проекта JARVIS фиксируются в этом файле.

Формат основан на принципах Keep a Changelog.

---

# [1.0.0] - 2026-07-27

## Добавлено

### JARVIS Core

- реализовано ядро личности JARVIS;
- добавлены Identity, Principles, Response Style и System Prompt;
- ядро вынесено в PostgreSQL (`jarvis_config`);
- создан скрипт автоматического развертывания `deploy_core.py`.

### Long-Term Memory

- долговременная память пользователя;
- AI-классификация памяти;
- семантический поиск (pgvector);
- сохранение новой памяти;
- удаление памяти;
- контекстные ответы на основе памяти.

### Workflow

- реализован полный pipeline обработки сообщений;
- добавлена загрузка JARVIS Core перед каждым запросом;
- реализована сборка общего контекста (`Build Context`);
- реализован Recall памяти;
- добавлена фильтрация релевантной памяти.

### Infrastructure

- PostgreSQL 17;
- pgvector;
- Docker;
- n8n;
- Telegram Bot;
- OpenAI GPT-4.1 Mini.

---

## Статус

✅ JARVIS Core v1 завершён.