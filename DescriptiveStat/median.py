import statistics


class Median:

    @staticmethod
    def median(data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        med = statistics.median(data)
        return med
