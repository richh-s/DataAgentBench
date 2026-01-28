code = """import json

# Load the UNIV CALIFORNIA patents data
california_patents_path = locals()['var_functions.query_db:4']
if isinstance(california_patents_path, str):
    with open(california_patents_path, 'r') as f:
        california_patents = json.load(f)
else:
    california_patents = california_patents_path

# Extract publication numbers from UNIV CALIFORNIA patents
publication_numbers = []
for patent in california_patents:
    patents_info = patent['Patents_info']
    # Extract publication number - look for patterns
    if 'pub. number' in patents_info:
        start = patents_info.find('pub. number') + len('pub. number')
        rest = patents_info[start:].strip()
        # Get the publication number (usually starts with US-, TW-, AU-, etc.)
        parts = rest.split()
        if parts:
            pub_num = parts[0]
            # Remove trailing punctuation
            pub_num = pub_num.rstrip('.,')
            publication_numbers.append(pub_num)
    elif 'publication number' in patents_info:
        start = patents_info.find('publication number') + len('publication number')
        rest = patents_info[start:].strip()
        parts = rest.split()
        if parts:
            pub_num = parts[0]
            pub_num = pub_num.rstrip('.,')
            publication_numbers.append(pub_num)

print(f"Found {len(publication_numbers)} UNIV CALIFORNIA publication numbers")
print("Sample publication numbers:", publication_numbers[:10])

# Create a result dictionary
result_data = {
    'publication_numbers': publication_numbers,
    'count': len(publication_numbers)
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
