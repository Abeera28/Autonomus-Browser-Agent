import psycopg2
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get database credentials from .env
db_url = os.getenv("DATABASE_URL")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")
db_host = os.getenv("DATABASE_HOST")
db_port = int(os.getenv("DATABASE_PORT", 5432))  # ✅ GET PORT FROM .env

print("=" * 60)
print("🔌 DATABASE CONNECTION TEST")
print("=" * 60)
print(f"Host: {db_host}")
print(f"Port: {db_port}")  # ✅ SHOW PORT
print(f"User: {db_user}")
print(f"Database: {db_name}")
print(f"URL: {db_url}")
print("=" * 60)

try:
    # Try to connect
    print("\n⏳ Attempting connection...")
    
    conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port  # ✅ USE VARIABLE, NOT HARDCODED 5432
    )
    
    # Get cursor
    cursor = conn.cursor()
    
    # Execute a simple query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print(f"\n✅ CONNECTION SUCCESSFUL!")
    print(f"PostgreSQL Version: {db_version[0]}")
    
    # Close connection
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ CONNECTION FAILED!")
    print(f"Error: {e}")
    print("\nTroubleshooting:")
    print("1. Check if Docker is running: docker ps")
    print("2. Check if PostgreSQL container is running: docker ps")
    print("3. Check credentials in .env file")
    print("4. Try: docker-compose restart")

print("=" * 60)