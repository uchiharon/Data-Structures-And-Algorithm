def truckTour(petrolpumps):
    # Write your code here

    max_fuel = start_point = 0
    for i in range(len(petrolpumps)):
        max_fuel += petrolpumps[i][0] - petrolpumps[i][1]
        if max_fuel < 0:
            start_point = i + 1
            max_fuel = 0
    return start_point