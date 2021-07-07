import src.functions as fn

if __name__ == '__main__':

    # given link station
    stations = [[0, 0, 10], [20, 20, 5], [10, 0, 12]]
    # given device points
    inputs = [(0, 0), (100, 100), (15, 10), (18, 18)]

    for point in inputs:
        fn.best_link_station(stations, point)
