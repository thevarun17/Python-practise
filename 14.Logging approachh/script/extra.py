import json

def extract_input_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data

def process_file_data(fdata):
    countries = {}
    for line in fdata:
        line = line.strip()  # Remove any leading/trailing whitespace
        if '#' in line:
            country_name, info = line.split('#', 1)
            if country_name not in countries:
                countries[country_name] = []
            countries[country_name].append(info)
    return countries

def create_output_file(jsondata, output_filename):
    try:
        with open(output_filename, 'w') as f:
            json.dump(jsondata, f, indent=4)
        return "success"
    except IOError as e:
        return f"Error writing file: {e}"

# Example usage
input_filename = 'newcountries.txt'
output_filename = 'output.txt'

# Extract input data
data = extract_input_data(input_filename)

# Process the file data
processed_data = process_file_data(data)

# Create output file
result = create_output_file(processed_data, output_filename)
print(result)
