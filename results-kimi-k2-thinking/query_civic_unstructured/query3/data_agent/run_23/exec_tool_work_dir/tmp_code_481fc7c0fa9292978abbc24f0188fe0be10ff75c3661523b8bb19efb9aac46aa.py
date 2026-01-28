code = """import json
import re

funding_results = locals()['var_functions.query_db:24']
civic_docs_path = locals()['var_functions.query_db:4']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('Loading data completed')
print('Funding records:', len(funding_results))
print('Civic docs:', len(civic_docs))

project_statuses = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5: continue
        
        skip_terms = ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']
        if any(term in line for term in skip_terms): continue
        
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:')):
            next_text = ' '.join(lines[i+1:i+5])
            if any(keyword in next_text for keyword in ['Updates:', 'Project Schedule:', 'construction', 'Complete', 'Advertise', 'Awaiting']):
                status = 'Unknown'
                next_text_lower = next_text.lower()
                
                if 'under construction' in next_text_lower:
                    status = 'Construction'
                elif 'construction was completed' in next_text_lower:
                    status = 'Completed'
                elif 'complete design' in next_text_lower or 'staff is working' in next_text_lower:
                    status = 'Design'
                elif 'advertise:' in next_text_lower or 'out to bid' in next_text_lower:
                    status = 'Bidding'
                elif 'awaiting' in next_text_lower:
                    status = 'Awaiting Approval'
                
                project_statuses[line] = status

print('Project statuses extracted:', len(project_statuses))

results = []
for funding in funding_results:
    proj_name = funding['Project_Name']
    status = 'Unknown'
    
    if proj_name in project_statuses:
        status = project_statuses[proj_name]
    else:
        base_name = proj_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '')
        
        for extracted_name, extracted_status in project_statuses.items():
            if base_name.lower() in extracted_name.lower() or extracted_name.lower() in base_name.lower():
                status = extracted_status
                break
    
    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': int(funding['Amount']),
        'Status': status
    })

output_lines = []
for r in results:
    output_lines.append('Project: ' + r['Project_Name'])
    output_lines.append('Funding: ' + r['Funding_Source'])
    output_lines.append('Amount: $' + '{:,}'.format(r['Amount']))
    output_lines.append('Status: ' + r['Status'])
    output_lines.append('')

final_output = '\n'.join(output_lines)

total_amount = sum(r['Amount'] for r in results)
status_counts = {}
for r in results:
    status_counts[r['Status']] = status_counts.get(r['Status'], 0) + 1

result_data = {
    'detailed_results': final_output,
    'total_projects': len(results),
    'total_amount': total_amount,
    'status_counts': status_counts
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
