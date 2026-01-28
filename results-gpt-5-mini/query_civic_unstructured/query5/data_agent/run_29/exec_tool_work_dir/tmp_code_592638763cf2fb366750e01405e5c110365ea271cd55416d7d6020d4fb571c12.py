code = """import json
import pandas as pd

# Load data
with open(var_call_RF5KUQDKAHcatKco1yXwKyuW, 'r') as f:
    funding_records = json.load(f)
with open(var_call_kzPaCpRaTreguFOvBPuotfG7, 'r') as f:
    civic_docs = json.load(f)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Prepare civic docs as list of dicts with filename and text lowercased
docs = []
for d in civic_docs:
    docs.append({'filename': d.get('filename','').lower(), 'text': d.get('text','').lower()})

# disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency', 'federal assistance', 'federal']

matched = []

for idx, row in fund_df.iterrows():
    pname = str(row['Project_Name']).strip()
    pname_low = pname.lower()
    # base name without parenthetical
    if '(' in pname_low:
        base = pname_low.split('(')[0].strip()
    else:
        base = pname_low
    found_context = ''
    found_any = False
    for d in docs:
        if base and base in d['text']:
            i = d['text'].find(base)
            start = max(0, i-300)
            end = min(len(d['text']), i+len(base)+300)
            found_context = d['text'][start:end]
            # include filename as context
            found_context = d['filename'] + '\n' + found_context
            found_any = True
            break
    # fallback: try full project name
    if not found_any and pname_low in d['text']:
        i = d['text'].find(pname_low)
        start = max(0, i-300)
        end = min(len(d['text']), i+len(pname_low)+300)
        found_context = d['text'][start:end]
        found_context = d['filename'] + '\n' + found_context
        found_any = True
    if not found_any:
        # try first 4 words
        tokens = base.split()
        if len(tokens) > 4:
            short = ' '.join(tokens[:4])
            for d in docs:
                if short in d['text']:
                    i = d['text'].find(short)
                    start = max(0, i-300)
                    end = min(len(d['text']), i+len(short)+300)
                    found_context = d['filename'] + '\n' + d['text'][start:end]
                    found_any = True
                    break
    if not found_any:
        continue
    # classify disaster
    is_disaster = any(k in pname_low for k in disaster_keywords) or any(k in found_context for k in disaster_keywords)
    started_2022 = '2022' in found_context
    if is_disaster and started_2022:
        matched.append({'Funding_ID': int(row['Funding_ID']), 'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})

total = sum(m['Amount'] for m in matched)
result = {'total_funding_2022_disaster_projects': total, 'matched_records': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Mmh90s31ZiG1mcuIAkQlcjXF': ['civic_docs'], 'var_call_3GU6IwnaLiLmQBgB80238sHz': ['Funding'], 'var_call_kzPaCpRaTreguFOvBPuotfG7': 'file_storage/call_kzPaCpRaTreguFOvBPuotfG7.json', 'var_call_RF5KUQDKAHcatKco1yXwKyuW': 'file_storage/call_RF5KUQDKAHcatKco1yXwKyuW.json', 'var_call_e6j7NZTHa1QN5xcH9Jb1yXS8': {'funding_count': 500, 'civic_docs_count': 19}}

exec(code, env_args)
