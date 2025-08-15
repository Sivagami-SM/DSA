class BinarySearch:
    def __init__(self, data):
        self.data = data

    def Binary(self, target):
        iterations = 0

        if isinstance(self.data, dict):
            items = list(self.data.items())
            pairs = []
            index = 0
            for item in items:
                pairs.append((item[1], index))
                index += 1

            # Sort pairs by value
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    try:
                        v1 = float(pairs[i][0])
                        v2 = float(pairs[j][0])
                    except (ValueError, TypeError):
                        v1 = str(pairs[i][0])
                        v2 = str(pairs[j][0])
                    if v1 > v2:
                        pairs[i], pairs[j] = pairs[j], pairs[i]

             # Extract sorted values for binary search
            values = []
            for p in pairs:
                values.append(p[0])

           #Binary search algorithm
            left, right = 0, len(values) - 1
            while left <= right:
                iterations += 1
                mid = (left + right) // 2
                try:
                    mid_val = float(values[mid])
                    tgt_val = float(target)
                except(ValueError,TypeError):
                    mid_val = str(values[mid])
                    tgt_val = str(target)

                if mid_val == tgt_val:
                    return f"Found at index: {mid}", iterations
                elif mid_val < tgt_val:
                    left = mid + 1
                else:
                    right = mid - 1

            return "Not Found", iterations

        
        elif isinstance(self.data, (list, tuple)):
            pairs = [(self.data[i], i) for i in range(len(self.data))]
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    try:
                        v1 = float(pairs[i][0])
                        v2 = float(pairs[j][0])
                    except (ValueError, TypeError):
                        v1 = str(pairs[i][0])
                        v2 = str(pairs[j][0])
                    if v1 > v2:
                        pairs[i], pairs[j] = pairs[j], pairs[i]

            values = []
            for p in pairs:
                values.append(p[0])

            #Binary search algorithm
            left, right = 0, len(values) - 1
            while left <= right:
                iterations += 1
                mid = (left + right) // 2

                try:
                    mid_val = float(values[mid])
                    tgt_val = float(target)
                except(ValueError,TypeError):
                    mid_val = str(values[mid])
                    tgt_val = str(target)

                if mid_val == tgt_val:
                    return f"Found at index: {pairs[mid][1]}", iterations
                elif mid_val < tgt_val:
                    left = mid + 1
                else:
                    right = mid - 1

            return "Not Found", iterations


        else:
            raise TypeError("Unsupported data type for searching")
