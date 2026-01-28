code = """import json
import re
from collections import defaultdict

# Load data from storage
funding_results = locals()['var_functions.query_db:24']
civic_docs_path = locals()['var_functions.query_db:4']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Found {len(funding_results)} FEMA-related funding records')
print(f'Found {len(civic_docs)} civic documents to search')

# Extract project statuses from civic documents
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Skip headers
        skip_terms = ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Project Schedule:', 'Project Description:', 'Project Updates:', 'Updates:']
        if any(term in line for term in skip_terms):
            continue
        
        # Look for project names that are followed by status info
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '□', '(cid:')) and '•' not in line:
            next_chunk = ' '.join(lines[i+1:i+5])
            if any(keyword in next_chunk for keyword in ['Updates:', 'Project Schedule:', 'construction', 'design', 'Complete', 'Advertise', 'Awaiting']):
                current_project = line
                
                # Determine status
                status = 'Unknown'
                next_text_lower = next_chunk.lower()
                
                if 'under construction' in next_text_lower:
                    status = 'Construction'
                elif 'construction was completed' in next_text_lower or 'complete construction' in next_text_lower:
                    status = 'Completed'
                elif 'complete design' in next_text_lower or 'staff is working' in next_text_lower:
                    status = 'Design'
                elif 'advertise:' in next_text_lower or 'out to bid' in next_text_lower:
                    status = 'Bidding'
                elif 'awaiting' in next_text_lower:
                    status = 'Awaiting Approval'
                elif 'not started' in next_text_lower:
                    status = 'Not Started'
                
                project_info[current_project] = status

print(f'Extracted {len(project_info)} project statuses from documents')

# Match funding records with statuses
results = []
for funding in funding_results:
    proj_name = funding['Project_Name']
    status = 'Unknown'
    
    # Direct match
    if proj_name in project_info:
        status = project_info[proj_name]
    else:
        # Base name without FEMA suffixes
        base_name = proj_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '').replace(' (CalJPIA Project)', '').replace(' (CalJPIA/FEMA Project)', '')
        
        # Find matching project
        for extracted_name, extracted_status in project_info.items():
            if base_name.lower() in extracted_name.lower() or extracted_name.lower() in base_name.lower():
                status = extracted_status
                break
    
    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': int(funding['Amount']),
        'Status': status
    })

print(f'Matched {len(results)} projects with funding and status')

# Format output
format_output = []
for r in results:
    format_output.append(f"Project: {r['Project_Name']}")
    format_output.append(f"Funding: {r['Funding_Source']}")
    format_output.append(f"Amount: ${r['Amount']:,}")
    format_output.append(f"Status: {r['Status']}")
    format_output.append("")

final_text = '\n'.join(format_output)

# Statistics
status_summary = defaultdict(int)
amt_summary = defaultdict(int)
for r in results:
    status_summary[r['Status']] += 1
    amt_summary[r['Status']] += r['Amount']

total_amount = sum(r['Amount'] for r in results)

print('__RESULT__:')
print(json.dumps({
    'detailed_results': final_text,
    'total_projects': len(results),
    'total_amount': total_amount,
    'status_counts': dict(status_summary),
    'status_amounts': dict(amt_summary)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
