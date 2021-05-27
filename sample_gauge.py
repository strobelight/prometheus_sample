import prometheus_client as pc
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from random import randint

class SampleGauge(object):
    def collect(self):
        g = GaugeMetricFamily('some_gauge', 'Tracking of blah')
        g.add_metric([], randint(10,100))
        yield g

def init():
    REGISTRY.register(SampleGauge())
