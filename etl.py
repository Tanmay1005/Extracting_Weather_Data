# Important Libraries 
#%%
import requests
import pandas as pd

def fetch_weather_data(city: str, api_key: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def transform_weather_data(data: dict):
    if not data:
        return None

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'wind_deg': data['wind']['deg']
    }
    return weather_info

def load_data_to_csv(data: dict, file_path: str):
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)

def main():
    api_key = 'Your_API_Key'
    city = 'Mumbai'
    weather_data = fetch_weather_data(city, api_key)
    if weather_data:
        transformed_data = transform_weather_data(weather_data)
        output_file = 'weather_data.csv'
        load_data_to_csv(transformed_data, output_file)
        print(f'Data saved to {output_file}')
    else:
        print('Failed to fetch data')

if __name__ == '__main__':
    main()
# %%
