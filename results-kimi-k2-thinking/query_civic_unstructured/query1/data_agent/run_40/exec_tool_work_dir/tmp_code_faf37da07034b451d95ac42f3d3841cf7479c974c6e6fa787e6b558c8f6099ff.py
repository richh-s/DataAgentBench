code = """import json

# Load funding data from file
funding_file = open('storage/query_result_6.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Get project names with funding > $50,000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record['Project_Name'].lower().strip())

# Load civic documents
civic_file = open('storage/query_result_10.json', 'r')
civic_data = json.load(civic_file)
civic_file.close()

# Count design capital projects
count = 0

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find design section
    design_marker = 'Capital Improvement Projects (Design)'
    construction_marker = 'Capital Improvement Projects (Construction)'
    
    start_pos = text.find(design_marker)
    if start_pos == -1:
        continue
    
    end_pos = text.find(construction_marker, start_pos)
    if end_pos == -1:
        end_pos = start_pos + 6000
    
    section = text[start_pos:end_pos]
    lines = section.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and not line.isupper():
            if 'Updates' not in line and 'Schedule' not in line and 'Page' not in line:
                low = line.lower()
                for funded in high_funding:
                    if funded in low or low in funded:
                        count = count + 1
                        break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
