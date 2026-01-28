code = """import json
import pandas as pd

# Load paper_docs result from storage file
with open(var_call_dbnGPAejJfi6emdHPFVIrVEl, 'r') as f:
    papers = json.load(f)

# Build DataFrame
df_papers = pd.DataFrame(papers)
# Extract title from filename
df_papers['title'] = df_papers['filename'].apply(lambda x: x[:-4] if isinstance(x, str) and x.lower().endswith('.txt') else x)
# Lowercase text for searching
df_papers['text_lower'] = df_papers['text'].str.lower().fillna('')

# Filter for domain 'physical activity' in text and publication year 2016 in header (first 400 chars)
mask_domain = df_papers['text_lower'].str.contains('physical activity')
mask_year = df_papers['text_lower'].str[:400].str.contains('2016')

df_phys2016 = df_papers[mask_domain & mask_year].copy()

# Prepare list of titles
titles = df_phys2016['title'].tolist()

# Load citations data
with open(var_call_oTLc5PGaHycLxkZ4xylG4cpf, 'r') as f:
    citations = json.load(f)

df_cit = pd.DataFrame(citations)
# Ensure proper types
if not df_cit.empty:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
    df_cit['citation_year'] = pd.to_numeric(df_cit['citation_year'], errors='coerce').fillna(0).astype(int)

# Aggregate total citations per title
cit_sum = df_cit.groupby('title', as_index=False)['citation_count'].sum()

# For each title in titles, find total citations (0 if missing)
results = []
for t in titles:
    match = cit_sum[cit_sum['title'] == t]
    total = int(match['citation_count'].iloc[0]) if not match.empty else 0
    results.append({'title': t, 'total_citations': total})

# If no matches found, return empty list
output = results

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_OB18P4IG2jUJdEuuLfD91d56': ['paper_docs'], 'var_call_dbnGPAejJfi6emdHPFVIrVEl': 'file_storage/call_dbnGPAejJfi6emdHPFVIrVEl.json', 'var_call_VWJrrkxeCphR7Am11x7Q57Po': ['Citations', 'sqlite_sequence'], 'var_call_oTLc5PGaHycLxkZ4xylG4cpf': 'file_storage/call_oTLc5PGaHycLxkZ4xylG4cpf.json'}

exec(code, env_args)
