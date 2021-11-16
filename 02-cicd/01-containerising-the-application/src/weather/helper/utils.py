def wind_deg_to_text(degree):
    """
    Accepts wind direction in degrees and returns a textual wind direction
    """
    sectors = ['Northerly', 'North Easterly', 'Easterly', 'South Easterly', 'Southerly', 'South Westerly', 'Westerly',
               'North Westerly']

    degree += 22.5;

    if degree < 0:
        degree = 360 - abs(degree) % 360
    else:
        degree = degree % 360;

    which_sector = int(degree // 45)
    return sectors[which_sector]
