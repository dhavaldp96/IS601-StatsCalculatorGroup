import statistics


class Mode:

    @staticmethod
    def mode(data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        mo = statistics.mode(data)
        return mo