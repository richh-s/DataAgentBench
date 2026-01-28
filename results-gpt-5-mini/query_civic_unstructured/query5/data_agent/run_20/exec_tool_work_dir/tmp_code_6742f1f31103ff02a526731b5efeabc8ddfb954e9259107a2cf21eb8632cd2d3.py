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
disaster_keywords = ['fema', 'caloes', 'caljpia', 'fema/','fema)']

# Filter funding records that look disaster-related by project name or source
mask = fund_df['Project_Name'].str.lower().apply(lambda x: any(k in x for k in disaster_keywords)) | fund_df['Funding_Source'].str.lower().str.contains('federal|assistance')
candidate_funding = fund_df[mask].copy()

# Prepare civic texts
texts = [doc.get('text','') for doc in civic_docs]

# Function to check if project is mentioned with a 2022 date nearby
def mentioned_in_2022(project_name):
    # create base name by removing parenthetical suffixes
    base = re.sub(r"\s*\(.*?\)\s*", "", project_name).strip()
    # Also prepare a looser pattern: split on commas/and/ at slashes
    patterns = [re.escape(base), re.escape(project_name)]
    for txt in texts:
        # search for project name or base in text
        for pat in patterns:
            for m in re.finditer(pat, txt, flags=re.IGNORECASE):
                # get surrounding paragraph (split by double newlines)
                # find paragraph containing the match
                parts = re.split(r"\n\n+", txt)
                for para in parts:
                    if re.search(pat, para, flags=re.IGNORECASE):
                        if '2022' in para:
                            return True
                        # also check nearby 200 chars window
                        start = max(0, m.start()-200)
                        end = min(len(txt), m.end()+200)
                        window = txt[start:end]
                        if '2022' in window:
                            return True
    return False

# For each candidate funding record, check if mentioned in civic_docs with 2022
matched_ids = []
for idx, row in candidate_funding.iterrows():
    pname = row['Project_Name']
    if mentioned_in_2022(pname):
        matched_ids.append(idx)

matched = candidate_funding.loc[matched_ids]

# Sum amounts
total = int(matched['Amount'].sum()) if not matched.empty else 0

# Prepare output: list matched project names and total
output = {
    'matched_projects': matched[['Project_Name','Funding_Source','Amount']].to_dict(orient='records'),
    'total_funding': total
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_m29B2fdk706Rumj5BYqv8E3y': ['civic_docs'], 'var_call_jVgbSxBJrasTFPLaEuOZIFcm': ['Funding'], 'var_call_szU8jleeW6R6ZPXj7FZ66L7h': 'file_storage/call_szU8jleeW6R6ZPXj7FZ66L7h.json', 'var_call_ZdI0zTwZSSr0CUg0n07Cn3pT': 'file_storage/call_ZdI0zTwZSSr0CUg0n07Cn3pT.json'}

exec(code, env_args)
