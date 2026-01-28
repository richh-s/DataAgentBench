code = """import json
import re

# Load disaster-related funding records
disaster_funding_file = locals()['var_functions.query_db:26']
with open(disaster_funding_file, 'r') as f:
    disaster_funding = json.load(f)

print("Loaded {} disaster funding records".format(len(disaster_funding)))

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:28']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print("Loaded {} civic documents".format(len(civic_docs)))

# Create project funding map
project_funding = {}
for record in disaster_funding:
    project_name = record['Project_Name']
    project_funding[project_name] = int(record['Amount'])

# Find projects that started in 2022
projects_started_2022 = set()

# Pattern to match 2022 in various date formats
year_2022_pattern = re.compile(r'2022[-\s]?(Spring|Summer|Fall|Winter|[A-Za-z]+|\d+)?', re.IGNORECASE)

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # For each disaster project, check if it's mentioned
    for project_name in project_funding.keys():
        # Skip if we already found this project started in 2022
        if project_name in projects_started_2022:
            continue
            
        # Check if project name appears in text
        if project_name.lower() in text.lower():
            # Look for date indicators near the project name
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if project_name.lower() in line.lower():
                    # Check this line and nearby lines for 2022 dates
                    context_lines = lines[max(0, i-2):min(len(lines), i+3)]
                    context_text = ' '.join(context_lines)
                    
                    # Check if 2022 is mentioned in context
                    if year_2022_pattern.search(context_text):
                        # Check for start-related keywords
                        start_keywords = ['begin', 'start', 'commence', 'advertise', 'design', 'construction', 'schedule', 'complete']
                        line_lower = line.lower()
                        
                        # Also check if project name contains 2022
                        if '2022' in project_name:
                            projects_started_2022.add(project_name)
                            break
                        
                        # Check for start indicators in context
                        if any(keyword in context_text.lower() for keyword in start_keywords):
                            projects_started_2022.add(project_name)
                            break

print("\nFound {} projects started in 2022".format(len(projects_started_2022)))

# Calculate total funding
total_funding = sum(project_funding[p] for p in projects_started_2022)

print("\nTotal funding: ${:,}".format(total_funding))

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(projects_started_2022),
    'projects': [{'name': p, 'amount': project_funding[p]} for p in sorted(projects_started_2022)]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
