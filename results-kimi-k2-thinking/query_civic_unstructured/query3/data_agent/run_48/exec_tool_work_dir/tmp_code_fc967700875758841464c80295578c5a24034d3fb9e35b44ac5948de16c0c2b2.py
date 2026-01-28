code = """import json

# Load funding data
f_handle = open(locals()['var_functions.query_db:2'])
funding_data = json.load(f_handle)
f_handle.close()

# Load civic documents  
c_handle = open(locals()['var_functions.query_db:0'])
civic_docs = json.load(c_handle)
c_handle.close()

# Find FEMA and emergency projects
fema_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if 'FEMA' in name or 'fema' in name or 'emergency' in name.lower():
        fema_projects.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source', ''),
            'Amount': int(rec.get('Amount', 0))
        })

# Extract project status from civic documents
status_list = []
for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        
        low = line.lower()
        if 'project' in low or 'repairs' in low or 'sirens' in low or 'warning' in low:
            st = None
            for j in range(i+1, min(i+4, len(lines))):
                nxt = lines[j].lower()
                if 'design' in nxt and 'committee' not in nxt:
                    st = 'design'
                    break
                if 'completed' in nxt or 'completion' in nxt:
                    st = 'completed'
                    break
                if 'not started' in nxt:
                    st = 'not started'
                    break
            if st:
                status_list.append({'name': line, 'status': st})

# Match projects with status
results = []
for proj in fema_projects:
    status = 'Unknown'
    for st in status_list:
        proj_low = proj['Project_Name'].lower()
        name_low = st['name'].lower()
        if proj_low in name_low or name_low in proj_low:
            status = st['status']
            break
    
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:52': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)
