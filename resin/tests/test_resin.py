import time

import pytest

from datadog_checks.dev.jmx import JVM_E2E_METRICS
from datadog_checks.dev.utils import get_metadata_metrics


@pytest.mark.e2e
def test_e2e(dd_agent_check):
    instance = {}
    aggregator = dd_agent_check(instance)
    aggregator.assert_service_check('resin.can_connect')

    # JMX for resin some times returns no metrics at all, so let's try a few times before asserting
    attempts = 5
    while attempts > 0 and not aggregator.metric_names:
        time.sleep(15)
        attempts -= 1
        aggregator = dd_agent_check(instance)
    if not aggregator.metric_names:
        pytest.fail("Resin has failed to emit metrics after 75s")

    metrics = [
        'resin.thread_pool.thread_active_count',
        'resin.thread_pool.thread_count',
        'resin.thread_pool.thread_idle_count',
        'resin.thread_pool.thread_max',
        'resin.thread_pool.thread_wait_count',
        'resin.connection_pool.connection_active_count',
        'resin.connection_pool.connection_count',
        'resin.connection_pool.connection_create_count',
        'resin.connection_pool.connection_idle_count',
        'resin.connection_pool.max_connections',
        'resin.connection_pool.max_create_connections',
        'resin.connection_pool.max_overflow_connections',
    ]
    for metric in metrics:
        aggregator.assert_metric(metric, at_least=0)

    # needed because https://github.com/DataDog/integrations-core/pull/9501
    jvm_e2e_metrics_new = list(JVM_E2E_METRICS)
    jvm_e2e_metrics_new.remove('jvm.gc.cms.count')
    jvm_e2e_metrics_new.remove('jvm.gc.parnew.time')
    for metric in jvm_e2e_metrics_new:
        aggregator.assert_metric(metric)

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics(), exclude=jvm_e2e_metrics_new)
