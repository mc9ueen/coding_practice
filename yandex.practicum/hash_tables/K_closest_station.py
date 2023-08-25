from math import sqrt


def find_closest_station(metros: list, buses: list):
    distances = []
    for metro in metros:
        result = []
        for bus in buses:
            distance_between_stations = sqrt((metro[0] - bus[0]) ** 2
                                             + (metro[1] - bus[1]) ** 2)
            if int(distance_between_stations) <= 20:
                result.append(distance_between_stations)
        distances.append(result)
    return distances


if __name__ == "__main__":
    amount_of_metro_stations = int(input())
    metro_stations = [tuple(map(int, input().split()))
                      for _ in range(amount_of_metro_stations)]
    amount_of_bus_stations = int(input())
    bus_stations = [tuple(map(int, input().split()))
                    for _ in range(amount_of_bus_stations)]
    print(len(max(find_closest_station(metro_stations, bus_stations),
                  key=len)))
