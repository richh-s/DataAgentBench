code = """import json

key_name = 'var_function-call-1660175416261696799'
file_path = locals()[key_name]

with open(file_path, 'r') as f:
    papers = json.load(f)

count_2016 = 0
count_pa = 0
examples_2016 = []
examples_pa = []

for p in papers:
    text = p.get('text', '')
    if '2016' in text[:1000]:
        count_2016 += 1
        if len(examples_2016) < 3:
            examples_2016.append(text[:200])
            
    if 'physical activity' in text.lower():
        count_pa += 1
        if len(examples_pa) < 3:
            examples_pa.append(text[:200])

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'count_2016_in_header': count_2016,
    'count_pa_in_text': count_pa,
    'examples_2016': examples_2016,
    'examples_pa': examples_pa
}))"""

env_args = {'var_function-call-8186241074131223286': ['paper_docs'], 'var_function-call-8186241074131224069': ['Citations', 'sqlite_sequence'], 'var_function-call-11444584410328735250': 'file_storage/function-call-11444584410328735250.json', 'var_function-call-1660175416261696799': 'file_storage/function-call-1660175416261696799.json', 'var_function-call-11009971784847056933': []}

exec(code, env_args)
