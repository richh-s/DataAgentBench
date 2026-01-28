code = """import json
import re
from datetime import datetime

# Load disaster-related funding records
disaster_funding_file = locals()['var_functions.query_db:26']
with open(disaster_funding_file, 'r') as f:
    disaster_funding = json.load(f)

print(f"Loaded {len(disaster_funding)} disaster-related funding records")
print("Sample:", disaster_funding[:3])

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:28']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"\nLoaded {len(civic_docs)} civic documents")

# Create a mapping of project names to funding info
project_funding = {}
for record in disaster_funding:
    project_name = record['Project_Name']
    project_funding[project_name] = {
        'amount': int(record['Amount']),
        'source': record['Funding_Source']
    }

print(f"\nTracking {len(project_funding)} disaster projects for start date information")

# Extract project information from civic documents
# Look for project names and date patterns
projects_with_dates = {}

# Patterns to match dates like 2022-Spring, 2022-Fall, 2022-02, 2022-March, etc.
date_patterns = [
    r'2022[-\s]Spring',
    r'2022[-\s]Summer', 
    r'2022[-\s]Fall',
    r'2022[-\s]Winter',
    r'2022[-\s]\d{1,2}',
    r'2022[-\s]\w+',
    r'(?<!\d)2022(?!\d)'  # Just the year 2022
]

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for each disaster project name in the text
    for project_name in project_funding.keys():
        # Clean project name for regex search (escape special characters)
        clean_name = re.escape(project_name)
        
        # Check if project is mentioned in this document
        if re.search(clean_name, text, re.IGNORECASE):
            # Look for date patterns near the project name
            # Search in the surrounding context
            lines = text.split('\n')
            for line in lines:
                if re.search(clean_name, line, re.IGNORECASE):
                    # Check if this line or nearby lines contain 2022
                    if '2022' in line:
                        if project_name not in projects_with_dates:
                            projects_with_dates[project_name] = []
                        projects_with_dates[project_name].append({
                            'date_ref': line.strip(),
                            'filename': filename
                        })
                        break

print(f"\nFound {len(projects_with_dates)} disaster projects mentioned with 2022 references")

# Identify projects that started in 2022
projects_started_2022 = []

for project_name, references in projects_with_dates.items():
    for ref in references:
        # Check for explicit start indicators
        line_lower = ref['date_ref'].lower()
        if any(indicator in line_lower for indicator in ['begin', 'start', 'commence', 'advertise', 'design', 'construction']):
            if project_name not in projects_started_2022:
                projects_started_2022.append(project_name)

print(f"\nProjects that appear to have started in 2022: {len(projects_started_2022)}")
for p in projects_started_2022:
    print(f"  - {p}: ${project_funding[p]['amount']:,}")

# Calculate total funding
total_funding = sum(project_funding[p]['amount'] for p in projects_started_2022)

print(f"\nTotal funding for disaster projects started in 2022: ${total_funding:,}")

# Also check for projects with 2022 in their name (like "2022 Morning View...")
year_in_name_projects = []
for project_name in project_funding.keys():
    if re.search(r'\b2022\b', project_name):
        year_in_name_projects.append(project_name)

print(f"\nProjects with '2022' in name: {len(year_in_name_projects)}")
for p in year_in_name_projects:
    print(f"  - {p}: ${project_funding[p]['amount']:,}")
    if p not in projects_started_2022:
        projects_started_2022.append(p)

# Recalculate total with name-based matches
total_funding_final = sum(project_funding[p]['amount'] for p in set(projects_started_2022))

print(f"\nFinal total funding for disaster projects started in 2022: ${total_funding_final:,}")

result = {
    'total_funding': total_funding_final,
    'project_count': len(set(projects_started_2022)),
    'projects': [{"name": p, "amount": project_funding[p]['amount']} for p in set(projects_started_2022)]
}

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
