code = """import json

# Access stored results
funding_data = var_functions.query_db_30
civic_docs_data = var_functions.query_db_32

# Create status mapping from civic documents
status_map = {}
for doc in civic_docs_data:
    text = doc['text']
    # Simple status extraction - look for status indicators after project mentions
    if 'construction was completed' in text.lower():
        # Extract project names from this doc
        lines = text.split('\n')
        for line in lines:
            if 'construction was completed' in line.lower():
                # Look back for project name
                idx = lines.index(line)
                for i in range(max(0, idx-5), idx):
                    proj_line = lines[i].strip()
                    if proj_line and not proj_line.startswith('(') and not proj_line.startswith('Page'):
                        status_map[proj_line] = 'Completed'
                        break
    elif 'under construction' in text.lower():
        lines = text.split('\n')
        for line in lines:
            if 'under construction' in line.lower():
                idx = lines.index(line)
                for i in range(max(0, idx-5), idx):
                    proj_line = lines[i].strip()
                    if proj_line and not proj_line.startswith('(') and not proj_line.startswith('Page'):
                        status_map[proj_line] = 'Construction'
                        break
    elif 'complete design:' in text.lower():
        lines = text.split('\n')
        for line in lines:
            if 'complete design:' in line.lower():
                idx = lines.index(line)
                for i in range(max(0, idx-5), idx):
                    proj_line = lines[i].strip()
                    if proj_line and not proj_line.startswith('(') and not proj_line.startswith('Page'):
                        status_map[proj_line] = 'Design'
                        break

# Build final results
results = []
for rec in funding_data:
    project_name = rec['Project_Name']
    base_name = project_name.split(' (')[0]
    
    # Find status
    status = 'Unknown'
    for doc_project, doc_status in status_map.items():
        if base_name in doc_project or doc_project in base_name:
            status = doc_status
            break
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': rec['Funding_Source'],
        'Amount': int(rec['Amount']),
        'Status': status
    })

# Sort by amount
results.sort(key=lambda x: x['Amount'], reverse=True)

# Create readable output
output = []
output.append("FEMA AND EMERGENCY RELATED PROJECTS")
output.append("=" * 70)
for r in results[:20]:
    output.append(f"{r['Project_Name']}")
    output.append(f"  Amount: ${r['Amount']:,}")
    output.append(f"  Funding: {r['Funding_Source']}")
    output.append(f"  Status: {r['Status']}")
    output.append("")

text_output = "\n".join(output)
print(text_output)

# Also return JSON for the final answer
__RESULT__ = json.dumps(results, indent=2)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
