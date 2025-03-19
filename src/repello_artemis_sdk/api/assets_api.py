from typing import List, Union

from ..base import BaseApi
from ..enums import ScanType
from ..utils import ApiEndpoints, artemis_logger


class AssetApi(BaseApi):
    """
    Api class for interacting with the asset endpoints.
    """

    def trigger_scan(
        self, asset_id: str, scans_to_run: Union[ScanType, List[ScanType]]
    ) -> bool:
        """
        Trigger a scan on the specified asset, given the scan type.
        Returns True if the scan was successfully triggered.
        """

        run_config = {}

        if isinstance(scans_to_run, ScanType):
            scans_to_run = [scans_to_run]

        for scan_type in scans_to_run:
            run_config[scan_type.value] = "*"

        response = self.api_client.post(
            ApiEndpoints.TRIGGER_SCAN(asset_id),
            {"run_config": run_config},
        )

        if response.ok:
            artemis_logger.info(
                f"Successfully triggered scans: {', '.join([scan.value for scan in scans_to_run])} on <asset:{asset_id}>"
            )
            return True

        else:
            artemis_logger.error(
                f"Failed to trigger scan on <asset:{asset_id}>: {response.text}"
            )
            return False
