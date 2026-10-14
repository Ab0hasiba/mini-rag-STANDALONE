from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    FILE_ALLOWED_EXTENTIONS:list
    FILE_MAX_SiZE:int

    model_config = SettingsConfigDict(env_file=".env")
def get_settings()->Settings:
    return Settings()
    