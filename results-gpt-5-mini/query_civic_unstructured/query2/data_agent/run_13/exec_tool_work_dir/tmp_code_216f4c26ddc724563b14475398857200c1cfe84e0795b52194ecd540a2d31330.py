code = """import json
import pandas as pd

funding_path = var_call_TUmevO8tahmvoGUCVw7U8Bfy
civic_path = var_call_zQkLJw2iym3t2IWOoS4vkm4o

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['Project_Name_low'] = funding_df['Project_Name'].str.lower()

park_keywords = ['park', 'playground', 'walkway', 'benches', 'shade', 'bluffs', 'paver', 'play']

candidates = set()
for doc in civic_records:
    text = doc.get('text','')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        l = line.lower()
        if 'completed' in l and '2022' in l:
            # look back a few lines for candidate names
            for j in range(max(0, i-4), i+1):
                candidate = lines[j].strip()
                if len(candidate) < 3:
                    continue
                window = (' '.join(lines[max(0,i-6):i+3])).lower()
                if any(k in candidate.lower() for k in park_keywords) or any(k in window for k in park_keywords):
                    cand = candidate
                    cand = cand.strip(' -:')
                    if len(cand) > 2:
                        candidates.add(cand.lower())
        if 'construction was completed' in l and '2022' in l:
            for j in range(max(0, i-5), i):
                candidate = lines[j].strip()
                if len(candidate) > 3:
                    window = (' '.join(lines[max(0,i-6):i+3])).lower()
                    if any(k in candidate.lower() for k in park_keywords) or any(k in window for k in park_keywords):
                        cand = candidate.strip(' -:')
                        candidates.add(cand.lower())
                        break

# Also extract sentences where park keyword and completed and 2022 appear
for doc in civic_records:
    text_low = doc.get('text','').lower()
    if all(x in text_low for x in ['2022','completed']):
        for k in park_keywords:
            if k in text_low:
                sentences = [s.strip() for s in doc.get('text','').split('.') if s.strip()]
                for s in sentences:
                    sl = s.lower()
                    if '2022' in sl and 'completed' in sl and k in sl:
                        candidates.add(s.strip().lower())

# Match funding projects to candidates by substring or token overlap
matched = []
matched_names = set()
for idx, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_low = row['Project_Name_low']
    if any(k in pname_low for k in park_keywords):
        # candidate likely park-related; check civic docs occurrence
        for doc in civic_records:
            if pname_low in doc.get('text','').lower():
                # check nearby if completed and 2022
                txt = doc.get('text','').lower()
                pos = txt.find(pname_low)
                window = txt[max(0,pos-400):pos+400]
                if 'completed' in window and '2022' in window:
                    if pname not in matched_names:
                        matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
                        matched_names.add(pname)
                    break
    # also match by comparing to extracted candidate phrases
    for cand in candidates:
        if cand in pname_low or pname_low in cand:
            if pname not in matched_names:
                matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
                matched_names.add(pname)
                break
        else:
            # token overlap
            cand_tokens = [t for t in [w for w in cand.split() if len(w)>4]]
            if any(tok in pname_low for tok in cand_tokens):
                if pname not in matched_names:
                    matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
                    matched_names.add(pname)
                    break

total = sum(item['Amount'] for item in matched)

output = {'total_funding': total, 'matched_projects': matched, 'candidates': list(candidates)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_7F65cxkXehOP67TdCcKr94V9': ['civic_docs'], 'var_call_j7BetpNtBnPAHqOl4xBQnreH': ['Funding'], 'var_call_TUmevO8tahmvoGUCVw7U8Bfy': 'file_storage/call_TUmevO8tahmvoGUCVw7U8Bfy.json', 'var_call_zQkLJw2iym3t2IWOoS4vkm4o': 'file_storage/call_zQkLJw2iym3t2IWOoS4vkm4o.json', 'var_call_MpLMplY97suCpXCa4g3YLFuE': {'funding_len': 500, 'civic_len': 19}}

exec(code, env_args)
