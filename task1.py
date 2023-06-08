import json

# Read the JSON file
with open('pos_0.png.json', 'r') as file:
    data = json.load(file)

# Create the given formatte
formatted_data = [
    {
        "dataset_name": "pos_0.png.json",
        "image_link": "",
        "annotation_type": "image",
        "annotation_objects": {},
        "annotation_attributes": {}
    }
]


for obj in data['objects']:
    class_title = obj['classTitle'].lower().replace(' ', '_')
    presence = 1 if class_title in ['vehicle', 'license_plate'] else 0

    bbox = obj['points']['exterior']
    x_min = bbox[0][0]
    y_min = bbox[0][1]
    x_max = bbox[1][0]
    y_max = bbox[1][1]


    formatted_data[0]['annotation_objects'][class_title] = {
        "presence": presence,
        "bbox": [x_min, y_min, x_max, y_max]
    }

   
    for tag in obj['tags']:
        tag_name = tag['name']
        tag_value = tag['value']
        if tag_name == 'Difficulty Score':
            tag_name = 'Difficulty_Score'
        if tag_name == 'Value':
            tag_name = 'License_Plate_Value'

        if class_title not in formatted_data[0]['annotation_attributes']:
            formatted_data[0]['annotation_attributes'][class_title] = {}
        formatted_data[0]['annotation_attributes'][class_title][tag_name] = tag_value


with open('formatted_pos_0.png.json', 'w') as file:
    json.dump(formatted_data, file, indent=4)
