code = """import json
civic_docs = json.load(open(var_call_3V3LBuTrnTf5FD8CAnAfAlHL, 'r', encoding='utf-8'))
funding = json.load(open(var_call_NT3Q3dsTFn3mJHGGbLBIEHZH, 'r', encoding='utf-8'))
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = 0
all_text = ''
for doc in civic_docs:
    all_text = all_text + ' ' + doc.get('text', '')
all_text_low = all_text.lower()
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'recovery', 'fire', 'woolsey', 'emergency']
matched = {}
for r in funding:
    name = r.get('Project_Name', '')
    name_low = name.lower()
    base = name_low.split(' (')[0].strip()
    variants = [name_low]
    if base and base != name_low:
        variants.append(base)
    found = False
    for v in variants:
        if not v:
            continue
        idx = all_text_low.find(v)
        if idx != -1:
            start = idx - 200
            if start < 0:
                start = 0
            end = idx + len(v) + 200
            if end > len(all_text_low):
                end = len(all_text_low)
            window = all_text_low[start:end]
            if '2022' in window and (any(k in window for k in keywords) or any(k in name_low for k in keywords)):
                matched[r['Project_Name']] = r
                found = True
                break
    if found:
        continue
# fallback: include projects whose name contains keyword and appear anywhere with 2022
for r in funding:
    if r['Project_Name'] in matched:
        continue
    name_low = r.get('Project_Name','').lower()
    if any(k in name_low for k in ['fema','caloes','caljpia']):
        base = name_low.split(' (')[0].strip()
        idx = all_text_low.find(base)
        if idx != -1:
            start = idx - 200
            if start < 0:
                start = 0
            end = idx + len(base) + 200
            if end > len(all_text_low):
                end = len(all_text_low)
            if '2022' in all_text_low[start:end]:
                matched[r['Project_Name']] = r
matched_list = list(matched.values())
total = sum(r['Amount'] for r in matched_list)
output = {'total_funding': total, 'matched_projects': [{'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in matched_list]}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ewZx9GEvkYHuhFSdepF0EpJu': ['civic_docs'], 'var_call_P0nG1k5Ak7Vdxl9PloiZ7Cjc': ['Funding'], 'var_call_3V3LBuTrnTf5FD8CAnAfAlHL': 'file_storage/call_3V3LBuTrnTf5FD8CAnAfAlHL.json', 'var_call_NT3Q3dsTFn3mJHGGbLBIEHZH': 'file_storage/call_NT3Q3dsTFn3mJHGGbLBIEHZH.json', 'var_call_4Yfs9I5iEcW8QJz9OXfc3Bde': 500}

exec(code, env_args)
