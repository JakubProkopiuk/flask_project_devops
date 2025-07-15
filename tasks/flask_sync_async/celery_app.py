from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent))

from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

@celery.task
def save_user_async(name, email):
    from app.app import db, User, app as flask_app
    with flask_app.app_context():
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()

