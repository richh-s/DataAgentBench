code = """import json

# Load data
with open(locals()['var_functions.query_db:6']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:30']) as d:
    docs = json.load(d)

# Build funding lookup table
funding_lookup = {item['Project_Name']: int(item['Amount']) for item in funding}

# Variables to track results
matching_projects = []
total_funding = 0

# Keywords to identify disaster projects and headers to skip
disaster_keywords = ['fema', 'caloes', 'caljpia', 'fire']
skip_indicators = ['Page', 'Agenda Item', 'Public Works', 'Commission Meeting', 'Chair', 'Prepared by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Complete:', 'Advertise:', 'Begin:', 'Updates:', 'Project Schedule:', 'Project Description:']

# Process each document
for doc in docs:
    lines = doc.get('text', '').split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip short or skip-worthy lines
        if len(line) < 5:
            continue
            
        if any(indicator in line for indicator in skip_indicators):
            continue
            
        # Look for 2022 in project names (avoiding detail lines)
        if '2022' in line and not line.startswith('(') and not line.startswith('•'):
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in disaster_keywords):
                # Find funding amount
                amount = 0
                if line in funding_lookup:
                    amount = funding_lookup[line]
                else:
                    base_name = line.split('(FEMA')[0].strip() if '(FEMA' in line else line
                    if base_name in funding_lookup:
                        amount = funding_lookup[base_name]
                
                if amount > 0:
                    matching_projects.append({'name': line, 'amount': amount})
                    total_funding += amount

# Prepare result
result = {
    'count': len(matching_projects),
    'total_funding': total_funding,
    'projects': matching_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
