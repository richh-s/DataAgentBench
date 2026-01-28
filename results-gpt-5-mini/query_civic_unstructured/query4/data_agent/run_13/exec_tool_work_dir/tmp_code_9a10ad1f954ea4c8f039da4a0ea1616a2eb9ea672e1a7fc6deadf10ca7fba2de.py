code = """import json
import re
import pandas as pd

# Load large results from storage file paths
with open(var_call_051hUJbqacaNbipl8yYolvK9, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_O1OOJQa8BhQXpdyEcl70Ja2Q, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Normalize funding rows to DataFrame
df_f = pd.DataFrame(funding_rows)
# Ensure Amount numeric
df_f['Amount'] = pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

# Function to get base name by removing parenthetical suffix
def base_name(name):
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()

# Precompute civic texts
civic_texts = [doc.get('text','').lower() for doc in civic_docs]

matched_bases = set()
matched_rows_idx = []

for idx, row in df_f.iterrows():
    pname = str(row['Project_Name'])
    base = base_name(pname).lower()
    found = False
    # Try several name variants to search in civic texts
    variants = {pname.lower(), base}
    # also replace '&' with 'and' and remove punctuation
    variants.add(base.replace('&','and'))
    for text in civic_texts:
        for var in variants:
            if var and var in text:
                # Find position(s) of occurrence(s)
                for m in re.finditer(re.escape(var), text):
                    start = m.start()
                    window = text[max(0, start-200): start+500]
                    # Check for Spring 2022 or months March/April/May 2022 nearby
                    if ('spring' in window and '2022' in window) or (('march' in window or 'mar' in window or 'april' in window or 'may' in window) and '2022' in window):
                        matched_bases.add(base)
                        matched_rows_idx.append(idx)
                        found = True
                        break
                if found:
                    break
        if found:
            break

# Now for each matched base name, sum all funding rows that share that base
matched_bases_list = list(matched_bases)
matched_projects_summary = []

total_funding = 0
for base in matched_bases_list:
    # sum amounts where base_name of funding row equals this base
    mask = df_f['Project_Name'].apply(lambda x: base_name(str(x)).lower() == base)
    amt = int(df_f.loc[mask, 'Amount'].sum())
    total_funding += amt
    matched_projects_summary.append({'project_base_name': base, 'funding_sum': int(amt)})

result = {
    'count_projects_started_spring_2022': len(matched_bases_list),
    'total_funding': int(total_funding),
    'projects': matched_projects_summary
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_P1y9gQYe2qdh6JUcN1kvGbyB': ['civic_docs'], 'var_call_6o8bFHtpjOFeJaIyPDcTgEHy': ['Funding'], 'var_call_051hUJbqacaNbipl8yYolvK9': 'file_storage/call_051hUJbqacaNbipl8yYolvK9.json', 'var_call_O1OOJQa8BhQXpdyEcl70Ja2Q': 'file_storage/call_O1OOJQa8BhQXpdyEcl70Ja2Q.json'}

exec(code, env_args)
