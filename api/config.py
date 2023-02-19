from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fast API Template"
    sqlalchemy_database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
