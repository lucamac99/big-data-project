from matplotlib import legend
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas
from shapely.geometry import Polygon
import warnings
warnings.filterwarnings(action='ignore')
from dataCleaning import data_cleaning

df, df_rent_price, df_house_price = data_cleaning()

# first plots of the data
""" df = df[df['index'].isna() == False]
df.groupby(['country'])['index'].mean().plot(kind='bar', figsize=(10,5), title='Average index by country', xlabel='Country', ylabel='Average index')
df.groupby(['country'])['price'].mean().plot(kind='bar', figsize=(10,5), title='Average price by country', xlabel='Country', ylabel='Average price')
 """
# bar plot of the rent_price index
ax = plt.gca()
df_rent_price.plot( x = 'country', y = '2020', ax = ax, figsize=(10,5), legend=True, kind='bar', title='Average rent price by country', xlabel='Country', ylabel='Average rent price')
plt.show()

# compare the rent_price and house_price indexes with a bar plot
countries = df_rent_price['country']
rentSeries = df_rent_price['2020']
priceSeries = df_house_price['2020']
df_bar = pd.DataFrame({"Rent":rentSeries,"Price":priceSeries, "country":countries})
ax = df_bar.plot.bar(x = 'country',color=["SkyBlue","IndianRed"], rot=0, title="Index complare\nRent vs. Price", figsize=(10,5))
ax.set_xlabel("Country")
ax.set_ylabel("Indexes")
plt.xticks(rotation=90)
plt.show()

# bar plot of the house_price index
ax = plt.gca()
df_house_price.plot( x = 'country', y = '2020', ax = ax, figsize=(10,5), legend=True, kind='bar', title='Average house price by country', xlabel='Country', ylabel='Average house price')

### GEOPLOTS ###

# Geoplots, first by year and then larger with last year
plt.rcParams['figure.figsize']=(12,10)
plt.rcParams['font.size']=12

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
europe=world[world.continent=='Europe']

#Remove Russia from map of Europe
europe=europe[(europe.name!='Russia')]

# Create a custom polygon
polygon = Polygon([(-25,35), (40,35), (40,75),(-25,75)])
poly_gdf = geopandas.GeoDataFrame([1], geometry=[polygon], crs=world.crs)

#Clip polygon from the map of Europe
europe=geopandas.clip(europe, polygon) 

selected_countries=europe[europe.name.isin(list(df_rent_price.country))]
df_rent_price['name'] = df_rent_price['country']
selected_countries=selected_countries.merge(df_rent_price, on='name',how='left')

#Range of Variable you see as map color. Here I select the minimum and maximum of all the years selected.
vmin=selected_countries[['1996','2000','2005','2010','2015','2020']].min().min()
vmax=selected_countries[['1996','2000','2005','2010','2015','2020']].max().max()

#Create subplots with 2 rows and 3 columns
fig,axs=plt.subplots(2,3)
fig.suptitle('Rent indicator price in Europe 1996–2020', fontweight='bold',fontsize=15)
#Adjust space betweeen rows
plt.subplots_adjust(bottom=0.2, top=0.9, hspace=0.25)
axs[0,0]=europe.plot(color='whitesmoke',edgecolor='black',ax=axs[0,0])
selected_countries.plot('1996',cmap='Reds',edgecolor='black',ax=axs[0,0], vmin=vmin, vmax=vmax)
axs[0,0].set_title('1996')
axs[0,0].xaxis.set_visible(False)
axs[0,1]=europe.plot(color='whitesmoke',edgecolor='black',ax=axs[0,1])
selected_countries.plot('2000',cmap='Reds',edgecolor='black',ax=axs[0,1], vmin=vmin, vmax=vmax)
axs[0,1].set_title('2000')
axs[0,1].xaxis.set_visible(False)
axs[0,1].yaxis.set_visible(False)
axs[0,2]=europe.plot(color='whitesmoke',edgecolor='black',ax=axs[0,2])
selected_countries.plot('2005',cmap='Reds',edgecolor='black',ax=axs[0,2], vmin=vmin, vmax=vmax)
axs[0,2].set_title('2005')
axs[0,2].xaxis.set_visible(False)
axs[0,2].yaxis.set_visible(False)
axs[1,0]=europe.plot(color='whitesmoke',edgecolor='black',ax=axs[1,0])
selected_countries.plot('2010',cmap='Reds',edgecolor='black',ax=axs[1,0], vmin=vmin, vmax=vmax)
axs[1,0].set_title('2010')
axs[1,1]=europe.plot(color='whitesmoke',edgecolor='black',ax=axs[1,1])
selected_countries.plot('2015',cmap='Reds',edgecolor='black',ax=axs[1,1], vmin=vmin, vmax=vmax)
axs[1,1].set_title('2015')
axs[1,1].yaxis.set_visible(False)
axs[1,2]=europe.plot(color='whitesmoke',edgecolor='black',ax=axs[1,2])
selected_countries.plot('2020',cmap='Reds',edgecolor='black',ax=axs[1,2], vmin=vmin, vmax=vmax)
axs[1,2].set_title('2020')
axs[1,2].yaxis.set_visible(False)

