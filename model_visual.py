# Importing Packages
import numpy as np
from datetime import datetime
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

def model_visualization(url, llat=23., ulat=51., llon=-130., rlon=-65.):
    nc = Dataset(url)
    lon = nc.variables['LON'][:]
    lat = nc.variables['LAT'][:]
    #depth = nc.variables['DEPTH'][:]
    #temp = nc.variables['TEMP'][:]
    #salt = nc.variables['SALT'][:]
    #u = nc.variables['U'][:]
    #v = nc.variables['V'][:]
    #w = nc.variables['W'][:]
    #taux = nc.variables['TAUX'][:]
    #tauy = nc.variables['TAUY'][:]
    #ssh = nc.variables['SSH'][:]
    
    return lat,lon,
    #depth,temp,salt,u,v,w,taux,tauy,ssh

    m = Basemap(projection='robin',
                llcrnrlat=llat,
                urcrnrlat=ulat,
                llcrnrlon=llon+1,
                urcrnrlon=rlon-1,
                lon_0 =180,
                resolution='i')              

# Function Calls
url = 'http://sodaserver.tamu.edu:80/opendap/SODA_2.2.8/ENSEMBLE_MEAN/SODA_2.2.8_187101.cdf'
lat, lon, = model_visualization(url)