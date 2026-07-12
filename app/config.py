from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Hybrid Token-Efficient Routing Agent"
    APP_VERSION: str = "1.0.0"

    FIREWORKS_API_KEY: str = ""

    FIREWORKS_BASE_URL: str = "https://api.fireworks.ai/inference/v1"

    DEFAULT_MODEL: str = "accounts/fireworks/models/gpt-oss-120b"

    CONFIDENCE_THRESHOLD: float = 0.85

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()