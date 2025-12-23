from app.models.schemas import Project

PROJECTS = [
    Project(
        title="Телеграм-бот: To-Do",
        description="CLI→бот, SQLite, FSM, уведомления.",
        stack=["Python", "aiogram", "SQLite"],
        repo="https://github.com/username/todo-bot",
        demo="https://t.me/your_todo_bot",
    ),
    Project(
        title="Файловый органайзер",
        description="Сортировка по типам, отчеты, конфиг.",
        stack=["Python"],
        repo="https://github.com/username/file-organizer",
    ),
]
