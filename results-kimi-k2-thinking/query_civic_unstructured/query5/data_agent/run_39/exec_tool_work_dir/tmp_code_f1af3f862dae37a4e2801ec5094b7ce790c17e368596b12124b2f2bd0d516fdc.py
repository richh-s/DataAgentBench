code = """import json
import re

# Load disaster-related funding records
disaster_funding = var_functions.query_db:26

# Load civic documents file path
civic_file = var_functions.query_db:28

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(disaster_funding)} disaster funding records")
print(f"Loaded {len(civic_docs)} civic documents")

# Create lookup for funding amounts
funding_lookup = {}
for record in disaster_funding:
    project_name = record['Project_Name']
    funding_lookup[project_name] = {
        'amount': int(record['Amount']),
        'source': record['Funding_Source']
    }

# Extract project information from civic documents
all_text = '\n\n'.join([doc.get('text', '') for doc in civic_docs])

# Pattern to find project names in the civic documents
# Look for common project name patterns followed by details
project_blocks = re.findall(r'([A-Z][A-Za-z0-9\s\(\)\-&/,]+?(?:Project|Improvements|Repairs|Replacement|Structure|System|Facility|Program))[^A-Za-z]*([\s\S]{0,500})', all_text)

print(f"Found {len(project_blocks)} potential project blocks")

# Identify disaster projects that started in 2022
projects_2022 = []

for project_name, context in project_blocks:
    project_name = project_name.strip()
    
    # Check if this is a disaster project in our funding lookup
    is_disaster = False
    funding_key = None
    
    # Check exact match
    if project_name in funding_lookup:
        is_disaster = True
        funding_key = project_name
    else:
        # Check base name without suffix
        base_name = project_name.split('(')[0].strip()
        for fname in funding_lookup.keys():
            if fname.startswith(base_name):
                is_disaster = True
                funding_key = fname
                break
    
    if not is_disaster:
        continue
    
    # Check if project started in 2022
    # Look for 2022 in context with indicators of start/completion
    context_lower = context.lower()
    if '2022' in context:
        # Check for indicators that suggest the project was active or completed in 2022
        if any(indicator in context_lower for indicator in ['completed', 'completion', 'construction', 'start', 'begin', 'advertise']):
            projects_2022.append({
                'Project_Name': project_name,
                'Funding_Name': funding_key,
                'Amount': funding_lookup[funding_key]['amount'],
                'Funding_Source': funding_lookup[funding_key]['source']
            })

# Remove duplicates
unique_projects = []
seen_names = set()
for p in projects_2022:
    if p['Funding_Name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['Funding_Name'])

total_funding = sum(p['Amount'] for p in unique_projects)

print(f"\nFound {len(unique_projects)} disaster projects from 2022")
print(f"Total funding: ${total_funding:,}")

for p in unique_projects:
    print(f"- {p['Funding_Name']}: ${p['Amount']:,}")

result = {
    'total_funding': total_funding,
    'project_count': len(unique_projects),
    'projects': unique_projects
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'test': True, 'funding_count': 0, 'civic_count': 0}, 'var_functions.query_db:26': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
