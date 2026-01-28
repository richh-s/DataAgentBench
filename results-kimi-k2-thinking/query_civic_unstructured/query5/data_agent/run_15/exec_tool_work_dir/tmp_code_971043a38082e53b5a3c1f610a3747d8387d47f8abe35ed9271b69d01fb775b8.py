code = """import json
import re

# Load the data
with open(var_functions.query_db:28, 'r') as f:
    civic_docs = json.load(f)

with open(var_functions.query_db:29, 'r') f:
    funding_data = json.load(f)

# Create funding dictionary
funding_dict = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Identify disaster-related projects in funding
disaster_project_names = []
for name in funding_dict.keys():
    if re.search(r'FEMA|CalOES|CalJPIA|disaster', name, re.IGNORECASE):
        disaster_project_names.append(name)

# Find which of these started in 2022 according to civic documents
docs_text = ' '.join([doc.get('text', '') for doc in civic_docs])

# Initialize tracking
projects_in_2022 = []
total_funding = 0

# Check for projects that mention 2022 and are disaster-related
for proj_name in disaster_project_names:
    # Check if project name appears in documents with 2022 date
    pattern = re.escape(proj_name)
    if re.search(pattern, docs_text):
        # Look for date context around the project
        # Find all occurrences and check surrounding text for 2022
        for match in re.finditer(pattern, docs_text):
            start = max(0, match.start() - 200)
            end = min(len(docs_text), match.end() + 200)
            context = docs_text[start:end]
            
            # Check for 2022 dates (excluding fiscal year references)
            if re.search(r'2022', context) and not re.search(r'2022-2023|FY\s*2022|Fiscal\s*Year\s*2022', context):
                amount = funding_dict[proj_name]
                projects_in_2022.append((proj_name, amount))
                total_funding += amount
                break

# Also look for explicit 2022 morning view project (starts with 2022)
if '2022 Morning View Resurfacing & Storm Drain Improvements' in funding_dict:
    # Check if this is a disaster project in the documents
    if re.search(r'2022 Morning View.*storm drain', docs_text, re.IGNORECASE) and \
       re.search(r'CalOES|FEMA|disaster', docs_text, re.IGNORECASE):
        amount = funding_dict['2022 Morning View Resurfacing & Storm Drain Improvements']
        if ('2022 Morning View Resurfacing & Storm Drain Improvements', amount) not in projects_in_2022:
            projects_in_2022.append(('2022 Morning View Resurfacing & Storm Drain Improvements', amount))
            total_funding += amount

# Remove duplicates
unique_projects = list(set(projects_in_2022))
total_funding = sum(amount for _, amount in unique_projects)

# Create output
result_text = f"DISASTER-RELATED PROJECTS THAT STARTED IN 2022:\n"
result_text += f"Total Funding: ${total_funding:,}\n\n"
result_text += "Projects:\n"
for proj_name, amount in sorted(unique_projects):
    result_text += f"  • {proj_name}: ${amount:,}\n"

result_text += f"\nTotal Count: {len(unique_projects)} projects"

print('__RESULT__')
print(json.dumps(result_text))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['Funding'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json'}

exec(code, env_args)
