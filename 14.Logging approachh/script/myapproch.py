def read_data_from_file(filename):
    country_data = {}
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
    return country_data


filename = 'newcountries.txt'
data = read_data_from_file(filename)
for country, ips in data.items():
    print(f'{country}: {ips}')
