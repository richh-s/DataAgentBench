code = """import json, re

# Load funding data
with open('/tmp/tmp_results/query_db_114.json', 'r') as f:
    funding = json.load(f)

# Load civic docs
with open('/tmp/tmp_results/query_db_30.json', 'r') as f:
    civic = json.load(f)

# Build funding set with cleaned names
fund_set = set()
for item in funding:
    name = item['Project_Name']
    fund_set.add(name)
    fund_set.add(re.sub(r'\s*\([^)]*\)\s*$', '', name).strip())

# Extract capital design projects and check matches
count = 0
for doc in civic:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Get section between Design and Construction
        start = text.index('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        section = text[start:end] if end > start else text[start:]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and not line.startswith('(') and 'Page' not in line:
                if 'FEMA' not in line and 'CalOES' not in line and 'fire' not in line:
                    if 'RECOMMENDED' not in line.upper() and 'Updates:' not in line:
                        clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
                        if line in fund_set or clean_line in fund_set:
                            count += 1

result = count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:112': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}], 'var_functions.query_db:114': 'file_storage/functions.query_db:114.json'}

exec(code, env_args)
