def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Alembic",
            "description": "Practice migrations",
            "priority": 2,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Learn Alembic"
    assert data["completed"] is False
    assert data["priority"] == 2
    assert "id" in data


def test_list_tasks(client):
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})

    response = client.get("/tasks")

    assert response.status_code == 200

    titles = [task["title"] for task in response.json()]

    assert "Task A" in titles
    assert "Task B" in titles


def test_get_task(client):
    created = client.post(
        "/tasks",
        json={"title": "Task to retrieve"},
    ).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Task to retrieve"


def test_get_missing_task(client):
    response = client.get(
        "/tasks/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404


def test_update_task(client):
    created = client.post(
        "/tasks",
        json={"title": "Old title"},
    ).json()

    task_id = created["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "completed": True,
            "priority": 3,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["completed"] is True
    assert data["priority"] == 3


def test_delete_task(client):
    created = client.post(
        "/tasks",
        json={"title": "To delete"},
    ).json()

    task_id = created["id"]

    delete_response = client.delete(
        f"/tasks/{task_id}"
    )

    assert delete_response.status_code == 204

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404


def test_create_task_rejects_empty_title(client):
    response = client.post(
        "/tasks",
        json={"title": ""},
    )

    assert response.status_code == 422


def test_create_task_rejects_invalid_priority(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Invalid priority",
            "priority": 10,
        },
    )

    assert response.status_code == 422