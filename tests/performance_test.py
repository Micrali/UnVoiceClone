from utils.metrics_calculator import calculate_metrics


def test_metrics_values():
    metrics = calculate_metrics()
    assert metrics['blackbox_success'] >= 60
