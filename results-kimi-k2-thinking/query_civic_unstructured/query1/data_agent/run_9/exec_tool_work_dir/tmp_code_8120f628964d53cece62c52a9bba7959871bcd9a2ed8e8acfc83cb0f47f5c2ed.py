code = """import json
funding_file = str(locals()['var_functions.query_db:2'])
civic_file = str(locals()['var_functions.query_db:8'])

with open(funding_file, 'r') as f:
    funding_data = json.load(f)
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

high_funding = [f for f in funding_data if int(f['Amount']) > 50000]
funding_lookup = {f['Project_Name'].lower(): int(f['Amount']) for f in high_funding}

capital_design = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        # Truncate at next major heading
        if 'Capital Improvement Projects (Construction)' in section:
            section = section.split('Capital Improvement Projects (Construction)')[0]
        for line in section.split('\n'):
            line = line.strip()
            if len(line) > 10 and line[0].isupper():
                skip_words = ['updates', 'schedule', 'advertise', 'construction', 'page', 'agenda item']
                if not any(word in line.lower() for word in skip_words):
                    capital_design.append(line)

matches = []
seen = set()
for proj in capital_design:
    key = proj.lower()
    if key in funding_lookup and proj not in seen:
        matches.append(proj)
        seen.add(proj)

print('__RESULT__:')
print(json.dumps(len(matches)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
