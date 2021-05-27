import prometheus_client as pc
from prometheus_client.core import CounterMetricFamily, REGISTRY

_ctr_value = 0

class SampleCounter(object):
    def collect(self):
        global _ctr_value
        c = CounterMetricFamily('some_counter', 'Count of blah')
        _ctr_value += 1
        c.add_metric([], _ctr_value)
        yield c

def init():
    REGISTRY.register(SampleCounter())

