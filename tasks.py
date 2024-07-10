from invoke import task
@task
def test(c):
    """Run tests and generate coverage report."""
    c.run("poetry run pytest")

@task
def coverage(c):
    """Generate HTML coverage report."""
    c.run("poetry run pytest --cov=src --cov-report=html")

@task
def lint(c):
    """Run linter checks using ruff."""
    c.run("poetry run ruff check .")

@task
def type_check(c):
    """Run type checks using mypy."""
    c.run("poetry run mypy src")

@task
def bandit(c):
    """Run security checks using bandit."""
    c.run("poetry run bandit -r src")

@task
def pre_commit(c):
    """Run all pre-commit hooks."""
    c.run("poetry run pre-commit run --all-files")

@task(pre=[test, lint, bandit])
def ci(c):
    """Run all checks for CI pipeline."""
    pass
