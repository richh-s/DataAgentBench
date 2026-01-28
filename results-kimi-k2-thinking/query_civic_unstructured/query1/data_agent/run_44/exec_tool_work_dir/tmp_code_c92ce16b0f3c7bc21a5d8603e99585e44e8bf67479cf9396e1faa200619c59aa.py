code = """import json

funding_file = locals()['var_functions.query_db:6']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file) as f:
    all_funding = json.load(f)

with open(civic_file) as f:
    all_civic = json.load(f)

# Find projects in design status from civic docs
design_projects = []
for doc in all_civic:
    text = doc.get('text','')
    # Find section for Capital Improvement Projects (Design)
    design_section = ''
    if 'Capital Improvement Projects (Design)' in text:
        start = text.index('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start + 50)
        if end == -1: end = start + 4000
        design_section = text[start:end]
        
    # Extract project names from this section
    lines = design_section.split('\n')
    for line in lines:
        line = line.strip()
        if line and 10 < len(line) < 150:
            if 'Project Schedule' not in line and 'Updates:' not in line:
                # Check for project keywords
                kws = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk']
                if any(k in line.lower() for k in kws):
                    clean_line = line.replace('•','').replace('■','').replace('●','').strip()
                    if clean_line not in design_projects:
                        design_projects.append(clean_line)

# Get funding records > $50k
funding_over_50k = []
for rec in all_funding:
    amt = int(rec['Amount'])
    if amt > 50000:
        funding_over_50k.append(rec['Project_Name'])

# Match projects
def norm_name(name):
    return ' '.join(name.lower().split())

normalized_design = [norm_name(p) for p in design_projects]
matched_projects = []

for fund_name in funding_over_50k:
    n_fund = norm_name(fund_name)
    for n_design in normalized_design:
        if n_fund in n_design or n_design in n_fund:
            if fund_name not in matched_projects:
                matched_projects.append(fund_name)
                break

result_count = len(matched_projects)
print('__RESULT__:')
print(json.dumps({'count': result_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
