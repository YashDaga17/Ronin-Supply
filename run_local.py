#!/usr/bin/env python3
"""
Local development runner for Ronin Supply.
This script sets up the application to run without Docker.
"""

import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def setup_local_env():
    """Set up local environment variables."""
    env_vars = {
        "SECRET_KEY": "dev-secret-key-change-in-production",
        "DATABASE_URL": "sqlite+aiosqlite:///./ronin_supply.db",
        "REDIS_URL": "redis://localhost:6379/0",  # Will fallback to memory if Redis unavailable
        "SUPABASE_URL": "https://demo.supabase.co",
        "SUPABASE_KEY": "demo-key",
        "SUPABASE_SERVICE_KEY": "demo-service-key",
        "GOOGLE_API_KEY": "your-gemini-api-key-here",
        "TAVILY_API_KEY": "your-tavily-api-key-here", 
        "PREDICTHQ_ACCESS_TOKEN": "your-predicthq-token-here",
        "OPENWEATHER_API_KEY": "your-openweather-key-here",
        "SMTP_USERNAME": "your-email@gmail.com",
        "SMTP_PASSWORD": "your-app-password",
        "DEBUG": "true",
        "LOG_LEVEL": "INFO",
    }
    
    for key, value in env_vars.items():
        if key not in os.environ:
            os.environ[key] = value

def main():
    """Run the application locally."""
    setup_local_env()
    
    print("🚀 Starting Ronin Supply locally...")
    print("📝 Using SQLite database (no PostgreSQL required)")
    print("💾 Redis will fallback to in-memory cache if unavailable")
    print("🌐 Server will be available at: http://localhost:8000")
    print("📚 API docs at: http://localhost:8000/docs")
    print("\n⚠️  Remember to set your real API keys in .env file for full functionality!\n")
    
    # Import and run the application
    import uvicorn
    
    uvicorn.run(
        "ronin_supply.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()