import statistics


class Stddev:

    @staticmethod
    def stddev(data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        stdd = statistics.stdev(data)
        return stdd