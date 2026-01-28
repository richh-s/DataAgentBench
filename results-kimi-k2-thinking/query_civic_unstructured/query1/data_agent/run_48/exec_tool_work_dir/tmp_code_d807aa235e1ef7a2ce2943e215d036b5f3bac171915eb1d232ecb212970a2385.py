code = """import json
import re

# Load funding data from the file
funding_file_path = var_functions.query_db:0
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Filter for Amount > 50000 (already done in query, but let's verify)
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]

# Load civic documents from the file
civic_file_path = var_functions.query_db:2
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital projects in design section
    design_pattern = r'Capital Improvement Projects \(Design\)\s*\n*([\s\S]*?)(?=\n\n[A-Z]|$)'
    design_matches = re.findall(design_pattern, text)
    
    for section in design_matches:
        # Extract project names from this section
        project_pattern = r'\n\n([A-Z][^\n]+?)(?=\n\n[Cc]id:|\n\n(?:Updates:|Project Description:|Project Schedule:|Estimated Schedule:)|\n\n[A-Z][^\n]+\n\n|$)'
        project_names = re.findall(project_pattern, section)
        
        for name in project_names:
            name = name.strip()
            if name and len(name) < 200:  # Filter out obviously wrong matches
                projects.append({
                    'Project_Name': name,
                    'type': 'capital',
                    'status': 'design',
                    'source_doc': doc['filename']
                })
    
    # Also check for pattern with "(Design)" at the end of section title
    alt_design_pattern = r'Capital Improvement Projects \(Design\)([\s\S]*?)(?=\n\n[A-Z][^\n]*\n\n|$)'
    alt_design_matches = re.findall(alt_design_pattern, text)
    
    for section in alt_design_matches:
        # Look for project names - they typically appear as standalone lines between blank lines
        lines = section.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Skip empty lines and known non-project lines
            if line and not line.startswith('(') and not line.startswith('•') and \
               'Updates:' not in line and 'Project Schedule:' not in line and \
               'Recommended Action' not in line and 'Discussion:' not in line and \
               len(line) > 5 and len(line) < 200:
                # Check if next line is blank or starts with a parenthesis (indicating project name)
                if i + 1 >= len(lines) or lines[i + 1].strip() == '' or lines[i + 1].strip().startswith('('):
                    projects.append({
                        'Project_Name': line,
                        'type': 'capital',
                        'status': 'design',
                        'source_doc': doc['filename']
                    })
            i += 1

# Debug: print extracted projects
print(f"DEBUG: Extracted {len(projects)} capital projects with design status")
for p in projects[:10]:
    print(f"  - {p['Project_Name']}")

# Now match with funding data
matched_projects = []
for project in projects:
    proj_name = project['Project_Name']
    
    # Look for exact match or partial match in funding data
    for fund in high_funding:
        fund_name = fund['Project_Name']
        
        # Check for exact match
        if proj_name == fund_name:
            matched_projects.append({
                'Project_Name': proj_name,
                'Funding_Amount': int(fund['Amount']),
                'Funding_Source': fund['Funding_Source'],
                'status': 'design',
                'type': 'capital'
            })
            break
        
        # Check for partial match (project name is subset of funding name)
        elif proj_name in fund_name and len(proj_name) > 10:
            matched_projects.append({
                'Project_Name': proj_name,
                'Funding_Amount': int(fund['Amount']),
                'Funding_Source': fund['Funding_Source'],
                'status': 'design',
                'type': 'capital',
                'Matched_Funding_Name': fund_name
            })
            break
        
        # Check for partial match (funding name is subset of project name)
        elif fund_name in proj_name and len(fund_name) > 10:
            matched_projects.append({
                'Project_Name': proj_name,
                'Funding_Amount': int(fund['Amount']),
                'Funding_Source': fund['Funding_Source'],
                'status': 'design',
                'type': 'capital',
                'Matched_Funding_Name': fund_name
            })
            break

print(f"\nDEBUG: Found {len(matched_projects)} matches with funding > $50,000")
for p in matched_projects[:10]:
    print(f"  - {p['Project_Name']}: ${p['Funding_Amount']}")

result = len(matched_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
