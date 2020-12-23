import gdal,os
from gdalconst import *
import geopandas as gpd
import pandas as pd

n32w115 = gpd.read_file(r'data\SRTM_split\n32w115\polygons.gpkg')
n32w116 = gpd.read_file(r'data\SRTM_split\n32w116\polygons.gpkg')

x=1