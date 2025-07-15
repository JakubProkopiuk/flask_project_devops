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
    from database import SessionLocal
    from models import User
    db = SessionLocal()
    db.add(User(name=name, email=email))
    db.commit()
    db.close()

