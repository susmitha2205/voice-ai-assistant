# metrics.py

import time
from collections import defaultdict


class Metrics:
    def __init__(self):
        self.latencies = defaultdict(list)
        self.counters = defaultdict(int)

    def record_latency(self, stage: str, duration: float):
        self.latencies[stage].append(duration)

    def increment(self, key: str):
        self.counters[key] += 1

    def summary(self):
        summary = {}

        for stage, values in self.latencies.items():
            summary[f"{stage}_avg_ms"] = round(
                sum(values) / len(values) * 1000, 2
            )

        summary.update(self.counters)
        return summary


metrics = Metrics()
