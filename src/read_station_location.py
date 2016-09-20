def rand_station_locations(N=50,sed=777):
    import requests
    import random
    import re
    data = requests.get(
        "http://www.ecad.eu/download/ensembles/data/ensembles_all_stations_v13.1.txt")  # read only 20 000 chars
    Data = []

    pattern = re.compile(r"[^-\d]*([\-]{0,1}\d+\.\d+)[^-\d]*")
    results = []
    for line in data:
        line = line.split('|')
        for i in line:
            match = pattern.match(i)
            if match:
                results.append(match.groups()[0])

    pairs = []
    i = 0
    end = len(results)
    while i < end - 1:
        pairs.append((results[i], results[i + 1]))
        i += 2

    # # Choose N random stations
    random.seed(sed)
    rand_obs_number = random.sample(range(0, 10001), N)
    k = 0
    lat={}
    lon={}
    for i in rand_obs_number:
       # print(i)
        lat[k]= float(pairs[i][0])
        lon[k] = float(pairs[i][1])
        k = k + 1

    return(lat,lon)



