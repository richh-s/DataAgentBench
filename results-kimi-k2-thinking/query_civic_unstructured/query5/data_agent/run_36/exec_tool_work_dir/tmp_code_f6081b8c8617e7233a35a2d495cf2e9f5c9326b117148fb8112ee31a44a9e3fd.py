code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Create a dictionary of funding by project name
funding_by_project = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_by_project[project_name] = amount

# Find disaster projects that started in 2022
disaster_projects_2022 = []
total_funding = 0

# Process each civic document
for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Split into lines and look for project information
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and footers
        if any(skip in line for skip in ['Page', 'Agenda Item', 'Public Works', 'Commission Meeting']):
            continue
        
        # Check if this line mentions 2022
        if '2022' in line:
            # Check if it appears to be a project name (not a date/schedule line)
            if not any(indicator in line for indicator in ['Complete', 'Advertise', 'Begin', 'Updates:', 'Project Schedule:', 'Project Description:']):
                # Look for disaster indicators
                is_disaster = False
                if any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery']):
                    is_disaster = True
                
                if is_disaster:
                    # Try to find funding for this project
                    if line in funding_by_project:
                        amount = funding_by_project[line]
                        disaster_projects_2022.append({'name': line, 'amount': amount})
                        total_funding += amount
                    else:
                        # Try variations without FEMA suffix
                        base_name = line.split('(FEMA')[0].strip()
                        if base_name in funding_by_project:
                            amount = funding_by_project[base_name]
                            disaster_projects_2022.append({'name': line, 'amount': amount})
                            total_funding += amount

# Count all FEMA/disaster projects in funding data for context
disaster_in_funding = []
for record in funding_data:
    project_name = record['Project_Name']
    if any(keyword in project_name.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire']):
        disaster_in_funding.append(project_name)

result = {
    'total_disaster_projects_in_funding': len(disaster_in_funding),
    'disaster_projects_2022_in_docs': len(disaster_projects_2022),
    'total_funding_for_2022_disaster_projects': total_funding,
    'matching_projects': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}}

exec(code, env_args)
