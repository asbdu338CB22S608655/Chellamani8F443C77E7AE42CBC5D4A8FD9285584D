def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices

product_list = ["bangles", "chains", "earings", "ring", "bangles"]
target = "bangles"

result = linear_search_product(product_list, target)
print(result)
# Output: [0, 3]