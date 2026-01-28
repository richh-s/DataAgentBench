code = """import json
import pandas as pd

# Load tool results from storage files
with open(var_call_szU8jleeW6R6ZPXj7FZ66L7h, 'r') as f:
    funding = json.load(f)
with open(var_call_ZdI0zTwZSSr0CUg0n07Cn3pT, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster indicators
keywords = ['fema', 'caloes', 'caljpia']

# Filter candidate disaster funding by project name or source
def is_disaster_row(row):
    name = row['Project_Name'].lower()
    source = row['Funding_Source'].lower()
    if any(k in name for k in keywords):
        return True
    if 'federal' in source or 'assistance' in source:
        return True
    return False

candidate = fund_df[fund_df.apply(is_disaster_row, axis=1)].copy()

# Prepare civic texts concatenated
texts = [d.get('text','') for d in civic_docs]

# Helper to get base project name without parenthetical suffix
def base_name(pname):
    if '(' in pname:
        return pname.split('(')[0].strip()
    return pname.strip()

# Check if project is mentioned near 2022 by simple containment
matched = []
for _, row in candidate.iterrows():
    pname = row['Project_Name']
    bname = base_name(pname).lower()
    found = False
    for txt in texts:
        tl = txt.lower()
        if bname in tl and '2022' in tl:
            found = True
            break
    if found:
        matched.append({'Project_Name': row['Project_Name'], 'Funding_Source': row['Funding_Source'], 'Amount': int(row['Amount'])})

total = sum(x['Amount'] for x in matched)

output = {'matched_projects': matched, 'total_funding': total}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_m29B2fdk706Rumj5BYqv8E3y': ['civic_docs'], 'var_call_jVgbSxBJrasTFPLaEuOZIFcm': ['Funding'], 'var_call_szU8jleeW6R6ZPXj7FZ66L7h': 'file_storage/call_szU8jleeW6R6ZPXj7FZ66L7h.json', 'var_call_ZdI0zTwZSSr0CUg0n07Cn3pT': 'file_storage/call_ZdI0zTwZSSr0CUg0n07Cn3pT.json'}

exec(code, env_args)
