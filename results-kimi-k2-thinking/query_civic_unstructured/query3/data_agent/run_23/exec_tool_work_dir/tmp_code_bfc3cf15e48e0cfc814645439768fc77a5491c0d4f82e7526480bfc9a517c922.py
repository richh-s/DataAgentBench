code = """import json
import re

# Load funding data
funding_data = locals()['var_functions.query_db:24']

# Load civic docs from file path
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as file:
    civic_docs = json.load(file)

# Extract project statuses from civic documents
project_info = {}
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        # Skip headers that are not project names
        if any(x in line for x in ['Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
        # Look for project names followed by status info
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:')):
            next_text = ' '.join(lines[i+1:i+6])
            if any(keyword in next_text for keyword in ['Updates:', 'Project Schedule:', 'construction', 'Complete', 'Advertise']):
                status = 'Unknown'
                next_lower = next_text.lower()
                if 'under construction' in next_lower:
                    status = 'Construction'
                elif 'construction was completed' in next_lower or 'complete construction' in next_lower:
                    status = 'Completed'
                elif 'complete design' in next_lower or 'staff is working' in next_lower:
                    status = 'Design'
                elif 'advertise:' in next_lower or 'out to bid' in next_lower:
                    status = 'Bidding'
                elif 'awaiting' in next_lower:
                    status = 'Awaiting Approval'
                project_info[line] = status

# Match funding with status
results = []
for record in funding_data:
    proj_name = record['Project_Name']
    status = 'Unknown'
    if proj_name in project_info:
        status = project_info[proj_name]
    else:
        base_name = proj_name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '')
        for extracted_name, extracted_status in project_info.items():
            if base_name.lower() in extracted_name.lower() or extracted_name.lower() in base_name.lower():
                status = extracted_status
                break
    results.append({'Project_Name': proj_name, 'Funding_Source': record['Funding_Source'], 'Amount': record['Amount'], 'Status': status})

# Format results
output_lines = []
for r in results:
    output_lines.append(f"Project: {r['Project_Name']}")
    output_lines.append(f"Funding: {r['Funding_Source']}")
    output_lines.append(f"Amount: ${int(r['Amount']):,}")
    output_lines.append(f"Status: {r['Status']}")
    output_lines.append('')

detailed_results = '\n'.join(output_lines)

# Summary statistics
total_projects = len(results)
total_amount = sum(int(r['Amount']) for r in results)
status_counts = {}
for r in results:
    status = r['Status']
    status_counts[status] = status_counts.get(status, 0) + 1

summary = f"Total Projects: {total_projects}\nTotal Amount: ${total_amount:,}\n"
summary += "Status Breakdown:\n"
for status, count in sorted(status_counts.items()):
    summary += f"  {status}: {count}\n"

final_output = detailed_results + "\n" + "="*60 + "\nSUMMARY\n" + "="*60 + "\n" + summary

print('__RESULT__:')
print(json.dumps({'output': final_output, 'total_projects': total_projects, 'total_amount': total_amount}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
