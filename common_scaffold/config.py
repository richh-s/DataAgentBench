import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# SQLite
SQLITE_PATH = os.getenv("SQLITE_PATH", "data/mydb.sqlite")
DUCKDB_PATH = os.getenv("DUCKDB_PATH", "data/mydb.duckdb")

# MySQL
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB = os.getenv("MYSQL_DB", "test")

# Other APIs
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Azure API
AZURE_API_BASE = os.getenv("AZURE_API_BASE")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION", "2024-08-01-preview") 