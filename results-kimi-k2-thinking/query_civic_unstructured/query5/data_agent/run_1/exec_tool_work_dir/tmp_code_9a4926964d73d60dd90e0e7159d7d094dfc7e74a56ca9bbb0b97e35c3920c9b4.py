code = """import json
import re

# Read the civic documents data
civic_docs_file = var_functions.query_db:6
if isinstance(civic_docs_file, str) and civic_docs_file.endswith('.json'):
    with open(civic_docs_file, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:6

# Read the funding data
funding_file = var_functions.query_db:7
if isinstance(funding_file, str) and funding_file.endswith('.json'):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:7

print(f"Number of civic documents: {len(civic_docs)}")
print(f"Number of funding records: {len(funding_data)}")

# Let's examine the first civic doc to understand structure
if civic_docs:
    print(f"\nFirst civic doc keys: {list(civic_docs[0].keys())}")
    print(f"First civic doc filename: {civic_docs[0].get('filename')}")
    
# Let's examine the first few funding records
print(f"\nFirst few funding records:")
for i, record in enumerate(funding_data[:5]):
    print(f"  {i+1}. {record}")

# Check for disaster-related project names in funding data
print(f"\nDisaster-related project names in funding data (containing FEMA, CalOES, CalJPIA):")
disaster_funding_projects = []
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    if any(keyword in proj_name for keyword in ['(FEMA', '(CalOES', '(CalJPIA']):
        disaster_funding_projects.append(proj_name)
        
for name in disaster_funding_projects[:10]:
    print(f"  - {name}")

if len(disaster_funding_projects) > 10:
    print(f"  ... and {len(disaster_funding_projects) - 10} more")

# Now let's extract projects from the civic documents text
print(f"\nExtracting projects from civic documents...")

# Pattern to match project names and information
project_pattern = r'([A-Z][A-Za-z\s&\-\(\)0-9/]+?(?:\s*\(FEMA\s+Project\)|\s*\(CalOES\s+Project\)|\s*\(CalJPIA\s+Project\)|\s*\(FEMA/CalOES\s+Project\))?)'

disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for disaster project sections
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Check if line contains disaster-related keywords
        if any(keyword in line for keyword in ['(FEMA', '(CalOES', '(CalJPIA']):
            # Extract project name (usually on the same line or previous line)
            project_name = line.strip()
            if project_name and len(project_name) < 200:
                # Check if this is likely a project name (not a header)
                if not any(header in project_name for header in ['Capital Improvement', 'Disaster Recovery', 'PROJECTS', 'AGENDA']):
                    disaster_projects.append({
                        'project_name': project_name,
                        'source_doc': doc.get('filename'),
                        'text_snippet': line.strip()
                    })
                    # Look for date information in nearby lines
                    context_start = max(0, i-3)
                    context_end = min(len(lines), i+4)
                    context = '\n'.join(lines[context_start:context_end])
                    
                    # Look for start dates containing 2022
                    if '2022' in context:
                        # Try to find the specific line with date info
                        for ctx_line in lines[context_start:context_end]:
                            if '2022' in ctx_line and any(date_ind in ctx_line for date_ind in ['Start', 'st:', 'Schedule', 'Complete', 'Begin']):
                                print(f"Found potential 2022 project: {project_name}")
                                print(f"  Context: {ctx_line.strip()}")

print(f"\nTotal disaster-related projects found in civic docs: {len(disaster_projects)}")

# Print unique project names
unique_projects = list(set([p['project_name'] for p in disaster_projects]))
print(f"Unique disaster project names:")
for name in unique_projects[:15]:
    print(f"  - {name}")

if len(unique_projects) > 15:
    print(f"  ... and {len(unique_projects) - 15} more")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
