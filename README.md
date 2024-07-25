
# MLOps Project

[![CI](https://github.com/jkcg-learning/mlops-project/actions/workflows/ci.yaml/badge.svg)](https://github.com/jkcg-learning/mlops-project/actions/workflows/ci.yaml)

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
- Model serving using `FastAPI`.
- Interactive UI for predictions using `Streamlit`.
- Monitoring using `Prometheus` and `Grafana`.
- Data drift detection using `Evidently`.

## Project Structure

```
mlops-project/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── retrain.yml
│       └── monitor_drift.yml
├── data/
│   ├── winequality-red.csv
│   └── winequality-prod.csv  # Simulated production data
├── dist/
├── docs/
│   └── (generated documentation)
├── mlruns/
│   └── (mlflow model runs)
├── src/
│   ├── config.yaml
│   ├── data_loader.py
│   ├── data_models.py
│   ├── main.py
│   ├── preprocess.py
│   ├── schema.py
│   ├── serve.py
│   ├── train_model.py
│   ├── ui.py
│   ├── utils.py
│   ├── retrain_model.py
│   ├── monitor_data_drift.py
│   └── tests/
│       ├── test_data_loader.py
│       ├── test_preprocess.py
│       └── test_train_model.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── generate_docs.sh
├── poetry.lock
├── prometheus.yml
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
docker-compose up --build
```

### Accessing the Applications

- **Streamlit UI**: [http://localhost:8501](http://localhost:8501)
- **FastAPI server (for predictions)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Prometheus**: [http://localhost:9090](http://localhost:9090)
- **Grafana**: [http://localhost:3000](http://localhost:3000) (Default login credentials are `admin` for both username and password)

## Continuous Integration

This project uses GitHub Actions for continuous integration and dependency management. The workflows are defined in the `.github/workflows` directory.

### CI Workflow

The `ci.yml` workflow includes steps for installing dependencies, linting, testing, and updating the changelog.

### Retraining Workflow

The `retrain.yml` workflow automatically retrains the model on a weekly basis.

### Monitor Data Drift

The `monitor_drift.yml` workflow runs weekly to monitor data drift using Evidently.

## Troubleshooting

### Loading the Latest Model from `mlruns`

Ensure that the model directory exists and is correctly referenced in the FastAPI application. The model should be saved in the `mlruns` directory.

### Matching Feature Names

Ensure that the feature names in the input data match exactly with the feature names used during training.

### FastAPI Application Schema

Ensure the FastAPI application uses the correct feature names in the input schema and when creating the input dataframe.

### Example Request Payload

The request payload to the `/predict` endpoint should look like this:
```json
{
    "fixed acidity": 7.4,
    "volatile acidity": 0.7,
    "citric acid": 0.0,
    "residual sugar": 1.9,
    "chlorides": 0.076,
    "free sulfur dioxide": 11.0,
    "total sulfur dioxide": 34.0,
    "density": 0.9978,
    "pH": 3.51,
    "sulphates": 0.56,
    "alcohol": 9.4
}
```

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
