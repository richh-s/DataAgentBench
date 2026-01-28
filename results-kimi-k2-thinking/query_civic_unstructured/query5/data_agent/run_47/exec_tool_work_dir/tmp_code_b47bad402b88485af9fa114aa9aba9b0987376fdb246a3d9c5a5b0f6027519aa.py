code = """import json
import re

# Get the file path from the variable
file_path = var_functions.query_db:12

# Read the civic documents
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Total documents loaded: {len(civic_docs)}")

# Look for disaster-related projects
# Disaster indicators in project names
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'recovery', 'fire', 'woolsey']

# Projects that mention 2022
projects_with_2022 = []

disaster_projects_2022 = []

for doc_idx, doc in enumerate(civic_docs):
    text = doc.get('text', '').lower()
    
    # Check if this is a disaster recovery section
    if 'disaster recovery' in text or 'disaster' in text:
        # Split into lines to find project names
        lines = doc.get('text', '').split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for lines that look like project names (not empty, reasonable length)
            if (len(line) > 10 and len(line) < 200 and 
                not line.startswith('(') and 
                not line.startswith('•') and
                not any(bad_word in line.lower() for bad_word in ['agenda', 'item', 'page', 'malibucity_agenda', 'commission'])):
                
                # Check if it's a disaster project
                line_lower = line.lower()
                has_disaster = any(keyword in line_lower for keyword in disaster_keywords)
                
                # Also check surrounding lines for 2022 and disaster context
                context_lines = lines[max(0, i-5):min(len(lines), i+10)]
                context = ' '.join(context_lines).lower()
                
                has_2022 = '2022' in context
                has_disaster_in_context = any(keyword in context for keyword in disaster_keywords)
                
                if has_2022 and (has_disaster or has_disaster_in_context):
                    # Clean up the project name
                    project_name = line.strip()
                    if not any(exclude in project_name.lower() for exclude in ['public works', 'commission', 'meeting', 'status report']):
                        disaster_projects_2022.append({
                            'Project_Name': project_name,
                            'Document_Index': doc_idx,
                            'Context': ' '.join(lines[max(0, i-2):min(len(lines), i+3)])
                        })

# Remove duplicates
unique_projects = {}
for proj in disaster_projects_2022:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

disaster_projects_unique = list(unique_projects.values())

print(f"\nFound {len(disaster_projects_unique)} unique disaster projects with 2022 references:")
for proj in disaster_projects_unique[:20]:  # Show first 20
    print(f"- {proj['Project_Name']}")

# Now get all funding data
result_info = {
    'disaster_projects_count': len(disaster_projects_unique),
    'sample_disaster_projects': disaster_projects_unique[:10]
}

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
