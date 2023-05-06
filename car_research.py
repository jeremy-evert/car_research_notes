import requests
from bs4 import BeautifulSoup
import csv

def get_car_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    car_listings = soup.find_all('div', class_='mmy-results-card')

    data = []
    for car in car_listings:
        manufacturer = car.find('span', class_='make').text.strip()
        origin = car.find('span', class_='origin').text.strip()
        weight = car.find('span', class_='weight').text.strip()
        price = car.find('span', class_='price').text.strip()
        trim = car.find('span', class_='trim').text.strip()
        towing_capacity = car.find('span', class_='towing-capacity').text.strip()
        num_rows_seats = car.find('span', class_='rows-seats').text.strip()
        seating_capacity = car.find('span', class_='seating-capacity').text.strip()
        passenger_cargo = car.find('span', class_='passenger-cargo').text.strip()
        city_mileage = car.find('span', class_='city-mpg').text.strip()
        highway_mileage = car.find('span', class_='hwy-mpg').text.strip()

        car_data = {
            'Manufacturer': manufacturer,
            'Country of Origin': origin,
            'Vehicle Weight': weight,
            'Price': price,
            'Trim Level': trim,
            'Towing Capacity': towing_capacity,
            'Number of Rows of Seats': num_rows_seats,
            'Seating Capacity': seating_capacity,
            'Passenger Cargo': passenger_cargo,
            'City Gas Mileage': city_mileage,
            'Highway Gas Mileage': highway_mileage
            # Add more fields as needed
        }
        data.append(car_data)

    return data

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to '{filename}' successfully.")

if __name__ == '__main__':
    url = 'https://www.edmunds.com/new-cars/'
    car_data = get_car_data(url)
    save_to_csv(car_data, 'car_data.csv')
