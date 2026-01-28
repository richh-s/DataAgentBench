code = """import json

# Load funding data (already a list)
funding_data = var_functions_query_db_24

# Load civic documents
civic_file = var_functions_query_db_4
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create mapping of project statuses
status_map = {}
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 5: continue
        
        # Look for project names (not headers, not bullet points)
        if not line.endswith(('.', ':', ';')) and not line.startswith(('•', '-', '(cid:')):
            # Check next lines for status indicators
            next_text = ' '.join(lines[i+1:i+5])
            if any(indicator in next_text for indicator in ['Updates:', 'Project Schedule:', 'construction']):
                # Determine status
                status = 'Unknown'
                next_lower = next_text.lower()
                if 'under construction' in next_lower:
                    status = 'Construction'
                elif 'construction was completed' in next_lower:
                    status = 'Completed'
                elif 'complete design' in next_lower or 'staff is working' in next_lower:
                    status = 'Design'
                elif 'advertise:' in next_lower or 'out to bid' in next_lower:
                    status = 'Bidding'
                elif 'awaiting' in next_lower:
                    status = 'Awaiting Approval'
                
                status_map[line] = status

# Match funding with statuses
results = []
for item in funding_data:
    name = item['Project_Name']
    amt = int(item['Amount'])
    source = item['Funding_Source']
    status = 'Unknown'
    
    # Exact match
    if name in status_map:
        status = status_map[name]
    else:
        # Base name without suffix
        base = name.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (FEMA/CalOES Project)', '')
        for key, val in status_map.items():
            if base.lower() in key.lower() or key.lower() in base.lower():
                status = val
                break
    
    results.append([name, source, amt, status])

# Format output
output = []
for r in results:
    output.append(f"Project: {r[0]}")
    output.append(f"Funding: {r[1]}")
    output.append(f"Amount: ${r[2]:,}")
    output.append(f"Status: {r[3]}")
    output.append("")

final_text = '\n'.join(output)

total_projects = len(results)
total_amount = sum(r[2] for r in results)

status_counts = {}
for r in results:
    status_counts[r[3]] = status_counts.get(r[3], 0) + 1

summary = f"Total Projects: {total_projects}\nTotal Amount: ${total_amount:,}\n\nStatus Breakdown:\n"
for s, c in sorted(status_counts.items()):
    summary += f"  {s}: {c}\n"

full_output = final_text + "\n" + "="*50 + "\nSUMMARY\n" + "="*50 + "\n" + summary

print('__RESULT__:')
print(json.dumps({'output': full_output, 'summary': summary}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'mongo_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'mongo_is_list': False, 'funding_is_list': False}, 'var_functions.query_db:24': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
