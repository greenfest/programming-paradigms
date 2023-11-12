def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [64, 25, 12, 22, 11]
sort_list_imperative(numbers)
print("Отсортированный список в порядке убывания:", numbers)


def sort_list_declarative(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers


numbers = [64, 25, 12, 22, 11]
sorted_numbers = sort_list_declarative(numbers)
print("Отсортированный список в порядке убывания:", sorted_numbers)
