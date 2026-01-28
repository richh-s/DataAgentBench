code = """import json
import re
import pandas as pd

# Load the MongoDB query result (file path stored in var_call_UiXFAWxlyIWYkqSXdENiIgwM)
with open(var_call_UiXFAWxlyIWYkqSXdENiIgwM, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load the Citations aggregate result (file path stored in var_call_tAhYfbZ5ec3wGmZhugmAT3IR)
with open(var_call_tAhYfbZ5ec3wGmZhugmAT3IR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df_docs = pd.DataFrame(docs)
# derive title
df_docs['title'] = df_docs['filename'].str.replace(r"\.txt$", '', regex=True)

# helper to extract publication year
venue_names = ['CHI','Ubicomp','CSCW','DIS','PervasiveHealth','WWW','IUI','OzCHI','TEI','AH']

def extract_year(text):
    if not isinstance(text, str):
        return None
    # find all years
    years = [m for m in re.finditer(r"\b(19|20)\d{2}\b", text)]
    if not years:
        return None
    # try to find year near venue names
    for ven in venue_names:
        for m in re.finditer(re.escape(ven), text, flags=re.IGNORECASE):
            ven_pos = m.start()
            # look for year within 120 chars after or before
            window_start = max(0, ven_pos-120)
            window_end = ven_pos+120
            for y in years:
                if window_start <= y.start() <= window_end:
                    return int(y.group(0))
    # if not found near venues, pick the earliest year occurrence
    # but ensure plausible publication year (1990-2025)
    for y in years:
        yy = int(y.group(0))
        if 1990 <= yy <= 2025:
            return yy
    return int(years[0].group(0))

# Extract year and domain flag
df_docs['pub_year'] = df_docs['text'].apply(extract_year)

def has_physical_activity(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    if 'physical activity' in t:
        return True
    if 'physical-activity' in t:
        return True
    # also check for phrases like 'activity tracking' with 'physical' nearby
    if 'physical' in t and 'activity' in t:
        # ensure proximity
        idx_p = t.find('physical')
        idx_a = t.find('activity')
        if abs(idx_p - idx_a) < 40:
            return True
    return False

df_docs['domain_physical_activity'] = df_docs['text'].apply(has_physical_activity)

# Filter for pub_year == 2016 and domain flag
df_filtered = df_docs[(df_docs['pub_year']==2016) & (df_docs['domain_physical_activity']==True)].copy()

# Prepare citations dataframe
df_cit = pd.DataFrame(citations)
# Normalize citation counts to int
if 'total_citations' in df_cit.columns:
    df_cit['total_citations'] = df_cit['total_citations'].astype(int)

# Merge on title
df_merged = pd.merge(df_filtered[['title','pub_year']], df_cit, on='title', how='left')

# Prepare result list of dicts with title and total_citations (int or None->0)
results = []
for _, row in df_merged.iterrows():
    tc = int(row['total_citations']) if pd.notna(row.get('total_citations')) else 0
    results.append({'title': row['title'], 'total_citations': tc})

# Print in required format as JSON string
import json as _json
print('__RESULT__:')
print(_json.dumps(results))"""

env_args = {'var_call_xDXDXv7O3Y8IsCnBirJ5usD6': ['paper_docs'], 'var_call_XXKoRyaVMde9ECUXLfDpTQ8d': ['Citations', 'sqlite_sequence'], 'var_call_UiXFAWxlyIWYkqSXdENiIgwM': 'file_storage/call_UiXFAWxlyIWYkqSXdENiIgwM.json', 'var_call_tAhYfbZ5ec3wGmZhugmAT3IR': 'file_storage/call_tAhYfbZ5ec3wGmZhugmAT3IR.json'}

exec(code, env_args)
