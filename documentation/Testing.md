# Testing

Als Testmöglichkeiten finden sich Unittest, pytests und End-To-End Tests.

## Pytest

Die Tests sind im Verzeichnis `tests/pytest/` definiert und können mit folgendem Befehl ausgeführt werden, solange `pytest` mit pip installiert wurde:

```bash
python -m pytest
```

Alternative kann das Skript `_test/run_pytest.sh` ausgeführt werden, welches einen Docker Container startet und dort die Tests ausführt.

## Unittest

Die Tests sind im Verzeichnis `tests/unit/` definiert und können mit folgendem Befehl ausgeführt werden:

```bash
python -m unittest discover -s tests/unit
```

Alternative kann das Skript `_test/run_unittest.sh` ausgeführt werden, welches einen Docker Container startet und dort die Tests ausführt.

## Integrationstest

Diese Tests sind im Verzeichnis `tests/integration/` definiert und können mit folgendem Befehl ausgeführt werden:

```bash
python -m unittest discover -s tests/integration
```

Alternative kann das Skript `_test/run_integrationtest.sh` ausgeführt werden, welches einen Docker Container startet und dort die Tests ausführt.

## End-to-End Test

Mit dem Skript `_test/run_node.sh` kann die Calculator App als Docker container gestartet werden. Dieser Container läuft intern am Port `3000`, welcher extern über den Port `8080` freigegeben wird. Über folgende Adresse kann auf die Calculator App zugegriffen werden: [http://localhost:8080](http://localhost:8080)
