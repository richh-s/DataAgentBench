code = """import json
import re

# Load funding data directly from the stored variable
funding_data = locals().get('var_functions.query_db:8')

# If it's a string (file path), load it
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Load civic docs data
civic_docs_data = locals().get('var_functions.query_db:32')
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

# Convert funding to list of dicts for easier processing
funding_list = funding_data if isinstance(funding_data, list) else []

# Extract disaster-related projects from civic docs
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'recovery']
disaster_projects_2022 = set()

for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for lines that might be project names
    for line in text.split('\n'):
        line = line.strip()
        # Skip empty or very short lines
        if len(line) < 10:
            continue
        # Skip lines that are clearly not project names  
        if line.startswith('(') or line.startswith('•') or line.startswith('◦'):
            continue
        
        # Check if it's disaster-related
        is_disaster = any(keyword in line for keyword in disaster_keywords)
        
        # Check if it has 2022 or is in 2022 context
        context_window = text[max(0, text.find(line)-200):min(len(text), text.find(line)+200)]
        has_2022_context = '2022' in context_window
        
        if is_disaster and has_2022_context:
            # Clean up the project name
            clean_name = re.sub(r'\s+', ' ', line).strip()
            disaster_projects_2022.add(clean_name)

# Also add any projects with 2022 in the name from funding data
for item in funding_list:
    proj_name = item['Project_Name']
    if '2022' in proj_name and any(kw in proj_name for kw in disaster_keywords):
        disaster_projects_2022.add(proj_name)

# Sum funding for all matched projects
total_funding = 0
for item in funding_list:
    fund_name = item['Project_Name']
    amount = int(item['Amount'])
    
    # Check against our disaster projects
    for disaster_proj in disaster_projects_2022:
        # Match if disaster project name is in funding name or vice versa
        if (disaster_proj in fund_name or fund_name in disaster_proj) and len(fund_name) > 5:
            total_funding += amount
            break

# Remove duplicates by checking project names we've already counted
unique_projects = set()
counted_funding = 0

for item in funding_list:
    fund_name = item['Project_Name']
    amount = int(item['Amount'])
    
    # Check if this is a disaster project
    qualifies = False
    
    # Direct match with our list
    for disaster_proj in disaster_projects_2022:
        if disaster_proj in fund_name or fund_name in disaster_proj:
            qualifies = True
            break
    
    # Or match disaster keywords + 2022
    if '2022' in fund_name and any(kw in fund_name for kw in disaster_keywords):
        qualifies = True
    
    if qualifies and fund_name not in unique_projects:
        counted_funding += amount
        unique_projects.add(fund_name)

result = {
    'total_funding': counted_funding,
    'project_count': len(unique_projects),
    'sample_projects': list(unique_projects)[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'total_funding': 0, 'projects_count': 0}, 'var_functions.query_db:24': [], 'var_functions.query_db:26': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:28': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:36': [{'total': 'None'}]}

exec(code, env_args)
