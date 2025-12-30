code = """import json

file_path = locals()['var_function-call-1860394560099388718']
with open(file_path, 'r') as f:
    papers = json.load(f)

print("First 5 headers:")
for i, p in enumerate(papers[:5]):
    print(f"--- Paper {i} ---")
    print(p['text'][:300])
    print("----------------")

count_pa = sum(1 for p in papers if 'physical activity' in p['text'].lower())
count_2016 = sum(1 for p in papers if '2016' in p['text'][:2000])
count_16 = sum(1 for p in papers if "'16" in p['text'][:2000])

print(f"Papers with 'physical activity': {count_pa}")
print(f"Papers with '2016' in header: {count_2016}")
print(f"Papers with ''16' in header: {count_16}")

print("__RESULT__:")
print(json.dumps("Debug info printed"))"""

env_args = {'var_function-call-10819517614772727470': 'file_storage/function-call-10819517614772727470.json', 'var_function-call-1860394560099388718': 'file_storage/function-call-1860394560099388718.json', 'var_function-call-475874978628204145': []}

exec(code, env_args)
