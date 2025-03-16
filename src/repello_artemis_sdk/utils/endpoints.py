class ApiEndpoints:
    """
    Class to store all the API endpoints
    """

    BASE_URL = "https://stageapimonza.repello.ai"

    # ----------- Users -----------
    USERS = BASE_URL + "/users"

    # ----------- Orgs -----------

    # ----------- Assets -----------
    ASSETS = BASE_URL + "/assets"
    ENGINE = BASE_URL + "/engine"

    TRIGGER_SCAN = lambda asset_id: f"{ApiEndpoints.ENGINE}/{asset_id}/trigger/"
