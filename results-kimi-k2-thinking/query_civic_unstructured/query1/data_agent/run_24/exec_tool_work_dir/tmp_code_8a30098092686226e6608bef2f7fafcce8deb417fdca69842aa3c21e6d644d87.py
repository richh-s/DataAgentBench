code = """import json

funding = json.load(open(vars['var_functions.query_db:86'], 'r'))
civic = json.load(open(vars['var_functions.query_db:64'], 'r'))

# Count matches
matched = 0
funding_names = set(r['Project_Name'] for r in funding)

for doc in civic:
    text = doc.get('text', '')
    # Find design section and extract project names
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)', 1)[1]
        # Split by next major heading
        section = section.split('\n\nCapital Improvement Projects', 1)[0]
        for line in section.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and len(line) > 5:
                    # Check if this project has funding > 50k
                    for fund_name in funding_names:
                        if fund_name == line or fund_name.startswith(line + ' '):
                            matched += 1
                            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:80': ['civic_docs'], 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json'}

exec(code, env_args)
