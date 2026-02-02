"""Redis connection and caching utilities."""

import json
from typing import Any, Optional
import redis.asyncio as redis
import structlog

from ronin_supply.config import settings

logger = structlog.get_logger()

# Global Redis connection
_redis_client: Optional[redis.Redis] = None


async def get_redis() -> redis.Redis:
    """Get Redis client instance."""
    global _redis_client
    
    if _redis_client is None:
        _redis_client = redis.from_url(
            settings.redis_url,
            encoding="utf-8",
            decode_responses=True,
        )
        
        # Test connection
        try:
            await _redis_client.ping()
            logger.info("Redis connection established")
        except Exception as e:
            logger.error("Failed to connect to Redis", error=str(e))
            raise
    
    return _redis_client


async def close_redis():
    """Close Redis connection."""
    global _redis_client
    if _redis_client:
        await _redis_client.close()
        _redis_client = None
        logger.info("Redis connection closed")


class CacheManager:
    """Redis-based cache manager."""
    
    def __init__(self):
        self.redis_client: Optional[redis.Redis] = None
    
    async def _get_client(self) -> redis.Redis:
        """Get Redis client."""
        if self.redis_client is None:
            self.redis_client = await get_redis()
        return self.redis_client
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        try:
            client = await self._get_client()
            value = await client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error("Cache get error", key=key, error=str(e))
            return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600) -> bool:
        """Set value in cache with TTL."""
        try:
            client = await self._get_client()
            serialized = json.dumps(value, default=str)
            await client.setex(key, ttl, serialized)
            return True
        except Exception as e:
            logger.error("Cache set error", key=key, error=str(e))
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache."""
        try:
            client = await self._get_client()
            await client.delete(key)
            return True
        except Exception as e:
            logger.error("Cache delete error", key=key, error=str(e))
            return False


# Global cache manager instance
cache = CacheManager()