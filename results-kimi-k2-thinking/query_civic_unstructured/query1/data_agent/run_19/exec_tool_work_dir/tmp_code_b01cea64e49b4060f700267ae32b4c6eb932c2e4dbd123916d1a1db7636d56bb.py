code = """import json

funding_var = locals()['var_functions.query_db:4']
civic_var = locals()['var_functions.query_db:11']

if isinstance(funding_var, str):
    funding = json.load(open(funding_var))
else:
    funding = funding_var

if isinstance(civic_var, str):
    civic = json.load(open(civic_var))
else:
    civic = civic_var

funded = set()
for rec in funding:
    if int(rec['Amount']) > 50000:
        funded.add(rec['Project_Name'])

design = set()
for doc in civic:
    text = doc.get('text', '')
    in_design = False
    for line in text.split('\n'):
        clean = line.strip()
        if 'Capital Improvement Projects' in clean and 'Design' in clean:
            in_design = True
        elif 'Capital Improvement Projects' in clean and 'Construction' in clean:
            break
        elif in_design and clean in funded:
            design.add(clean)

count = len(design)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
