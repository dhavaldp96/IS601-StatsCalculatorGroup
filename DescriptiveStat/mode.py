import statistics


class Mode:

    @staticmethod
    def mode(data):
        mo = statistics.mode(data)
        return mo