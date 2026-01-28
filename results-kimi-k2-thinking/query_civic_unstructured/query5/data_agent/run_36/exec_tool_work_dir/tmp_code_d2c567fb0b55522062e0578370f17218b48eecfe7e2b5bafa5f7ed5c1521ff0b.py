code = """import json
import re

# Load funding data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    funding = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:30'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup
funding_lookup = {}
for item in funding:
    funding_lookup[item['Project_Name']] = int(item['Amount'])

# Extract disaster projects starting in 2022
disaster_2022 = []
total = 0

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 5:
            continue
        
        skip_words = ['Page', 'Agenda', 'Public', 'Commission', 'Chair', 'Prepared', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Complete:', 'Advertise:', 'Begin:', 'Updates:']
        if any(word in line for word in skip_words):
            continue
        
        if '2022' in line and not line.startswith('(') and not line.startswith('•'):
            is_disaster = any(k in line.lower() for k in ['fema', 'caloes', 'caljpia', 'fire'])
            if is_disaster:
                clean_line = line
                fund_amount = 0
                
                # Try exact match
                if clean_line in funding_lookup:
                    fund_amount = funding_lookup[clean_line]
                else:
                    # Try base name without FEMA suffix
                    base = clean_line.split('(FEMA')[0].strip()
                    if base in funding_lookup:
                        fund_amount = funding_lookup[base]
                
                if fund_amount > 0:
                    disaster_2022.append({'name': clean_line, 'amount': fund_amount})
                    total += fund_amount

result = {
    'count': len(disaster_2022),
    'total': total,
    'projects': disaster_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
