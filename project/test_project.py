import project, os, pytest

def main():
    test_add()
    test_delete()
    test_mark_done()
    test_save()
    test_display()

def test_add():
    project.add("Buy Groceries")
    assert project.database == [{"task": "Buy groceries", "status": "pending"}]

def test_delete():
    project.add("Clean room")
    assert project.database == [
        {"task": "Buy groceries", "status": "pending"},
        {"task": "Clean room", "status": "pending"}
    ]
    project.delete(1)
    assert project.database == [{"task": "Clean room", "status": "pending"}]
    project.delete(3)
    assert project.database == [{"task": "Clean room", "status": "pending"}]

def test_mark_done():
    project.database[0]["status"] = "done"
    assert project.database[0]["status"] == "done"

def test_save():
    project.save()
    assert os.path.exists("todo-list.txt")
    with open("todo-list.txt") as file:
        content = file.read()
        assert "1. Clean room [DONE]" in content

def test_display():
    project.display()

if __name__ == "__main__":
    main()
