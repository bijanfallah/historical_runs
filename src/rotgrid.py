#!/usr/bin/python
"""

rotgrid.py
==========

This module contains routines to calculate the position of a given point as
seen in a rotated grid.

The easiest interface is by instantiating Rotgrid and calling the
transform() method.

For repeated calculations with the same lats and lons (e.g. transforming
every point on the non-rotated grid), it may be more efficient to call
rotgrid_core directly.  This requires some terms to have been
pre-calculated by the calling routine.  (Note: a version of
Rotgrid.transform() has been tried, in which previously calculated terms
were cached in a dictionary, but the dictionary lookups proved to be as
expensive as redoing the floating-point calculation.)

"""

# Standard library imports
import math

# Global variables
dtor = math.pi / 180.
rtod = 1 / dtor


class Rotgrid:
    """
    Rotated grid class.  For more info, see doc strings for '__init__'
    and 'transform' methods.
    """

    def __init__(self, lonpole, latpole,
                 polerotate=0,
                 nPoleGridLon=None,
                 lonMin=-180.):

        """
        Set up rotated grid for transformations.

        Inputs:

        lonpole, latpole: longitude (degrees) and latitude (degrees) of the
                          pole of the rotated grid, as seen in the
                          non-rotated grid

        polerotate: optional input -- by default, the calculation assumes
                    that the rotated grid is singly rotated, i.e. that the
                    common meridian which passes through poles of rotated
                    and non-rotated grid has the same longitude value in
                    both grids.  If there is additional rotation about the
                    pole of the rotated grid, then set this input to the
                    value in degrees

        nPoleGridLon: an alternative way of specifying the longitudinal
                      rotation between grids: specify as the longitude
                      (degrees) of the true north pole as seen in the
                      rotated grid.  If set, overrides polerotate.

        lonMin:  minimum longitude for output of transforms to be perfomed
                 defaults to -180 so that longitudes are normally output in
                 the range [-180, 180) but e.g. specify as 0 if [0, 360) is
                 desired.
        """

        self.lonpole = lonpole

        latpoler = latpole * dtor
        self.coslatpole = math.cos(latpoler)
        self.sinlatpole = math.sin(latpoler)

        if nPoleGridLon is None:
            self.polerotate = polerotate
        else:
            self.polerotate = lonpole - nPoleGridLon + 180.

        self.lonMin = lonMin
        self.lonMax = lonMin + 360.

    def transform(self, lon, lat, inverse=False):
        # type: (object, object, object) -> object

        """
        Performs transformations to/from rotated grid.

        Inputs:

          lon, lat: longitude (degrees) and latitude (degrees)
                    of a point X, as seen in the non-rotated grid

          inverse: optional input -- set to a true value for inverse transform
                          (coords on rotated grid to coords on nonrotated)

        Returns:

            The coordinates of the point X (in degrees) as seen in the rotated
            grid (or the non-rotated grid in case of inverse transform), as a
            2-element tuple: (longitude, latitude)

        """

        # calculate trig terms relating to longitude
        lonpole = self.lonpole

        if inverse:
            lonpole += 180.
            lon += self.polerotate

        dlonr = (lon - lonpole) * dtor
        cosdlonr = math.cos(dlonr)
        sindlonr = math.sin(dlonr)

        # likewise for latitude
        latr = lat * dtor
        coslatr = math.cos(latr)
        sinlatr = math.sin(latr)

        # now the main caluculation
        dlonrotr, latrotr = \
            rotgrid_core(self.coslatpole, self.sinlatpole,
                         cosdlonr, sindlonr,
                         coslatr, sinlatr)

        lonrot = lonpole + dlonrotr * rtod
        latrot = latrotr * rtod

        if not inverse:
            lonrot -= self.polerotate

        # put lonrot back in range
        while lonrot < self.lonMin:
            lonrot += 360.

        while lonrot >= self.lonMax:
            lonrot -= 360.

        # print "Transform returning (%s, %s)" % (lonrot, latrot)
        return (lonrot, latrot)


def rotgrid_core(coslatpole, sinlatpole,
                 cosdlon, sindlon, coslat, sinlat):
    """
    Inputs:

      coslatpole, sinlatpole:
            cos and sine of latitude of the pole
            of the rotated grid, as seen in the non-rotated grid

      sindlon, cosdlon, coslat, sinlat:
            cos and sine of longitude offset
            and cos and sine of latitude
            of a point X, as seen in the non-rotated grid

            (NB longitude offset is taken from the common meridian which
            passes through poles of rotated and non-rotated grid)

    Returns:

      The coordinates of the point X (in radians) as seen in the rotated grid.
      as a 2-element tuple: (longitude offset, latitude)

      (NB longitude offset is taken from the common meridian which
      passes through poles of the rotated of non-rotated grids)

    """

    cycdx = coslat * cosdlon

    # Evaluate rotated longitude
    dlonrot = math.atan2(coslat * sindlon,
                         cycdx * sinlatpole - sinlat * coslatpole)

    # Evaluate rotated latitude
    sinlatrot = cycdx * coslatpole + sinlat * sinlatpole

    # put in range -1 to 1 in case of slight rounding error
    #  avoid error on calculating e.g. asin(1.00000001)
    if sinlatrot > 1.:
        sinlatrot = 1.

    if sinlatrot < -1.:
        sinlatrot = -1.

    latrot = math.asin(sinlatrot)

    return (dlonrot, latrot)

# --------------------------
# main program - to test
if __name__ == "__main__":

    lonpole = 177.5
    latpole = 37.5

    lon = -3.
    lat = 51.

    polerot = 10.

    mapping = Rotgrid(lonpole, latpole, polerotate=polerot)
    (lonrot, latrot) = mapping.transform(lon, lat)
    (lon2, lat2) = mapping.transform(lonrot, latrot, inverse=True)

    print 'Rotated grid: '
    print
    print ' Location of pole of rotated grid as seen in non-rotated grid:'
    print '   Lon=%s, Lat=%s'%(lonpole,latpole)
    print
    print ' Additional axial rotation about pole of rotated grid: %s' % polerot
    print
    print 'Location of chosen point in non-rotated grid:'
    print '  Lon=%s, Lat=%s'%(lon,lat)
    print
    print 'Location of chosen point as seen in rotated grid:'
    print '  Lon=%s, Lat=%s'%(lonrot,latrot)
    print
    print 'Location of chosen point put back into non-rotated grid:'
    print '  Lon=%s, Lat=%s'%(lon2,lat2)

