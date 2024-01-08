"""Platform specific check interface."""
from abc import ABC, abstractmethod

class PlatformSpecificCheck(ABC):
    """Platform specific test"""

    @abstractmethod
    def inst(cls):
        """Get singleton instanace of the check."""

    @abstractmethod
    def check_default_algorithms(self):
        """Check default algorithm."""

    @abstractmethod
    def check_measurement_count(self):
        """Check measurement count."""
