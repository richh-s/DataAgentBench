code = """import json
import re
from pathlib import Path

# Load funding data
funding_file = Path('file_storage/functions.query_db:2.json')
civic_file = Path('file_storage/functions.query_db:3.json')

funding_data = json.loads(funding_file.read_text())
civic_docs_data = json.loads(civic_file.read_text())

# Create project funding map
project_funding = {}
for item in funding_data:
    project_funding[item['Project_Name']] = int(item['Amount'])

# Extract disaster projects
all_text = " ".join([doc['text'] for doc in civic_docs_data])

disaster_projects = []
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'drainage', 'storm drain', 'culvert', 'slope']

# Look for projects that start in 2022
for project_name, amount in project_funding.items():
    # Check if disaster-related
    is_disaster = False
    if any(kw in project_name for kw in disaster_keywords):
        is_disaster = True
    
    if is_disaster and project_name in all_text:
        # Check for 2022 start date in context
        positions = [m.start() for m in re.finditer(re.escape(project_name), all_text)]
        for pos in positions:
            start = max(0, pos - 300)
            end = min(len(all_text), pos + 300)
            context = all_text[start:end]
            
            if '2022' in context:
                disaster_projects.append({
                    'project': project_name,
                    'amount': amount
                })

# Calculate totals
total_funding = sum(p['amount'] for p in disaster_projects)

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022': total_funding,
    'project_count': len(disaster_projects),
    'projects': disaster_projects
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'funding_type': "<class 'str'>", 'funding_preview': 'file_path', 'civic_type': "<class 'str'>", 'civic_preview': 'file_storage/functions.query_db:3.json'}, 'var_functions.execute_python:16': {'funding_count': 500, 'civic_count': 5, 'sample_funding': {'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, 'sample_civic': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChai'}}

exec(code, env_args)
