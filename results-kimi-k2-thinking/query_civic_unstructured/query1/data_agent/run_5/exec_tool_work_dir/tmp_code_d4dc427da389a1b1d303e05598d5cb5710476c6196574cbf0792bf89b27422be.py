code = """import json

# Load funding data
with open(locals()['var_functions.query_db:44']) as f:
    funding = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

# Create funding lookup
funding_names = {}
for rec in funding:
    funding_names[rec['Project_Name']] = int(rec['Amount'])

print('Funding projects count:', len(funding_names))

# Extract design projects
design_list = []
for doc in docs:
    txt = doc.get('text', '')
    start_marker = 'Capital Improvement Projects (Design)'
    end_marker = 'Capital improvement Projects (Construction)'
    
    start = txt.find(start_marker)
    if start > 0:
        end = txt.find(end_marker, start)
        if end < 0:
            end = len(txt)
        section = txt[start:end]
        
        parts = section.split('\n\n')
        for part in parts:
            part = part.strip()
            if len(part) > 20 and 'Design)' not in part:
                lines = [L.strip() for L in part.split('\n') if L.strip()]
                if lines:
                    name = lines[0]
                    if name and 'Updates' not in name and 'Schedule' not in name and not name.isupper():
                        design_list.append(name)

print('Design projects count:', len(design_list))

# Match
def clean(n):
    n2 = n.split('(')[0].strip().lower()
    n2 = n2.replace('project', '').strip()
    return n2

matched = 0
for dname in design_list:
    dclean = clean(dname)
    for fund_name in list(funding_names.keys()):
        fclean = clean(fund_name)
        if dclean in fclean or fclean in dclean:
            matched += 1
            del funding_names[fund_name]
            break

result = {'count': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
