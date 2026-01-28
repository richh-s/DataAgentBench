code = """import json
import re

# Read the funding data
with open('var_functions.query_db:6', 'r') as f:
    funding_data = json.load(f)

# Read the civic documents
with open('var_functions.query_db:5', 'r') as f:
    civic_docs = json.load(f)

print(f"Number of funding records: {len(funding_data)}")
print(f"Number of civic documents: {len(civic_docs)}")
print(f"First funding record: {funding_data[0]}")
print(f"First civic doc keys: {list(civic_docs[0].keys())}")

def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines and header/footer lines
        if not line or line.startswith('Page') or line.startswith('Agenda Item'):
            i += 1
            continue
            
        # Look for potential project names (title case, not common headers)
        if (len(line) > 10 and 
            line[0].isupper() and 
            not any(keyword in line.lower() for keyword in ['commission', 'meeting', 'agenda', 'report', 'public works', 'capital improvement', 'disaster recovery'])):
            
            project_name = line
            st = None
            et = None
            
            # Scan ahead for schedule info
            j = i + 1
            while j < min(i + 20, len(lines)):
                next_line = lines[j].strip()
                
                # Look for dates containing 2022
                if '2022' in next_line:
                    if 'Spring' in next_line:
                        if not st:
                            st = '2022-Spring'
                        elif not et:
                            et = '2022-Spring'
                    elif any(phase in next_line for phase in ['Complete Design:', 'Begin Construction:', 'Complete Construction:', 'Advertise:']):
                        if not st and ('Begin' in next_line or 'Complete Design' in next_line):
                            st = '2022'
                        elif not et and 'Complete' in next_line:
                            et = '2022'
                
                j += 1
            
            # Determine type
            if any(keyword in project_name.lower() for keyword in ['fema', 'fire', 'disaster']):
                type_val = 'disaster'
            else:
                type_val = 'capital'
            
            # Add project if it has a 2022 start time
            if st and '2022' in st:
                projects.append({
                    'Project_Name': project_name,
                    'st': st,
                    'et': et,
                    'status': None,
                    'type': type_val,
                    'topic': ''
                })
        
        i += 1
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

print(f"Extracted {len(all_projects)} projects with 2022 dates")
if all_projects:
    for p in all_projects[:10]:
        print(f"  {p['Project_Name']}: {p['st']}")
else:
    print("No projects found - checking document structure...")
    # Show a snippet of the first document
    if civic_docs:
        print("First 500 chars of first document:")
        print(civic_docs[0].get('text', '')[:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
