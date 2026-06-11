readings = [10, -5, 20, 200, 15, 30, -2]
max_range = 50

valid_readings = []
discarded = 0

for r in readings:
    if r < 0 or r > max_range:
        discarded = discarded + 1
    else:
        valid_readings += [r]

        total = 0

        for r in valid_readings:
            total = total + r

            if len(valid_readings) == 0:
                average = 0
            else:
                average = total / len(valid_readings)

print("Valid  readings:", len(valid_readings))
print("Discarded   readings:", discarded)
print("Average:", average)
