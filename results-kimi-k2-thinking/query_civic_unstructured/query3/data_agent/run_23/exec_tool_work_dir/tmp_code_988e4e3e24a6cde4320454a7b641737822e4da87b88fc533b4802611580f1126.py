code = """import json
import re

# Get data from storage
funding_result = locals()['var_functions.query_db_24']
civic_file_path = locals()['var_functions.query_db_4']

# Load civic documents
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project info from civic documents
project_statuses = {}

for doc in civic_docs:
    text = doc.get('text', '')
    # Split into lines and process
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5: continue
        
        # Skip header lines
        header_terms = ['Item', 'To:', 'Prepared by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Project Schedule:', 'Project Description:', 'Updates:']
        if any(term in line for term in header_terms): continue
        
        # Look for potential project names (not ending with punctuation, not bullet points)
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:', '□')):
            # Check if next few lines contain status information
            next_chunk = '\n'.join(lines[i+1:i+6])
            if any(indicator in next_chunk for indicator in ['Updates:', 'Project Schedule:', 'construction', 'design', 'Complete', 'Advertise', 'Awaiting']):
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
                
                project_statuses[line] = status

# Match funding records with statuses
results = []
for funding in funding_result:
    proj_name = funding['Project_Name']
    status = 'Unknown'
    
    # Exact match
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
                (len(base_name) > 12 and base_name[:12].lower() in extracted_name.lower())):
                status = extracted_status
                break
    
    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': int(funding['Amount']),
        'Status': status
    })

# Format detailed results
detailed_lines = []
for r in results:
    detailed_lines.append(f"Project: {r['Project_Name']}")
    detailed_lines.append(f"  Funding: {r['Funding_Source']}")
    detailed_lines.append(f"  Amount: ${r['Amount']:,}")
    detailed_lines.append(f"  Status: {r['Status']}")
    detailed_lines.append("")

detailed_output = '\n'.join(detailed_lines)

# Summary statistics
total_projects = len(results)
total_amount = sum(r['Amount'] for r in results)

# Count by status
status_counts = {}
amount_by_status = {}
for r in results:
    status = r['Status']
    status_counts[status] = status_counts.get(status, 0) + 1
    amount_by_status[status] = amount_by_status.get(status, 0) + r['Amount']

summary = f"""SUMMARY
{'='*60}
Total FEMA/Emergency Projects: {total_projects}
Total Funding Amount: ${total_amount:,}

Projects by Status:
"""
for status in sorted(status_counts.keys()):
    count = status_counts[status]
    amount = amount_by_status[status]
    percentage = (amount / total_amount * 100) if total_amount > 0 else 0
    summary += f"  {status}: {count} projects, ${amount:,} ({percentage:.1f}%)\n"

final_result = detailed_output + summary

print('__RESULT__:')
print(json.dumps({'final_output': final_result, 'total_projects': total_projects, 'total_amount': total_amount}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
