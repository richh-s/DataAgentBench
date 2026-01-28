code = """import json
import re

# Access the FEMA/emergency funding records directly (already a list)
funding_records = var_functions.query_db:24

# Load civic documents from the file path
civic_docs_file = var_functions.query_db:4
with open(civic_docs_file, 'r') as f:
    civic_documents = json.load(f)

print(f"Loaded {len(funding_records)} funding records")
print(f"Loaded {len(civic_documents)} civic documents")

# Extract project statuses from civic documents
project_status_map = {}

for doc in civic_documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5:
            continue
        
        # Skip header/metadata lines
        skip_terms = ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Project Schedule:', 'Project Description:', 'Updates:']
        if any(term in line for term in skip_terms):
            continue
        
        # Look for project names (not ending with punctuation, not bullet points)
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:', '□')):
            # Check if next few lines contain status information
            next_chunk = ' '.join(lines[i+1:i+6])
            
            status_indicators = ['Updates:', 'Project Schedule:', 'construction', 'design', 'Complete', 'Advertise', 'Awaiting']
            if any(indicator in next_chunk for indicator in status_indicators):
                # Determine status based on keywords
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
                
                project_status_map[line] = status

print(f"Extracted {len(project_status_map)} project statuses")

# Match funding records with project statuses
matched_results = []

for funding in funding_records:
    proj_name = funding['Project_Name']
    status = 'Unknown'
    
    # Direct match
    if proj_name in project_status_map:
        status = project_status_map[proj_name]
    else:
        # Try base name without FEMA/CalOES suffixes
        base_name = proj_name
        for suffix in [' (FEMA Project)', ' (CalOES Project)', ' (FEMA/CalOES Project)', ' (CalJPIA Project)', ' (CalJPIA/FEMA Project)']:
            base_name = base_name.replace(suffix, '')
        
        # Partial match
        for extracted_name, extracted_status in project_status_map.items():
            if (base_name.lower() in extracted_name.lower() or 
                extracted_name.lower() in base_name.lower() or
                (len(base_name) > 12 and base_name[:12].lower() in extracted_name.lower())):
                status = extracted_status
                break
    
    matched_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': int(funding['Amount']),
        'Status': status
    })

print(f"Matched {len(matched_results)} projects with funding and status")

# Format the results
detailed_lines = []
for r in matched_results:
    detailed_lines.append(f"Project: {r['Project_Name']}")
    detailed_lines.append(f"  Funding Source: {r['Funding_Source']}")
    detailed_lines.append(f"  Amount: ${r['Amount']:,}")
    detailed_lines.append(f"  Status: {r['Status']}")
    detailed_lines.append("")

detailed_text = '\n'.join(detailed_lines)

# Calculate summary statistics
total_projects = len(matched_results)
total_funding = sum(r['Amount'] for r in matched_results)

status_counts = {}
amount_by_status = {}
for r in matched_results:
    status = r['Status']
    status_counts[status] = status_counts.get(status, 0) + 1
    amount_by_status[status] = amount_by_status.get(status, 0) + r['Amount']

summary = f"""SUMMARY
{'='*60}
Total FEMA/Emergency Projects: {total_projects}
Total Funding Amount: ${total_funding:,}

Projects by Status:
"""

for status in sorted(status_counts.keys()):
    count = status_counts[status]
    amount = amount_by_status[status]
    percentage = (amount / total_funding * 100) if total_funding > 0 else 0
    summary += f"  {status}: {count} projects (${amount:,})\n"

final_output = detailed_text + summary

print('__RESULT__:')
print(json.dumps({
    'complete_results': final_output,
    'total_projects': total_projects,
    'total_amount': total_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
