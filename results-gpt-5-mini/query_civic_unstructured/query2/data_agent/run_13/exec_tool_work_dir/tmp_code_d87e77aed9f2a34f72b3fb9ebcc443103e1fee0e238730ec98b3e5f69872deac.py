code = """import json
import pandas as pd
import re

funding_path = var_call_TUmevO8tahmvoGUCVw7U8Bfy
civic_path = var_call_zQkLJw2iym3t2IWOoS4vkm4o

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['Project_Name_low'] = funding_df['Project_Name'].str.lower()

park_keywords = ['park', 'playground', 'walkway', 'benches', 'shade', 'bluffs', 'paver', 'playground', 'walk']

candidates = set()
for doc in civic_records:
    text = doc.get('text','')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        l = line.lower()
        # if this line indicates completion in 2022
        if 'completed' in l and '2022' in l:
            # look backward up to 4 lines for a candidate
            for j in range(max(0, i-4), i+1):
                candidate = lines[j].strip()
                if len(candidate) < 3:
                    continue
                # require candidate line to contain any park keyword OR the window contains park keyword
                window = (' '.join(lines[max(0,i-6):i+3])).lower()
                if any(k in candidate.lower() for k in park_keywords) or any(k in window for k in park_keywords):
                    # clean candidate
                    cand = re.sub(r"^[^A-Za-z0-9]+", '', candidate)
                    cand = cand.strip(' -:\u2022')
                    if len(cand) > 2:
                        candidates.add(cand.lower())
        else:
            # also catch lines like 'construction was completed, november 2022' without 'completed' maybe 'construction was completed' covers
            if 'construction was completed' in l and '2022' in l:
                # previous non-empty line as candidate
                for j in range(i-1, max(-1, i-6), -1):
                    if j < 0:
                        break
                    candidate = lines[j].strip()
                    if len(candidate) > 3:
                        window = (' '.join(lines[max(0,i-6):i+3])).lower()
                        if any(k in candidate.lower() for k in park_keywords) or any(k in window for k in park_keywords):
                            cand = re.sub(r"^[^A-Za-z0-9]+", '', candidate)
                            cand = cand.strip(' -:\u2022')
                            if len(cand) > 2:
                                candidates.add(cand.lower())
                            break

# Additionally, search for any lines that explicitly mention a park keyword and also 'completed' and 2022 somewhere nearby
for doc in civic_records:
    text_low = doc.get('text','').lower()
    for k in park_keywords:
        if k in text_low and '2022' in text_low and 'completed' in text_low:
            # try to extract sentence containing park keyword
            # split into sentences
            sentences = re.split(r'[\.\n]', doc.get('text',''))
            for s in sentences:
                sl = s.lower()
                if k in sl and '2022' in sl and 'completed' in sl:
                    cand = s.strip()
                    cand = re.sub(r"^[^A-Za-z0-9]+", '', cand)
                    if len(cand) > 3:
                        candidates.add(cand.lower())

# Now match funding records by substring and token overlap
matched = []
matched_names = set()
for idx, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_low = row['Project_Name_low']
    for cand in candidates:
        if cand in pname_low or pname_low in cand:
            matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
            matched_names.add(pname)
            break
        # token overlap: any token from cand longer than 4 chars in pname_low
        cand_tokens = [t for t in re.split(r"[^a-z0-9]", cand) if len(t) > 4]
        if any(tok in pname_low for tok in cand_tokens):
            if pname not in matched_names:
                matched.append({'Project_Name': pname, 'Amount': int(row['Amount'])})
                matched_names.add(pname)
                break

# Also, include funding rows that explicitly contain park keywords and are likely completed in 2022 by scanning civic docs for project name occurrence near completed 2022
for idx, row in funding_df.iterrows():
    pname_low = row['Project_Name_low']
    if not any(k in pname_low for k in park_keywords):
        continue
    for doc in civic_records:
        text_low = doc.get('text','').lower()
        pos = text_low.find(pname_low)
        if pos != -1:
            window = text_low[max(0,pos-400): pos+400]
            if 'completed' in window and '2022' in window:
                if row['Project_Name'] not in matched_names:
                    matched.append({'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})
                    matched_names.add(row['Project_Name'])
                break

# Sum matched amounts
total = sum(item['Amount'] for item in matched)

output = {'total_funding': total, 'matched_projects': matched, 'candidates': list(candidates)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_7F65cxkXehOP67TdCcKr94V9': ['civic_docs'], 'var_call_j7BetpNtBnPAHqOl4xBQnreH': ['Funding'], 'var_call_TUmevO8tahmvoGUCVw7U8Bfy': 'file_storage/call_TUmevO8tahmvoGUCVw7U8Bfy.json', 'var_call_zQkLJw2iym3t2IWOoS4vkm4o': 'file_storage/call_zQkLJw2iym3t2IWOoS4vkm4o.json', 'var_call_MpLMplY97suCpXCa4g3YLFuE': {'funding_len': 500, 'civic_len': 19}}

exec(code, env_args)
