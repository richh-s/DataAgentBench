code = """import json
import re

# Read funding data
f_path = locals()['var_functions.query_db:6']
c_path = locals()['var_functions.query_db:2']

with open(f_path) as f_funding:
    funding_all = json.load(f_funding)

with open(c_path) as f_civic:
    civic_all = json.load(f_civic)

# Step 1: Extract capital design projects from civic documents
design_capital = []

for doc in civic_all:
    text = doc.get('text', '')
    # Find Capital Improvement Projects (Design) section
    section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Not Started|$)', 
                              text, re.DOTALL | re.IGNORECASE)
    if section_match:
        section = section_match.group(1)
        lines = section.split('\n')
        for line in lines:
            name = line.strip()
            if name and len(name) < 120 and 'Project Schedule' not in name and 'Updates:' not in name and len(name) > 10:
                clean_name = re.sub(r'^[A-Z0-9]+[.)]\s*', '', name)
                # Check if it contains relevant keywords
                keywords = ['road','beach','park','storm','drain','project','repair','improvement','bridge','median','crosswalk','facility']
                if any(word in clean_name.lower() for word in keywords):
                    if not (clean_name.isupper() and len(clean_name.split()) <= 3):
                        design_capital.append(clean_name)

# Remove duplicates
design_capital_unique = []
seen = set()
for proj in design_capital:
    if proj not in seen:
        design_capital_unique.append(proj)
        seen.add(proj)

# Step 2: Get funding projects > 50000
high_funding = []
for rec in funding_all:
    amt = int(rec['Amount'])
    if amt > 50000:
        high_funding.append({'name': rec['Project_Name'], 'amount': amt})

# Step 3: Find matches (flexible matching)
matches = []
matched_names = set()

design_normalized = [' '.join(p.lower().split()) for p in design_capital_unique]

for fund in high_funding:
    fund_name_normalized = ' '.join(fund['name'].lower().split())
    # Direct match
    if fund_name_normalized in design_normalized:
        if fund_name_normalized not in matched_names:
            matched_names.add(fund_name_normalized)
            matches.append(fund['name'])
    else:
        # Partial matching
        for design_name in design_normalized:
            if (design_name in fund_name_normalized or fund_name_normalized in design_name) and fund_name_normalized not in matched_names:
                matched_names.add(fund_name_normalized)
                matches.append(fund['name'])

print('__RESULT__:')
print(json.dumps({
    'design_capital_projects': design_capital_unique,
    'high_funding_projects': high_funding,
    'matches': matches,
    'count': len(matches)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}, 'var_functions.execute_python:30': {'funding_path': 'file_storage/functions.query_db:6.json', 'civic_path': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
