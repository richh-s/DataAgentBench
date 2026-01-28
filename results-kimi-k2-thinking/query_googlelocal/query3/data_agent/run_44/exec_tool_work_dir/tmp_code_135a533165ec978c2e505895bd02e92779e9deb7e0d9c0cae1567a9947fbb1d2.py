code = """import json

business_data_file = locals()['var_functions.query_db:0']
if isinstance(business_data_file, str) and business_data_file.endswith('.json'):
    with open(business_data_file, 'r') as f:
        business_data = json.load(f)
else:
    business_data = locals()['var_functions.query_db:0']

output = []
output.append(f'Total businesses: {len(business_data)}')
output.append('')
output.append(f'First business hours field: {business_data[0]["hours"]}')
output.append(f'Type: {type(business_data[0]["hours"])}')
output.append('')
output.append('Second business:')
output.append(f'Name: {business_data[1]["name"]}')
output.append(f'Hours: {business_data[1]["hours"]}')
output.append('')
output.append(f'Type of second business hours: {type(business_data[1]["hours"])}')
if business_data[1]['hours'] != 'None':
    try:
        parsed = json.loads(business_data[1]['hours'])
        output.append('Successfully parsed JSON')
        output.append(f'Parsed type: {type(parsed)}')
        output.append(f'First 2 days: {parsed[:2]}')
    except Exception as e:
        output.append(f'Error parsing: {str(e)}')

result_str = json.dumps(output)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
