def solution(clothes):
    category_count = dict()
    for name, category in clothes:
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
    count = 1
    for value in category_count.values():
        count *= value + 1
    return count - 1
