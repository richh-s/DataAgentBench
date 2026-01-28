code = """import json, re

funding_file = locals()['var_functions.query_db:0']
with open(funding_file) as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file) as f:
    civic_docs = json.load(f)

funding_map = {}
for r in funding_data:
    if int(r['Amount']) > 50000:
        funding_map[r['Project_Name']] = int(r['Amount'])

count = 0
seen = set()

for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        parts = re.split(r'Capital Improvement Projects \(Design\)', text)
        if len(parts) > 1:
            design_section = parts[1].split('Capital Improvement Projects')[0]
            for line in design_section.split('\n'):
                line = line.strip()
                if line and line[0].isupper() and len(line) > 10:
                    if any(kw in line for kw in ['Project', 'Improvements', 'Repair']):
                        if line in funding_map:
                            if line not in seen:
                                count += 1
                                seen.add(line)
                        else:
                            for funded in funding_map:
                                if line.startswith(funded) or funded.startswith(line.split('(')[0].strip()):
                                    if funded not in seen:
                                        count += 1
                                        seen.add(funded)
                                    break

result = count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
