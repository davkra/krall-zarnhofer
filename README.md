# TechDemo: Continuous Delivery Integration

David Krall  
Daniel Zarnhofer

---

> Das [GitLab Repository](https://git-iit.fh-joanneum.at/msd-contdel/techdemo-ws24/krall-zarnhofer) dieses Projekts ist nicht das Hauptrepository.  
> Das Hauptrepository befindet sich auf GitHub unter: [https://github.com/davkra/krall-zarnhofer](https://github.com/davkra/krall-zarnhofer) und wird [mit diesem Repository gespiegelt.](#voraussetzungen)

## Table of Contents

- [TechDemo: Continuous Delivery Integration](#techdemo-continuous-delivery-integration)
  - [Table of Contents](#table-of-contents)
  - [Checklist](#checklist)
  - [Einleitung](#einleitung)
  - [Ziel](#ziel)
  - [Voraussetzungen](#voraussetzungen)
    - [Branching Strategie](#branching-strategie)
  - [Usage](#usage)
  - [Tech Stack](#tech-stack)
  - [Pipeline-Dokumentation](#pipeline-dokumentation)

## Checklist

Für eine genauere Liste an Aufgaben und Zielen, bitte die [Checkliste](./CHECKLIST.md) öffnen. Diese dient als Grundlage für alle relevanten CD Aspekte, die in dieser Demo implementiert wurden.

## Einleitung

Dieses Repository dient als Vorlage für die TechDemo des Continuous Delivery (CD) Kurses. Der Fokus liegt auf der Integration von CD Prinzipien in existierende Software, anstatt neue Software von Neuem zu erstellen. Das Ziel ist eine Demonstration vom automatischen Builden, Testen und Ausliefern in einem Software Entwicklungs Szenario.

## Ziel

Das Hauptziel sind CD Praktiken zur Automatisierung von Prozessen, um einen besseren und effizienteren Software Development Lebenszyklus zu gewährleisten. Dazu zählen:

- Automatisierte Builds mit Build Tools.
- Automatisierte Tests mit Unit, Integration, und End-to-End tests.
- Continuous deployment auf eine Produktiv System.

## Voraussetzungen

Die folgende Software wird in diesem Projekt verwendet:

- **Git**: Versionskontrolle.
- **Python und Node.js**: Für die Entwicklung einer Calculator App.
- **Docker**: Zur Containerisierung.

Außerdem müssen sowohl das Haupt als auch das Spiegel Repository konfiguriert werden. Dies ist notwendig, falls Code Änderungen gepusht werden sollen.

```bash
# Mirror Repository
git remote set-url --add --push origin git@git-iit.fh-joanneum.at:msd-contdel/techdemo-ws24/krall-zarnhofer.git

# Main Repository
git remote set-url --add --push origin git@github.com:davkra/krall-zarnhofer.git
```

Diese Remotes benötigen SSH-Key zur Verbindung über SSH. Alternative können die Remotes auch via https hinzugefügt werden:

```bash
# Mirror Repository
git remote set-url --add --push origin https://git-iit.fh-joanneum.at/msd-contdel/techdemo-ws24/krall-zarnhofer.git

# Main Repository
git remote set-url --add --push origin https://github.com/davkra/krall-zarnhofer.git
```

Die beiden Skripte [gitsetup.sh](./gitsetup.sh) und [gitsetup.cmd](./gitsetup.cmd) (je nach Betriebssystem) können verwendet werden, um die Konfiguration durchzuführen, nachdem dieses geclont wurde.

### Branching Strategie

Als Branching Strategie bzw. Git Workflow wurde ein Trunked based flow gewählt. Dabei handelt es sich um einen main Branch, auf welchen alle Code Änderungen gepusht werden. Einzelne Feature Branches sollen möglichst rasch gemergt werden, damit eine CD Pipeline optimal genutzt werden kann.

## Usage

Bei dem Projekt handelt es sich um einen einfachen Taschenrechner, welcher in Python implementiert ist und anschließend mit Hilfe von JavaScript in einer Node Umgebung als Web-App läuft.

1. **Projekt Kompilieren und Starten**:

   ```bash
   ./_test/run_node.sh
   ```

   Alternative kann auch die DockerHub Version verwendet werden:

   ```bash
   docker run --rm -it --init -p 8080:3000 --name calculator --hostname calculator dkralledu/calculator sh -c 'npm start'
   ```

2. **Tests starten**:

   ```bash
   ./_test/run_<pytest|unittest|integrationtest>.sh
   ```

## Tech Stack

- **Programmiersprachen**: Python, JavaScript
- **Build Tools**: Pip, NPM.
- **Testing Frameworks**: pytest, unittest.
- **CI/CD**: GitHub Actions.

## Pipeline-Dokumentation

`.github/workflows/calculator.yml`:

Jobs: `test`, `build`, `deploy`

1. `test`
   - verwendet `ubuntu-24.04`
   - Steps:
      1. `Code Checkout`
      2. `Install dependencies` (flake8 pytest coverage) mit pip
      3. `Lint with flake8` Code check für syntax oder Code Style Fehler
      4. `Run pytest` pytest mit Python im Verzeichnis `calculator` ausführen
      5. `Run Unit tests` Unit Tests mit Python im Verzeichnis `calculator`ausführen
      6. `Run Integration tests` Integrations Tests mit Python im Verzeichnis `calculator` ausführen
      7. `Run code coverage` Code Coverage mit Python durchführen und Ergebnisse reporten
2. `build`
   - verwendet `ubuntu-24.04`
   - Steps:
      1. `Code Checkout`
      2. `Install dependencies` (flake8 pytest coverage) mit pip
      3. `Run hello world` Hello world program aus dem calculator ausführen
3. `deploy` (nur bei push auf den Main Branch)
   - verwendet `ubuntu-24.04`
   - Steps:
      1. `Code Checkout`
      2. `Install dependencies` (flake8 pytest coverage) mit pip
      3. `Package calculator` Python wheel package erstellen
      4. `Deploy package as artifact` zuvor erstelltes wheel package auf GitHub hochladen
      5. `Log in to Docker Hub` auf Docker Hub anmelden (mit Hilfe von GitHub Secrets)
      6. `Build Docker image` Docker Image der Calculator App erstellen
      7. `Push Docker image` docker Image auf Docker Hub pushen (mit Hilfe von GitHub Secrets)
