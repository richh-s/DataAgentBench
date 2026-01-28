code = """import json, re

# Load data from stored file paths
f_file = open(str(var_functions.query_db:2))
funding = json.load(f_file)
f_file.close()

c_file = open(str(var_functions.query_db:6))
civic = json.load(c_file)
c_file.close()

# Create funding map for amounts > 50000
fund = {}
for item in funding:
    amt = float(item['Amount'])
    if amt > 50000:
        name = item['Project_Name']
        fund[name] = amt
        # Also add clean name without parenthetical
        clean = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        if clean != name:
            fund[clean] = amt

# Find capital design projects
design_projects = []
for doc in civic:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section between Design and Construction
        start = text.find('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        section = text[start:end] if end > start else text[start:]
        
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 15 and 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                if 'Page' not in line and 'Agenda' not in line:
                    if 'RECOMMENDED' not in line.upper() and 'Updates:' not in line and 'Schedule:' not in line:
                        if not line.startswith('('):
                            design_projects.append(line)

# Count matches with funding > 50000
count = 0
for proj in design_projects:
    clean_proj = re.sub(r'\s*\([^)]*\)\s*$', '', proj).strip()
    if proj in fund or clean_proj in fund:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
