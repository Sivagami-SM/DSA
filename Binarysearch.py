class BinarySearch:
    def __init__(self, data):
        self.data = data 

    def Binary(self, target):
        iterations = 0
        tgt_val = float(target) 

        pairs = []
        if isinstance(self.data, dict):
            for key,value in self.data.items():
                pairs.append((float(value), key))
        elif isinstance(self.data, (list, tuple)):
            idx = 0
            for value in self.data:
                pairs.append((float(value), idx))
                idx += 1
        else:
            raise TypeError("Unsupported data type for searching")

        sorted_data = sorted(pairs)

        # Binary search
        left, right = 0, len(sorted_data) - 1
        while left <= right:
            iterations += 1
            mid = (left + right) // 2
            mid_val = sorted_data[mid][0]

            if mid_val == tgt_val:
                pos = sorted_data[mid][1]
                if isinstance(self.data, dict):
                    return f"Found at key: {pos}", iterations
                else:
                    return f"Found at index: {pos}", iterations
            elif mid_val < tgt_val:
                left = mid + 1
            else:
                right = mid - 1

        return "Not Found", iterations
