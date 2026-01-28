code = """import json, re, pandas as pd

# Load previous tool results
with open(var_call_szU8jleeW6R6ZPXj7FZ66L7h, 'r') as f:
    funding = json.load(f)
with open(var_call_ZdI0zTwZSSr0CUg0n07Cn3pT, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding)
# Ensure Amount is numeric
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Define disaster indicators
disaster_keywords = ['fema', 'caloes', 'caljpia', 'fema/']

# Filter funding records that look disaster-related by project name or source
mask_name = fund_df['Project_Name'].str.lower().apply(lambda x: any(k in x for k in disaster_keywords))
mask_source = fund_df['Funding_Source'].str.lower().str.contains('federal|assistance|fema')
candidate_funding = fund_df[mask_name | mask_source].copy()

# Prepare civic texts
texts = [doc.get('text','') for doc in civic_docs]

# Function to check if project is mentioned with a 2022 date nearby
def mentioned_in_2022(project_name):
    base = re.sub(r"\s*\(.*?\)\s*", "", project_name).strip()
    patterns = [re.escape(base), re.escape(project_name)]
    for txt in texts:
        for pat in patterns:
            for m in re.finditer(pat, txt, flags=re.IGNORECASE):
                # look for '2022' in a window around the match
                start = max(0, m.start()-400)
                end = min(len(txt), m.end()+400)
                window = txt[start:end]
                if '2022' in window:
                    return True
                # also check the paragraph containing the match
                parts = re.split(r"\n\n+", txt)
                for para in parts:
                    if re.search(pat, para, flags=re.IGNORECASE) and '2022' in para:
                        return True
    return False

# For each candidate funding record, check if mentioned in civic_docs with 2022
matched = []
for _, row in candidate_funding.iterrows():
    pname = row['Project_Name']
    if mentioned_in_2022(pname):
        matched.append({'Project_Name': pname, 'Funding_Source': row['Funding_Source'], 'Amount': int(row['Amount'])})

# Sum amounts
total = sum(r['Amount'] for r in matched)

output = {'matched_projects': matched, 'total_funding': total}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_m29B2fdk706Rumj5BYqv8E3y': ['civic_docs'], 'var_call_jVgbSxBJrasTFPLaEuOZIFcm': ['Funding'], 'var_call_szU8jleeW6R6ZPXj7FZ66L7h': 'file_storage/call_szU8jleeW6R6ZPXj7FZ66L7h.json', 'var_call_ZdI0zTwZSSr0CUg0n07Cn3pT': 'file_storage/call_ZdI0zTwZSSr0CUg0n07Cn3pT.json'}

exec(code, env_args)
