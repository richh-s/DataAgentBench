code = """import json
import pandas as pd
import re

# Load data from storage file paths provided by previous tool calls
funding_path = var_call_TUmevO8tahmvoGUCVw7U8Bfy
civic_path = var_call_zQkLJw2iym3t2IWOoS4vkm4o

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

# Normalize funding dataframe
funding_df = pd.DataFrame(funding_records)
# Ensure Amount is integer
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['Project_Name_low'] = funding_df['Project_Name'].str.lower()

# Search civic docs for lines indicating completion in 2022 and containing park-related context
park_keywords = ['park', 'playground', 'walkway', 'benches', 'shade', 'playground', 'playground', 'playground', 'playground', 'bluffs']
completed_projects_candidates = set()

for doc in civic_records:
    text = doc.get('text','')
    # split into lines
    lines = text.split('\n')
    for i, line in enumerate(lines):
        l = line.lower()
        # consider lines that mention completed and 2022
        if 'completed' in l and '2022' in l:
            # examine a window of surrounding lines for project names and park keywords
            start = max(0, i-8)
            end = min(len(lines), i+3)
            block = '\n'.join(lines[start:end]).lower()
            # If block contains park keywords, try to find project name candidates
            if any(k in block for k in park_keywords):
                # try to extract capitalized project-like lines from original window (not lower)
                window_orig = '\n'.join(lines[start:end])
                # split into lines and pick lines that are short (<=80) and contain letters and not just 'updates' or 'project schedule'
                for w in window_orig.split('\n'):
                    ws = w.strip()
                    if not ws:
                        continue
                    wl = ws.lower()
                    if any(k in wl for k in park_keywords):
                        # use this as candidate name (strip bullets and numbering)
                        cand = re.sub(r"^[^A-Za-z0-9]*", '', ws)
                        cand = cand.split('\t')[0].strip(' -:\u2022')
                        if len(cand) > 3:
                            completed_projects_candidates.add(cand.lower())

# As a fallback, also look for lines that explicitly name known funding projects and mention completed in nearby lines
for doc in civic_records:
    text = doc.get('text','')
    text_low = text.lower()
    for idx, fr in funding_df.iterrows():
        fname = fr['Project_Name_low']
        # if project name mentions park-related keyword
        if any(k in fname for k in park_keywords):
            # if the civic doc mentions the project name and also mentions 'completed' and '2022' somewhere nearby
            if fname in text_low:
                # find index of occurrence
                pos = text_low.find(fname)
                # check window around pos for 'completed' and '2022'
                window = text_low[max(0,pos-500): pos+500]
                if 'completed' in window and '2022' in window:
                    completed_projects_candidates.add(fname)

# Now match funding records whose project names match any candidate (substring match)
matched_rows = []
for idx, fr in funding_df.iterrows():
    fname = fr['Project_Name_low']
    for cand in completed_projects_candidates:
        if cand in fname or fname in cand:
            matched_rows.append(fr)
            break

matched_df = pd.DataFrame(matched_rows)
if matched_df.empty:
    total = 0
else:
    total = int(matched_df['Amount'].sum())

# Prepare readable matched project list
matched_list = matched_df[['Project_Name','Amount']].to_dict(orient='records')

output = {
    'total_funding': total,
    'matched_projects': matched_list,
    'candidates_extracted': list(completed_projects_candidates)[:100]
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_7F65cxkXehOP67TdCcKr94V9': ['civic_docs'], 'var_call_j7BetpNtBnPAHqOl4xBQnreH': ['Funding'], 'var_call_TUmevO8tahmvoGUCVw7U8Bfy': 'file_storage/call_TUmevO8tahmvoGUCVw7U8Bfy.json', 'var_call_zQkLJw2iym3t2IWOoS4vkm4o': 'file_storage/call_zQkLJw2iym3t2IWOoS4vkm4o.json'}

exec(code, env_args)
