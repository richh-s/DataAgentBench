code = """import json
import pandas as pd
import re

# Load the data
funding_data = var_functions.query_db_14
all_projects = var_functions.query_db_2
projects_2022 = var_functions.query_db_16

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

print("Data loaded successfully")
print(f"Funding records: {len(funding_df)}")
print(f"2022 filtered docs: {len(projects_2022)}")

# Extract project names from funding data for easy lookup
funding_project_names = funding_df['Project_Name'].tolist()

# Search for Spring 2022 mentions in documents and match with project names
spring_2022_matches = []

for doc in projects_2022:
    text = doc.get('text', '').replace('\u2019', "'").replace('\u2013', '-')
    
    # Look for Spring 2022 patterns
    spring_pattern = re.finditer(r'Spring[^\n]{0,50}2022', text)
    
    for match in spring_pattern:
        # Get surrounding context
        start_pos = max(0, match.start() - 200)
        end_pos = match.end() + 200
        context = text[start_pos:end_pos]
        
        # Check which project names appear in this context
        for proj_name in funding_project_names:
            # Check if project name appears in context (case insensitive)
            if re.search(re.escape(proj_name[:60]), context, re.IGNORECASE):
                # Get the exact funding record
                funding_record = funding_df[funding_df['Project_Name'] == proj_name]
                if not funding_record.empty:
                    amount = funding_record.iloc[0]['Amount']
                    spring_2022_matches.append({
                        'Project_Name': proj_name,
                        'Amount': amount,
                        'Context': context[:200]
                    })

# Remove duplicates
unique_matches = []
seen = set()
for match in spring_2022_matches:
    if match['Project_Name'] not in seen:
        unique_matches.append(match)
        seen.add(match['Project_Name'])

# Calculate totals
total_funding = sum(m['Amount'] for m in unique_matches)
project_count = len(unique_matches)

print(f"\nFound {project_count} projects starting Spring 2022")
print(f"Total funding: {total_funding}")

result = {
    'project_count': project_count,
    'total_funding': int(total_funding),
    'projects': unique_matches
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}}

exec(code, env_args)
