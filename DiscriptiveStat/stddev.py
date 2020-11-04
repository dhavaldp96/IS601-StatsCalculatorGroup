import statistics


class Stddev:

    @staticmethod
    def stddev(data):
        stdd = statistics.stdev(data)
        return stdd