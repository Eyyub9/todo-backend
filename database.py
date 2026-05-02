import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Önce Render'ın sunduğu DATABASE_URL ortam değişkenini kontrol et
# Eğer bulamazsa senin yerel (localhost) adresini varsayılan olarak kullan
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:12345@localhost:5432/todo_db")

# 2. ÖNEMLİ DÜZELTME: Render ve bazı bulut sağlayıcılar 'postgres://' formatında URL verir.
# Ancak SQLAlchemy 1.4+ sürümünden itibaren 'postgresql://' (ql takısı şart) formatını zorunlu kılar.
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Engine oluşturma
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()