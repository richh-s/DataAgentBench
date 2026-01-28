code = """import json

# Load funding data
f_file = open(var_functions.query_db:5)
funding_records = json.load(f_file)
f_file.close()

# Load civic docs  
c_file = open(var_functions.query_db:6)
civic_docs = json.load(c_file)
c_file.close()

# Map funding amounts
funding_map = {}
for item in funding_records:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Find design capital projects
projects = set()
for doc in civic_docs:
    text = doc.get('text')
    if text and 'Capital Improvement Projects' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10 and not any(x in line for x in ['Page', 'Schedule', 'Updates']):
                # Check if design status mentioned
                ctx_start = text.find(line)
                ctx = text[ctx_start:ctx_start+300]
                if 'Design' in ctx:
                    projects.add(line)

# Count matches with funding > 50000
count = 0
for proj in projects:
    for fund_name, amt in funding_map.items():
        if amt > 50000:
            # Simple name matching
            if proj.lower() in fund_name.lower() or fund_name.lower() in proj.lower():
                if abs(len(proj)-len(fund_name)) < 35:
                    count += 1
                    break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
