# ============================================================================
# GeoJSON. Copyright (C) 2007 Sean C. Gillies
#
# See ../LICENSE.txt
# 
# Contact: Sean Gillies, sgillies@frii.com
# ============================================================================

"""
SimpleWebFeature is a working example of a class that satisfies the Python geo
interface.
"""

from geojson.base import GeoJSON
import geojson.geometry 

class Feature(GeoJSON):

    """A (WGS84) GIS Feature."""

    def __init__(self, id=None, geometry=None, properties=None, **extra):
        super(Feature, self).__init__(**extra)
        self.id = id
        self.geometry = self.to_instance(geometry, strict=True)
        if properties is None:
            properties = {}
        self.properties = properties 

    @property
    def __geo_interface__(self):
        d = super(Feature, self).__geo_interface__
        d.update(id=self.id,
                 geometry=self.geometry.__geo_interface__,
                 properties=self.properties)
        return d


class FeatureCollection(GeoJSON):

    """A collection of Features."""

    def __init__(self, features, **extra):
        super(FeatureCollection, self).__init__(**extra)
        self.features = features

    @property
    def __geo_interface__(self):
        d = super(FeatureCollection, self).__geo_interface__
        d.update(features=self.features)
        return d
    
   

