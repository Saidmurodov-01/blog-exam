from database import engine, SessionLocal
from models import Base
from crud import create_user, create_post, create_comment
import json


# Jadvallarni yaratish
Base.metadata.create_all(bind=engine)
print("Jadvallar yaratildi.")


def load_demo_data():
    db = SessionLocal()

    with open("demo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Users
    for u in data.get("users", []):
        try:
            create_user(db, u["username"], u["email"])
        except Exception as e:
            db.rollback()
            print(f"User '{u['username']}' qo‘shilmadi: {e}")
    db.commit()

    # 2. Posts
    for p in data.get("posts", []):
        try:
            create_post(db, p["user_id"], p["title"], p["body"])
        except Exception as e:
            db.rollback()
            print(f"Post '{p['title']}' qo‘shilmadi: {e}")
    db.commit()

    # 3. Comments
    for c in data.get("comments", []):
        try:
            create_comment(db, c["user_id"], c["post_id"], c["text"])
        except Exception as e:
            db.rollback()
            print(f"Comment qo‘shilmadi: {e}")
    db.commit()

    db.close()
    print("Demo ma’lumotlar yuklandi.")


if __name__ == "__main__":

    load_demo_data()
    
