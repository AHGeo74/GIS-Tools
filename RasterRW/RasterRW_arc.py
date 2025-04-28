#RasterRW (quick ArcPy variant)-> A raster reader that takes the pixel values and writes a CSV

### IMPORTS ###

import arcpy
from arcpy.sa import *
import csv

### TEXT INSERTS ###


### CONSTANTS ###


### GLOBAL -- USER INPUT ###
dir_path =  ""
file_name = ""
csv_output = ""

### GLOBAL -- INTERNAL ###


### FUNCTIONS ###
def test_raster(raster, x, y):
    point = arcpy.management.GetCellValue(raster, f"{x} {y}")
    print(point)

def raster_loop_1(raster):

    for x in range(-180, 181, 1):  #-180, 180+1
        for y in range(-90, 91, 1): #-90, 90+1
            point = arcpy.management.GetCellValue(raster, f"{x} {y}")
            print(f"{x}, {y}, {point}")
            with open("output.csv", "a") as fp:
                writer = csv.writer(fp, delimiter=",")
                # writer.writerow(["your", "header", "foo"])  # write header
                writer.writerow((x, y, point))

def raster_loop(raster):
    
    lst = []
    
    for x in range(-180, 181, 1):  #-180, 180+1

        for y in range(-90, 91, 1): #-90, 90+1
            point = arcpy.management.GetCellValue(raster, f"{x} {y}")
            lst.append((x, y, point))
            print(f"{x}, {y}, {point}")

        with open("output.csv", "a") as fp:
            writer = csv.writer(fp, delimiter=",")
            writer.writerows(lst)

        lst = []


### MAIN PROGRAM ###
dir_path = input("Directory Path: ")

#set directory
arcpy.env.workspace = rf"{dir_path}"
print("Arcpy Workspace Defined")

raster = input("File name & extension: ")
raster_loop(raster)


input("Done?")
