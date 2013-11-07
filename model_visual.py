# Importing Packages
import numpy as np
from datetime import datetime
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

def model_visualization(url, llat, ulat, llon, rlon):
    nc = Dataset(url)
    lon = nc.variables['LON'][:]
    lat = nc.variables['LAT'][:]
    #time = nc.variables['TIME1'][:]
    #depth = nc.variables['DEPTH1_3'][0:1]
    temp = nc.variables['TEMP'][:]
    #salt = nc.variables['SALT'][:]
    #u = nc.variables['U'][:]
    #v = nc.variables['V'][:]
    #w = nc.variables['W'][:]
    #taux = nc.variables['TAUX'][:]
    #tauy = nc.variables['TAUY'][:]
    #ssh = nc.variables['SSH'][:]
    
    return lat,lon,temp 
   
    m = Basemap(projection='robin',
                llcrnrlat=llat,
                urcrnrlat=ulat,
                llcrnrlon=llon+1,
                urcrnrlon=rlon-1,
                lon_0 =180,
                resolution='i')              

# Function Calls
url = 'http://sodaserver.tamu.edu:80/opendap/TEMP/SODA_2.3.1_01-01_python.cdf'
#nino 3.4 region
llat = -5.
ulat = 5.
llon = -170.
rlon = -120.
lat, lon, temp = model_visualization(url,llat,ulat,llon,rlon)