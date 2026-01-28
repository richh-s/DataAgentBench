code = """import json, re

# load extracted projects list
path_proj = var_call_YwzUunU3MguEsIXEYIsurGSq
with open(path_proj,'r',encoding='utf-8') as f:
    proj_data = json.load(f)
projects = proj_data['projects_design_capital']

# keep only plausible project names: title case-ish, contains letters, limited punctuation, not too long, no sentence-like commas
clean = []
for p in projects:
    if len(p) < 5 or len(p) > 80:
        continue
    if re.search(r'\b(project|Projects)\b', p) and p.lower().startswith('project'):
        continue
    if re.search(r'\b(Updates|Schedule|Description|Commission|Council|Caltrans|County|Staff|Bids|budget|approval|advertise|construction)\b', p, re.IGNORECASE) and not re.search(r'\b(Improvement|Improvements|Repair|Repairs|Replacement|Resurfacing|Drain|Storm|Park|Playground|Skate|Water|Traffic|Signals|Biofilter|Master Plan|Median|Crosswalk|Warning|Study|Retaining Wall)\b', p, re.IGNORECASE):
        continue
    if re.search(r'[\.!?]$', p):
        continue
    if p.count(',')>=1:
        continue
    if not re.search(r'[A-Za-z]', p):
        continue
    # exclude lines starting with common stopwords
    if re.match(r'^(The|This|In|On|At|By|For|From|And|Or|To)\b', p):
        continue
    clean.append(p)

clean_set = set(clean)

# load funding project names > 50k
path_fund = var_call_KU1wQdtuB5OuP1pbP3EtQymq
with open(path_fund,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_names = set(r['Project_Name'] for r in fund)

# direct match
matches = sorted(clean_set.intersection(fund_names))

result = {'count': len(matches), 'matches': matches}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_plwekHHhqasuFuajAwHtbUgg': [{'cnt': '276'}], 'var_call_ZlyIG70BMoMqpaUG34RJQ2KT': 'file_storage/call_ZlyIG70BMoMqpaUG34RJQ2KT.json', 'var_call_YwzUunU3MguEsIXEYIsurGSq': 'file_storage/call_YwzUunU3MguEsIXEYIsurGSq.json', 'var_call_KU1wQdtuB5OuP1pbP3EtQymq': 'file_storage/call_KU1wQdtuB5OuP1pbP3EtQymq.json'}

exec(code, env_args)
