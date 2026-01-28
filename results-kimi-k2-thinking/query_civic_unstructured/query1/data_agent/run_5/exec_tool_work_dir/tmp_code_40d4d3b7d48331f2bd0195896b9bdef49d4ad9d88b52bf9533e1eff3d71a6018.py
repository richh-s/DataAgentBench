code = """import json
import sys

# Load data
with open(locals()['var_functions.query_db:72']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    docs = json.load(f)

# Get funding names
funding_names = set()
for r in funding:
    funding_names.add(r['Project_Name'])

# Look for design projects
design_names = []
for doc in docs:
    text = doc.get('text', '')
    if 'Design' in text:
        # Try to find capital improvement design section
        if 'Capital Improvement Projects (Design)' in text:
            idx = text.find('Capital Improvement Projects (Design)')
            section = text[idx:idx+2000]
            lines = [l.strip() for l in section.split('\n') if l.strip()]
            for line in lines:
                if len(line) > 10 and '(' not in line and not line.startswith('•'):
                    design_names.append(line)

# Normalize and match matches = 0 for dname in design_names[:100]:
    dclean = dname.lower()[:30]
    for fname in list(funding_names):
        fclean = fname.lower()[:30]
        if dclean in fclean or fclean in dclean:
            matches +=1
            funding_names.discard(fname)
            break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
