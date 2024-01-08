"""TDX specific check."""

from cctrusted_vm import CCTrustedVmSdk
from cctrusted_base.tcg import TcgAlgorithmRegistry
from tests.inc.check import PlatformSpecificCheck

class CCTrustedVmSdkTdxCheck(PlatformSpecificCheck):
    """TDX specific check."""

    _inst = None

    @classmethod
    def inst(cls):
        """Singleton instance function."""
        if cls._inst is None:
            cls._inst = cls()
        return cls._inst

    def check_default_algorithms(self):
        """Check default algorithm."""
        algo = CCTrustedVmSdk.inst().get_default_algorithms()
        assert algo is not None
        algo_str = TcgAlgorithmRegistry.get_algorithm_string(algo.alg_id)
        assert algo_str != "UNKNOWN"

    def check_measurement_count(self):
        """Check measurement count."""
        sdk = CCTrustedVmSdk.inst()
        count = sdk.get_measurement_count()
        assert count == 4
