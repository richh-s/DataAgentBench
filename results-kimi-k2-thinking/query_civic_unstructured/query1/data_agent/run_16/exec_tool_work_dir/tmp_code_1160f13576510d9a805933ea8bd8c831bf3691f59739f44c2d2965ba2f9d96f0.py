code = """import json
import re

# Load funding data
with open('var_functions.query_db:32', 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open('var_functions.query_db:8', 'r') as f:
    civic_docs = json.load(f)

# Create dictionary mapping project names to amounts
funding_dict = {record['Project_Name']: int(record['Amount']) for record in funding_records}

# Function to extract design projects and separate capital vs disaster
def extract_design_projects_from_docs(docs):
    capital_design = set()
    disaster_design = set()
    
    for doc in docs:
        text = doc.get('text', '')
        
        # Find the Design section
        design_start = text.find('Capital Improvement Projects (Design)')
        if design_start < 0:
            continue
            
        # Find end of Design section
        construction_start = text.find('Capital Improvement Projects (Construction)', design_start)
        if construction_start < 0:
            construction_start = text.find('DISASTER RECOVERY PROJECTS', design_start)
        if construction_start < 0:
            construction_start = len(text)
            
        design_section = text[design_start:construction_start]
        
        # Extract lines that look like project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project name patterns
            if (line and len(line) > 10 and not line.startswith('(') and 
                line[0].isupper() and 'Capital Improvement' not in line and
                'Updates:' not in line and 'Project Schedule' not in line and
                'Complete Design' not in line and 'Advertise:' not in line and
                'Begin Construction:' not in line and len(line.split()) > 2):
                
                clean_line = re.sub(r'[:;\-•*]+$', '', line).strip()
                if len(clean_line) > 10:
                    capital_design.add(clean_line)
    
    # Also check for disaster projects in FEMA sections
    for doc in docs:
        text = doc.get('text', '')
        
        # Find disaster recovery section
        disaster_start = text.find('DISASTER RECOVERY PROJECTS')
        if disaster_start < 0:
            continue
            
        next_section = text.find('\n\n', disaster_start)
        if next_section < 0:
            next_section = len(text)
            
        disaster_section = text[disaster_start:next_section]
        
        # Extract project names from disaster section
        lines = disaster_section.split('\n')
        for line in lines:
            line = line.strip()
            if (line and len(line) > 10 and line[0].isupper() and 
                'DISASTER RECOVERY' not in line and 'Updates:' not in line and
                'Project Schedule' not in line):
                
                clean_line = re.sub(r'[:;\-•*]+$', '', line).strip()
                if len(clean_line) > 10:
                    disaster_design.add(clean_line)
    
    return capital_design, disaster_design

# Extract projects from documents
capital_design_projects, disaster_design_projects = extract_design_projects_from_docs(civic_docs)

# Match funding with capital design projects
matched_projects = []

for project_name in funding_dict:
    amount = funding_dict[project_name]
    
    # Check for exact match or partial match
    in_capital = False
    
    # Direct match
    for dp in capital_design_projects:
        if (project_name.lower() in dp.lower() or 
            dp.lower() in project_name.lower()):
            in_capital = True
            break
    
    # Check if it's a disaster project (these should be excluded from capital)
    is_disaster = False
    
    # Check for FEMA/CalOES suffixes
    if re.search(r'(\(FEMA[^)]*\)|CalOES|CalJPIA)', project_name):
        is_disaster = True
    
    # Also check disaster section match
    if not is_disaster:
        for dp in disaster_design_projects:
            if project_name.lower() in dp.lower() or dp.lower() in project_name.lower():
                is_disaster = True
                break
    
    # Base name check for variants
    base_name = re.sub(r'\s*\([^)]+\)$', '', project_name)
    if not in_capital and not is_disaster:
        for dp in capital_design_projects:
            base_dp = re.sub(r'\s*\([^)]+\)$', '', dp)
            if (base_name.lower() in base_dp.lower() or 
                base_dp.lower() in base_name.lower()):
                in_capital = True
                break
    
    # If it's capital design with funding > 50000, include it
    if in_capital and not is_disaster and amount > 50000:
        matched_projects.append({
            'project_name': project_name,
            'amount': amount
        })

# Count results
count = len(matched_projects)

# Sort by amount for debugging
matched_projects.sort(key=lambda x: x['amount'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_capital_design_funded': count,
    'sample_projects': matched_projects[:10]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
