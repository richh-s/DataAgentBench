code = """import json

# Load the data files
civic_docs = json.loads(open('var_functions.query_db:20').read())
funding_records = json.loads(open('var_functions.query_db:30').read())

print('Documents:', len(civic_docs), 'Funding:', len(funding_records))

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) > 10 and ('park' in line.lower() or 'playground' in line.lower()):
            # Look for completion in next few lines
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip().lower()
                if 'completed' in next_line and '2022' in next_line:
                    park_projects.append(line)
                    print('Found:', line)
                    break

# Match with funding
total = 0
for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    for proj in park_projects:
        if proj.lower() in fund_name or fund_name in proj.lower():
            total += int(fund.get('Amount', 0))
            print('Match:', proj, '->', fund.get('Project_Name')
            break

print('Total funding:', total)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
