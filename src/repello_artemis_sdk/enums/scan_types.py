from enum import Enum


class ScanType(Enum):
    """
    Enum class for the different types of scans that can be triggered.
    """

    quick_scan = "quick_scan"
    safety_scan = "safety_analysis"
    owasp = "owasp"
    mitre = "mitre"
    nist = "nist"
    business_ctx = "business_ctx"
    whistleblower = "whistleblower"
    fingerprint = "fingerprint"
