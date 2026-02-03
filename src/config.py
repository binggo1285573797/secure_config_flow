import os

# Security review implemented
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
SERVICE_TOKEN = os.getenv("SERVICE_TOKEN", "")

# Old legacy config below
DEBUG = True
