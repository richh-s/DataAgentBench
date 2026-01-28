code = """import json
import re

# Load data
civic_docs = json.loads(open(locals()['var_functions.query_db:28']).read())
funding_data = json.loads(open(locals()['var_functions.query_db:29']).read())

# Create funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find disaster projects in funding
disaster_projects = []
for name in funding_dict.keys():
    if any(kw in name.upper() for kw in ['FEMA', 'CALOES', 'CALJPIA']):
        disaster_projects.append(name)

# Combine all civic document text
all_text = ' '.join([doc.get('text', '') for doc in civic_docs])

# Find which disaster projects started in 2022
projects_found = []
total = 0

for proj_name in disaster_projects:
    # Check if in documents
    if proj_name in all_text:
        # Check context for 2022 start date
        idx = all_text.find(proj_name)
        context = all_text[max(0, idx-300):min(len(all_text), idx+300)]
        
        # Check for 2022 references (not fiscal year)
        if re.search(r'2022', context) and not re.search(r'2022-2023|Fiscal Year|FY', context):
            amount = funding_dict[proj_name]
            projects_found.append((proj_name, amount))
            total += amount

# Remove duplicates
unique = list(set(projects_found))

# Calculate final total
final_total = sum(amt for _, amt in unique)

# Format output
output = "Total funding: $" + str(final_total) + " for " + str(len(unique)) + " projects"
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['Funding'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json'}

exec(code, env_args)
