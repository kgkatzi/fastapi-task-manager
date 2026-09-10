from app.db.models import Task


def test_create_task_via_model(db_session):
    task = Task(
        title="Direct model test",
        description="via SQLAlchemy",
    )

    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)

    assert task.id is not None
    assert task.completed is False
    assert task.priority == 0

    db_session.delete(task)
    db_session.commit()