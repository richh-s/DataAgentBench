code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:46']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:30']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Build funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[project_name] = amount

# Extract disaster projects that mention 2022 from civic documents
disaster_projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 5:
            continue
            
        # Skip headers, footers and detail lines
        skip_patterns = [
            'Page', 'Agenda Item', 'Public Works', 'Commission', 
            'Chair', 'Prepared by', 'Date prepared', 'Meeting date', 
            'Subject', 'RECOMMENDED', 'DISCUSSION', 'Complete:', 
            'Advertise:', 'Begin:', 'Updates:', 'Project Schedule:', 
            'Project Description:', 'Project Updates:'
        ]
        
        if any(pattern in line for pattern in skip_patterns):
            continue
        
        # Look for lines containing 2022 that are not bullet points
        if '2022' in line and not line.startswith('(') and not line.startswith('•'):
            # Check if it's a disaster project
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'recovery']):
                # Try to find funding for this project
                funding_amount = 0
                
                # Check exact match first
                if line in funding_lookup:
                    funding_amount = funding_lookup[line]
                else:
                    # Try without FEMA/CalOES suffixes
                    base_name = line.split('(FEMA')[0].strip()
                    if base_name in funding_lookup:
                        funding_amount = funding_lookup[base_name]
                
                if funding_amount > 0:
                    disaster_projects_2022.append({
                        'name': line,
                        'amount': funding_amount
                    })

# Calculate total funding
total_funding = sum(p['amount'] for p in disaster_projects_2022)

result = {
    'total_disaster_projects_2022': len(disaster_projects_2022),
    'total_funding_amount': total_funding,
    'projects': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
