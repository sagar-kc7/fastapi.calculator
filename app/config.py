from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Calculator"
    debug: bool = False
    version: str = "1.0"

    class Config:
        env_file = ".env"


settings = Settings()
