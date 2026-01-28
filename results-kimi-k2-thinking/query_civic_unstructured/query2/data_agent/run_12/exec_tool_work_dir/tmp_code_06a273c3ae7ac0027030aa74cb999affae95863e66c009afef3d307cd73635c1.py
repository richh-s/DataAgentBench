code = """import json, re

# Load the data from storage
civic_data = var_functions.query_db_65
civic_docs = json.loads(open(civic_data).read())

funding_data_file = var_functions.query_db_66
funding_records = json.loads(open(funding_data_file).read())

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_records)) + ' funding records')

# Find park projects with 2022 in document
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    low_text = text.lower()
    # Check whole document for 2022 completion of park projects
    if 'park' in low_text and '2022' in text and 'completed' in low_text:
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if line_clean and 'park' in line_clean.lower() and len(line_clean) < 150:
                if line_clean not in park_projects:
                    park_projects.append(line_clean)

print('Found ' + str(len(park_projects)) + ' park projects in 2022')

# Clean names
def clean_name(n):
    if not n:
        return ''
    n = re.sub(r'(?i)\s+Project\s*$', '', n)
    n = re.sub(r'(?i)\s*-\s*Design\s*$', '', n)
    n = re.sub(r'(?i)\s*-\s*Construction\s*$', '', n)
    return n.strip().lower()

# Calculate total funding
total_funding = 0
for fund in funding_records:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    if not name or amount == 0:
        continue
    clean_fund = clean_name(name)
    for park in park_projects:
        clean_park = clean_name(park)
        if clean_park and (clean_park in clean_fund or clean_fund in clean_park):
            total_funding = total_funding + amount
            break

result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:65': 'file_storage/functions.query_db:65.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
