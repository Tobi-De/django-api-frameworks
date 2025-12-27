import pytest
from tests.utils import API_CONFIGS, fetch_api_data


@pytest.mark.benchmark(group="api_comparison")
@pytest.mark.parametrize(
    "service,endpoint",
    [(service, endpoint) for service, config in API_CONFIGS.items() for endpoint in config["endpoints"]],
)
def test_endpoints(benchmark, service, endpoint):
    """
    Compare performance across all active endpoints.
    Each endpoint is benchmarked separately for accurate comparison.
    """

    def make_request():
        return fetch_api_data(service, endpoint)

    # Benchmark this specific endpoint with pedantic mode for more accurate results
    result = benchmark.pedantic(make_request, rounds=10, warmup_rounds=3)

    # Verify the response is valid
    assert isinstance(result, dict) or isinstance(result, list), f"Invalid response format from {service} {endpoint}"
