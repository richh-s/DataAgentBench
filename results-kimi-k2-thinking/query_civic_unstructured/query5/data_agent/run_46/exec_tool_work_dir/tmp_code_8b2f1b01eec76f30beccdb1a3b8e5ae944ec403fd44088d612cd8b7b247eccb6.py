code = """import json

# Get the stored data
funding_data = locals()['var_functions.query_db:56']
civic_docs_data = locals()['var_functions.query_db:58']

# Calculate total funding for all disaster projects
total_disaster_funding = sum(int(record['Amount']) for record in funding_data)

# Identify disaster projects that started in 2022
projects_2022 = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for projects with 2022 in their name or schedule
    if '2022' in text:
        # Extract project names and check if they're disaster projects
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Check for project names that start with 2022
            if line.startswith('2022') and ('Storm' in line or 'Drain' in line or 'Road' in line):
                # Clean up project name
                base_name = line.split(' (')[0].strip()
                projects_2022.append(base_name)

# Match with funding records
funding_2022 = 0
matched_projects = []
for record in funding_data:
    project_name = record['Project_Name']
    base_name = project_name.split(' (')[0].strip()
    amount = int(record['Amount'])
    
    # Check if this project started in 2022
    for proj2022 in projects_2022:
        if proj2022 in project_name or base_name in proj2022:
            funding_2022 += amount
            if base_name not in matched_projects:
                matched_projects.append(base_name)

# Also check for projects with 2022 in their name specifically
for record in funding_data:
    project_name = record['Project_Name']
    if '2022' in project_name:
        funding_2022 += int(record['Amount'])
        base_name = project_name.split(' (')[0].strip()
        if base_name not in matched_projects:
            matched_projects.append(base_name)

print('__RESULT__:')
print(json.dumps({
    'total_disaster_funding_2022': funding_2022,
    'projects_matched': len(matched_projects),
    'all_disaster_funding': total_disaster_funding
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000', 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000', 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000', 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000', 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000', 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000', 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000', 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000', 'Funding_Source': 'Private Sponsor'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000', 'Funding_Source': 'Impact Investment Fund'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000', 'Funding_Source': 'Development Bank Loan'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000', 'Funding_Source': 'Federal Assistance'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000', 'Funding_Source': 'National Foundation Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000', 'Funding_Source': 'Community Fund'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000', 'Funding_Source': 'Environmental Grant'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000', 'Funding_Source': 'State Development Grant'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Local Business Support'}], 'var_functions.query_db:44': [{'total_funding': '1410000'}], 'var_functions.query_db:46': [], 'var_functions.query_db:52': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'total_amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'total_amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'total_amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'total_amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'total_amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'total_amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'total_amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'total_amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'total_amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'total_amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'total_amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'total_amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'total_amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'total_amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'total_amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'total_amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'total_amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'total_amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'total_amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'total_amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'total_amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'total_amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'total_amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'total_amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'total_amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'total_amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'total_amount': '77000'}], 'var_functions.query_db:56': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
