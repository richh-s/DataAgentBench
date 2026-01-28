code = """import json
import re
from collections import defaultdict

# Load funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections
    # Pattern matches projects with their details
    # Common patterns in the text:
    # Project Name\n\n(•) Updates:\n\n(•) Project Schedule:\n
    # Split by common project headers
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    section_type = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Detect project status categories
        if 'Capital Improvement Projects (Design)' in line:
            section_type = 'design'
            continue
        elif 'Capital Improvement Projects (Construction)' in line:
            section_type = 'construction'
            continue
        elif 'Capital Improvement Projects (Not Started)' in line:
            section_type = 'not started'
            continue
        elif 'Disaster Recovery Projects' in line:
            section_type = 'disaster'
            continue
            
        # Look for project names (they typically appear at the start of a section)
        # Project names are usually followed by updates or schedule sections
        if section_type and line and not line.startswith('(') and not line.startswith('•') and 
           'Updates:' not in line and 'Schedule:' not in line and 
           len(line) > 10 and 'Page' not in line and 'Agenda Item' not in line:
            
            # This is likely a project name
            project_name = line.strip()
            
            # Skip if it's a heading like "RECOMMENDED ACTION"
            if any(keyword in project_name.upper() for keyword in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'TO:', 'PREPARED', 'APPROVED', 'DATE']):
                continue
                
            # Create project record
            if section_type == 'design':
                project_status = 'design'
            elif section_type == 'construction':
                project_status = 'completed'
            elif section_type == 'not started':
                project_status = 'not started'
            else:
                project_status = 'unknown'
            
            # Determine project type (capital or disaster)
            project_type = 'capital'  # Default based on section headers
            
            # Check if it's a disaster project based on name patterns
            if any(keyword in project_name for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency']):
                project_type = 'disaster'
            
            # Determine topics based on name
            topics = []
            if 'park' in project_name.lower():
                topics.append('park')
            if 'road' in project_name.lower() or 'drive' in project_name.lower() or 'lane' in project_name.lower():
                topics.append('road')
            if 'drain' in project_name.lower():
                topics.append('drainage')
            if 'storm' in project_name.lower():
                topics.append('storm drain')
            if 'bridge' in project_name.lower():
                topics.append('bridge')
            if 'traffic' in project_name.lower():
                topics.append('traffic')
            if 'warning' in project_name.lower() or 'siren' in project_name.lower():
                topics.append('emergency warning')
            if 'water' in project_name.lower():
                topics.append('water treatment')
            if 'playground' in project_name.lower():
                topics.append('playground')
            if 'median' in project_name.lower():
                topics.append('highway')
            
            current_project = {
                'Project_Name': project_name,
                'type': project_type,
                'status': project_status,
                'topic': ', '.join(topics),
                'st': None,
                'et': None
            }
            
            projects.append(current_project)

# Clean up project names (remove parenthetical info for matching)
cleaned_projects = []
for proj in projects:
    name = proj['Project_Name']
    # Remove parenthetical suffixes for matching purposes
    clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
    cleaned_projects.append({
        'Project_Name': name,
        'Clean_Name': clean_name,
        'type': proj['type'],
        'status': proj['status'],
        'topic': proj['topic']
    })

print(f"Extracted {len(cleaned_projects)} projects from civic documents")

# Show some sample projects
for i, proj in enumerate(cleaned_projects[:10]):
    print(f"{i+1}. {proj['Project_Name']} | Type: {proj['type']} | Status: {proj['status']}")

# Filter for capital projects with design status
capital_design_projects = [p for p in cleaned_projects if p['type'] == 'capital' and p['status'] == 'design']
print(f"\nCapital projects in design status: {len(capital_design_projects)}")
for proj in capital_design_projects[:10]:
    print(f"- {proj['Project_Name']}")

# Filter funding > 50000
funding_gt_50k = [f for f in funding_data if float(f.get('Amount', 0)) > 50000]
print(f"\nProjects with funding > $50,000: {len(funding_gt_50k)}")
for f in funding_gt_50k[:5]:
    print(f"- {f['Project_Name']}: ${f['Amount']}")

# Match projects with funding
matched_projects = []
for proj in capital_design_projects:
    proj_name = proj['Project_Name']
    proj_clean = proj['Clean_Name']
    
    for fund in funding_gt_50k:
        fund_name = fund['Project_Name']
        fund_clean = re.sub(r'\s*\([^)]*\)\s*$', '', fund_name).strip()
        
        # Check for exact match or partial match
        if (proj_name == fund_name or proj_clean == fund_clean or
            fund_clean in proj_clean or proj_clean in fund_clean):
            matched_projects.append({
                'Project_Name': proj_name,
                'Funding_Amount': float(fund['Amount']),
                'Funding_Source': fund['Funding_Source']
            })
            break

print(f"\nMatched capital design projects with funding > $50,000: {len(matched_projects)}")
for mp in matched_projects:
    print(f"- {mp['Project_Name']}: ${mp['Funding_Amount']}")

# Prepare final result
final_result = {
    'count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
