code = """import json, os

f_path = locals()['var_functions.query_db:2']
c_path = locals()['var_functions.query_db:0']

funding_data = json.loads(open(f_path).read())
civic_docs = json.loads(open(c_path).read())

fema_list = []
for rec in funding_data:
    n = rec['Project_Name']
    if 'FEMA' in n or 'fema' in n or 'emergency' in n.lower():
        fema_list.append({
            'Project_Name': n,
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount'])
        })

status_entries = []
for doc in civic_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10:
            low = line.lower()
            for kw in ['project', 'repairs', 'sirens', 'warning', 'drainage', 'improvements']:
                if kw in low:
                    st = None
                    for j in range(i+1, min(i+5, len(lines))):
                        nxt = lines[j].lower()
                        if 'design' in nxt and 'committee' not in nxt:
                            st = 'design'
                            break
                        if 'completed' in nxt or 'construction was completed' in nxt:
                            st = 'completed'
                            break
                        if 'not started' in nxt:
                            st = 'not started'
                            break
                    if st:
                        status_entries.append({'name': line, 'status': st})
                    break

results = []
for proj in fema_list:
    status = 'Unknown'
    proj_low = proj['Project_Name'].lower()
    for se in status_entries:
        se_low = se['name'].lower()
        if proj_low in se_low or se_low in proj_low:
            status = se['status']
            break
    results.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status
    })

print('__RESULT__:')
output_str = json.dumps(results)
print(output_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.execute_python:52': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)
