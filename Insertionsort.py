class InsertionSort:
    def __init__(self, data):
        self.data = data

    def Insertion(self, sort_order="Ascending"): 
        if isinstance(self.data, dict):
            items = list(self.data.items())
        elif isinstance(self.data, tuple):
            items = list(self.data)
        else:
            items = self.data[:]

        n = len(items)
        iterations = 0

        if isinstance(self.data, dict):
            for i in range(1, n):
                key_item = items[i]
                key_val = key_item[1]

                try:
                    key_val_num = float(key_val)
                except(ValueError,TypeError):
                    key_val_num = str(key_val)

                j = i - 1
                iterations += 1
                while j >= 0:
                    try:
                        compare_val = float(items[j][1])
                    except(ValueError,TypeError):
                        compare_val = str(items[j][1])

                    if (sort_order == "Ascending" and compare_val > key_val_num) or \
                    (sort_order == "Descending" and compare_val < key_val_num):
                        items[j + 1] = items[j]
                        j -= 1
                    else:
                        break
                items[j + 1] = key_item

            return dict(items), iterations

        elif isinstance(self.data, (list, tuple)):
            for i in range(1, n):
                key_item = items[i]

                try:
                    key_num = float(key_item)
                except:
                    key_num = str(key_item)

                j = i - 1
                iterations += 1
                while j >= 0:
                    try:
                        compare_val = float(items[j])
                    except(ValueError,TypeError):
                        compare_val = str(items[j])

                    if (sort_order == "Ascending" and compare_val > key_num) or \
                        (sort_order == "Descending" and compare_val < key_num):
                        items[j + 1] = items[j]
                        j -= 1
                    else:
                        break
                items[j + 1] = key_item

            return (tuple(items) if isinstance(self.data, tuple) else items), iterations

        else:
            raise TypeError("Unsupported data type for sorting")
