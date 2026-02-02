"""Configuration management for Ronin Supply system."""

from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )
    
    # Application
    app_name: str = Field(default="Ronin Supply", description="Application name")
    app_version: str = Field(default="0.1.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")
    log_level: str = Field(default="INFO", description="Logging level")
    secret_key: str = Field(description="Secret key for JWT and encryption")
    
    # Database
    database_url: str = Field(description="PostgreSQL database URL")
    redis_url: str = Field(description="Redis connection URL")
    
    # Supabase
    supabase_url: str = Field(description="Supabase project URL")
    supabase_key: str = Field(description="Supabase anon key")
    supabase_service_key: str = Field(description="Supabase service key")
    
    # AI Services
    google_api_key: str = Field(description="Google Gemini API key")
    openai_api_key: Optional[str] = Field(default=None, description="OpenAI API key")
    
    # Web Intelligence APIs
    tavily_api_key: str = Field(description="Tavily API key for web intelligence")
    predicthq_access_token: str = Field(description="PredictHQ access token")
    openweather_api_key: str = Field(description="OpenWeatherMap API key")
    
    # Email Configuration
    smtp_host: str = Field(default="smtp.gmail.com", description="SMTP server host")
    smtp_port: int = Field(default=587, description="SMTP server port")
    smtp_username: str = Field(description="SMTP username")
    smtp_password: str = Field(description="SMTP password")
    
    # Marketplace APIs
    ebay_client_id: Optional[str] = Field(default=None, description="eBay client ID")
    ebay_client_secret: Optional[str] = Field(default=None, description="eBay client secret")
    amazon_access_key: Optional[str] = Field(default=None, description="Amazon access key")
    amazon_secret_key: Optional[str] = Field(default=None, description="Amazon secret key")
    
    # Geographic Services
    google_maps_api_key: Optional[str] = Field(default=None, description="Google Maps API key")
    
    # Rate Limiting
    rate_limit_requests_per_minute: int = Field(default=60, description="Rate limit per minute")
    rate_limit_burst: int = Field(default=10, description="Rate limit burst")


# Global settings instance
settings = Settings()