code = """import json
import re
from collections import defaultdict

funding_data = var_functions.query_db_56

civic_file_path = var_functions.query_db_57
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded data:')
print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

project_statuses = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5: continue
        
        skip_terms = ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Project Schedule:', 'Project Description:', 'Project Updates:', 'Updates:']
        if any(term in line for term in skip_terms): continue
        
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:')):
            next_chunk = ' '.join(lines[i+1:i+6])
            if any(keyword in next_chunk for keyword in ['Updates:', 'Project Schedule:', 'construction', 'design', 'Complete', 'Advertise', 'Awaiting']):
                status = 'Unknown'
                next_lower = next_chunk.lower()
                if 'under construction' in next_lower:
                    status = 'Construction'
                elif 'construction was completed' in next_lower or 'complete construction' in next_lower:
                    status = 'Completed'
                elif 'complete design' in next_lower or 'staff is working' in next_lower or 'finalize the design' in next_lower:
                    status = 'Design'
                elif 'advertise:' in next_lower or 'out to bid' in next_lower:
                    status = 'Bidding'
                elif 'awaiting' in next_lower:
                    status = 'Awaiting Approval'
                elif 'not started' in next_lower or 'identified in the' in next_lower:
                    status = 'Not Started'
                project_statuses[line] = status

print('Project statuses extracted:', len(project_statuses))

results = []
for record in funding_data:
    proj_name = record['Project_Name']
    status = 'Unknown'
    if proj_name in project_statuses:
        status = project_statuses[proj_name]
    else:
        base_name = proj_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (FEMA/CalOES Project)', ' (CalJPIA Project)', ' (CalJPIA/FEMA Project)']:
            base_name = base_name.replace(suffix, '')
        for extracted_name, extracted_status in project_statuses.items():
            if base_name.lower() in extracted_name.lower() or extracted_name.lower() in base_name.lower():
                status = extracted_status
                break
    results.append({
        'Project_Name': proj_name,
        'Funding_Source': record['Funding_Source'],
        'Amount': int(record['Amount']),
        'Status': status
    })

print('Matched results:', len(results))

detailed_output = []
for r in sorted(results, key=lambda x: x['Project_Name']):
    detailed_output.append('Project: ' + r['Project_Name'])
    detailed_output.append('Funding Source: ' + r['Funding_Source'])
    detailed_output.append('Amount: $' + str(r['Amount']))
    detailed_output.append('Status: ' + r['Status'])
    detailed_output.append('')

output_text = '\\n'.join(detailed_output)

total_projects = len(results)
total_amount = sum(r['Amount'] for r in results)

status_counts = defaultdict(int)
amount_by_status = defaultdict(int)
for r in results:
    status_counts[r['Status']] += 1
    amount_by_status[r['Status']] += r['Amount']

summary_lines = []
summary_lines.append('SUMMARY')
summary_lines.append('='*60)
summary_lines.append('Total FEMA/Emergency Projects: ' + str(total_projects))
summary_lines.append('Total Funding: $' + str(total_amount))
summary_lines.append('')
summary_lines.append('Projects by Status:')
for status in sorted(status_counts.keys()):
    count = status_counts[status]
    amount = amount_by_status[status]
    summary_lines.append('  ' + status + ': ' + str(count) + ' projects, $' + str(amount))

summary_text = '\\n'.join(summary_lines)

final_result = output_text + '\\n\\n' + summary_text

result_data = {
    'output': final_result,
    'total_projects': total_projects,
    'total_amount': total_amount
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:56': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:57': 'file_storage/functions.query_db:57.json'}

exec(code, env_args)
