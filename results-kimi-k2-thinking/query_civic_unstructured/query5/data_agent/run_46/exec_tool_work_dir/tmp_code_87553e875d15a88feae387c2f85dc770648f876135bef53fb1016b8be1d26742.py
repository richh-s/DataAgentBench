code = """import json
import re
from collections import defaultdict

# Get the data from storage
civic_docs = locals()['var_functions.query_db:32']
funding_records = locals()['var_functions.query_db:2']

# Extract disaster-related projects that started in 2022
# Disaster indicators: FEMA, CalOES, CalJPIA, "disaster recovery", "fire"
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'recovery', 'woolsey']
starting_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    
    # Look for project sections
    for line in lines:
        line = line.strip()
        
        # Detect project boundaries - project names are typically capitalized and may have suffixes
        project_match = re.match(r'^([A-Z][A-Za-z\s\-&]+?)(?:\s*\((FEMA|CalOES|CalJPIA)[^\)]*\))?$', line)
        
        if project_match:
            project_name = project_match.group(1).strip()
            project_type = project_match.group(2) if project_match.group(2) else None
            
            # Check if it's a disaster project (by suffix or containing keywords)
            is_disaster = False
            if project_type in ['FEMA', 'CalOES', 'CalJPIA']:
                is_disaster = True
            
            # Check line for disaster keywords
            lower_line = line.lower()
            if any(keyword in lower_line for keyword in ['fema', 'disaster', 'caloes', 'caljpia', 'recovery']):
                is_disaster = True
                
            if is_disaster:
                current_project = project_name
                # Look for schedule/info in subsequent lines within the document
                # Search for 2022 mentions near this project
                if '2022' in text:
                    # Find the position of this project and check nearby for 2022
                    proj_pos = text.find(line)
                    if proj_pos != -1:
                        # Look for date patterns around this project
                        snippet = text[proj_pos:proj_pos+500]
                        if re.search(r'2022[-\s\w]*(?:Spring|Fall|Summer|Winter|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', snippet, re.I):
                            starting_2022_projects.append(project_name)

# Also look for projects with 2022 in their name
for doc in civic_docs:
    text = doc.get('text', '')
    # Pattern: 2022 at the start of a project name
    matches = re.findall(r'(\d{4}\s+[A-Za-z\s\-&]+|^[A-Za-z\s\-&]+\s+2022)', text, re.M)
    for match in matches:
        if '2022' in match and any(kw in text.lower() for kw in disaster_keywords):
            # Clean up the project name
            project_name = re.sub(r'^\d{4}\s+', '', match).strip()
            project_name = re.sub(r'\s+2022$', '', project_name).strip()
            starting_2022_projects.append(project_name)

# Remove duplicates while preserving order
seen = set()
disaster_2022_projects = []
for proj in starting_2022_projects:
    if proj not in seen and proj:
        seen.add(proj)
        disaster_2022_projects.append(proj)

print(f"Found {len(disaster_2022_projects)} disaster-related projects: {disaster_2022_projects[:10]}...")

# Now get funding for these projects
funding_amounts = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    for disaster_proj in disaster_2022_projects:
        # Match project names (handle partial matches)
        if disaster_proj.lower() in project_name.lower() or project_name.lower() in disaster_proj.lower():
            amount = int(record.get('Amount', 0))
            funding_amounts[project_name] = amount

# Calculate total
total_funding = sum(funding_amounts.values())

print(f"Total funding: ${total_funding:,}")
print(f"Projects with funding: {len(funding_amounts)}")

# Detailed breakdown
print("\nFunding breakdown:")
for proj, amount in funding_amounts.items():
    print(f"  {proj}: ${amount:,}")

print('__RESULT__:')
print(json.dumps({
    "total_funding": total_funding,
    "project_count": len(funding_amounts),
    "funding_breakdown": funding_amounts
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
