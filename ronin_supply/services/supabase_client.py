"""Supabase client integration for storage and additional database features."""

from typing import Optional, Dict, Any, List
from supabase import create_client, Client
import structlog

from ronin_supply.config import settings

logger = structlog.get_logger()


class SupabaseService:
    """Supabase integration for storage and additional features."""
    
    def __init__(self):
        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_key
        )
    
    async def upload_file(
        self, 
        bucket: str, 
        file_path: str, 
        file_data: bytes,
        content_type: str = "application/octet-stream"
    ) -> Optional[str]:
        """Upload file to Supabase storage."""
        try:
            response = self.client.storage.from_(bucket).upload(
                file_path,
                file_data,
                file_options={"content-type": content_type}
            )
            
            if response.status_code == 200:
                # Get public URL
                public_url = self.client.storage.from_(bucket).get_public_url(file_path)
                return public_url
            else:
                logger.error("File upload failed", response=response)
                return None
                
        except Exception as e:
            logger.error("Supabase upload error", bucket=bucket, path=file_path, error=str(e))
            return None
    
    async def delete_file(self, bucket: str, file_path: str) -> bool:
        """Delete file from Supabase storage."""
        try:
            response = self.client.storage.from_(bucket).remove([file_path])
            return response.status_code == 200
        except Exception as e:
            logger.error("Supabase delete error", bucket=bucket, path=file_path, error=str(e))
            return False
    
    async def get_file_url(self, bucket: str, file_path: str) -> Optional[str]:
        """Get public URL for file."""
        try:
            return self.client.storage.from_(bucket).get_public_url(file_path)
        except Exception as e:
            logger.error("Supabase URL error", bucket=bucket, path=file_path, error=str(e))
            return None


# Global Supabase service instance
supabase_service = SupabaseService()