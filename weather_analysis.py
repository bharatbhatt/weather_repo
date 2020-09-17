import requests
import matplotlib.pyplot as plt 

api_token="api_token_shared"
website_url = "http://api.openweathermap.org/data/2.5/forecast?q=" +"Delhi" + "&appid=" + api_token + "&units=metric"
res = requests.get(website_url)
if res.status_code == 200: 
  print("Successfully Get the data") 
  json_data=res.json() 
else: 
  print("Have issue in get call. Error code{}:{}",format(res.status_code))
date_list=list()
humidity_list=list()
temp_list=list()
for k, v in json_data.items():
  if 'list' in k:
    for i in v:
      date_list.append(i['dt_txt'])
      humidity_list.append(i['main']['humidity'])
      temp_list.append(i['main']['temp'])
print(temp_list)
print(humidity_list)
print(date_list)
plt.grid(color='b', linestyle=':', linewidth=0.1)
plt.plot(date_list, temp_list, color ='orange',  
         label ="Temperature'C" ) 
plt.plot(date_list, humidity_list, color ='blue',  
         label ='Humidity%') 
plt.xlabel('Date and time ') 
plt.ylabel('Temperature and Humidity') 
plt.title('Variation of temp and humidity from 17-Sep to 22 Sep.\nNote: Data is captured 3 times a day')
plt.legend() 
plt.show() 
