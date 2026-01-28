code = """import json, re

# The variables should already be the parsed data
civic_docs = var_functions.query_db_32
funding = var_functions.query_db_30

# Create project status mapping from civic documents
status_map = {}
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Skip metadata lines
        if line.startswith('(') or line.startswith('Page') or line.startswith('Agenda'):
            continue
        
        # Detect project names (uppercase first letter, not metadata)
        if len(line) > 10 and line[0].isupper() and ':' not in line[:30]:
            current_project = line
            continue
        
        # If we have a current project, look for status
        if current_project:
            lower = line.lower()
            if 'complete design:' in lower or 'advertise:' in lower:
                status_map[current_project] = 'Design'
            elif 'under construction' in lower or 'begin construction' in lower:
                status_map[current_project] = 'Construction'
            elif 'construction was completed' in lower:
                status_map[current_project] = 'Completed'
            elif 'not started' in lower or 'preliminary design' in lower:
                status_map[current_project] = 'Not Started'

print("Status map size:", len(status_map))

# Process FEMA/Emergency funding records
results = []
for rec in funding:
    project_name = rec['Project_Name']
    amount = rec['Amount']
    
    # Find status
    status = 'Unknown'
    base_name = project_name.split(' (')[0]
    
    for doc_project, doc_status in status_map.items():
        if base_name.upper() in doc_project.upper() or doc_project.upper() in base_name.upper():
            status = doc_status
            break
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': rec['Funding_Source'],
        'Amount': amount,
        'Status': status
    })

# Sort by amount descending
results.sort(key=lambda x: int(x['Amount']), reverse=True)

# Format output
output_lines = []
output_lines.append("FEMA and Emergency Related Projects:")
output_lines.append("=" * 60)

for r in results:
    line = f"{r['Project_Name']} | ${r['Amount']} | {r['Funding_Source']} | Status: {r['Status']}"
    output_lines.append(line)

final_text = "\n".join(output_lines)
print(final_text[:2000])

# Return as JSON-serializable
__RESULT__ = json.dumps(results)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
