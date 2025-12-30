code = """import json

file_path = locals()['var_function-call-1860394560099388718']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = {}

headers = []
for i, p in enumerate(papers[:5]):
    headers.append(p['text'][:300])
debug_info['headers'] = headers

count_pa = sum(1 for p in papers if 'physical activity' in p['text'].lower())
count_2016 = sum(1 for p in papers if '2016' in p['text'][:2000])
count_16 = sum(1 for p in papers if "'16" in p['text'][:2000])

debug_info['count_pa'] = count_pa
debug_info['count_2016'] = count_2016
debug_info['count_16'] = count_16

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10819517614772727470': 'file_storage/function-call-10819517614772727470.json', 'var_function-call-1860394560099388718': 'file_storage/function-call-1860394560099388718.json', 'var_function-call-475874978628204145': [], 'var_function-call-4305763543364550069': 'Debug info printed'}

exec(code, env_args)
