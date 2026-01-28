code = """import json
import re

# Load the civic documents data from the stored file path
civic_docs = json.load(open(locals()['var_functions.query_db:2']))

# Extract projects with 2022 start dates
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip common headers
        if any(x in line for x in ['Page', 'Agenda Item', 'Public Works', 'Commission', 'Chair', 'Prepared by:', 'Date prepared:', 'Meeting date:', 'Subject:']):
            continue
        
        # Check for 2022 in the line
        if '2022' in line:
            # Make sure it's not a detail line
            if not any(indicator in line for indicator in ['Complete', 'Advertise:', 'Begin', 'Updates:', 'Project Schedule:', 'Project Description:']):
                
                # Check if it looks like a project name (not a bullet/detail line)
                if not line.startswith('(') and not line.startswith('•') and not line.startswith('-'):
                    is_disaster = any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery'])
                    
                    projects_2022.append({
                        'name': line,
                        'is_disaster': is_disaster
                    })

# Load funding data
funding = json.load(open(locals()['var_functions.query_db:6']))
funding_by_name = {item['Project_Name']: int(item['Amount']) for item in funding}

# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
total_funding = 0

for project in projects_2022:
    if project['is_disaster']:
        name = project['name']
        # Look for exact match in funding data
        if name in funding_by_name:
            amount = funding_by_name[name]
            disaster_projects_2022.append({
                'name': name,
                'amount': amount
            })
            total_funding += amount
        else:
            # Try without FEMA suffixes variations
            base_name = name.split('(FEMA')[0].strip()
            if base_name in funding_by_name:
                amount = funding_by_name[base_name]
                disaster_projects_2022.append({
                    'name': name,
                    'amount': amount
                })
                total_funding += amount

result = {
    'disaster_projects_matching_2022': len(disaster_projects_2022),
    'total_funding_amount': total_funding,
    'projects': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}}

exec(code, env_args)
