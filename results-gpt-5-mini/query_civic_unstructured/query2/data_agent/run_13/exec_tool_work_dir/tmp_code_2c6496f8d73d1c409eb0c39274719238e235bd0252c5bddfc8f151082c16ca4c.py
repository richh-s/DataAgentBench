code = """import json
import pandas as pd

# Load data from storage file paths provided by previous tool calls
funding_path = var_call_TUmevO8tahmvoGUCVw7U8Bfy
civic_path = var_call_zQkLJw2iym3t2IWOoS4vkm4o

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
with open(civic_path, 'r') as f:
    civic_records = json.load(f)

# Normalize funding dataframe
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['Project_Name_low'] = funding_df['Project_Name'].str.lower()

park_keywords = ['park', 'playground', 'walkway', 'benches', 'shade', 'bluffs', 'paver']

matched = []

# For each funding project that looks park-related, search civic docs for completion in 2022
for idx, row in funding_df.iterrows():
    pname_low = row['Project_Name_low']
    if not any(k in pname_low for k in park_keywords):
        continue
    found = False
    for doc in civic_records:
        text_low = doc.get('text','').lower()
        if pname_low in text_low:
            # find position(s)
            start = 0
            while True:
                pos = text_low.find(pname_low, start)
                if pos == -1:
                    break
                window = text_low[max(0, pos-500): pos+500]
                if 'completed' in window and '2022' in window:
                    found = True
                    break
                start = pos + 1
        if found:
            matched.append({'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})
            break

# Also handle projects that may be mentioned in civic docs as park projects completed in 2022 but funding names differ slightly
# Extract park project name phrases from civic docs by finding lines with park keywords and 'completed' and '2022'
civic_candidates = set()
for doc in civic_records:
    text = doc.get('text','')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        l = line.lower()
        if 'completed' in l and '2022' in l and any(k in l for k in park_keywords):
            # look backwards for a project title line (up to 3 lines before)
            for j in range(max(0, i-3), i+1):
                candidate = lines[j].strip()
                if len(candidate) > 3 and any(k in candidate.lower() for k in park_keywords):
                    civic_candidates.add(candidate.lower())

# Try to match funding projects to these civic candidates by substring overlap
for cand in civic_candidates:
    for idx, row in funding_df.iterrows():
        pname_low = row['Project_Name_low']
        if any(k in pname_low for k in park_keywords):
            if cand in pname_low or pname_low in cand or any(word in pname_low for word in cand.split() if len(word)>4):
                # ensure not already added
                if not any(d['Project_Name']==row['Project_Name'] for d in matched):
                    matched.append({'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})

# Sum amounts
total = sum(d['Amount'] for d in matched)

output = {
    'total_funding': total,
    'matched_projects': matched,
    'civic_candidates_found': list(civic_candidates)
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_7F65cxkXehOP67TdCcKr94V9': ['civic_docs'], 'var_call_j7BetpNtBnPAHqOl4xBQnreH': ['Funding'], 'var_call_TUmevO8tahmvoGUCVw7U8Bfy': 'file_storage/call_TUmevO8tahmvoGUCVw7U8Bfy.json', 'var_call_zQkLJw2iym3t2IWOoS4vkm4o': 'file_storage/call_zQkLJw2iym3t2IWOoS4vkm4o.json'}

exec(code, env_args)
