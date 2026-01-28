code = """import json
import pandas as pd
p1 = var_call_RF5KUQDKAHcatKco1yXwKyuW
p2 = var_call_kzPaCpRaTreguFOvBPuotfG7
with open(p1, 'r') as f:
    funding_records = json.load(f)
with open(p2, 'r') as f:
    civic_docs = json.load(f)
df = pd.DataFrame(funding_records)
df['Amount'] = df['Amount'].astype(int)
docs_list = []
for d in civic_docs:
    docs_list.append({'filename': d.get('filename', '').lower(), 'text': d.get('text', '').lower()})
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency', 'federal assistance', 'federal']
matched = []
for _, row in df.iterrows():
    pname = str(row['Project_Name']).strip()
    lname = pname.lower()
    if '(' in lname:
        base = lname.split('(')[0].strip()
    else:
        base = lname
    found = False
    context = ''
    for d in docs_list:
        if base and base in d['text']:
            i = d['text'].find(base)
            start = max(0, i - 300)
            end = min(len(d['text']), i + len(base) + 300)
            context = d['filename'] + chr(10) + d['text'][start:end]
            found = True
            break
    if not found:
        for d in docs_list:
            if lname in d['text']:
                i = d['text'].find(lname)
                start = max(0, i - 300)
                end = min(len(d['text']), i + len(lname) + 300)
                context = d['filename'] + chr(10) + d['text'][start:end]
                found = True
                break
    if not found:
        tokens = base.split()
        if len(tokens) > 4:
            short = ' '.join(tokens[:4])
            for d in docs_list:
                if short in d['text']:
                    i = d['text'].find(short)
                    start = max(0, i - 300)
                    end = min(len(d['text']), i + len(short) + 300)
                    context = d['filename'] + chr(10) + d['text'][start:end]
                    found = True
                    break
    if not found:
        continue
    is_disaster = any(k in lname for k in keywords) or any(k in context for k in keywords)
    started_2022 = '2022' in context
    if is_disaster and started_2022:
        matched.append({'Funding_ID': int(row['Funding_ID']), 'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})
total = sum(m['Amount'] for m in matched)
res = {'total_funding_2022_disaster_projects': total, 'matched_records': matched}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Mmh90s31ZiG1mcuIAkQlcjXF': ['civic_docs'], 'var_call_3GU6IwnaLiLmQBgB80238sHz': ['Funding'], 'var_call_kzPaCpRaTreguFOvBPuotfG7': 'file_storage/call_kzPaCpRaTreguFOvBPuotfG7.json', 'var_call_RF5KUQDKAHcatKco1yXwKyuW': 'file_storage/call_RF5KUQDKAHcatKco1yXwKyuW.json', 'var_call_e6j7NZTHa1QN5xcH9Jb1yXS8': {'funding_count': 500, 'civic_docs_count': 19}}

exec(code, env_args)
