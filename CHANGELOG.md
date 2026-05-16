# Changelog
All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.2.0 - 2025-05-16
Backend rewrite with proper API layer.

### Changed
- Replaced multi-table Account inheritance with single-table + type field
- Replaced IncomeCategory/ExpenseCategory with single Category table + type field
- Added custom User model with JWT authentication
- Added Django REST Framework API with full CRUD endpoints
- Fixed `on_delete=SET_NULL` to `PROTECT` on financial record FKs
- Fixed `is_payed` → `is_paid`
- Migrated from `requirements.txt` to `uv` + `pyproject.toml`
- Updated Python 3.7 → 3.12, Django 3.2 → 5.1, Postgres → 16
- Added `django-cors-headers`, `django-filter`, `psycopg[binary]`, `gunicorn`
- Added pytest + factory_boy test suite (52 tests)
- Added test settings with SQLite (no Docker needed for local tests)
- Replaced Travis CI (removed)
- Updated Docker setup with uv and SELinux volume labels

### Removed
- Multi-table inheritance (CreditCard, SavingsAccount, Invest models)
- Separate IncomeCategory/ExpenseCategory models
- `requirements.txt`, `devenv.sh`, `make_env_codecov.py`, `.travis.yml`
- `backend/settings/example.py`
