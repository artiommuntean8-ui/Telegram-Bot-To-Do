import aiosqlite

DB_PATH = "tasks.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
        """)
        await db.commit()

async def add_task(user_id: int, text: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO tasks (user_id, text) VALUES (?, ?)", (user_id, text))
        await db.commit()

async def get_tasks(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT id, text, done FROM tasks WHERE user_id=? ORDER BY id DESC", (user_id,)) as cur:
            return await cur.fetchall()

async def complete_task(task_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))
        await db.commit()
