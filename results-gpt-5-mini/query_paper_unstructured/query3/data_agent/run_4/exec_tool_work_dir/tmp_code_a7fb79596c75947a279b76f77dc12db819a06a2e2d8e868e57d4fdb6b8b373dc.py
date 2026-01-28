code = """import json
import re
import pandas as pd

# Load data from previous query results (file paths)
with open(var_call_mIDlEHIrjY3dhdzq9sBVWJ3X, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_D1iVuSK87384ELWaBAvHUfdV, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Create DataFrames
docs_df = pd.DataFrame(docs)
# Derive title from filename
docs_df['title'] = docs_df['filename'].str.replace(r"\.txt$", '', regex=True)

# Extract first 4-digit year (1990-2026) from text
def extract_year(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if m:
        try:
            y = int(m.group(0))
            return y
        except:
            return None
    return None

docs_df['year'] = docs_df['text'].apply(extract_year)
# Mark empirical contribution if 'empirical' appears in text
docs_df['has_empirical'] = docs_df['text'].str.lower().str.contains('empirical')

# Load citations
cits_df = pd.DataFrame(citations)
# Ensure titles match exactly and convert total_citations to int
cits_df = cits_df.rename(columns={"total_citations": "total_citations"})
# Some citation counts may be strings; convert
cits_df['total_citations'] = cits_df['total_citations'].apply(lambda x: int(x) if x is not None and str(x).isdigit() else 0)

# Filter docs for empirical and year > 2016
filtered = docs_df[(docs_df['has_empirical']) & (docs_df['year'].notnull()) & (docs_df['year'] > 2016)].copy()

# Merge with citations on title
merged = pd.merge(filtered, cits_df[['title','total_citations']], on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)

# Prepare output list
output = []
for _, row in merged.iterrows():
    output.append({
        'title': row['title'],
        'total_citation_count': int(row['total_citations'])
    })

# Sort by citations desc
output = sorted(output, key=lambda x: x['total_citation_count'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_mIDlEHIrjY3dhdzq9sBVWJ3X': 'file_storage/call_mIDlEHIrjY3dhdzq9sBVWJ3X.json', 'var_call_D1iVuSK87384ELWaBAvHUfdV': 'file_storage/call_D1iVuSK87384ELWaBAvHUfdV.json'}

exec(code, env_args)
