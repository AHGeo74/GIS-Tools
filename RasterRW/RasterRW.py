#RasterRW -> A raster reader that takes the pixel values and writes a CSV

# IMPORTS
import pandas as pd
import geopandas as gpd
import rasterio as rio
import os, math, time, sys

# TEXT INSERTS


# CONSTANTS


# GLOBAL -- USER INPUT
dir_path =  ""
file_name = ""
csv_output = ""

# GLOBAL -- INTERNAL


# FUNCTIONS
def test_raster(raster, x, y):
    print(f'test return = {raster[x, y]}')

def raster_loop(raster):
    
    for x in range(0, raster.length(), 1):
        for y in range(0, raster.width(), 1):
            pass
        pass


# MAIN PROGRAM

