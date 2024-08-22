from sqlalchemy.orm import Session
import models
import schemas
import auth


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Task)
        .filter(models.Task.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_task(db: Session, task_id: int, user_id: int):
    return (
        db.query(models.Task)
        .filter(models.Task.id == task_id, models.Task.owner_id == user_id)
        .first()
    )


def update_task(db: Session, task_id: int, task: schemas.TaskUpdate, user_id: int):
    db_task = (
        db.query(models.Task)
        .filter(models.Task.id == task_id, models.Task.owner_id == user_id)
        .first()
    )
    if not db_task:
        return None
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
