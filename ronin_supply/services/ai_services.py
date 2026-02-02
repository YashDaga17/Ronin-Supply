"""AI service integrations (Gemini, OpenAI, etc.)."""

from typing import Optional, Dict, Any, List
import google.generativeai as genai
import structlog

from ronin_supply.config import settings

logger = structlog.get_logger()

# Configure Gemini
genai.configure(api_key=settings.google_api_key)


class GeminiService:
    """Gemini 3 Flash AI service integration."""
    
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.vision_model = genai.GenerativeModel('gemini-1.5-flash')
    
    async def generate_text(
        self, 
        prompt: str, 
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> Optional[str]:
        """Generate text using Gemini 3 Flash."""
        try:
            response = await self.model.generate_content_async(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=max_tokens,
                    temperature=temperature,
                )
            )
            return response.text
        except Exception as e:
            logger.error("Gemini text generation error", error=str(e))
            return None
    
    async def analyze_image(
        self, 
        image_data: bytes, 
        prompt: str
    ) -> Optional[str]:
        """Analyze image using Gemini Vision."""
        try:
            # This will be implemented in later tasks
            # when we handle image processing for The Salvager
            response = await self.vision_model.generate_content_async([
                prompt,
                {"mime_type": "image/jpeg", "data": image_data}
            ])
            return response.text
        except Exception as e:
            logger.error("Gemini vision analysis error", error=str(e))
            return None


# Global AI service instances
gemini_service = GeminiService()