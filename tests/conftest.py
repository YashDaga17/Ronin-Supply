"""Pytest configuration and fixtures."""

import asyncio
import os
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.pool import StaticPool

# Set test environment variables before importing app
os.environ.update({
    "SECRET_KEY": "test-secret-key",
    "DATABASE_URL": "sqlite+aiosqlite:///:memory:",
    "REDIS_URL": "redis://localhost:6379/0",
    "SUPABASE_URL": "https://test.supabase.co",
    "SUPABASE_KEY": "test-key",
    "SUPABASE_SERVICE_KEY": "test-service-key",
    "GOOGLE_API_KEY": "test-google-key",
    "TAVILY_API_KEY": "test-tavily-key",
    "PREDICTHQ_ACCESS_TOKEN": "test-predicthq-token",
    "OPENWEATHER_API_KEY": "test-weather-key",
    "SMTP_USERNAME": "test@example.com",
    "SMTP_PASSWORD": "test-password",
    "DEBUG": "true",
})

from ronin_supply.main import app
from ronin_supply.core.database import Base, get_db
from ronin_supply.config import settings


# Test database URL (in-memory SQLite for testing)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Create test engine
test_engine = create_async_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Create test session factory
TestSessionLocal = async_sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@pytest_asyncio.fixture
async def db_session():
    """Create test database session."""
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with TestSessionLocal() as session:
        yield session


@pytest.fixture
def client(db_session):
    """Create test client with database override."""
    
    async def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()