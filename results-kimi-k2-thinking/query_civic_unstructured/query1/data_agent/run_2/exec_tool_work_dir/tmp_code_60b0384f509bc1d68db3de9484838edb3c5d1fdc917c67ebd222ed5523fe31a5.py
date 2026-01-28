code = """import json
import os

# Get the file paths from storage
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:2']

# Load funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_dict = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        funding_dict[record['Project_Name'].lower()] = amount

# Extract capital design projects - manual list from text
# These are projects mentioned in Capital Improvement Projects (Design) section
design_projects = {
    'clover heights storm drain',
    'latigo canyon road retaining wall repair project',
    'pch median improvements project',
    'trancas canyon park upper and lower slopes repair',
    'outdoor warning signs',
    'malibu bluffs park south walkway repairs',
    'trancas canyon park playground',
    'malibu canyon road traffic study',
    '2022 morning view resurfacing & storm drain improvements',
    'westward beach road drainage improvements project',
    'civic center water treatment facility phase 2',
    'permanent skate park',
    'pch at trancas canyon road right turn lane',
    'westward beach road repair project',
    'storm drain master plan',
    'trancas canyon park upper and lower slopes repair duplicate',
    '2017 sycamore drive slope repair',
    'paseo canyon park project',
    'zuma beach water treatment facility improvements (phase ii)',
    'winter canyon road emergency slope repairs'
}

# Also extract from the actual text
found_design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Find design section
    design_start = lower_text.find('capital improvement projects (design)')
    if design_start == -1:
        continue
    
    # Find section end
    end = len(text)
    for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']:
        pos = lower_text.find(marker, design_start + 10)
        if pos > design_start and pos < end:
            end = pos
    
    section = text[design_start:end]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) > 15:
            # Skip update/schedule lines
            if ('updates:' not in line.lower() and 
                'project schedule' not in line.lower() and
                'complete design' not in line.lower() and
                'advertise:' not in line.lower() and
                'begin construction' not in line.lower() and
                not line.startswith('(') and not line.startswith('cid:')):
                
                # Remove project markers
                project_name = line.strip('•- ').strip()
                if project_name and ' ' in project_name:
                    found_design_projects.add(project_name.lower())

# Count matching projects
count = 0
matched_projects = []

for proj in found_design_projects.union(design_projects):
    for fund_proj in funding_dict:
        proj_words = proj.split()
        fund_words = fund_proj.split()
        
        # Check if projects match (overlap of key words)
        key_match = False
        if len(proj_words) >= 2 and len(fund_words) >= 2:
            # Common words like 'project', 'road', etc.
            proj_key = [w for w in proj_words if w not in ['project', 'road', 'and', 'drain', 'improvements', 'repair', 'repairs', 'street', 'canyon', 'park', 'capital', 'improvement']]
            fund_key = [w for w in fund_words if w not in ['project', 'road', 'and', 'drain', 'improvements', 'repair', 'repairs', 'street', 'canyon', 'park', 'capital', 'improvement']]
            
            # Check if at least 2 key words match
            matches = len(set(proj_key) & set(fund_key))
            if matches >= 2:
                key_match = True
        
        if proj == fund_proj or proj in fund_proj or fund_proj in proj or key_match:
            count += 1
            matched_projects.append(proj)
            break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
