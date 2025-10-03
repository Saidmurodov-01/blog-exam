from database import SessionLocal
import crud

db = SessionLocal()

#Test: user qo‘shish
user = crud.create_user(db, "test_user", "test@example.com")
print("Created User:", user.username)

#Test: post qo‘shish
post = crud.create_post(db, user.id, "Test Post", "Bu test post body.")
print("Created Post:", post.title)

# Test: comment qo‘shish
comment = crud.create_comment(db, user.id, post.id, "Bu comment matni.")
print("Created Comment:", comment.text)

#Test: postni yangilash
updated = crud.update_post(db, post.id, "Yangilangan sarlavha", "Yangilangan body.")
print("Updated Post:", updated.title)

#Test: postni o‘chirish
deleted = crud.delete_post(db, post.id)
print("Deleted Post:", deleted.title if deleted else "Post topilmadi")

#Test: user postlari
posts = crud.get_user_posts(db, user.id)
print("User Posts:", [p.title for p in posts])

#Test: comment count
count = crud.get_post_comment_count(db, post.id)
print("Comment Count:", count)

# Test: latest posts
latest = crud.get_latest_posts(db)
print("Latest Posts:", [p.title for p in latest])

# Test: search by title
search = crud.search_posts_by_title(db, "Yangilangan")
print("Search Results:", [p.title for p in search])

# Test: pagination
paged = crud.paginate_posts(db, page=1, per_page=2)
print("Paginated Posts:", [p.title for p in paged])

db.close()