code = """import json
import re
import os

# Debug available variables
print("Available variables starting with 'var_':")
for key in list(locals().keys()):
    if key.startswith('var_'):
        print(f"  {key}")

print("\nLoading university patents data...")
# Process the UNIV CALIFORNIA patents
if 'var_functions.query_db:22' in locals():
    file_path = locals()['var_functions.query_db:22']
    if isinstance(file_path, str) and os.path.exists(file_path):
        with open(file_path, 'r') as f:
            univ_patents = json.load(f)
        
        print(f"\nLoaded {len(univ_patents)} patents from UNIV CALIFORNIA")
        
        # Extract publication numbers for UNIV CALIFORNIA patents
        pub_numbers = []
        for patent in univ_patents:
            info = patent.get('Patents_info', '')
            # Extract publication number patterns like US-2022074631-A1, etc.
            matches = re.findall(r'([A-Z]{2}-[A-Z0-9-]+-[A-Z0-9]+)', info)
            if matches:
                pub_numbers.extend(matches)
        
        print(f"Extracted {len(pub_numbers)} publication numbers")
        print("Sample publications:", pub_numbers[:10])
        
        # Store the list for later use
        publication_list = pub_numbers
    else:
        print(f"File not found or not a valid path: {file_path}")
        publication_list = []
else:
    print("Variable var_functions.query_db:22 not found")
    publication_list = []

print("__RESULT__:")
print(json.dumps({"count": len(publication_list), "samples": publication_list[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
