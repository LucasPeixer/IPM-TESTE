from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context
import os
from app.models import task_model, user_model  # Ajuste conforme a estrutura do seu projeto

# Configuração do logging
fileConfig(context.config.config_file_name)

# O modelo Base que contém o MetaData
target_metadata = task_model.Base.metadata  # Aqui é onde você define o 'Base'

# Função para incluir o modelo no contexto de migração
def run_migrations_online():
    # Conexão com o banco de dados
    connectable = engine_from_config(
        context.config.get_section(context.config.default_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()
