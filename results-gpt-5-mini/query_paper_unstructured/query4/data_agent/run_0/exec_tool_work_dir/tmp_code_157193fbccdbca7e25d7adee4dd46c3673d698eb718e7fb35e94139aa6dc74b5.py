code = """import json, re
path = var_call_LXL8ZA4trbYjT9RIvZMnHL63
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    if re.search(r'physical activity', text, re.I) and re.search(r'\b2016\b', text):
        titles.append(title)

# deduplicate
titles = list(dict.fromkeys(titles))
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_call_dZzFsi4SOtro7Uw908RvLc2W': ['paper_docs'], 'var_call_LXL8ZA4trbYjT9RIvZMnHL63': 'file_storage/call_LXL8ZA4trbYjT9RIvZMnHL63.json', 'var_call_RN46vEKa6noQo1hbV1WtR7CC': [], 'var_call_os7AOcjj2rufSpBsKHwOLaNF': 'file_storage/call_os7AOcjj2rufSpBsKHwOLaNF.json', 'var_call_9GUtUiD2tMzvSetv4WScVci1': []}

exec(code, env_args)
