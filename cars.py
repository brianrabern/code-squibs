# pylint: disable-all

def only_the_red(cars):
    results = []
    for car in cars:
        if car["color"] == 'red':
            results.append(car)

    return results


def old_guzzlers(cars):
    results = []
    for car in cars:
        if car["year"] < 1980 and car["mpg"] < 12:
            results.append(car)

    return results


def big_ones(cars):
    results = []
    for car in cars:
        if car["length"] > 25 or car["max_weight"] > 4000:
            results.append(car)

    return results


def sort_by_make(cars):
    results = {}
    for car in cars:
        make = car['make']
        if make not in results:
            results[make] = []
        results[make].append(car)

    return results


my_cars = [
    {"make": "ford", "model": 8, "year": 1955},
    {"make": "chevy", "model": 12, "year": 1964},
    {"make": "ford", "model": 11, "year": 1978},
    {"make": "chevy", "model": 19, "year": 2000},
]

print(sort_by_make(my_cars))
