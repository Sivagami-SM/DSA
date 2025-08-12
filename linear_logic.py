
class LinearSearch:
    def __init__(self, data):
        self.data = data

    def Linear(self, target):
        iterations = 0

        if isinstance(self.data, dict):
            idx = 0
            for key in self.data:
                iterations += 1
                if str(self.data[key]) == target:
                    return f"Found at index:{idx}", iterations
                idx += 1
            return "Not Found", iterations

        elif isinstance(self.data, (list, tuple)):
            i = 0
            for val in self.data:
                iterations += 1
                if str(val) == target:
                    return f"Found at index: {i}", iterations
                i += 1
            return "Not Found", iterations

        
        elif isinstance(self.data, str):
            iterations = len(self.data)
            if target in self.data:
                return "Found", iterations
            else:
                return "Not Found", iterations
        else:
            raise TypeError("Unsupported data type for searching")
