import os
import json

# Folder path containing the JSON files
folder_path = "C:\Users\ASUS\Downloads\sampleJson"

# List to store the JSON data from each file
json_data = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            json_data.append(data)

# Combine the JSON data into a single list
combined_data = []
for data in json_data:
    combined_data.extend(data)

# Modify class names
class_mapping = {
    "vehicle": "car",
    "license_plate": "number"
}

for data in combined_data:
    class_title = data["classTitle"]
    if class_title in class_mapping:
        data["classTitle"] = class_mapping[class_title]

# Write the combined and modified data to a new JSON file
output_file = "combined_data.json"
with open(output_file, 'w') as file:
    json.dump(combined_data, file, indent=4)

print("Combined JSON data has been saved to:", output_file)