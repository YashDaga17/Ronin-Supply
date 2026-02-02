"""Optional Redis connection with fallback to in-memory cache."""

import json
from typing import Any, Optional, Dict
import structlog

logger = structlog.get_logger()

# In-memory cache fallback
_memory_cache: Dict[str, Any] = {}


class OptionalCacheManager:
    """Cache manager that works with or without Redis."""
    
    def __init__(self):
        self.redis_client = None
        self.use_redis = False
    
    async def _try_redis_connection(self):
        """Try to connect to Redis, fall back to memory cache if unavailable."""
        try:
            import redis.asyncio as redis
            from ronin_supply.config import settings
            
            self.redis_client = redis.from_url(
                settings.redis_url,
                encoding="utf-8",
                decode_responses=True,
            )
            await self.redis_client.ping()
            self.use_redis = True
            logger.info("Redis connection established")
        except Exception as e:
            logger.warning("Redis unavailable, using in-memory cache", error=str(e))
            self.use_redis = False
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if not hasattr(self, 'use_redis'):
            await self._try_redis_connection()
        
        try:
            if self.use_redis and self.redis_client:
                value = await self.redis_client.get(key)
                if value:
                    return json.loads(value)
            else:
                # Use in-memory cache
                return _memory_cache.get(key)
        except Exception as e:
            logger.error("Cache get error", key=key, error=str(e))
        
        return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600) -> bool:
        """Set value in cache with TTL."""
        if not hasattr(self, 'use_redis'):
            await self._try_redis_connection()
        
        try:
            serialized = json.dumps(value, default=str)
            
            if self.use_redis and self.redis_client:
                await self.redis_client.setex(key, ttl, serialized)
            else:
                # Use in-memory cache (ignore TTL for simplicity)
                _memory_cache[key] = value
            
            return True
        except Exception as e:
            logger.error("Cache set error", key=key, error=str(e))
            return False
    
    async def delete(self, key: str) -> bool:
        """Delete key from cache."""
        if not hasattr(self, 'use_redis'):
            await self._try_redis_connection()
        
        try:
            if self.use_redis and self.redis_client:
                await self.redis_client.delete(key)
            else:
                _memory_cache.pop(key, None)
            return True
        except Exception as e:
            logger.error("Cache delete error", key=key, error=str(e))
            return False


# Global cache manager instance
cache = OptionalCacheManager()