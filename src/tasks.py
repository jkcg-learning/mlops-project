from invoke import task

@task
def lint(c):
    c.run("ruff check .")

@task
def test(c):
    c.run("pytest")

@task
def bandit(c):
    c.run("bandit -r .")
