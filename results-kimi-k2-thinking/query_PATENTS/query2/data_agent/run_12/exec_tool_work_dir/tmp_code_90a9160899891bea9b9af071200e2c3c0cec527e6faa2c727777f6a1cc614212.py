code = """# Load and analyze patent data
import json
import re

# Get the data
result_value = locals()['var_functions.query_db:2']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = result_value

print('Total records loaded: ' + str(len(patents_data)))

# Let's look at Patents_info to find country codes
countries = []
for i in range(min(10, len(patents_data))):
    patents_info = patents_data[i].get('Patents_info', '')
    print('Sample Patents_info ' + str(i) + ': ' + patents_info[:300])
    
    # Look for country code patterns
    country_match = re.search(r'country_code\s*[:=]\s*["\']?([A-Z]{2})', patents_info, re.IGNORECASE)
    if country_match:
        countries.append(country_match.group(1))

print('Found country codes: ' + str(set(countries)))

# Try to extract country codes more broadly
german_patents = []
for rec in patents_data:
    patents_info = rec.get('Patents_info', '')
    if 'DE' in patents_info or 'Germany' in patents_info or 'country_code: DE' in patents_info:
        german_patents.append(rec)

print('Potential German patents: ' + str(len(german_patents)))

print('__RESULT__:')
print(str(len(patents_data)))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433}

exec(code, env_args)
