code = """import json
civic_path=locals()['var_functions.query_db:70']
funding_path=locals()['var_functions.query_db:71']
with open(civic_path) as f:
    civic=json.load(f)
with open(funding_path) as f:
    funding=json.load(f)

spring=set()
months=['March','April','May','Spring']
for doc in civic:
    txt=doc.get('text','')
    lines=txt.split('\n')
    for i,line in enumerate(lines):
        if '2022' in line and any(m in line for m in months):
            for j in range(max(0,i-5),i):
                prev=lines[j].strip()
                if prev and len(prev)>8 and prev[0].isupper() and ':' not in prev:
                    spring.add(prev)
                    break

mapping={}
for f in funding:
    mapping[f['Project_Name'].lower()]=int(f['Amount'])

total=0
for proj in spring:
    p=proj.lower()
    for name,amount in mapping.items():
        if p in name or name in p:
            total+=amount
            break

result={'count':len(spring),'funding':total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:48': [{'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Broad Beach Road Water Quality Repair', 'Amount': '93000'}, {'Project_Name': 'City Hall Roof Replacement', 'Amount': '79000'}, {'Project_Name': 'City Hall Solar Project', 'Amount': '38000'}, {'Project_Name': 'City Traffic Signals Backup Power', 'Amount': '85000'}, {'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Amount': '10000'}, {'Project_Name': 'Citywide Guardrail Replacement', 'Amount': '30000'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Amount': '64000'}, {'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Amount': '45000'}, {'Project_Name': 'Civic Center Way Improvements', 'Amount': '37000'}], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json'}

exec(code, env_args)
