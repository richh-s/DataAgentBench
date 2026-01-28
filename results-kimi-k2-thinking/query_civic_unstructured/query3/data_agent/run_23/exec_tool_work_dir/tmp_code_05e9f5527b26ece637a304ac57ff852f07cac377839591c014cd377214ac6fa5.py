code = """import json
import re

# Load data
funding_records = locals()['var_functions.query_db_56']
civic_path = locals()['var_functions.query_db_57']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_records), 'funding records and', len(civic_docs), 'civic documents')

# Extract project statuses
status_map = {}
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5: continue
        
        # Skip headers
        skip = ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:']
        if any(term in line for term in skip): continue
        
        # Look for project names with following status
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:')):
            next_text = ' '.join(lines[i+1:i+5])
            if 'Updates:' in next_text or 'Project Schedule:' in next_text or 'construction' in next_text:
                status = 'Unknown'
                nt = next_text.lower()
                if 'under construction' in nt: status = 'Construction'
                elif 'completed' in nt: status = 'Completed'
                elif 'design' in nt: status = 'Design'
                elif 'advertise' in nt or 'bid' in nt: status = 'Bidding'
                elif 'awaiting' in nt or 'waiting' in nt: status = 'Awaiting'
                elif 'not started' in nt: status = 'Not Started'
                status_map[line] = status

print('Project statuses extracted:', len(status_map))

# Match funding records
results = []
for rec in funding_records:
    name = rec['Project_Name']
    amt = int(rec['Amount'])
    src = rec['Funding_Source']
    status = 'Unknown'
    
    if name in status_map: status = status_map[name]
    else:
        base = name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (CalJPIA/FEMA Project)', '')
        for en, es in status_map.items():
            if base.lower() in en.lower() or en.lower() in base.lower():
                status = es
                break
    
    results.append({'Project': name, 'Funding': src, 'Amount': amt, 'Status': status})

# Format output
output_lines = []
for r in sorted(results, key=lambda x: x['Project']):
    output_lines.append('Project: ' + str(r['Project']))
    output_lines.append('Funding: ' + str(r['Funding']))
    output_lines.append('Amount: $' + str(r['Amount']))
    output_lines.append('Status: ' + str(r['Status']))
    output_lines.append('')

details = '\n'.join(output_lines)

# Summary
from collections import defaultdict
status_counts = defaultdict(int)
total_amt = 0
for r in results:
    status_counts[r['Status']] += 1
    total_amt += r['Amount']

summary = 'SUMMARY\n' + '='*60 + '\n'
summary += 'Total Projects: ' + str(len(results)) + '\n'
summary += 'Total Funding: $' + str(total_amt) + '\n\nStatus Breakdown:\n'
for s, c in sorted(status_counts.items()):
    summary += '  ' + s + ': ' + str(c) + '\n'

final_text = details + '\n' + summary

print('__RESULT__:')
result = {'output': final_text, 'total_projects': len(results), 'total_amount': total_amt}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:56': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:57': 'file_storage/functions.query_db:57.json'}

exec(code, env_args)
