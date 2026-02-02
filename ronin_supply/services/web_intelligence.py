"""Web intelligence services (Tavily, PredictHQ, etc.)."""

from typing import Optional, Dict, Any, List
import httpx
import structlog
from tavily import TavilyClient

from ronin_supply.config import settings
from ronin_supply.core.redis_optional import cache

logger = structlog.get_logger()


class TavilyService:
    """Tavily API integration for web intelligence."""
    
    def __init__(self):
        self.client = TavilyClient(api_key=settings.tavily_api_key)
    
    async def search(
        self, 
        query: str, 
        max_results: int = 5,
        include_domains: Optional[List[str]] = None,
        exclude_domains: Optional[List[str]] = None
    ) -> Optional[Dict[str, Any]]:
        """Search web using Tavily API."""
        try:
            # Check cache first
            cache_key = f"tavily_search:{hash(query)}"
            cached_result = await cache.get(cache_key)
            if cached_result:
                return cached_result
            
            response = self.client.search(
                query=query,
                max_results=max_results,
                include_domains=include_domains,
                exclude_domains=exclude_domains,
                include_raw_content=True
            )
            
            # Cache for 1 hour
            await cache.set(cache_key, response, ttl=3600)
            return response
            
        except Exception as e:
            logger.error("Tavily search error", query=query, error=str(e))
            return None


class PredictHQService:
    """PredictHQ API integration for event data."""
    
    def __init__(self):
        self.base_url = "https://api.predicthq.com/v1"
        self.headers = {
            "Authorization": f"Bearer {settings.predicthq_access_token}",
            "Accept": "application/json"
        }
    
    async def get_events(
        self,
        location: str,
        start_date: str,
        end_date: str,
        categories: Optional[List[str]] = None
    ) -> Optional[Dict[str, Any]]:
        """Get events from PredictHQ API."""
        try:
            # Check cache first
            cache_key = f"predicthq_events:{hash(f'{location}_{start_date}_{end_date}')}"
            cached_result = await cache.get(cache_key)
            if cached_result:
                return cached_result
            
            params = {
                "location.place_id": location,
                "start.gte": start_date,
                "end.lte": end_date,
                "limit": 50
            }
            
            if categories:
                params["category"] = ",".join(categories)
            
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/events",
                    headers=self.headers,
                    params=params
                )
                response.raise_for_status()
                result = response.json()
                
                # Cache for 30 minutes
                await cache.set(cache_key, result, ttl=1800)
                return result
                
        except Exception as e:
            logger.error("PredictHQ API error", location=location, error=str(e))
            return None


class OpenWeatherService:
    """OpenWeatherMap API integration."""
    
    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.api_key = settings.openweather_api_key
    
    async def get_weather_forecast(
        self,
        lat: float,
        lon: float,
        days: int = 5
    ) -> Optional[Dict[str, Any]]:
        """Get weather forecast for coordinates."""
        try:
            # Check cache first
            cache_key = f"weather_forecast:{lat}_{lon}_{days}"
            cached_result = await cache.get(cache_key)
            if cached_result:
                return cached_result
            
            params = {
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "metric",
                "cnt": days * 8  # 8 forecasts per day (3-hour intervals)
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/forecast",
                    params=params
                )
                response.raise_for_status()
                result = response.json()
                
                # Cache for 15 minutes
                await cache.set(cache_key, result, ttl=900)
                return result
                
        except Exception as e:
            logger.error("OpenWeather API error", lat=lat, lon=lon, error=str(e))
            return None


# Global service instances
tavily_service = TavilyService()
predicthq_service = PredictHQService()
openweather_service = OpenWeatherService()