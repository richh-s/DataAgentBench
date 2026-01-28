code = """import json
import re
from collections import defaultdict

# Read the full civic docs result
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Total civic documents: {len(civic_docs)}")

# Look for patterns that might indicate disaster projects with 2022 dates
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']
projects_found = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project patterns
    # Try to find lines that mention projects with dates
    lines = text.split('\n')
    for line in lines:
        if '2022' in line:
            # Check if this is a project line
            if any(keyword in line for keyword in disaster_keywords):
                projects_found.append({
                    'filename': doc['filename'],
                    'line': line.strip()
                })

print(f"Found {len(projects_found)} potential disaster project lines with 2022:")
for p in projects_found[:10]:
    print(f"  {p['filename']}: {p['line']}")

# Also look for project sections more systematically
project_sections = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project sections that might contain disaster projects
    if 'Disaster' in text or 'FEMA' in text or 'CalOES' in text or 'CalJPIA' in text:
        # Try to extract project names and dates
        # This is a heuristic approach
        sections = re.split(r'\n\s*\n', text)
        for section in sections:
            if '2022' in section and any(keyword in section for keyword in disaster_keywords):
                project_sections.append(section)

print(f"\nFound {len(project_sections)} sections with disaster keywords and 2022")
for i, section in enumerate(project_sections[:3]):
    print(f"\nSection {i+1}:")
    print(section[:500] + "..." if len(section) > 500 else section)

# Let's also check the funding data to see what disaster projects exist
funding_file_path = var_functions.query_db:7
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

print(f"\nTotal funding records: {len(funding_data)}")

# Identify disaster-related projects from funding data (based on naming patterns)
disaster_project_names = []
for record in funding_data:
    project_name = record['Project_Name']
    if ('(FEMA' in project_name or '(CalOES' in project_name or '(CalJPIA' in project_name or
        'Disaster' in project_name or 'Fire' in project_name):
        disaster_project_names.append(project_name)

print(f"Disaster-related project names from funding data ({len(disaster_project_names)}):")
for name in sorted(disaster_project_names)[:20]:
    print(f"  {name}")

# Count disaster projects
print('\n__RESULT__:')
print(json.dumps({
    'total_civic_docs': len(civic_docs),
    'potential_disaster_lines': len(projects_found),
    'potential_disaster_sections': len(project_sections),
    'total_funding_records': len(funding_data),
    'disaster_project_names_count': len(disaster_project_names)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
