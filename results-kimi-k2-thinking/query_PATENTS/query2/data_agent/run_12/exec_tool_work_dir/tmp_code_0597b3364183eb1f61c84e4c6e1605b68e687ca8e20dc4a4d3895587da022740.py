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

# Extract country codes from Patents_info and find German patents
german_patents = []
for rec in patents_data:
    patents_info = rec.get('Patents_info', '')
    # Look for country_code (DE is German)
    if 'DE' in patents_info or 'Germany' in patents_info:
        # More specific check for country_code
        if 'country_code: DE' in patents_info or '"country_code": "DE"' in patents_info:
            german_patents.append(rec)

print('German patents identified: ' + str(len(german_patents)))

# Also look for German in title or other fields
german_keywords = ['german', 'germany', 'deutschland']
for i in range(min(5, len(german_patents))):
    patents_info_check = german_patents[i].get('Patents_info', '')
    title_check = str(german_patents[i].get('title_localized', ''))
    print('Sample German patent ' + str(i) + ':')
    print('  Grant date: ' + german_patents[i]['grant_date'])
    print('  Info excerpt: ' + patents_info_check[:150])
    print('  Title excerpt: ' + title_check[:100])
    print('---')

print('__RESULT__:')
print(str(len(german_patents)))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433}

exec(code, env_args)
