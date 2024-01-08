"""Platform specific check factory."""
from cctrusted_vm.cvm import ConfidentialVM
from cctrusted_vm.sdk import CCTrustedVmSdk
from tests.tdx.tdx_check import CCTrustedVmSdkTdxCheck

class PlatformCheck():
    """Platform specific test"""

    @staticmethod
    def inst():
        """Get instacne for the platform specific check."""
        cc_type = CCTrustedVmSdk.inst()._cvm.detect_cc_type()
        if cc_type == ConfidentialVM.TYPE_CC_TDX:
            return CCTrustedVmSdkTdxCheck.inst()
        raise NotImplementedError("Not implemented!")
