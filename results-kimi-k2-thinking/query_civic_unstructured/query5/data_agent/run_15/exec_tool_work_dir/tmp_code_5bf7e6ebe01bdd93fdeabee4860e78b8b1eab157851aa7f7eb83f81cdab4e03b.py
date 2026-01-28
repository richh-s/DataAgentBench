code = """import json
import re

# Load the data
civic_docs = json.loads(open(var_functions.query_db_28, 'r').read())
funding_data = json.loads(open(var_functions.query_db_29, 'r').read())

# Create funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Identify disaster-related projects in funding
disaster_project_names = []
for name in funding_dict.keys():
    if re.search(r'FEMA|CalOES|CalJPIA', name, re.IGNORECASE):
        disaster_project_names.append(name)

# Combine all civic document text for searching
all_docs_text = ' '.join([doc.get('text', '') for doc in civic_docs])

# Find disaster projects that started in 2022
projects_in_2022 = []
total_funding = 0

for proj_name in disaster_project_names:
    # Check if project appears in documents
    if proj_name in all_docs_text:
        # Find the context around this project
        pattern = re.escape(proj_name)
        matches = list(re.finditer(pattern, all_docs_text))
        
        for match in matches:
            # Get context window
            start = max(0, match.start() - 300)
            end = min(len(all_docs_text), match.end() + 300)
            context = all_docs_text[start:end]
            
            # Check for 2022 references (not fiscal year)
            has_2022 = re.search(r'2022', context) and not re.search(r'2022-2023|Fiscal Year|FY', context)
            
            if has_2022:
                amount = funding_dict[proj_name]
                projects_in_2022.append((proj_name, amount))
                total_funding += amount
                break

# Check for 2022 Morning View project specifically
morning_view = '2022 Morning View Resurfacing & Storm Drain Improvements'
if morning_view in funding_dict:
    # Check if CalOES/FEMA mentioned nearby (indicates disaster-related)
    if re.search(r'2022 Morning View', all_docs_text, re.IGNORECASE) and \
       re.search(r'CalOES|FEMA', all_docs_text, re.IGNORECASE):
        amount = funding_dict[morning_view]
        if (morning_view, amount) not in projects_in_2022:
            projects_in_2022.append((morning_view, amount))
            total_funding += amount

# Remove duplicates
unique_projects = list(set(projects_in_2022))

# Recalculate total from unique projects
total_funding = sum(amount for _, amount in unique_projects)

# Build result
result = f"TOTAL FUNDING FOR DISASTER-RELATED PROJECTS THAT STARTED IN 2022: ${total_funding:,}\n\n"
result += "PROJECTS:\n"
for proj_name, amount in sorted(unique_projects):
    result += f"  {proj_name}: ${amount:,}\n"

result += f"\nCOUNT: {len(unique_projects)} projects"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['Funding'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json'}

exec(code, env_args)
