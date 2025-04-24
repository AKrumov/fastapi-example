import os
import pytest
from app.config.settings_cfg import Settings


@pytest.fixture
def mock_env():
    # Mock environment variables for testing purposes
    os.environ["APP_NAME"] = "Test App"
    os.environ["APP_VERSION"] = "1.0.0"
    os.environ["APP_ROOT_PATH"] = "/api/v1"
    os.environ["APP_HOST"] = "0.0.0.0"
    os.environ["APP_PORT"] = "8080"
    os.environ["LOG_FORMAT"] = "%(levelname)s:     %(asctime)s - %(message)s"
    os.environ["LOG_LEVEL"] = "iNfO"

    yield
    # Clean up environment variables
    del os.environ["APP_NAME"]
    del os.environ["APP_VERSION"]
    del os.environ["APP_ROOT_PATH"]
    del os.environ["APP_HOST"]
    del os.environ["APP_PORT"]
    del os.environ["LOG_FORMAT"]
    del os.environ["LOG_LEVEL"]


def test_settings_load_from_env(mock_env):
    # Initialize settings with the mocked environment
    settings = Settings()

    # Check application-specific settings
    assert settings.app['name'] == "Test App"
    assert settings.app['version'] == "1.0.0"
    assert settings.app['root_path'] == "/api/v1"
    assert settings.app['host'] == "0.0.0.0"
    assert settings.app['port'] == 8080

    # Check Log settings
    assert settings.log['format'] == "%(levelname)s:     %(asctime)s - %(message)s"
    assert settings.log['level'] == "INFO"

