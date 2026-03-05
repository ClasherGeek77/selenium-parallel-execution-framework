import logging
import abc
from typing import Any

logger = logging.getLogger(__name__)

class DataFactory(abc.ABC):
    """
    Principal-Grade Data Factory for API-driven test data isolation.
    """
    @abc.abstractmethod
    def create_user(self, **kwargs) -> dict[str, Any]:
        """Create a test user via API."""
        pass

    @abc.abstractmethod
    def delete_user(self, user_id: str) -> None:
        """Cleanup test user via API."""
        pass

class MockDataFactory(DataFactory):
    def create_user(self, **kwargs) -> dict[str, Any]:
        logger.info(f"Mocking user creation with attributes: {kwargs}")
        return {"id": "mock-123", "username": "test_user"}

    def delete_user(self, user_id: str) -> None:
        logger.info(f"Mocking user deletion: {user_id}")
