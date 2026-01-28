code = """import json
import re
import pandas as pd

# Load data files from storage keys
with open(var_call_GFKuGiEUWp4gojAfgOX0vlGM, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_IA052drrJgZbeYVgVDV4ItOX, 'r') as f:
    funding = json.load(f)

# Convert funding to DataFrame
fund_df = pd.DataFrame(funding)
# Ensure Amount numeric
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'caloes', 'caljpia']

# Helper to normalize project name
def normalize(name):
    name = re.sub(r"\(.*?\)", "", name)  # remove parentheses content
    return re.sub(r"\s+", " ", name).strip().lower()

# Build a big text corpus list
docs = []
for doc in civic_docs:
    text = doc.get('text','')
    filename = doc.get('filename','')
    docs.append({'filename': filename.lower(), 'text': text.lower()})

matches = []

for idx, row in fund_df.iterrows():
    pname = row['Project_Name']
    pname_l = pname.lower()
    # Check if funding record itself indicates disaster via keywords
    is_disaster = any(k in pname_l for k in disaster_keywords)
    # Also check funding source maybe indicates federal assistance etc
    if not is_disaster:
        src = str(row.get('Funding_Source','')).lower()
        if any(k in src for k in ['fema','caloes','caljpia','federal assistance']):
            is_disaster = True
    if not is_disaster:
        continue

    # Now check if project started in 2022 by searching civic docs
    started_2022 = False
    core = normalize(pname)
    # if project name itself contains 2022
    if '2022' in pname_l:
        started_2022 = True
    else:
        for d in docs:
            text = d['text']
            # If core name non-empty, search
            if core and core in text:
                # find all occurrences
                for m in re.finditer(re.escape(core), text):
                    start = max(0, m.start()-200)
                    end = min(len(text), m.end()+200)
                    window = text[start:end]
                    if '2022' in window:
                        started_2022 = True
                        break
                if started_2022:
                    break
            # also consider if filename has 2022 and project name at least appears in doc
            if d['filename'] and '2022' in d['filename'] and (core in text):
                started_2022 = True
                break
    if started_2022:
        matches.append({'Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})

# Sum amounts
total = sum(m['Amount'] for m in matches)

# Prepare output
output = {'total_disaster_funding_started_2022': total, 'matched_records': matches}

import json
print("----BEGIN PRINT FORMAT----")
print('print("__RESULT__:")')
print('print(\'{}\')'.format(json.dumps(output)))
print("----END PRINT FORMAT----")"""

env_args = {'var_call_WdAUq4FdzXMRWPpkrBvinOIF': ['civic_docs'], 'var_call_wwSjWegAh834UWWjF6AXP8TA': ['Funding'], 'var_call_GFKuGiEUWp4gojAfgOX0vlGM': 'file_storage/call_GFKuGiEUWp4gojAfgOX0vlGM.json', 'var_call_IA052drrJgZbeYVgVDV4ItOX': 'file_storage/call_IA052drrJgZbeYVgVDV4ItOX.json'}

exec(code, env_args)
