cars = ["audi", "audi", "audi", "porsche", "porsche", "Benz"]
final_counted_cars={}
for car in cars:
    if car not in final_counted_cars:
        final_counted_cars.update({car:1})
    elif car in final_counted_cars:
        final_counted_cars.update({car:final_counted_cars[car]+1})
print(final_counted_cars)
    