# add colorbar
cax = fig.add_axes([0.92, 0.2, 0.03, 0.7]) #[left, bottom, width, height]
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# fake up the array of the scalar mappable.
sm._A = []
lgd=fig.colorbar(sm, cax=cax).set_label('gCO$_2$e/kWh', rotation=0,y=1.05, labelpad=-35)
plt.savefig('Rent_price.jpeg',
 dpi=300)
plt.show()

# single larger plot of European rent price
fig,ax=plt.subplots()
fig.suptitle('Rent price index in Europe 2020', fontweight='bold',fontsize=15)
ax=europe.plot(color='whitesmoke',edgecolor='black',ax=ax)
selected_countries.plot('2020',cmap='Reds',edgecolor='black',ax=ax, vmin=vmin, vmax=vmax, legend=True)
ax.set_title('2020')
ax.xaxis.set_visible(False)

plt.savefig('Rent_price.jpeg', dpi=300)
plt.show()

# let's do the same with the house_price index
selected_countries=europe[europe.name.isin(list(df_house_price.country))]
df_house_price['name'] = df_house_price['country']
selected_countries=selected_countries.merge(df_house_price, on='name',how='left')

#Range of Variable you see as map color. Here I select the minimum and maximum of all the years selected.
vmin=selected_countries[['2020']].min().min()
vmax=selected_countries[['2020']].max().max()

fig,ax=plt.subplots()
fig.suptitle('Housing price index in Europe 2020', fontweight='bold',fontsize=15)
ax=europe.plot(color='whitesmoke',edgecolor='black',ax=ax)
selected_countries.plot('2020',cmap='Reds',edgecolor='black',ax=ax, vmin=vmin, vmax=vmax, legend=True)
ax.set_title('2020')
ax.xaxis.set_visible(False)

plt.savefig('Rent_price.jpeg', dpi=300)
plt.show()

#############################################################################################################################

COUNTRIES = df["country"].values
COUNTRIES_ = np.unique(COUNTRIES)

df['name'] = df['country']
df = df.groupby(['country']).mean()
print(df)

PRICE_LENGTH = df["price"].values
INDEX_LENGTH = df["index"].values

COLORS = ["#1B9E77", "#D95F02", "#7570B3", "#E7298A", "#66A61E", "#E6AB02", "#F0F8FF", "#000000", "#7570B3", "#00FFFF", "#00E672", "#A7AB12", "#1AAE90", "#00FF00", "#0000AA", "#FFF000", "#66FF00", "#808080", "#B22222", "#903FEF", "#676767", "#FEA000", "#66A51E", "#EEFF00", "#DC143C", "#0065FF", "#8787FF"]

fig, ax = plt.subplots(figsize=(8,8))
for country, color in zip(COUNTRIES_, COLORS):
    idxs = np.where(COUNTRIES_ == country)
    # No legend will be generated if we don't pass label=coutry
    ax.scatter(
        PRICE_LENGTH[idxs], INDEX_LENGTH[idxs], label=country,
        s=50, color=color, alpha=0.7,
    )
plt.xlabel("Price (€)") 
plt.ylabel("Index")
ax.legend();