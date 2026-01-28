code = """import json
import re
from collections import defaultdict

# Load the data - Funding results are already a list
funding_results = var_functions_query_db_24
civic_docs_path = var_functions_query_db_4

# Load civic documents
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded data:')
print(f'- {len(funding_results)} funding records')
print(f'- {len(civic_docs)} civic documents')

# Extract project statuses from civic documents
project_statuses = {}
status_keywords = {
    'construction': ['under construction'],
    'completed': ['construction was completed', 'complete construction', 'construction completed'],
    'design': ['complete design', 'staff is working', 'finalize the design'],
    'bidding': ['advertise:', 'out to bid', 'bids are due'],
    'awaiting': ['awaiting'],
    'not started': ['not started', 'identified in the']
}

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5: continue
        
        # Skip header lines
        if any(term in line for term in ['Item', 'To:', 'Prepared by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Project Schedule:', 'Project Description:']):
            continue
        
        # Look for project names (lines without punctuation at end, not bullet points)
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:', '□')):
            # Look ahead for status information
            next_text = ' '.join(lines[i+1:i+6])
            
            if any(keyword in next_text for keyword in ['Updates:', 'Project Schedule:', 'construction', 'Complete', 'Advertise', 'Awaiting']):
                # Determine status
                status = 'Unknown'
                next_lower = next_text.lower()
                
                if any(keyword in next_lower for keyword in status_keywords['construction']):
                    status = 'Construction'
                elif any(keyword in next_lower for keyword in status_keywords['completed']):
                    status = 'Completed'
                elif any(keyword in next_lower for keyword in status_keywords['design']):
                    status = 'Design'
                elif any(keyword in next_lower for keyword in status_keywords['bidding']):
                    status = 'Bidding'
                elif any(keyword in next_lower for keyword in status_keywords['awaiting']):
                    status = 'Awaiting Approval'
                elif any(keyword in next_lower for keyword in status_keywords['not started']):
                    status = 'Not Started'
                
                project_statuses[line] = status

print(f'Extracted {len(project_statuses)} project statuses')

# Match funding records with project statuses
matched_projects = []
for funding in funding_results:
    proj_name = funding['Project_Name']
    status = 'Unknown'
    
    # Direct match
    if proj_name in project_statuses:
        status = project_statuses[proj_name]
    else:
        # Try base name without FEMA/CalOES suffixes
        base_name = proj_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (FEMA/CalOES Project)', ' (CalJPIA Project)', ' (CalJPIA/FEMA Project)']:
            base_name = base_name.replace(suffix, '')
        
        # Partial match
        for extracted_name, extracted_status in project_statuses.items():
            if (base_name.lower() in extracted_name.lower() or 
                extracted_name.lower() in base_name.lower() or
                (len(base_name) > 10 and base_name[:12].lower() in extracted_name.lower())):
                status = extracted_status
                break
    
    matched_projects.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': int(funding['Amount']),
        'Status': status
    })

print(f'Matched {len(matched_projects)} projects')

# Format detailed results
details = []
for project in matched_projects:
    details.append(f"Project: {project['Project_Name']}")
    details.append(f"  Funding Source: {project['Funding_Source']}")
    details.append(f"  Amount: ${project['Amount']:,}")
    details.append(f"  Status: {project['Status']}")
    details.append("")

detailed_output = '\n'.join(details)

# Summary statistics
total_projects = len(matched_projects)
total_funding = sum(p['Amount'] for p in matched_projects)

status_summary = defaultdict(int)
amount_summary = defaultdict(int)
for p in matched_projects:
    status_summary[p['Status']] += 1
    amount_summary[p['Status']] += p['Amount']

summary = f"""SUMMARY
{'='*50}
Total FEMA/Emergency Projects: {total_projects}
Total Funding Amount: ${total_funding:,}

Projects by Status:
"""

for status in sorted(status_summary.keys()):
    count = status_summary[status]
    amount = amount_summary[status]
    summary += f"  {status}: {count} projects, ${amount:,}\n"

final_result = detailed_output + '\n' + summary

print('__RESULT__:')
print(json.dumps({
    'complete_results': final_result,
    'total_projects': total_projects,
    'total_amount': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
