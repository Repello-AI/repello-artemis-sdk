# Repello Artemis SDK

A Python client SDK for triggering actions on Repello's Artemis Platform.

## Installation

You can install the package from PyPI:

```bash
pip install repello-artemis-sdk
```

## Requirements

- Python 3.8 or higher
- `requests` library (automatically installed as a dependency)

## Quick Start

```python
from repello_artemis_sdk import RepelloArtemisClient
from repello_artemis_sdk.enums import ScanType

# Initialize the client with your credentials
client = RepelloArtemisClient(
    client_id="your-client-id",
    client_secret="your-client-secret",
    log_to_console=True,  # Optional: Enable console logging
    log_to_file="artemis.log"  # Optional: Log to file
)

# Trigger a scan on an asset
client.assets.trigger_scan("asset_id", ScanType.quick_scan)
```

## Features

- Simple, intuitive API for interacting with Repello's Artemis Platform
- Supports different scan types for assets
- Configurable logging (console and/or file)
- Type hints for better IDE integration

## Authentication

The SDK uses client credentials for authentication. You need to provide your `client_id` and `client_secret` when initializing the client:

```python
client = RepelloArtemisClient(client_id, client_secret)
```

Head to [platform.repello.ai](https://platform.repello.ai) and login to your account, go to the CI/CD page, create a client secret, then copy the client ID and client secret.

## API Reference

### Client Initialization

```python
RepelloArtemisClient(
    client_id: str,
    client_secret: str,
    log_to_console: bool = False,
    log_to_file: str = None
)
```

Parameters:
- `client_id`: Your Repello Artemis client ID
- `client_secret`: Your Repello Artemis client secret
- `log_to_console`: (Optional) Enable logging to console
- `log_to_file`: (Optional) Path to log file

### Assets

#### Trigger Scan

```python
client.assets.trigger_scan(asset_id: str, scan_type: ScanType)
```

Parameters:
- `asset_id`: ID of the asset to scan
- `scan_type`: Type of scan to perform (from `ScanType` enum)

Available scan types:
- `ScanType.quick_scan`: Performs a quick scan on the asset
- Other scan types (refer to the `ScanType` enum documentation)

## Changelog
See the CHANGELOG.md file for details on all changes and releases.

## License

This project is licensed under the Apache License 2.0 - see the details in the license file.


## Issues

If you encounter any problems, please file an issue at the [GitHub repository](https://github.com/Repello-AI/repello-artemis-sdk/issues).