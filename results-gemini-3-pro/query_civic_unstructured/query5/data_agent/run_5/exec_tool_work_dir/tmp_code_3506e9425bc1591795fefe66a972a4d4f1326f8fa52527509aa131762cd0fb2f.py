code = """import json
import pandas as pd
import re

funding_key = 'var_function-call-5948002065454245776'
civic_key = 'var_function-call-16801435053076295994'

file_path_funding = locals()[funding_key]
file_path_civic = locals()[civic_key]

df_funding = pd.read_json(file_path_funding)

with open(file_path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + chr(10)

disaster_suffixes = [
    '(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)', 
    '(FEMA/CalOES Project)', '(FEMA)', '(CalOES)'
]

def is_disaster_funding(name):
    for suffix in disaster_suffixes:
        if suffix.lower() in name.lower():
            return True
    return False

def get_base_name(name):
    base = name
    for suffix in disaster_suffixes:
        base = base.replace(suffix, '').strip()
    return base

project_info = {} 
unique_base_names = set([get_base_name(n) for n in df_funding['Project_Name'].unique()])

for base_name in unique_base_names:
    try:
        pattern = re.escape(base_name)
        matches = [m.start() for m in re.finditer(pattern, full_text, re.IGNORECASE)]
        
        for match_idx in matches:
            context = full_text[match_idx:match_idx+2000]
            # Search for Begin Construction
            date_match = re.search(r'Begin Construction:\s*([^\n]*)', context, re.IGNORECASE)
            if date_match:
                date_str = date_match.group(1).strip()
                project_info[base_name] = date_str
                break 
    except Exception:
        continue

total_funding = 0
debug_list = []

for index, row in df_funding.iterrows():
    name = row['Project_Name']
    amount = row['Amount']
    
    if is_disaster_funding(name):
        base_name = get_base_name(name)
        start_date = project_info.get(base_name)
        
        if start_date and "2022" in start_date:
            total_funding += amount
            debug_list.append({"name": name, "base": base_name, "date": start_date, "amount": amount})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": debug_list}))"""

env_args = {'var_function-call-8962819121667412249': ['Funding'], 'var_function-call-8962819121667415660': ['civic_docs'], 'var_function-call-5948002065454245776': 'file_storage/function-call-5948002065454245776.json', 'var_function-call-8815674849536334134': 'file_storage/function-call-8815674849536334134.json', 'var_function-call-16801435053076295994': 'file_storage/function-call-16801435053076295994.json'}

exec(code, env_args)
