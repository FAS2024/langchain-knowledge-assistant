from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Add your app to sys.path so Alembic can import it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# === Import FastAPI settings and models ===
from app.core.config import settings
from app.db.base import Base  # Base class that includes metadata
from app.models.document import Document  # Ensure all models are imported

# Alembic Config object (provides access to .ini file values)
config = context.config

sync_db_url = settings.DATABASE_URL.replace("asyncpg", "psycopg2")
config.set_main_option("sqlalchemy.url", sync_db_url)

# Setup Python logging based on config file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the metadata for Alembic to use during autogeneration
target_metadata = Base.metadata

# === Offline Migration ===
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# === Online Migration ===
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section) or {}, 
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

# === Choose Mode ===
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
