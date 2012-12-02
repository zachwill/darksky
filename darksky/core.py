"""
Core functionality for the Dark Sky API.

https://developer.darkskyapp.com/docs
"""

import os
import mapq
import requests as req


def key(api_key=None):
    """Save the API key in an environment variable."""
    if api_key:
        os.environ['DARK_SKY_API'] = api_key
    else:
        api_key = os.getenv('DARK_SKY_API', '')
    return api_key


def mapquest(api_key=None):
    """Save or request your Mapquest API key."""
    if api_key:
        os.environ['MAPQUEST_API_KEY'] = api_key
    else:
        api_key = os.getenv('MAPQUEST_API_KEY', '')
    return api_key


def _check_lat_lng(lat, lng):
    """Check whether the latitude and longitude of a coordinate were given."""
    if not lng:
        # Then `lat` is actually a string.
        lat, lng = location(lat)
    return (str(lat), str(lng))


def brief(lat, lng=None, api_key=None):
    """Get a brief forecast for a given location."""
    if not api_key:
        api_key = key()
    lat, lng = _check_lat_lng(lat, lng)
    url = "https://api.darkskyapp.com/v1/brief_forecast/%s/%s,%s" % (api_key, lat, lng)
    return req.get(url).json


def forecast(lat, lng=None, api_key=None):
    """Get a specific forecast for a given location."""
    if not api_key:
        api_key = key()
    lat, lng = _check_lat_lng(lat, lng)
    url = "https://api.darkskyapp.com/v1/forecast/%s/%s,%s" % (api_key, lat, lng)
    return req.get(url).json


def interesting(api_key=None):
    if not api_key:
        api_key = key()
    url = "https://api.darkskyapp.com/v1/interesting/%s" % api_key
    return req.get(url).json


def location(place):
    """Find the latitude and longitude for a location."""
    results = mapq.latlng(place)
    return (results['lat'], results['lng'])
