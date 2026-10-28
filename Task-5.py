usage = float(input("Enter monthly data usage in GB: "))
budget = float(input("Enter your budget: "))

plans = [
    ("Basic", 5, 2, 399),
    ("Standard", 15, 1, 599),
    ("Premium", 30, 0, 899)
]

best_plan = None
lowest_cost = float("inf")

for name, included, extra_rate, price in plans:
    extra = max(0, usage - included)
    cost = price + extra * extra_rate

    print(name, "plan cost: Rs.", cost)

    if cost <= budget and cost < lowest_cost:
        lowest_cost = cost
        best_plan = name

if best_plan:
    print("Best eligible plan:", best_plan)
    print("Total cost: Rs.", lowest_cost)
else:
    print("No plan fits your budget")