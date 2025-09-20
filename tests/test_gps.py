from panic_bracelet.gps import get_location

def test_get_location():
    lat, lon = get_location()
    assert isinstance(lat, float)
    assert isinstance(lon, float)
