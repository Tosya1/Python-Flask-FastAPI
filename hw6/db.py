import databases
import sqlalchemy
from settings import settings
from models.order import Status

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("last_name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(32)),
    sqlalchemy.Column("password", sqlalchemy.String(50)),
)

goods = sqlalchemy.Table(
    "goods",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(64)),
    sqlalchemy.Column("description", sqlalchemy.Text(250)),
    sqlalchemy.Column("price", sqlalchemy.Float(2)),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users.c.id)),
    sqlalchemy.Column("good_id", sqlalchemy.ForeignKey(goods.c.id)),
    sqlalchemy.Column("created_on", sqlalchemy.DateTime()),
    sqlalchemy.Column("status", sqlalchemy.Enum(Status)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
