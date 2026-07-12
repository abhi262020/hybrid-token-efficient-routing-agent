import time


class Metrics:

    def __init__(self):
        self.start = time.time()

    def latency(self):

        return round(
            time.time() - self.start,
            3
        )