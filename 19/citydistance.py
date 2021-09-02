"""
Work out the distance (user specified units) given two cities using haversine equation
"""
import sys
from pygeocoder import Geocoder
import numpy as np


def get_distance(loca, locb):
    """
    use haversine forumla
    """
    earth_rad = 6371.0
    dlat = np.deg2rad(locb[0] - loca[0])
    dlon = np.deg2rad(locb[1] - loca[1])
    app = np.sin(dlat / 2) * np.sin(dlat / 2) + np.cos(np.deg2rad(loca[0])) * np.cos(
        np.deg2rad(locb[0])
    ) * np.sin(dlon / 2) * np.sin(dlon / 2)
    cpp = 2 * np.arctan2(np.sqrt(app), np.sqrt(1 - app))
    return earth_rad * cpp


def get_latlongs(location):
    """
    get lattitude and longitude
    """
    geocoder = Geocoder()
    return geocoder.geocode(location)[0].coordinates


def convert_km_to_miles(kilometer):
    """
    convert kilometers to miles
    """
    miles_per_km = 0.621371192
    return kilometer * miles_per_km


def main():
    """
    wrapper function
    """
    # get first city
    print("Type the first City: ")
    citya = input()

    # get second city
    print("Type the second city: ")
    cityb = input()

    # get units
    units = ""
    while (units != "km") & (units != "m"):
        print("Type distance units (miles or kilometers): ")
        units = str.lower(input())
        if units in ["clicks", "km", "kilometers", "kilometer"]:
            units = "km"
        elif units in ["m", "mile", "miles"]:
            units = "m"
        else:
            print("units not recognised, please try again")

    # find the distance in km
    try:
        distance = get_distance(get_latlongs(citya), get_latlongs(cityb))
        # display the distance
        if units == "km":
            print(str(distance), " km")
        else:
            distance = convert_km_to_miles(distance)
            print(str(distance), " miles")

    except KeyError:
        print("Error raised.  Are the input cities correct?")


if __name__ == "__main__":
    sys.exit(main())
