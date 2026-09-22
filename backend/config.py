from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DBdddd_NAME: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: fkj
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="djrhg",
        env_file_encoding="utf-8"
    )


settings = Settings()