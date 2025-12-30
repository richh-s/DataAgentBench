code = """import pandas as pd
import json
import re

funding_rows = pd.read_json(locals()['var_function-call-3462127422727608690'])
with open(locals()['var_function-call-3462127422727608521'], 'r') as f:
    civic_docs = json.load(f)

full_text = " ".join([d['text'] for d in civic_docs])

project_names = funding_rows['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

found_blocks = []
for name in project_names:
    matches = [m.start() for m in re.finditer(re.escape(name), full_text)]
    for m in matches:
        snippet = full_text[m+len(name):m+len(name)+200]
        if "Updates:" in snippet:
            found_blocks.append({'name': name, 'start': m, 'length': len(name)})
found_blocks.sort(key=lambda x: x['start'])

unique_blocks = []
if found_blocks:
    current = found_blocks[0]
    for i in range(1, len(found_blocks)):
        next_block = found_blocks[i]
        if next_block['start'] < current['start'] + current['length']:
            if next_block['length'] > current['length']:
                current = next_block
        else:
            unique_blocks.append(current)
            current = next_block
    unique_blocks.append(current)

projects_with_text = []
for i in range(len(unique_blocks)):
    start = unique_blocks[i]['start']
    name = unique_blocks[i]['name']
    if i < len(unique_blocks) - 1:
        end = unique_blocks[i+1]['start']
    else:
        end = len(full_text)
    projects_with_text.append({'name': name, 'text': full_text[start:end]})

patt = re.compile(r"(construction\s+was\s+completed|complete\s+construction).*?2022", re.IGNORECASE | re.DOTALL)

print("Candidates completed in 2022 with 'park' keyword:")
for p in projects_with_text:
    if patt.search(p['text']):
        name = p['name']
        text = p['text'].lower()
        if "park" in name.lower() or "park" in text or "playground" in text:
             print(f"NAME: {name}")
             print(f"TEXT SNIPPET: {p['text'][:200]}")
             print("-" * 20)

print("__RESULT__:")
print("DONE")"""

env_args = {'var_function-call-3462127422727608690': 'file_storage/function-call-3462127422727608690.json', 'var_function-call-3462127422727608521': 'file_storage/function-call-3462127422727608521.json', 'var_function-call-14876303256783267391': 21000.0}

exec(code, env_args)
