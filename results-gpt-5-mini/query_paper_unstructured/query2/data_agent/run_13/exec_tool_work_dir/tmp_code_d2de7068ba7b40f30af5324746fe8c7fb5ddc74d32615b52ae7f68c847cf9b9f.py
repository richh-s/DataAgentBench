code = """import json
import pandas as pd

# Load the large results from the stored JSON file paths provided by previous tool calls
with open(var_call_3lukTR5DXPkuZwOWpba1CV4x, 'r', encoding='utf-8') as f:
    citations = json.load(f)

with open(var_call_seXLQQfVzVLeI4mtT2TBYYBQ, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Create dataframes
df_cit = pd.DataFrame(citations)
df_pap = pd.DataFrame(papers)

# Normalize citation_count to numeric
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')
else:
    df_cit['citation_count'] = pd.NA

# Ensure titles are strings
df_cit['title'] = df_cit['title'].astype(str)

# Extract title from filename in papers (remove trailing .txt if present)
def filename_to_title(fn):
    if not isinstance(fn, str):
        return fn
    if fn.lower().endswith('.txt'):
        return fn[:-4]
    return fn

if 'filename' in df_pap.columns:
    df_pap['title'] = df_pap['filename'].apply(filename_to_title)
else:
    df_pap['title'] = None

# Merge citations (for 2018) with papers on title
merged = pd.merge(df_cit, df_pap, on='title', how='left')

# Identify ACM papers by searching for the word 'ACM' as a whole word in the text (case-insensitive)
merged['text'] = merged.get('text', pd.Series([None]*len(merged)))
merged['is_acm'] = merged['text'].fillna('').str.contains(r"\bacm\b", case=False, regex=True)

# Filter to ACM papers
acm_papers = merged[merged['is_acm'] == True].copy()

# Compute average citation_count for those ACM papers
# Exclude NaN citation counts
valid_counts = acm_papers['citation_count'].dropna().astype(float)

if len(valid_counts) == 0:
    result = {"average_citation_count": None, "num_acm_papers_in_2018_citations": 0}
else:
    avg = valid_counts.mean()
    # round to 4 decimal places for readability
    result = {"average_citation_count": round(float(avg), 4), "num_acm_papers_in_2018_citations": int(len(valid_counts))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3lukTR5DXPkuZwOWpba1CV4x': 'file_storage/call_3lukTR5DXPkuZwOWpba1CV4x.json', 'var_call_seXLQQfVzVLeI4mtT2TBYYBQ': 'file_storage/call_seXLQQfVzVLeI4mtT2TBYYBQ.json'}

exec(code, env_args)
