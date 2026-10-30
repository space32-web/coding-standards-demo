# coding-standards-demo

Учебный проект (учёт товаров на складе), в котором внедрены стандарты
кодирования Python.

## Применяемые стандарты

| Стандарт | Как применяется |
|---|---|
| PEP 8 | Стиль кода, проверка `flake8` |
| PEP 257 | Docstring у модулей, классов и функций |
| Conventional Commits | Формат сообщений коммитов (`feat:`, `fix:`, `docs:`, `style:`, `chore:`, `ci:`) |

## Автоматическая проверка

- `setup.cfg` — настройки flake8 (длина строки 79);
- `.pre-commit-config.yaml` — проверка перед каждым коммитом
  (`pip install pre-commit && pre-commit install`);
- `.github/workflows/lint.yml` — GitHub Actions запускает flake8 и pytest
  при каждом push и pull request.

## Запуск

```bash
pip install -r requirements-dev.txt
python inventory.py
flake8 .
pytest
```
