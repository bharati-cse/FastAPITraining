from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    #MongoDB settings
    MONGO_URI: str ="mongodb://localhost:27017"
    MONGO_DB_NAME: str = "it_servicedesk"
    #gives the app a name
    APP_NAME: str = "IT Sevice Desk App API"
    #informs pydantic-settings to load values from .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
#Shared setting object that all other files can import
settings = Settings()