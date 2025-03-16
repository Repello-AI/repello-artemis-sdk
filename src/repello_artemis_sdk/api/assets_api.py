from ..base import BaseApi
from ..enums import ScanType
from ..utils import ApiEndpoints, artemis_logger


class AssetApi(BaseApi):
    """
    Api class for interacting with the asset endpoints.
    """

    def trigger_scan(self, asset_id: str, scan_type: ScanType) -> None:
        """
        Trigger a scan on the specified asset, given the scan type.
        """

        response = self.api_client.post(
            ApiEndpoints.TRIGGER_SCAN(asset_id),
            {
                "run_config": {scan_type.value: "*"},
            },
        )

        if response.ok:
            artemis_logger.info(
                f"Successfully triggered {scan_type.value} on <asset:{asset_id}>"
            )

        else:
            artemis_logger.error(
                f"Failed to trigger scan on <asset:{asset_id}>: {response.text}"
            )
