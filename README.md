# MLOps Project with CI/CD

[![CI](https://github.com/jkcg-learning/mlops-project/actions/workflows/ci.yml/badge.svg)](https://github.com/jkcg-learning/mlops-project/actions/workflows/ci.yml)

## Overview

This project is an MLOps template designed for predicting wine quality based on various physicochemical properties. The project demonstrates best practices in Machine Learning Operations (MLOps) including data loading, preprocessing, model training, validation, and deployment. It uses a variety of modern tools and frameworks to ensure reproducibility, scalability, and maintainability.

## Features

- Data loading and validation using `pandas` and `pydantic`.
- Data preprocessing using `pandas` and `pandera`.
- Model training using `scikit-learn` and `mlflow`.
- Configuration management using `OmegaConf`.
- Logging using `loguru`.
- Unit testing using `pytest`.
- Code linting and formatting using `ruff`.
- Security checks using `bandit`.
- Type checking using `mypy`.
- Documentation generation using `pdoc`.
- Changelog management using `Commitizen`.
- Continuous integration using `GitHub Actions`.
- Containerization using `Docker`.

## Project Structure

```
mlops-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   └── winequality-red.csv
├── dist/
├── docs/
│   └── (generated documentation)
├── src/
│   ├── config.yaml
│   ├── data_loader.py
│   ├── data_models.py
│   ├── main.py
│   ├── preprocess.py
│   ├── schema.py
│   ├── train_model.py
│   ├── utils.py
│   └── tests/
│       ├── test_data_loader.py
│       ├── test_preprocess.py
│       └── test_train_model.py
├── .dockerignore
├── Dockerfile
├── generate_docs.sh
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Setup

### Prerequisites

- Python 3.9
- Poetry
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/jkcg-learning/mlops-project.git
   cd mlops-project
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

### Configuration

Modify the `src/config.yaml` file to configure the data paths, model parameters, and other settings.

## Usage

### Running the Project

To run the main script, use:
```sh
poetry run python src/main.py --config src/config.yaml
```

### Running Tests

To run the tests, use:
```sh
poetry run pytest
```

### Generating Documentation

To generate the documentation, run:
```sh
./generate_docs.sh
```

### Building the Project

To build the project, run:
```sh
poetry build
```

### Docker

To build and run the Docker container:
```sh
docker build -t mlops-project .
docker run -it --rm mlops-project
```

## Continuous Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml`. It includes steps for installing dependencies, linting, testing, and updating the changelog.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [pydantic](https://pydantic-docs.helpmanual.io/)
- [pandera](https://pandera.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)
- [mlflow](https://mlflow.org/)
- [OmegaConf](https://omegaconf.readthedocs.io/)
- [loguru](https://loguru.readthedocs.io/)
- [pytest](https://pytest.org/)
- [ruff](https://github.com/charliermarsh/ruff)
- [bandit](https://bandit.readthedocs.io/)
- [mypy](http://mypy-lang.org/)
- [pdoc](https://pdoc.dev/)
- [Commitizen](https://commitizen-tools.github.io/commitizen/)
- [Docker](https://www.docker.com/)

## Contact

If you have any questions or feedback, please feel free to contact us at [contact@jkcg.me].
