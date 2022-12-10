import requests
import pytest

# Configure pytest
def pytest_configure(config):
    pytest.api_url = 'http://localhost:8000'
    pytest.api_unavailable = api_unavailable()
    # Uncomment the below to stop ALL tests if the SyncLink Server is down
    # if pytest.api_unavailable:
    #     pytest.exit(f'FATAL - API unavailable: {pytest.api_url}')

# Use this to "skipif" individual tests that require an available API
def api_unavailable(api_url = None):
    if "status" not in api_unavailable.__dict__ : api_unavailable.status = None
    if api_unavailable.status != None:
        return api_unavailable.status
    try:
        api_url = api_url if api_url != None else pytest.api_url
        request = requests.get(api_url, timeout = 5)
        api_unavailable.status = False
    except requests.exceptions.ConnectionError:
        api_unavailable.status = True
    return api_unavailable.status