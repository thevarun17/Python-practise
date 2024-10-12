import logging

# Configure logging
logging.basicConfig(filename='run.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_data_from_file(filename):
    country_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('#')
                if len(parts) == 4:
                    country = parts[0]
                    ip_address = parts[1]
                    if country in country_data:
                        country_data[country].append(ip_address)
                    else:
                        country_data[country] = [ip_address]
        logging.info(f"Successfully read data from file '{filename}'")
    except FileNotFoundError:
        logging.error(f"Error: File '{filename}' not found.")
    except Exception as e:
        logging.error(f"Error reading file '{filename}': {str(e)}")
    return country_data

# Example usage:
filename = 'newcountries.txt'  # Assuming data.txt is in the same directory as your script
logging.info(f"Starting script with file '{filename}'")
data = read_data_from_file(filename)
for country, ips in data.items():
    print(f'{country}: {ips}')
