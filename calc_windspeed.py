def windspeed(u,v,minmag = 0.1):
    mag = (u**2)+(v**2)**0.5
    output = np.where(mag>minmag,mag,minmag)
    return output

