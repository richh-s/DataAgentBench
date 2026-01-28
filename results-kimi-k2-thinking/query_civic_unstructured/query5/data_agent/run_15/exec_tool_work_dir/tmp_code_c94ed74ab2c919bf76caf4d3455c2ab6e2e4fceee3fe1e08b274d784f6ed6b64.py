code = """import json
import re

# Load data from stored results
civic_docs_key = 'var_functions.query_db:28'
funding_key = 'var_functions.query_db:29'

civic_docs = json.loads(open(locals()['var_functions.query_db:28']).read())
funding_data = json.loads(open(locals()['var_functions.query_db:29']).read())

# Build funding dictionary
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Identify disaster-related projects (those with FEMA/CalOES/CalJPIA in name)
disaster_projects = []
for proj_name in funding_dict.keys():
    if any(keyword in proj_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA']):
        disaster_projects.append(proj_name)

# Combine all civic document text
all_docs_text = ' '.join([doc.get('text', '') for doc in civic_docs])

# Check for 2022 start dates in disaster projects
projects_2022 = []
total_funding = 0

for proj_name in disaster_projects:
    # Find project in documents
    if proj_name in all_docs_text:
        # Check surrounding context for 2022
        pattern = re.escape(proj_name)
        matches = re.finditer(pattern, all_docs_text)
        
        for match in matches:
            # Check context window
            context = all_docs_text[max(0, match.start()-300):min(len(all_docs_text), match.end()+300)]
            
            # Look for 2022, excluding fiscal year references
            if re.search(r'2022', context) and not re.search(r'2022-2023|Fiscal.*Year|FY.*2022', context):
                amount = funding_dict[proj_name]
                projects_2022.append((proj_name, amount))
                total_funding += amount
                break

# Remove duplicates
unique_projects = []
seen = set()
for name, amt in projects_2022:
    if name not in seen:
        seen.add(name)
        unique_projects.append((name, amt))

# Recalculate total
total = sum(amt for _, amt in unique_projects)

# Create result
result_str = "Total funding for disaster-related projects that started in 2022: $" + str(total) + "\n\n"
result_str += "Projects:\n"
for proj_name, amount in sorted(unique_projects):
    result_str = result_str + "  " + proj_name + ": $" + str(amount) + "\n"
result_str = result_str + "\nCount: " + str(len(unique_projects)) + " projects"

print('__RESULT__:')
print(json.dumps(result_str))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:16': ['Funding'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:29': 'file_storage/functions.query_db:29.json'}

exec(code, env_args)
