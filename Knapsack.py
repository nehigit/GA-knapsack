
class Knapsack:
    def __init__(self, max_capacity, items):
        self.max_capacity = max_capacity
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def get_total_value(self, zero_one_list):
        # Returns total value of items in the knapsack
        total_weight = total_value = 0
        for i in range(len(zero_one_list)):
            item, weight, value = self.items[i]
            if total_weight + weight <= self.max_capacity:
                total_weight += zero_one_list[i] * weight
                total_value += zero_one_list[i] * value
        return total_value

    def print_items(self, zero_one_list):
        total_weight = total_value = 0
        for i in range(len(zero_one_list)):
            item, weight, value = self.items[i]
            if total_weight + weight <= self.max_capacity:
                if zero_one_list[i] > 0:
                    total_weight += weight
                    total_value += value
                    print(f'Item: {item}: weight = {weight}, value = {value}, knapsack weight: {round(total_weight, 2)}')
        print(f'\nTotal knapsack weight: {round(total_weight, 2)}\nTotal knapsack value: {total_value}')

