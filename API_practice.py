#!/usr/bin/env python
# coding: utf-8

# In[11]:


x = [25.12903645, 25.92017388, 26.62509167, -59.98969384, 37.30571269]
y = [-67.59741259, 11.09532135, 74.84233102, -76.89176677, -61.13376282]
coordinates = zip(x, y)


# In[12]:


# Use the tuple() function to display the latitude and longitude combinations.
for coordinate in coordinates:
    print(coordinate[0], coordinate[1])


# In[13]:


from citipy import citipy


# In[14]:


for coordinate in coordinates:
    print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name,
          citipy.nearest_city(coordinate[0], coordinate[1]).country_code)
  


# In[17]:


import requests
requests.__version__


# In[33]:


# Import the requests library.
import requests

# Import the API key.
from config import weather_api_key


# In[34]:


url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
print(url)


# In[35]:


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
print(city_url)


# In[36]:


city_weather = requests.get(city_url)
city_weather


# In[37]:


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Bston"
city_weather = requests.get(city_url)
city_weather


# In[38]:


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
city_weather


# In[39]:


city_weather.text


# In[40]:


city_weather.json()


# In[41]:


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
if city_weather.status_code == 200:
    print(f"City Weather found.")
else:
    print(f"City weather not found.")


# In[45]:


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Bston"
city_weather = requests.get(city_url)
if city_weather.json():
    print(f"City Weather found.")
else:
    print(f"City weather not found.")


# In[46]:


print(city_url)


# In[47]:


# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
city_weather.json()


# In[48]:


boston_data = city_weather.json()


# In[49]:


boston_data['sys']


# In[50]:


boston_data['sys']['country']


# In[51]:


boston_data['dt']


# In[52]:


lat = boston_data["coord"]["lat"]
lng = boston_data["coord"]["lon"]
max_temp = boston_data["main"]["temp_max"]
humidity = boston_data["main"]["humidity"]
clouds = boston_data["clouds"]["all"]
wind = boston_data["wind"]["speed"]
print(lat, lng, max_temp, humidity, clouds, wind)


# In[53]:


from datetime import datetime
# Get the date from the JSON file.
date = boston_data["dt"]
# Convert the UTC date to a date format with year, month, day, hours, minutes, and seconds.
datetime.utcfromtimestamp(date)


# In[54]:


datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')


# In[55]:


city_data = []


# In[ ]:




