code = """import json

# Load data from file paths
funding_path = "var_functions.query_db_190"
mongo_path = "var_functions.query_db_182"

with open(funding_path) as f:
    funding_data = json.load(f)

with open(mongo_path) as f:
    mongo_data = json.load(f)

# Extract unique funding project names
funding_names = set()
for record in funding_data:
    funding_names.add(record['Project_Name'])

# Look for design status in project text
matches = set()

for doc in mongo_data:
    text = doc.get('text', '')
    
    # Check if document contains design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        # Look for end markers
        end_construction = text.find('Capital Improvement Projects (Construction)', design_start)
        end_not_started = text.find('Capital Improvement Projects (Not Started)', design_start)
        
        if end_construction > 0:
            design_section = text[design_start:end_construction]
        elif end_not_started > 0:
            design_section = text[design_start:end_not_started]
        else:
            design_section = text[design_start:]
        
        # Extract lines from design section
        for line in design_section.splitlines():
            clean_line = line.strip()
            if len(clean_line) > 5 and not clean_line.startswith('(') and not clean_line.startswith('•'):
                if 'Updates:' not in clean_line and 'Schedule:' not in clean_line:
                    # Check if any funding project matches
                    for fund_name in funding_names:
                        if fund_name.lower() in clean_line.lower() or clean_line.lower() in fund_name.lower():
                            matches.add(fund_name)

result = len(matches)
print('RESULT:', result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json', 'var_functions.execute_python:132': {'debug': 'complete'}, 'var_functions.query_db:134': [{'Project_Name': 'Birdview Avenue Improvements'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)'}, {'Project_Name': 'Broad Beach Road Water Quality Repair'}, {'Project_Name': 'City Hall Roof Replacement'}, {'Project_Name': 'City Traffic Signals Backup Power'}, {'Project_Name': 'Civic Center Stormwater Diversion Structure'}, {'Project_Name': 'Clover Heights Storm Drain'}, {'Project_Name': 'Corral Canyon Culvert Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)'}, {'Project_Name': 'Discussion'}, {'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project'}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs'}], 'var_functions.query_db:136': 'file_storage/functions.query_db:136.json', 'var_functions.query_db:138': 'file_storage/functions.query_db:138.json', 'var_functions.query_db:158': 'file_storage/functions.query_db:158.json', 'var_functions.query_db:162': 'file_storage/functions.query_db:162.json', 'var_functions.query_db:182': 'file_storage/functions.query_db:182.json', 'var_functions.execute_python:186': 0, 'var_functions.query_db:188': 'file_storage/functions.query_db:188.json', 'var_functions.query_db:190': 'file_storage/functions.query_db:190.json'}

exec(code, env_args)
