code = """import json
import re
import os

# Read the civic documents from file  
civic_file = 'civic_docs_query_result.json'
with open(civic_file, 'r', encoding='utf-8') as f:
    all_docs = json.load(f)

print(f"Total documents: {len(all_docs)}")

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in all_docs:
    text = doc.get('text', '')
    
    # Find project blocks
    sections = re.split(r'\n\s*\n', text)
    
    for section in sections:
        # Check if park-related
        if re.search(r'park', section, re.IGNORECASE):
            # Check if completed in 2022
            if re.search(r'completed.*?(2022|Nov|Novemb|Dec|Decemb|November|December)', section, re.IGNORECASE):
                # Extract project name
                lines = section.strip().split('\n')
                if lines:
                    project_name = lines[0].strip()
                    # Filter out non-project lines
                    skip_terms = ['Public Works', 'Commission', 'Agenda', 'Meeting', 'Item', 'To:', 'Prepared by', 
                                'Approved by', 'Date', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Staff']
                    should_skip = any(term in project_name for term in skip_terms)
                    
                    if not should_skip and len(project_name) < 150:
                        # Find completion date
                        date_match = re.search(r'completed[^\n]*', section, re.IGNORECASE)
                        date_info = date_match.group() if date_match else ""
                        
                        park_projects_2022.append({
                            'project_name': project_name,
                            'completion_info': date_info,
                            'full_text': section[:500]
                        })

print(f"Found {len(park_projects_2022)} park projects completed in 2022")

for i, proj in enumerate(park_projects_2022):
    print(f"\n{i+1}. {proj['project_name']}")
    print(f"   {proj['completion_info']}")

result = park_projects_2022
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
