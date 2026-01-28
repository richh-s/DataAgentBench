code = """import json

with open(locals()['var_functions.query_db:44']) as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

funding_projects = {}
for rec in funding_data:
    funding_projects[rec['Project_Name']] = int(rec['Amount'])

print('Funding projects > 50000:', len(funding_projects))

# Extract design status projects
design_names = []
for doc in civic_docs:
    txt = doc.get('text', '')
    
    # Find design section using index
    design_start = txt.find('Capital Improvement Projects (Design)')
    if design_start < 0:
        continue
    
    design_end = txt.find('Capital Improvement Projects (Construction)', design_start)
    if design_end < 0:
        design_end = len(txt)
    
    section = txt[design_start:design_end]
    
    # Split into project blocks
    blocks = section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block and 'Design)' not in block and len(block) > 20:
            lines = [line.strip() for line in block.split('\n') if line.strip()]
            if lines:
                first_line = lines[0]
                if first_line and 'Updates' not in first_line and 'Schedule' not in first_line and not first_line.isupper():
                    design_names.append(first_line)

print('Design projects found:', len(design_names))

# Match projects
def normalize(n):
    n2 = n.split('(')[0].strip().lower()
    n2 = n2.replace('project', '').replace('improvements', '').strip()
    return n2

matched = 0
matched_list = []
funding_left = dict(funding_projects)

for dname in design_names:
    dclean = normalize(dname)
    
    for fund_name in list(funding_left.keys()):
        fclean = normalize(fund_name)
        
        if dclean in fclean or fclean in dclean:
            matched += 1
            matched_list.append({'project': fund_name, 'amount': funding_left[fund_name]})
            del funding_left[fund_name]
            break

print('Matched count:', matched)

result = json.dumps({'count': matched})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
