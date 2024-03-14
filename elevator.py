"""
Notes for executing: run on command line with the following format: 
python3 elevator.py <starting floor> <floors to visit> 

Resources used: 
https://realpython.com/knn-python/ (used a modified/simplified version of nearest neighbors algorithm to 
find the nearest floor to the current floor, and continue to calculate the total travel cost)

https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/ (python lambda function)

"""

import sys


def calculate_travel_time(starting_floor, floors_to_visit):
    total_travel_time = 0
    floor_order = []
    floor_order.append(starting_floor)
    current_floor = starting_floor # nearest neighbor approach

    while len(floors_to_visit) > 0:

        nearest_floor = min(floors_to_visit, key=lambda x: abs(x - current_floor)) # find nearest floor to current_floor, could also use numpy to do this (more lines of code though)

        total_travel_time += abs(current_floor - nearest_floor) * 10 # calculate total travel time

        current_floor = nearest_floor # update current floor

        floor_order.append(current_floor) # add to floor order list to output

        floors_to_visit.remove(nearest_floor)  # remove from floors visited

    return total_travel_time, floor_order



def main():

    if len(sys.argv) != 3:
        print("Usage: <filename> <starting_floor> <floor_list>") # error checking: too many or too little command line arguments
        sys.exit(1)

    try:
        starting_floor = int(sys.argv[1]) 
        floors_to_visit = [int(x) for x in sys.argv[2].split(",")]
    except ValueError:
        print("Invalid input: please provide valid integer floor values") # error checking: if invalid input, error out
        sys.exit(1)

   
    total_time, floor_order = calculate_travel_time(starting_floor, floors_to_visit)

    floors_to_visit.insert(0, starting_floor) # add starting floor to beginning of list for printing


    print(total_time, end=" ")
    print(",".join(map(str, floor_order))) # prints travel time and floor order in correct format

if __name__ == "__main__":
    main()




