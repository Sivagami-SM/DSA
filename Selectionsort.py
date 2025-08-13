class SelectionSort:
    def __init__(self, data):
        self.data = data

    def Selection(self, sort_order="Ascending"):
        if isinstance(self.data, dict):
            items = list(self.data.items())
        elif isinstance(self.data, tuple):
            items = list(self.data)
        else:
            items = self.data[:]

        n = len(items)
        iterations = 0

        if isinstance(self.data, dict):
            for i in range(n):
                selected_index = i
                iterations += 1
                for j in range(i + 1, n):
                    try:
                        val1 = float(items[j][1])
                        val2 = float(items[selected_index][1])
                    except(ValueError,TypeError):
                        val1 = str(items[j][1])
                        val2 = str(items[selected_index][1])

                    if sort_order == "Ascending":
                        if val1 < val2:
                            selected_index = j
                    elif sort_order == "Descending":
                        if val1 > val2:
                            selected_index = j

                if selected_index != i:
                    items[i], items[selected_index] = items[selected_index], items[i]

            return dict(items), iterations

        elif isinstance(self.data, (list, tuple)):
            for i in range(n):
                selected_index = i
                iterations += 1
                for j in range(i + 1, n):
                    try:
                        val1 = float(items[j])
                        val2 = float(items[selected_index])
                    except(ValueError,TypeError):
                        val1 = str(items[j])
                        val2 = str(items[selected_index])

                    if sort_order == "Ascending":
                        if val1 < val2:
                            selected_index = j
                    elif sort_order == "Descending":
                        if val1 > val2:
                            selected_index = j

                if selected_index != i:
                    items[i], items[selected_index] = items[selected_index], items[i]

            return (tuple(items) if isinstance(self.data, tuple) else items), iterations

        else:
            raise TypeError("Unsupported data type for sorting")
