# Containerisierung

## Docker

Zur Containerisierung wurde ein [Dockerfile](../Dockerfile) erstellt, mit dessen Hilfe eine Python und Node Umgebung eingerichtet wird und benötigte Pip-Packages in einem Container installiert werden. Als Basis Image wird [alpine:latest](https://hub.docker.com/_/alpine/), welches für kompaktere Container sorgt.

Mit folgendem Docker-Befehl kann ein Image erstellt werden, solange man sich im selben Verzeichnis wie das Dockerfile befindet. Dabei werden alle wichtigen Build-Tools installiert und benötigte Dateien in den Container kopiert:

```docker
docker build -t calculator .
```

Aus dem Image kann anschließend ein Container gebaut und gestartet werden:

```docker
docker run -it --name calculator --hostname calculator --rm calculator
docker run --rm -it -p 3000:3000 --name calculator --hostname calculator calculator
```

Im Anschluss können beispielsweise die Python Tests durchgeführt werden,

```bash
python -m pytest
```

eine Python package erstellt werden,

```bash
python -b build
```

oder die Weboberfläche gestartet werden:

```bash
node app.js
```

Mit `exit` kann der Container verlassen werden, wobei dieser im Anschluss zerstört wird, da die Flag `--rm` verwendet wird.

### Docker ignore

Damit Docker gewisse Dateien ignoriert und nicht in das Image kopiert, kann eine `.dockerignore` Datei angelegt werden, welche ähnlich wie eine `.gitignore` Datei funktioniert.

## Docker in GitHub Actions

Für den GitHub workflow wird aktuell ein Ubuntu Base Image der Version 24.04 verwendet. Diese Information kann aus der [python-app.yml](../.github/workflows/python-app.yml) Datei entnommen werden.

```yml
    runs-on: ubuntu-24.04
```

## Referenzen

- [https://elliottback.medium.com/python-this-environment-is-externally-managed-error-and-docker-6062aac20a6e](https://elliottback.medium.com/python-this-environment-is-externally-managed-error-and-docker-6062aac20a6e)
- [https://stackoverflow.com/questions/68673221/warning-running-pip-as-the-root-user](https://stackoverflow.com/questions/68673221/warning-running-pip-as-the-root-user)
- [https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md](https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md)
- [https://stackoverflow.com/questions/14639001/command-not-working-as-expected-if-run-via-bin-sh-c](https://stackoverflow.com/questions/14639001/command-not-working-as-expected-if-run-via-bin-sh-c)
