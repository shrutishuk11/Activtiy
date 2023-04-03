def get_discounted_cost(original_cost: int, is_member: bool) -> int:
    discount_member = 0.1
    discount_fathers_day = 0.05

    if is_member:
        discount = discount_member + discount_fathers_day
    else:
        discount = discount_fathers_day

    discounted_cost = original_cost * (1 - discount)
    discounted_cost = int(discounted_cost)
    return discounted_cost