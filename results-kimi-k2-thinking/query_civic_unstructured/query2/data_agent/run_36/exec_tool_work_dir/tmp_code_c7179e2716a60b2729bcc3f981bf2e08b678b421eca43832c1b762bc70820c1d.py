code = """import json
import pandas as pd
import re

# Load funding data
funding_path = var_functions.query_db:39
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load park documents
park_path = var_functions.query_db:38
with open(park_path, 'r') as f:
    park_docs = json.load(f)

# Extract park projects completed in 2022
park_2022_projects = []

for doc in park_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for park/playground with completed and 2022
    if ('park' in lower_text or 'playground' in lower_text) and 'completed' in lower_text and '2022' in lower_text:
        # Look for specific project name patterns
        patterns = [
            r'([A-Z][a-zA-Z\s]{5,}Park[A-Za-z\s]{0,50})[^.]*?(?:completed|completion)[^.]*?(?:2022|November\s+2022|December\s+2022)',
            r'([A-Z][a-zA-Z\s]{5,}Playground[A-Za-z\s]{0,30})[^.]*?(?:completed|completion)[^.]*?(?:2022)',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                project_name = match.group(1).strip()
                # Clean up
                project_name = re.sub(r'\s+', ' ', project_name)
                project_name = re.sub(r'^[\-\•\■\s]+', '', project_name)
                
                # Verify context
                context_start = max(0, match.start() - 200)
                context_end = min(len(text), match.end() + 200)
                context = text[context_start:context_end].lower()
                
                if 'completed' in context and '2022' in context and len(project_name) > 10:
                    park_2022_projects.append(project_name)

# Remove duplicates
unique_park_projects = list(set(park_2022_projects))

# Match with funding data
matched_projects = []
for park_proj in unique_park_projects:
    park_lower = park_proj.lower()
    matches = funding_df[funding_df['Project_Name'].str.lower().str.contains(park_lower, na=False)]
    
    if not matches.empty:
        for _, match in matches.iterrows():
            if match['Amount'] > 0:
                matched_projects.append({
                    'project_name': match['Project_Name'],
                    'amount': int(match['Amount']),
                    'funding_source': match['Funding_Source']
                })

# Remove duplicates
deduped = {p['project_name']: p for p in matched_projects}
final_projects = list(deduped.values())
total_funding = sum(p['amount'] for p in final_projects)

result_data = {
    'total_funding': total_funding,
    'project_count': len(final_projects),
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.execute_python:34': {'files': []}, 'var_functions.execute_python:36': {}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
