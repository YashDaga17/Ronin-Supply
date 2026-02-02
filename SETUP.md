# Ronin Supply Setup Guide

## No Docker Required! 🎉

This application is designed to work without Docker. Here are your hosting options:

## Option 1: Local Development (Recommended to Start)

### Quick Setup
```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run_local.py
```

**What you get:**
- ✅ SQLite database (no setup required)
- ✅ In-memory cache (Redis fallback)
- ✅ All core functionality
- ✅ API documentation at http://localhost:8000/docs

## Option 2: Cloud Services (Production Ready)

### Database Options
1. **Supabase** (Recommended)
   - Free PostgreSQL with PostGIS
   - Built-in file storage
   - Real-time features
   - Sign up at: https://supabase.com

2. **Railway**
   - PostgreSQL + Redis
   - Easy deployment
   - Sign up at: https://railway.app

3. **Render**
   - PostgreSQL hosting
   - Sign up at: https://render.com

### Configuration
Update your `.env` file:
```bash
# Supabase example
DATABASE_URL=postgresql+asyncpg://user:pass@db.supabase.co:5432/postgres
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key

# Redis (optional - will use memory cache if not available)
REDIS_URL=redis://user:pass@redis-host:6379
```

## Option 3: Local PostgreSQL + Redis

If you want the full stack locally:

### macOS
```bash
brew install postgresql redis
brew services start postgresql
brew services start redis
createdb ronin_supply
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib redis-server
sudo systemctl start postgresql redis-server
sudo -u postgres createdb ronin_supply
```

### Windows
1. Download PostgreSQL from https://www.postgresql.org/download/windows/
2. Download Redis from https://github.com/microsoftarchive/redis/releases
3. Create database: `createdb ronin_supply`

## API Keys Setup

The application needs these API keys for full functionality:

### Required for Core Features
```bash
GOOGLE_API_KEY=your-gemini-api-key        # AI processing
TAVILY_API_KEY=your-tavily-key            # Web intelligence
PREDICTHQ_ACCESS_TOKEN=your-predicthq-key # Event data
OPENWEATHER_API_KEY=your-weather-key      # Weather data
```

### Optional for Extended Features
```bash
EBAY_CLIENT_ID=your-ebay-id              # Marketplace integration
AMAZON_ACCESS_KEY=your-amazon-key        # Marketplace integration
SMTP_USERNAME=your-email@gmail.com       # Email notifications
SMTP_PASSWORD=your-app-password          # Email notifications
```

## Getting API Keys

1. **Google Gemini**: https://makersuite.google.com/app/apikey
2. **Tavily**: https://tavily.com (sign up for API access)
3. **PredictHQ**: https://www.predicthq.com (free tier available)
4. **OpenWeatherMap**: https://openweathermap.org/api (free tier)

## Deployment Options

### 1. Railway (Easiest)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway up
```

### 2. Render
1. Connect your GitHub repo
2. Set environment variables
3. Deploy automatically

### 3. Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
heroku config:set DATABASE_URL=your-db-url
git push heroku main
```

### 4. DigitalOcean App Platform
1. Connect GitHub repo
2. Configure environment variables
3. Deploy

## Testing Your Setup

```bash
# Run tests
pytest

# Check API endpoints
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/docs  # API documentation
```

## Troubleshooting

### "Module not found" errors
```bash
# Make sure you're in the virtual environment
source venv/bin/activate
pip install -r requirements.txt
```

### Database connection issues
```bash
# Check your DATABASE_URL in .env
# For SQLite (default): sqlite+aiosqlite:///./ronin_supply.db
# For PostgreSQL: postgresql+asyncpg://user:pass@host:5432/dbname
```

### Redis connection issues
The app will automatically fall back to in-memory cache if Redis is unavailable.

## Next Steps

1. ✅ Get the basic app running with `python run_local.py`
2. 🔑 Add your API keys to `.env` file
3. 🚀 Deploy to a cloud service
4. 📊 Start implementing the three modules (tasks 2-13)

Need help? Check the main README.md or create an issue!