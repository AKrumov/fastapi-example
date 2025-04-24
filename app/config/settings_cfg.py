from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default=None, json_schema_extra={"env": "app_name"})
    app_version: str = Field(default=None, json_schema_extra={"env": "app_version"})
    app_root_path: str = Field(default="/api/v1", json_schema_extra={"env": "app_root_path"})
    app_host: str = Field(default="0.0.0.0", json_schema_extra={"env": "app_host"})
    app_port: int = Field(default=8080, json_schema_extra={"env": "app_port"})
    app_workers: int = Field(default=1, json_schema_extra={"env": "app_workers"})

    log_format: str = Field(default="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_level: str = Field(default="info", json_schema_extra={"env": "log_level"})

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @property
    def app(self) -> Dict[str, any]:
        return {
            "name": self.app_name,
            "version": self.app_version,
            "root_path": self.app_root_path,
            "host": self.app_host,
            "port": self.app_port,
            "workers": self.app_workers,
        }

    @property
    def log(self) -> Dict[str, any]:
        return {
            "format": self.log_format,
            "level": self.log_level.upper(),
        }