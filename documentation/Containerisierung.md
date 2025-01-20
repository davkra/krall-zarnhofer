# Containerisierung

## Docker

Zur Containerisierung wurde ein [Dockerfile](../Dockerfile) erstellt, mit dessen Hilfe eine Python Umgebung eingerichtet wird (`python:3.10.12`) und benötigte Pip-Packages in einem Container installiert werden.

Mit folgendem Docker-Befehl kann ein Image erstellt werden, solange man sich im selben Verzeichnis wie das Dockerfile befindet. Dabei werden alle wichtigen Build-Tools installiert und benötigte Dateien in den Container kopiert:

```docker
docker build -t calculator .
```

Aus dem Image kann anschließend ein Container gebaut und gestartet werden:

```docker
docker run -it --name calculator --hostname calculator --rm calculator
```

Im Anschluss können beispielsweise die Python Tests durchgeführt werden:

```bash
python -m pytest
```

Mit `exit` kann der Container verlassen werden, wobei dieser im Anschluss zerstört wird.

### Docker ignore

Damit Docker gewisse Dateien ignoriert und nicht in das Image kopiert, kann eine `.dockerignore` Datei angelegt werden, welche ähnlich wie eine `.gitignore` Datei funktioniert.

## Docker in GitHub Actions

Für den GitHub workflow wird aktuell ein Ubuntu Base Image der Version 24.04 verwendet. Diese Information kann aus der [python-app.yml](../.github/workflows/python-app.yml) Datei entnommen werden.

```yml
    runs-on: ubuntu-24.04
```
