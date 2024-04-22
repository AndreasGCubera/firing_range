from random import choice

colors = ["red", "blue", "yellow" "green", "black", "purple", "silver", "white"]
vehicles = ["car", "truck", "bike", None]


class Traffic:
    def __iter__(self):
        return self

    def __next__(self):
        vehicle = choice(vehicles)
        if vehicle is None:
            raise StopIteration

        color = choice(colors)

        return f"{color} {vehicle}"


def traffic():
    while True:
        vehicle = choice(vehicles)
        color = choice(colors)
        yield f"{color} {vehicle}"


count = 0
for count, vehicle in enumerate(Traffic(), start=1):
    print(f"Waiting for {vehicle}")

print(f"Merged after {count} vehicles")
