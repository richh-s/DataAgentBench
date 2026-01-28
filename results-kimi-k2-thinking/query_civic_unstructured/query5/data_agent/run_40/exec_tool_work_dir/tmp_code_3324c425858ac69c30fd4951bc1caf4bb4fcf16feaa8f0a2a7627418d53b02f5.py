code = """import json

# Load the data files
civic_path = locals()['var_functions.query_db:66']
funding_path = locals()['var_functions.query_db:67']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup map
funding_map = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if name:
        funding_map[name] = int(rec.get('Amount', '0'))

# Initialize results
result_funding = 0
result_count = 0

# Search for disaster projects that started in 2022
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check disaster project markers
        if line.find('(FEMA Project)') != -1 or line.find('(CalJPIA Project)') != -1 or line.find('(CalOES Project)') != -1 or line.find('FEMA/CalOES Project') != -1:
            # Look for 2022 start date
            has_2022 = False
            for j in range(i, min(i+6, len(lines))):
                if lines[j].find('2022') != -1:
                    lower_line = lines[j].lower()
                    if lower_line.find('st:') != -1 or lower_line.find('start:') != -1:
                        has_2022 = True
                        break
            
            if has_2022:
                amount = funding_map.get(line, 0)
                if amount > 0:
                    result_funding += amount
                    result_count += 1

output = {'total_funding': result_funding, 'project_count': result_count}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
