code = """import json
import pandas as pd

# Load Mongo query result (file path stored in var_call_da88hpSQYBAwDy7A0FwUKBX1)
with open(var_call_da88hpSQYBAwDy7A0FwUKBX1, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Load SQLite query result (file path stored in var_call_mIolvS20WXkBRRAKIVUS8UNP)
with open(var_call_mIolvS20WXkBRRAKIVUS8UNP, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Create DataFrame for papers
df_p = pd.DataFrame(papers)
# Ensure filename exists
if 'filename' not in df_p.columns:
    df_p['filename'] = None

# Extract title from filename (remove .txt)

def extract_title(fn):
    if not fn or not isinstance(fn, str):
        return None
    return fn.rstrip().removesuffix('.txt') if hasattr(fn, 'removesuffix') else (fn.rstrip()[:-4] if fn.rstrip().lower().endswith('.txt') else fn.rstrip())

# Handle Python versions without str.removesuffix by fallback above

df_p['title'] = df_p['filename'].apply(extract_title)

# Normalize contribution: could be list or string

def contrib_to_str(c):
    if c is None:
        return ''
    if isinstance(c, list):
        return ' '.join([str(x) for x in c])
    return str(c)

if 'contribution' not in df_p.columns:
    df_p['contribution'] = ''

df_p['contribution_str'] = df_p['contribution'].apply(contrib_to_str).str.lower()

# Normalize year

def to_int_year(y):
    if y is None:
        return None
    try:
        return int(y)
    except:
        try:
            # sometimes year can be embedded in a string
            s = str(y)
            digits = ''.join(ch for ch in s if ch.isdigit())
            if len(digits) >= 4:
                return int(digits[:4])
        except:
            return None
    return None

if 'year' not in df_p.columns:
    df_p['year'] = None

df_p['year_int'] = df_p['year'].apply(to_int_year)

# Filter: contribution contains 'empirical' and year > 2016
mask = df_p['contribution_str'].str.contains('empirical', na=False) & (df_p['year_int'] > 2016)
df_empirical = df_p[mask].copy()

# Prepare citations DataFrame
df_c = pd.DataFrame(citations)
if 'title' not in df_c.columns:
    df_c['title'] = None
if 'total_citations' in df_c.columns:
    df_c['total_citations_int'] = pd.to_numeric(df_c['total_citations'], errors='coerce').fillna(0).astype(int)
else:
    df_c['total_citations_int'] = 0

# Join on title
# Titles from papers are assumed to match citations titles
result = pd.merge(df_empirical[['title']], df_c[['title','total_citations_int']], on='title', how='left')

# Replace NaN with 0
result['total_citations_int'] = result['total_citations_int'].fillna(0).astype(int)

# Build output list
output = []
for _, row in result.iterrows():
    if row['title'] is None:
        continue
    output.append({'title': row['title'], 'total_citations': int(row['total_citations_int'])})

# Sort output by title
output = sorted(output, key=lambda x: x['title'])

import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_OP0npdWdsUOkowIeKcl908it': ['paper_docs'], 'var_call_da88hpSQYBAwDy7A0FwUKBX1': 'file_storage/call_da88hpSQYBAwDy7A0FwUKBX1.json', 'var_call_LTWSz7PHWkx8ELyUNdvVbWlE': ['Citations', 'sqlite_sequence'], 'var_call_mIolvS20WXkBRRAKIVUS8UNP': 'file_storage/call_mIolvS20WXkBRRAKIVUS8UNP.json'}

exec(code, env_args)
