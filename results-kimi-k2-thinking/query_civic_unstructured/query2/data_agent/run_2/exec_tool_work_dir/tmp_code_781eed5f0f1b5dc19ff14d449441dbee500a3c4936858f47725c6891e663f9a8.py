code = """import json
import re

# Load the civic documents data - access via locals()
civic_docs_key = 'var_functions.query_db:0'
if civic_docs_key in locals():
    civic_docs_path = locals()[civic_docs_key]
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

# Load the funding data - access via locals()
funding_key = 'var_functions.query_db:2'
if funding_key in locals():
    funding_path = locals()[funding_key]
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = []

# Create a list to store extracted projects
extracted_projects = []

# Function to extract project information from document text
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    in_project_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and bullet points
        if not line or line.startswith('(') or line.startswith('•') or line.startswith('■'):
            i += 1
            continue
        
        # Check if we're entering a project section
        if ('Updates:' in line or 'Project Schedule:' in line or 'Project Description:' in line):
            # Look backwards for project name
            for j in range(i-1, max(i-5, -1), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and not prev_line.startswith('•'):
                    if len(prev_line) < 100 and prev_line[0].isupper():
                        current_project = prev_line
                        in_project_section = True
                        break
        
        # If we have a current project, look for completion info
        if current_project and in_project_section:
            section_text = '\n'.join(lines[i:min(i+10, len(lines))])
            
            # Check if completed in 2022
            if 'completed' in section_text.lower() and '2022' in section_text:
                # Extract topics
                topics = []
                if 'park' in current_project.lower():
                    topics.append('park')
                if 'playground' in current_project.lower():
                    topics.append('playground')
                
                # Also check section for park references
                if 'park' in section_text.lower():
                    topics.append('park')
                
                if topics:
                    projects.append({
                        'Project_Name': current_project,
                        'topic': ','.join(set(topics)),
                        'status': 'completed',
                        'st': None,
                        'et': '2022'
                    })
                
                current_project = None
                in_project_section = False
        
        i += 1
    
    return projects

# Process all documents
for doc in civic_docs:
    if 'text' in doc:
        projects = extract_projects_from_text(doc['text'])
        extracted_projects.extend(projects)

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in extracted_projects:
    if proj['Project_Name'] not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj['Project_Name'])

print("EXTRACTED PARK PROJECTS COMPLETED IN 2022:")
for proj in unique_projects:
    print(f"- {proj['Project_Name']}: {proj['topic']}, {proj['status']}, {proj['et']}")

print(f"\nTotal extracted: {len(unique_projects)}")

# Match projects with funding data
matched_projects = []
total_funding = 0

for proj in unique_projects:
    proj_name = proj['Project_Name'].lower()
    
    # Look for matches in funding data (exact or partial)
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '').lower()
        fund_amount = int(fund.get('Amount', 0))
        
        # Check if project names match (allowing for partial matches)
        if (proj_name in fund_name or fund_name in proj_name):
            matched_projects.append({
                'project_name': proj['Project_Name'],
                'funding_name': fund.get('Project_Name'),
                'amount': fund_amount
            })
            total_funding += fund_amount

# Remove duplicate funding matches (same project matched multiple times)
unique_matches = []
seen_funding_names = set()
for match in matched_projects:
    if match['funding_name'] not in seen_funding_names:
        unique_matches.append(match)
        seen_funding_names.add(match['funding_name'])

print("\nMATCHED PROJECTS WITH FUNDING:")
for match in unique_matches:
    print(f"- {match['project_name']} -> {match['funding_name']}: ${match['amount']:,}")

print(f"\nTOTAL FUNDING: ${total_funding:,}")

# Return the final answer
answer = f"The total funding for park-related projects completed in 2022 is ${total_funding:,}."
print("\n__RESULT__:")
print(answer)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
