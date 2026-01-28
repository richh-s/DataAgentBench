code = """import pandas as pd
import json
import re

funding_rows = pd.read_json(locals()['var_function-call-3462127422727608690'])
funding_rows['Amount'] = pd.to_numeric(funding_rows['Amount'])

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

matched_projects = []
total_amt = 0.0

for p in projects_with_text:
    if patt.search(p['text']):
        name = p['name']
        name_lower = name.lower()
        text_lower = p['text'].lower()
        
        is_park = False
        if "park" in name_lower:
            is_park = True
            if "malibu park" in name_lower and "malibu bluffs" not in name_lower:
                 if any(k in name_lower for k in ['drainage', 'resurfacing', 'storm', 'culvert']):
                     is_park = False
        
        if "playground" in name_lower or "skate" in name_lower:
            is_park = True
            
        if not is_park:
            # Check text for strong keywords
            # Using simple "park" might overlap with "parking". Use boundary or " park "
            # "playground" is safe.
            if "playground" in text_lower:
                if not any(k in name_lower for k in ['drainage', 'resurfacing', 'storm', 'culvert']):
                     is_park = True
            # For "park", check surrounding
            if re.search(r"\bpark\b", text_lower):
                 if not any(k in name_lower for k in ['drainage', 'resurfacing', 'storm', 'culvert']):
                     # "Malibu Park" is a location, so check if name is NOT "Malibu Park..."
                     if "malibu park" not in name_lower:
                         is_park = True
        
        if is_park:
             amount = funding_rows[funding_rows['Project_Name'] == name]['Amount'].values[0]
             matched_projects.append({"name": name, "amount": amount})
             total_amt += amount

print("__RESULT__:")
print(json.dumps({"projects": matched_projects, "total": total_amt}))"""

env_args = {'var_function-call-3462127422727608690': 'file_storage/function-call-3462127422727608690.json', 'var_function-call-3462127422727608521': 'file_storage/function-call-3462127422727608521.json', 'var_function-call-14876303256783267391': 21000.0}

exec(code, env_args)
