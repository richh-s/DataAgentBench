code = """import json

# Get data from previous queries
civic_docs = None
funding_data = None

# Try to read the civic docs directly from the variable
if 'var_functions.query_db:22' in locals():
    civic_docs_path = locals()['var_functions.query_db:22']
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)

if 'var_functions.query_db:19' in locals():
    funding_path = locals()['var_functions.query_db:19']
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
if funding_data:
    for item in funding_data:
        funding_lookup[item['Project_Name']] = int(item['Total_Amount'])

# Simple extraction of Spring 2022 projects
spring_projects = []
if civic_docs:
    for doc in civic_docs:
        text = doc['text']
        # Look for the specific pattern we saw in the data: "2022 Morning View..."
        if '2022' in text and 'Morning View' in text:
            spring_projects.append('2022 Morning View Resurfacing & Storm Drain Improvements')
        # Check for other 2022 projects
        lines = text.split('\n')
        for line in lines:
            if '2022' in line and ('Project' in line or 'Improvements' in line):
                clean_line = line.strip()
                if len(clean_line) > 20:
                    spring_projects.append(clean_line)

# Remove duplicates and get unique project names
unique_projects = list(set(spring_projects))

# Match with funding
total_funding = 0
matched = []

for proj in unique_projects:
    # Clean the name to match funding table format
    name_to_check = proj.split('\n')[0].strip()
    
    if name_to_check in funding_lookup:
        amount = funding_lookup[name_to_check]
        total_funding += amount
        matched.append({'name': name_to_check, 'funding': amount})
    elif '2022 Morning View Resurfacing & Storm Drain Improvements' in name_to_check:
        # This is the one we know exists
        morning_view_name = '2022 Morning View Resurfacing & Storm Drain Improvements'
        if morning_view_name in funding_lookup:
            amount = funding_lookup[morning_view_name]
            total_funding += amount
            matched.append({'name': morning_view_name, 'funding': amount})

result = {
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [], 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.query_db:30': [{'Total_Funding': 'None'}]}

exec(code, env_args)
