# https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/
import requests
from math import sqrt, pow

OPEN_SKY_API = 'https://opensky-network.org/api/states/all'


class Plane(object):

    def __init__(self, lat, long, callsign, altitude, country, ica_id):
        self.lat = lat
        self.long = long
        self.distance = 1000000
        self.callsign = callsign
        self.altitude = altitude
        self.country = country
        self.ica_id = ica_id

    def __repr__(self):
        return '<Plane lat={}, long={}, distance={}, callsign={}, altitude={}, country={}, ica_id={}/>'.format(
            self.lat, self.long, self.distance, self.callsign, self.altitude, self.country, self.ica_id)


def get_best_point(planes, x, y):
    """
    Traverse all the planes and determine the plane that has a latitude and longitude closest to the
    given point (x, y)

    :param planes: The list of plane objects to traverse
    :param x: Latitude of the point to consider
    :param y: Longitude of the point to consider
    :return: The plane which is closest to the provided point (x, y)
    """
    best_plane = None
    for p in planes:
        if p.lat is None or p.long is None:
            continue

        dist = calculate_distance(x, y, p.lat, p.long)
        if best_plane is None or dist < best_plane.distance:
            p.distance = dist
            best_plane = p

    return best_plane


def calculate_distance(p1, p2, q1, q2):
    """
    Calculate the distance between the two points using the Euclidean distance formular.
    https://en.wikipedia.org/wiki/Euclidean_distance

    :param p1:
    :param p2:
    :param q1:
    :param q2:
    :return: The distance between the points
    """
    return sqrt(pow(p1 - q1, 2) + pow(p2 - q2, 2))


def load_plane_data():
    """
    Loads the plane data from the OpenSky API. Read their documentation here:
    https://opensky-network.org/apidoc/rest.html

    :return: List of plane objects, constructed based on the data returned from the Open Sky API.
    """
    req = requests.get(OPEN_SKY_API).json()
    planes = []
    for p in req['states']:
        plane = Plane(
            lat=p[6],
            long=p[5],
            callsign=p[1],
            altitude=p[7],
            country=p[2],
            ica_id=p[0]
        )
        planes.append(plane)

    return planes


p = load_plane_data()
print('Closest to Eifel Tower: {}'.format(get_best_point(p, 48.8584, 2.2945)))
print('Closest to JFK: {}'.format(get_best_point(p, 40.6413, 73.7781)))

