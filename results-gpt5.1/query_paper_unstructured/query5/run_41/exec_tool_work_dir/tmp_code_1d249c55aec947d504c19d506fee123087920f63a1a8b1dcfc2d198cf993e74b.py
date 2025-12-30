code = """import json, pandas as pd
from pathlib import Path

# Load citations data
citations = var_call_dPtw1bcNtNZeL209CQT980qM

# Load full paper docs from file
paper_docs_path = Path(var_call_MuflBYRtX8BKSGORzEGHLVnY)
with paper_docs_path.open() as f:
    paper_docs = json.load(f)

# Build mapping from title (filename without .txt) to venue by simple heuristic search in text
records = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if not filename:
        continue
    title = filename.replace('.txt','')
    upper_text = text.upper()
    venue = None
    for v in ['CHI', 'UBICOMP', 'CSCW', 'DIS', 'PERVASIVEHEALTH', 'WWW', 'IUI', 'OZCHI', 'TEI', 'AH']:
        if v in upper_text:
            venue = v
            break
    records.append({'title': title, 'venue': venue})

venue_df = pd.DataFrame(records)

cit_df = pd.DataFrame(citations)
# citation_count may be string; convert
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# Join on title
merged = cit_df.merge(venue_df, on='title', how='left')

# Filter to CHI venue
chi_cits = merged[merged['venue'] == 'CHI']

# Total citation counts for all CHI papers cited in 2020
result_val = int(chi_cits['citation_count'].sum())

out = json.dumps(result_val)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dPtw1bcNtNZeL209CQT980qM': 'file_storage/call_dPtw1bcNtNZeL209CQT980qM.json', 'var_call_MuflBYRtX8BKSGORzEGHLVnY': 'file_storage/call_MuflBYRtX8BKSGORzEGHLVnY.json'}

exec(code, env_args)
