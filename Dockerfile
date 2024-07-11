# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files to leverage Docker cache
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Ensure the mlruns directory is copied
COPY mlruns /app/mlruns

# Expose the ports FastAPI and Streamlit will run on
EXPOSE 8000
EXPOSE 8501

# Run the FastAPI application and Streamlit in parallel
CMD ["sh", "-c", "poetry run uvicorn src.serve:app --host 0.0.0.0 --port 8000 & poetry run streamlit run src/ui.py --server.port 8501"]
