class BinarySearch:
    def __init__(self, data):
        self.data = data

    def Binary(self, target):
        iterations = 0

        if isinstance(self.data, dict):
            items = list(self.data.items())
        
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    if str(items[i][1]) > str(items[j][1]):
                        items[i], items[j] = items[j], items[i]

            values = [item[1] for item in items]

        elif isinstance(self.data, (list, tuple)):
       
            values = list(self.data)
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    if str(values[i]) > str(values[j]):
                        values[i], values[j] = values[j], values[i]

        elif isinstance(self.data, str):
            values = [s.strip() for s in self.data.split(",")]
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    if values[i] > values[j]:  
                        values[i], values[j] = values[j], values[i]
        else:
            raise TypeError("Unsupported data type for searching")

        # Binary search
        left, right = 0, len(values) - 1
        while left <= right:
            iterations += 1
            mid = (left + right) // 2
            if str(values[mid]) == str(target):
                if isinstance(self.data, dict):
                    return f"Found at key: {items[mid][0]}", iterations
                return f"Found at index: {mid}", iterations
            elif str(values[mid]) < str(target):
                left = mid + 1
            else:
                right = mid - 1

        return "Not Found", iterations