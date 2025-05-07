![Coverage](https://img.shields.io/badge/Coverage-89%25-brightgreen)

# Currency Converter (Python Terminal App)

This project is a terminal-based currency converter application built in Python. It allows users to convert between world currencies based on exchange rates relative to USD, update exchange rates, and persist data using a local JSON file.

## Features

- Convert from any supported currency to any other (via USD as intermediary)
- Interactive text-based UI
- Preloaded exchange rates from `currencies.json`
- Persistent updates to rates saved across sessions
- Custom exception handling
- Modular structure using clean, testable classes

## Testing and Coverage

This project includes unit, integration, and mock-based CLI tests using Python’s `unittest` framework.

- **Total Coverage:** 89%
- **All modules (`converter/`) at 100%**
- **All test files in `tests/`**
- **Test discovery path:** `tests/`

### Run tests & check coverage:

```bash
pip install coverage
coverage run -m unittest discover -s tests
coverage report -m
```

Optional HTML report:

```bash
coverage html
open htmlcov/index.html
```

## Automation

- **GitHub Actions:** Automatically runs tests and reports failures on push/PR via `.github/workflows/test.yml`
- **Dockerfile:** Project can be containerized and deployed easily

### Docker Run:

```bash
docker build -t currency-converter .
docker run -it --rm currency-converter
```

## Integration Tests

Includes integration tests in `test_integration.py`, verifying interactions between currency modules and conversion flows after updates, additions, and removals.

## Mock-Based CLI Tests

Simulate user input for `main.py` using `unittest.mock.patch`, verifying key flows and interaction behaviors.

## Project Structure

```
currency_converter/
├── main.py
├── currencies.json
├── Dockerfile
├── README.md
├── converter/
│   ├── currency.py
│   ├── registry.py
│   └── converter.py
├── tests/
│   ├── test_converter.py
│   ├── test_registry.py
│   ├── test_main_cli.py
│   └── test_integration.py
└── .github/
    └── workflows/
        └── test.yml
```


