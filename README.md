Dark Sky
========

A small, Pythonic wrapper for the [Dark Sky API](https://developer.darkskyapp.com/docs).

Make sure to register for a [Mapquest API key](http://developer.mapquest.com/)
to take full advantage of the library.


Installation
------------

```
pip install darksky
```

It's then pretty beneficial to go ahead and save your API keys as environment
variables.

```
export DARK_SKY_API=my_dark_sky_api_key
export MAPQUEST_API_KEY=my_mapquest_api_key
```


Usage
-----

```python
import darksky as ds

# Haven't saved your API key as an environment variable?
ds.key('my_dark_sky_api_key')

# You can also save your Mapquest API key
ds.mapquest('mapquest_api_key')

# Look up interesting storms
ds.interesting()

# Get a brief forecast for a latitude/longitude
ds.brief(37.775002, -122.418297)

# Or for a given address
ds.brief('155 9th St San Francisco, CA')

# Alternatively, get the full forecast
ds.forecast(37.775002, -122.418297)

# Same goes for an address
ds.forecast('155 9th St San Francisco, CA')

# Fetch the latitude/longitude manually
ds.location('155 9th St San Francisco, CA')
```
