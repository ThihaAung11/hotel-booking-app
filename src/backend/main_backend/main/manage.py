import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from main.extensions import db
    from main.models import User

    click.echo("create user")
    user = User(username="admin", email="thihaaung@onow.com", password="admin@123", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
