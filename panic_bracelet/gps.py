import random

def get_location():
    """
    Returns simulated GPS coordinates as a tuple (latitude, longitude).
    Later, you can replace this with real GPS module integration.
    """
    # Example: random location in Delhi
    latitude = round(28.6139 + random.uniform(-0.01, 0.01), 6)
    longitude = round(77.2090 + random.uniform(-0.01, 0.01), 6)
    return latitude, longitude
