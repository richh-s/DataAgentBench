code = """import json

# Load the data from the file
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Get the distinct business IDs that had reviews in 2018
business_ids_2018 = locals()['var_functions.query_db:5']

# Convert business_ref to business_id format (businessref_X -> businessid_X)
business_ids_to_check = []
for item in business_ids_2018:
    ref_id = item['business_ref']  # e.g., "businessref_13"
    num = ref_id.split('_')[1]     # e.g., "13"
    business_id = f"businessid_{num}"  # e.g., "businessid_13"
    business_ids_to_check.append(business_id)

# Count businesses with BusinessParking or BikeParking
count = 0
businesses_with_parking = []

for business in business_data:
    if business['business_id'] in business_ids_to_check:
        attributes = business.get('attributes', {})
        if attributes and attributes != 'None':
            # Check for BikeParking
            bike_parking = attributes.get('BikeParking')
            has_bike_parking = bike_parking == 'True'
            
            # Check for BusinessParking
            business_parking = attributes.get('BusinessParking')
            has_business_parking = False
            if business_parking and business_parking != 'None':
                # Check if any parking type is True
                if isinstance(business_parking, str):
                    # Parse the string representation of dict
                    try:
                        parking_dict = eval(business_parking)
                        has_business_parking = any(parking_dict.values())
                    except:
                        has_business_parking = False
            
            # Check if either parking type is available
            if has_bike_parking or has_business_parking:
                count += 1
                businesses_with_parking.append({
                    'business_id': business['business_id'],
                    'bike_parking': bike_parking,
                    'business_parking': business_parking
                })

print("__RESULT__:")
print(json.dumps({
    'count': count,
    'businesses': businesses_with_parking
}))"""

env_args = {'var_functions.query_db:0': [{'business_ref': 'businessref_77'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}], 'var_functions.query_db:2': [{'business_ref': 'businessref_77'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_43'}], 'var_functions.query_db:5': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_80'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
