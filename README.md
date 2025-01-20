# TechDemo: Continuous Delivery Integration

David Krall  
Daniel Zarnhofer

---

> Das [GitLab Repository](https://git-iit.fh-joanneum.at/msd-contdel/techdemo-ws24/krall-zarnhofer) dieses Projekts ist nicht das Hauptrepository.  
> Das Hauptrepository befindet sich auf GitHub unter: [https://github.com/davkra/krall-zarnhofer](https://github.com/davkra/krall-zarnhofer) und wird [mit diesem Repository gespiegelt.](#prerequisites)

## Table of Contents

- [TechDemo: Continuous Delivery Integration](#techdemo-continuous-delivery-integration)
  - [Table of Contents](#table-of-contents)
  - [Checklist](#checklist)
  - [Introduction](#introduction)
  - [Objective](#objective)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Tech Stack](#tech-stack)
  - [Testing](#testing)
  - [Continuous Delivery Workflow](#continuous-delivery-workflow)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Checklist

For a detailed list of tasks and goals, refer to the [Checkliste](./CHECKLIST.md). This document serves as a guide to ensure all relevant CD aspects are integrated into this demo.

## Introduction

This repository serves as a guide for the TechDemo of the Continuous Delivery (CD) course. It focuses on integrating CD principles into an existing software project rather than developing new software from scratch. The aim is to demonstrate automated builds, tests, and deployments in a real-world scenario.

## Objective

The main objective is to apply CD practices by automating key processes, ensuring a smoother and more efficient software development lifecycle. This includes:

- Automated builds with build tools.
- Automated testing with unit, integration, and end-to-end tests.
- Continuous deployment to production-like environments.

## Getting Started

### Prerequisites

Ensure the following software and tools are installed:

- **Git**: Version control.
- **Java JDK / Python / Node.js**: Depending on the tech stack used in your project.
- **Docker** (optional): For containerized deployments.

Furthermore both the main and the mirror repository need to be added to the local Git workspace. This is necessary in case new code needs to be pushed to the remote repository.

```bash
# Mirror Repository
git remote set-url --add --push origin git@git-iit.fh-joanneum.at:msd-contdel/techdemo-ws24/krall-zarnhofer.git

# Main Repository
git remote set-url --add --push origin git@github.com:davkra/krall-zarnhofer.git
```

These remotes depend on correct configurations of SSH-key. Alternatively the repositories can also be added via https:

```bash
# Mirror Repository
git remote set-url --add --push origin https://git-iit.fh-joanneum.at/msd-contdel/techdemo-ws24/krall-zarnhofer.git

# Main Repository
git remote set-url --add --push origin https://github.com/davkra/krall-zarnhofer.git
```

The two scripts [gitsetup.sh](./gitsetup.sh) and [gitsetup.cmd](./gitsetup.cmd) (depending on the operating system) can be used to correctly configure the repository after cloning it.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/continuous-delivery-techdemo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd continuous-delivery-techdemo
   ```

3. Install dependencies:
   - For Node.js:

     ```bash
     npm install
     ```

   - For Python:

     ```bash
     pip install -r requirements.txt
     ```

   - For Java:

     ```bash
     mvn install
     ```

## Usage

1. **Build the project**:
   - Java: `mvn clean install`
   - Python: `python setup.py build`
   - JavaScript: `npm run build`

2. **Run the tests**:
   - Execute unit and integration tests to verify the functionality.

3. **Deploy the project**: The deployment is automated through the provided scripts or configured CI/CD pipeline.

## Tech Stack

- **Primary Language**: Java, Python, JavaScript (choose based on your project).
- **Build Tools**: Maven, Pip, NPM.
- **Testing Frameworks**: JUnit, pytest, Jest.
- **CI/CD**: Jenkins, GitHub Actions.

## Testing

To ensure high-quality code, testing is integrated throughout the development process. You can run the following test suites:

1. **Unit Tests**: Validating individual components.
2. **Integration Tests**: Ensuring modules work together.
3. **End-to-End Tests**: Testing complete workflows.

   ```bash
   npm test
   ```

## Continuous Delivery Workflow

The following CD practices are integrated into this project:

- **Automated Builds**: Triggered on every commit.
- **Automated Tests**: Running unit, integration, and e2e tests.
- **Continuous Deployment**: Deployments to a staging environment with approval steps for production deployment.

## Contributing

We welcome contributions. Please follow the **TODO** [contributing guidelines](./CONTRIBUTING.md) for submitting issues and pull requests.

## License

This project is licensed under the MIT License. See the **TODO** [LICENSE](./LICENSE.md) file for details.

## Contact

For any inquiries or issues, please reach out to [michael.ulm@fh-joanneum.at](mailto:michael.ulm@fh-joanneum.at).
