code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Find park projects completed in 2022
park_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Look for documents mentioning both park and completion in 2022
    if 'park' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for completion statements with 2022
            if '2022' in line and ('completed' in line.lower() or 'construction was completed' in line.lower()):
                # Look backwards to find project name
                for j in range(i-1, max(0, i-5), -1):
                    prev_line = lines[j].strip()
                    prev_lower = prev_line.lower()
                    
                    if prev_line and len(prev_line) > 5 and 'Updates:' not in prev_line:
                        skip_words = ['capital improvement', 'disaster recovery', 'public works', 'commission', 'agenda', 'subject:', 'page ']
                        if not any(word in prev_lower for word in skip_words):
                            if 'park' in prev_lower:
                                park_projects_2022.append(prev_line)
                                break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Match funding records
project_funding = {}
total_funding = 0

for project in park_projects_2022:
    proj_lower = project.lower()
    for fund in funding_records:
        fund_name = fund['Project_Name'].lower()
        
        # Match if names are similar
        if proj_lower == fund_name or proj_lower in fund_name or fund_name in proj_lower:
            amount = int(fund['Amount'])
            if project not in project_funding:
                project_funding[project] = 0
            project_funding[project] += amount
            total_funding += amount

result = {
    'total_funding': total_funding,
    'project_funding': project_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:30': [{'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}]}

exec(code, env_args)
