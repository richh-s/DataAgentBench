code = """import json
import re

# Load UNIV CALIFORNIA patents
with open(var_functions.query_db:40, 'r') as f:
    univ_patents = json.load(f)

# Extract publication numbers
univ_pub_numbers = set()
for patent in univ_patents:
    info = patent['Patents_info']
    
    # Try different patterns to find publication numbers
    patterns = [
        r'pub\. number\s+([A-Z]{2}-[^\s,\.]+)',
        r'publication number\s+([A-Z]{2}-[^\s,\.]+)',
        r'publication no\.\s+([A-Z]{2}-[^\s,\.]+)'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, info, re.IGNORECASE)
        if matches:
            for match in matches:
                if match and len(match) > 5:  # Ensure it's a real publication number
                    univ_pub_numbers.add(match.strip())
            break

print('__RESULT__:') 
print(json.dumps({
    'total_univ_patents': len(univ_patents),
    'unique_pub_numbers': len(univ_pub_numbers),
    'sample_pub_numbers': list(univ_pub_numbers)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'storage_keys': ['var_functions.query_db:0', 'var_functions.query_db:2'], 'current_dir': []}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:34': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
