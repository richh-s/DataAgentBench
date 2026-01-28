code = """import json
import re

# Load the funding data
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load the civic docs
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a list to hold all extracted projects
all_projects = []

# Process each civic document
for doc in civic_docs:
    if 'text' in doc:
        text = doc['text']
        
        # Look for capital projects in design status
        # We'll look for patterns indicating capital projects with design status
        
        # Pattern 1: Look for "Capital Improvement Projects (Design)" section
        if 'Capital Improvement Projects' in text and 'Design' in text:
            lines = text.split('\n')
            in_design_section = False
            
            for line in lines:
                line = line.strip()
                
                # Check if we're in the design section
                if 'Capital Improvement Projects' in line and 'Design' in line:
                    in_design_section = True
                    continue
                
                # If we're in design section, look for project names
                if in_design_section:
                    # Project names are often bolded or start with special chars
                    # Look for lines that don't start with common non-project text
                    if line and not any(x in line for x in ['Updates:', 'Schedule:', 'To:', 'Prepared by:', 'Approved by:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', '•', '(cid:']):
                        # Check if it's a reasonable project name length
                        if 5 < len(line) < 100:
                            # Clean up the line
                            clean_name = re.sub(r'^[\d\.\s\-\•]+', '', line)
                            clean_name = re.sub(r'\s+', ' ', clean_name).strip()
                            
                            if clean_name and len(clean_name) > 3:
                                all_projects.append({
                                    'Project_Name': clean_name,
                                    'status': 'design',
                                    'type': 'capital'
                                })
                                # Only take first few from this section to avoid over-collecting
                                if len(all_projects) > 30:
                                    break

# Remove duplicates and clean up
unique_projects = []
project_names = set()

for proj in all_projects:
    name_key = proj['Project_Name'].lower().strip()
    if name_key not in project_names:
        project_names.add(name_key)
        unique_projects.append(proj)

# Get funding projects with amount > 50000
funding_projects = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_projects[item['Project_Name']] = item

# Define helper function to match project names
def normalize_name(name):
    if not name:
        return ''
    
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)  # Normalize spaces
    name = re.sub(r'\(fema[^\)]+\)', '', name)  # Remove FEMA suffixes
    name = re.sub(r'\(cal[^\)]+\)', '', name)   # Remove CalOES/CalJPIA suffixes
    name = re.sub(r'[^a-z0-9\s]', '', name)     # Remove special characters
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Match projects
matched_projects = []
for proj in unique_projects:
    proj_norm = normalize_name(proj['Project_Name'])
    
    if not proj_norm:
        continue
        
    for funding_name, funding_rec in funding_projects.items():
        fund_norm = normalize_name(funding_name)
        
        # Check if one name contains the other
        if proj_norm in fund_norm or fund_norm in proj_norm:
            matched_projects.append({
                'project_name': proj['Project_Name'],
                'funding_name': funding_name,
                'amount': int(funding_rec['Amount'])
            })
            break  # Match found, move to next project

# Create result
result = {
    'count': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
