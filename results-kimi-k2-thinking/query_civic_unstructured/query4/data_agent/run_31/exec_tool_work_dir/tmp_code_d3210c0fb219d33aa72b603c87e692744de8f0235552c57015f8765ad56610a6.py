code = """import json
import pandas as pd
import re

# Load all the data
print("Loading funding data...")
all_funding = var_functions.query_db_14
print(f"Funding records: {len(all_funding)}")

print("Loading all project documents...")
all_docs = var_functions.query_db_2
print(f"All docs: {len(all_docs)}")

print("Loading 2022-filtered documents...")
filtered_docs = var_functions.query_db_16
print(f"2022-filtered docs: {len(filtered_docs)}")

# Create funding DataFrame
funding_df = pd.DataFrame(all_funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Look for Spring 2022 schedules and extract associated project names
spring_2022_projects = []

for doc in filtered_docs:
    text = doc.get('text', '')
    
    # Clean text for easier parsing
    clean_text = text.replace('\u2019', "'").replace('\u2013', '-')
    
    # Find all occurrences of Spring 2022
    for match in re.finditer(r'Spring[^\n]{0,100}2022', clean_text, re.IGNORECASE):
        # Get surrounding context to find project name
        context_start = max(0, match.start() - 500)
        context_end = match.end() + 200
        context = clean_text[context_start:context_end]
        
        # Look for project names in this context by checking against funding project names
        for idx, funding_row in funding_df.iterrows():
            project_name = funding_row['Project_Name']
            
            # Check if project name appears in the context
            if project_name[:50] in context:  # Match first 50 chars
                spring_2022_projects.append({
                    'Project_Name': project_name,
                    'Amount': funding_row['Amount'],
                    'Context_snippet': context[:150].replace('\n', ' ')
                })
                break  # Found a match for this occurrence

# Remove duplicates
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())
total_funding = sum(p['Amount'] for p in final_projects)

print(f"\nFound {len(final_projects)} unique projects with Spring 2022 start:")
for proj in final_projects:
    print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")

print(f"\nTOTAL: {len(final_projects)} projects, ${total_funding:,} funding")

result = {
    'project_count': len(final_projects),
    'total_funding': int(total_funding),
    'projects': final_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:26': {'funding': None, 'projects_all': None, 'projects_2022': None}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
