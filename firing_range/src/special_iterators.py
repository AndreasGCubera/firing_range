specials = ["pumpking spice latte", "caramel macchiato", "mocha cappuccino"]

first_iterator = specials.__iter__()
second_iterator = specials.__iter__()
print(type(first_iterator))

item = first_iterator.__next__()
print(item)

item = first_iterator.__next__()
print(item)

first_first_iterator = iter(specials)
second_second_iterator = iter(specials)

for item in specials:
    print(item)

for number, (item) in enumerate(specials, start=1):
    print(f"#{number}. {item}")
