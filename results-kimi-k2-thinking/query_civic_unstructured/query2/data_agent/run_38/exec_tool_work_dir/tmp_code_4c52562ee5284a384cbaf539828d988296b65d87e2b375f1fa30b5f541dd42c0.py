code = """import json
import re

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup table
funding_dict = {}
for item in funding_data:
    proj_name = item['Project_Name'].lower().strip()
    amount = int(item['Amount'])
    funding_dict[proj_name] = amount

# Process civic documents to find park projects completed in 2022
park_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document contains park projects completed in 2022
    lower_text = text.lower()
    if 'park' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        # Extract individual lines
        lines = text.splitlines()
        for line in lines:
            clean_line = line.strip()
            if clean_line and len(clean_line) < 150:
                line_lower = clean_line.lower()
                # Check if this line is a park project name
                has_park = 'park' in line_lower
                has_project_type = any(word in line_lower for word in ['project', 'repairs', 'improvements', 'construction', 'renovation'])
                if has_park and has_project_type:
                    park_project_names.append(clean_line)

# Remove duplicates
unique_park_projects = list(set(park_project_names))

# Match with funding data and calculate total
total_funding_amount = 0
matched_project_list = []

for park_proj in unique_park_projects:
    # Try exact match first
    if park_proj.lower() in funding_dict:
        total_funding_amount += funding_dict[park_proj.lower()]
        matched_project_list.append(park_proj)
    else:
        # Try partial matching
        park_words = set(park_proj.lower().split())
        for funding_key in funding_dict:
            funding_words = set(funding_key.split())
            common = park_words & funding_words
            if len(common) >= 2:  # At least 2 words match
                total_funding_amount += funding_dict[funding_key]
                matched_project_list.append(park_proj + ' (' + funding_key + ')')
                break

# Prepare final result
final_result = {
    'total_funding_dollars': total_funding_amount,
    'number_of_matched_projects': len(matched_project_list),
    'matched_projects': matched_project_list[:10]
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
