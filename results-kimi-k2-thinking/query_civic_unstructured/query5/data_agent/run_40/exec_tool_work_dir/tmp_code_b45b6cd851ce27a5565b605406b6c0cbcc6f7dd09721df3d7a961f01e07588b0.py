code = """import json

# Load the data
civic_file = open(locals()['var_functions.query_db:66'], 'r')
civic_docs = json.load(civic_file)
civic_file.close()

funding_file = open(locals()['var_functions.query_db:67'], 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Build funding lookup
funding_lookup = {}
for rec in funding_data:
    name = rec.get('Project_Name', '')
    amount = rec.get('Amount', '0')
    if name:
        funding_lookup[name] = int(amount)

# Find disaster projects that started in 2022
total_funding = 0
project_count = 0

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this is a disaster project
        is_disaster = False
        if line.find('(FEMA Project)') >= 0:
            is_disaster = True
        elif line.find('(CalJPIA Project)') >= 0:
            is_disaster = True
        elif line.find('(CalOES Project)') >= 0:
            is_disaster = True
        elif line.find('FEMA/CalOES Project') >= 0:
            is_disaster = True
        
        if is_disaster:
            # Look for 2022 start date in nearby lines
            found_2022 = False
            start_pos = max(0, i-2)
            end_pos = min(len(lines), i+6)
            
            for j in range(start_pos, end_pos):
                context_line = lines[j]
                if context_line.find('2022') >= 0:
                    lower_line = context_line.lower()
                    if lower_line.find('st:') >= 0 or lower_line.find('start:') >= 0:
                        found_2022 = True
                        break
            
            if found_2022:
                amount = funding_lookup.get(line, 0)
                if amount > 0:
                    total_funding += amount
                    project_count += 1

result = {'total_funding': total_funding, 'project_count': project_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json', 'var_functions.execute_python:92': {'status': 'checked'}}

exec(code, env_args)
