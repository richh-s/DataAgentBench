code = """import json

business_data_file = locals()['var_functions.query_db:0']
if isinstance(business_data_file, str) and business_data_file.endswith('.json'):
    with open(business_data_file, 'r') as f:
        business_data = json.load(f)
else:
    business_data = locals()['var_functions.query_db:0']

print('Total businesses:', len(business_data))
print()
print('First business hours field:', business_data[0]['hours'])
print('Type:', type(business_data[0]['hours']))
print()
print('Second business:')
print('Name:', business_data[1]['name'])
print('Hours:', business_data[1]['hours'])
print()
print('Type of second business hours:', type(business_data[1]['hours']))
if business_data[1]['hours'] != 'None':
    try:
        parsed = json.loads(business_data[1]['hours'])
        print('Successfully parsed JSON')
        print('Parsed type:', type(parsed))
        print('First 2 days:', parsed[:2])
    except Exception as e:
        print('Error parsing:', str(e))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
