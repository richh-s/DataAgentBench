code = """import json

# Read the full result from the file
file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Count businesses that offer either business parking or bike parking
count = 0
businesses_with_parking = []

for business in businesses:
    attributes = business.get('attributes')
    if attributes is None or attributes == 'None':
        continue
    
    has_business_parking = False
    has_bike_parking = False
    
    # Check for BusinessParking
    if isinstance(attributes, dict):
        business_parking = attributes.get('BusinessParking')
        if business_parking and business_parking != 'None':
            # Check if it's a string representation of a dict or an actual dict
            if isinstance(business_parking, str):
                # Check if any parking option is True
                if 'True' in business_parking:
                    has_business_parking = True
            elif isinstance(business_parking, dict):
                # Check if any value in the dict is True
                if any(v for v in business_parking.values() if isinstance(v, bool) and v):
                    has_business_parking = True
        
        # Check for BikeParking
        bike_parking = attributes.get('BikeParking')
        if bike_parking and bike_parking != 'None':
            if isinstance(bike_parking, str):
                if bike_parking == 'True':
                    has_bike_parking = True
            elif isinstance(bike_parking, bool):
                if bike_parking:
                    has_bike_parking = True
    
    if has_business_parking or has_bike_parking:
        count += 1
        businesses_with_parking.append(business['business_id'])

print('__RESULT__:')
print(json.dumps({'count': count, 'businesses': businesses_with_parking}))"""

env_args = {'var_functions.list_db:0': ['review', 'tip', 'user'], 'var_functions.query_db:2': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_functions.list_db:5': ['business', 'checkin'], 'var_functions.execute_python:10': ['businessid_13', 'businessid_79', 'businessid_91', 'businessid_46', 'businessid_47'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
