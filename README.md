# Ronin Supply

AI-powered Retail Operating System with hyper-local intelligence and autonomous supply chain management.

## Overview

Ronin Supply is a modular monolith architecture with three specialized AI-powered modules:

- **The Merchant**: Autonomous supply chain negotiation using Scout and Negotiator agents
- **The Seer**: Hyper-local micro-event forecasting with geographic precision  
- **The Salvager**: Visual grading & profit recovery engine with marketplace automation

## Features

- **Hyper-Local Intelligence**: Zip code level demand forecasting using real-world events
- **Web Intelligence**: Real-time market data using Tavily API and PredictHQ
- **AI-Powered Negotiation**: Automated supplier negotiations with cultural adaptation
- **Visual Grading**: Computer vision analysis for returned item profit recovery
- **Geographic Analytics**: PostGIS-powered spatial analysis and optimization
- **Real-Time Updates**: WebSocket-based dashboard with live intelligence feeds

## Technology Stack

- **Backend**: FastAPI, Python 3.11+
- **Database**: PostgreSQL with PostGIS and pgvector extensions
- **Cache**: Redis for intelligent caching and rate limiting
- **AI Services**: Gemini 3 Flash, LangGraph for agent orchestration
- **Web Intelligence**: Tavily API, PredictHQ, OpenWeatherMap
- **Storage**: Supabase for file storage and additional features
- **Containerization**: Docker and Docker Compose

## Quick Start (No Docker Required)

### Prerequisites

- Python 3.11+
- API keys for external services (see `.env.example`)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ronin-supply
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy environment configuration:
```bash
cp .env.example .env
# Edit .env with your API keys
```

5. Run the application:
```bash
python run_local.py
```

The application will be available at `http://localhost:8000`

### API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

### Running Tests

```bash
source venv/bin/activate
pytest
```

### Code Formatting

```bash
pip install black isort flake8
black ronin_supply tests
isort ronin_supply tests
flake8 ronin_supply tests
```

## Database Options

### 1. SQLite (Default - No Setup Required)
The application uses SQLite by default for local development. No additional setup needed.

### 2. PostgreSQL (Optional)
For production-like development:

```bash
# macOS
brew install postgresql
brew services start postgresql
createdb ronin_supply

# Update .env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/ronin_supply
```

### 3. Cloud Databases (Recommended for Production)
- **Supabase**: PostgreSQL with built-in PostGIS support
- **Railway**: PostgreSQL + Redis hosting
- **Render**: Database hosting
- **Neon**: Serverless PostgreSQL

## Docker (Optional)

If you prefer Docker:

```bash
# Start infrastructure services
docker compose up -d postgres redis

# Or run everything in containers
docker compose --profile full up
```

## Configuration

All configuration is managed through environment variables. See `.env.example` for required settings.

### Required API Keys

- **Google Gemini API**: For AI processing and vision analysis
- **Tavily API**: For web intelligence and supplier research
- **PredictHQ**: For ML-ready event data with impact scoring
- **OpenWeatherMap**: For hyper-local weather data
- **Supabase**: For file storage and additional database features

### Optional API Keys

- **eBay, Amazon**: For marketplace integrations (The Salvager)
- **Google Maps**: For enhanced geographic services

## Architecture

The system follows a modular monolith pattern with event-driven communication between modules:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   The Merchant  │    │    The Seer     │    │  The Salvager   │
│                 │    │                 │    │                 │
│ Scout Agent     │    │ Event Analysis  │    │ Visual Grading  │
│ Negotiator      │    │ Forecasting     │    │ Profit Recovery │
│ Auto-Personality│    │ Geographic Intel│    │ Marketplace     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │  Event System   │
                    │  FastAPI Core   │
                    │  Database       │
                    └─────────────────┘
```

## License

[License information]

## Contributing

[Contributing guidelines]