import requests
from bs4 import BeautifulSoup
import csv

def get_car_data():
    # Define a dictionary of car manufacturers and their associated websites
    car_manufacturers = {
        'Subaru': 'https://www.subaru.com/',
        'Ford': 'https://www.ford.com',
        'Chevrolet': 'https://www.chevrolet.com',
        'Toyota': 'https://www.toyota.com',
        'Honda': 'https://www.honda.com',
        # Add other car manufacturers and their websites here
    }

    # Create a list to store the car data
    car_data = []

    # Iterate over each car manufacturer
    for manufacturer, website in car_manufacturers.items():
        # Send a GET request to the car manufacturer's website
        response = requests.get(website)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the car listings on the page
        car_listings = soup.find_all('div', class_='car-listing')

        # Extract data for each car listing
        for car in car_listings:
            vehicle_weight = car.find('span', class_='weight').text
            price = car.find('span', class_='price').text
            trim_level = car.find('span', class_='trim-level').text
            towing_capacity = car.find('span', class_='towing-capacity').text
            rows_of_seats = car.find('span', class_='rows-of-seats').text
            seating_capacity = car.find('span', class_='seating-capacity').text
            passenger_cargo = car.find('span', class_='passenger-cargo').text
            city_gas_mileage = car.find('span', class_='city-gas-mileage').text
            highway_gas_mileage = car.find('span', class_='highway-gas-mileage').text
            heated_seats = car.find('span', class_='heated-seats').text
            adaptive_cruise_control = car.find('span', class_='adaptive-cruise-control').text
            backup_camera = car.find('span', class_='backup-camera').text

            # Create a dictionary for the car data
            car_info = {
                'Manufacturer': manufacturer,
                'Website': website,
                'Vehicle Weight': vehicle_weight,
                'Price': price,
                'Trim Level': trim_level,
                'Towing Capacity': towing_capacity,
                'Number of Rows of Seats': rows_of_seats,
                'Seating Capacity': seating_capacity,
                'Passenger Cargo': passenger_cargo,
                'City Gas Mileage': city_gas_mileage,
                'Highway Gas Mileage': highway_gas_mileage,
                'Heated Front Row Seats': heated_seats,
                'Adaptive Cruise Control': adaptive_cruise_control,
                'Backup Camera': backup_camera
            }

            # Add the car data to the list
            car_data.append(car_info)

    # Write the car data to a CSV file
    if car_data:
        with open('car_data.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=car_data[0].keys())

            # Write the header row
            writer.writeheader()

            # Write the data rows
            writer.writerows(car_data)

        print("Car data has been successfully downloaded and saved to 'car_data.csv'.")

# Call the function to start the scraping process
get_car_data()

