# Automatisierung

## Projekt - Calculator

Kleine, einfache Taschenrechner Application geschrieben in Python.

### Calculator

Der Source Code und die Tests befinden sich im Verzeichnis `calculator`.

#### Kompilieren und Starten des Programs

```python
python calculator.py
```

#### Testen und Starten des Programs

Als Testprogramm wurde [pytest](https://docs.pytest.org/en/stable/) verwendet. Die Tests können auch lokal ausgeführt werden.

```python
python -m pytest
```

## GitHub Actions

Zu finden unter [`.github/workflows/python-app.yml`](../.github/workflows/python-app.yml).  
Als Vorlage wurde die GitHub Action `Python application` verwendet.

### Steps

Als Basis wird Ubuntu mit der Version 24.04 verwendet.

>*This workflow will install Python dependencies, run tests and lint with a single version of Python*

1. [Git checkout](https://github.com/actions/checkout/tree/v4/)
2. [setup-python](https://github.com/actions/setup-python/tree/v3/)
3. Installation der Python Abhängigkeiten mit [pip](https://pypi.org/project/pip/)
4. [Flake8](https://pypi.org/project/flake8/) benutzen, um Syntax oder Code Style Fehler zu finden
5. Tests mit [pytest](https://docs.pytest.org/en/stable/) durchführen
6. Python Programm starten
7. Package des Python Programms erstellen
8. Package auf GitHub bereitstellen, jedoch nur falls auf den `main`-Branch gepusht wird

## Referenzen

- [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)
- [https://github.com/davkra/krall-zarnhofer/actions](https://github.com/davkra/krall-zarnhofer/actions)
