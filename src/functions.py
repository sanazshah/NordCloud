# general function script
import math

def power(st: list, in_point: tuple) -> float:
    '''
    calculating a link station’s power
    :param st: the link station
    :param in_point: the point where the device is located
    :return: power's link station
    '''
    d = math.sqrt((st[0] - in_point[0])**2 + (st[1] - in_point[1])**2)
    power = 0 if d > st[2] else (st[2] - d) ** 2
    return power


def best_link_station(stations: list, device_point: tuple)-> None:
    '''
    finding the most suitable link station
    :param stations: List of link stations
    :param in_point:the point where the device is located
    :return:  the most suitable (with most power) link station
    '''
    powers = [power(st, device_point) for st in stations]
    win_power = max(powers)
    index_a = powers.index(win_power)
    winner = stations[index_a]
    if win_power != 0:
        print(
            f"Best link station for point {device_point[0]},{device_point[1]} is {winner[0]},{winner[1]} with power {win_power}")
    else:
        print(
            f"No link station within reach for point {device_point[0]},{device_point[0]}")