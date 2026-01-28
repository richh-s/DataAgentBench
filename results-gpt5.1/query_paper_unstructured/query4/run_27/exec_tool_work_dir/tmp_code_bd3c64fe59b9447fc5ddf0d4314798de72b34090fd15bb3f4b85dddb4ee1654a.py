code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo results
file_path = Path(var_call_NXMOHSVqm5ZoaMYRx3HwbIeQ)
with open(file_path, 'r') as f:
    mongo_records = json.load(f)

# Extract title (from filename), year, and domain relevance from text
papers = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = filename.replace('.txt', '')
    # Heuristic: extract 4-digit years between 2000-2025, take the earliest as publication year
    years = sorted({int(y) for y in re.findall(r'\b(20[0-2][0-9]|19[9-9][0-9])\b', text)})
    pub_year = years[0] if years else None
    # domain match for physical activity (substring, case-insensitive)
    if re.search(r'physical activity', text, re.IGNORECASE):
        papers.append({'title': title, 'year': pub_year})

# Filter to 2016
papers_2016 = [p for p in papers if p['year'] == 2016]

# Load citations results
file_path2 = Path(var_call_qvGEa7SRtYRBHSYe3VlVDTre)
with open(file_path2, 'r') as f2:
    citations_records = json.load(f2)

cit_df = pd.DataFrame(citations_records)
# Normalize types
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on exact title
p_df = pd.DataFrame(papers_2016)
if not p_df.empty:
    merged = p_df.merge(cit_df, left_on='title', right_on='title', how='left')
    result = merged[['title', 'total_citations']].fillna(0)
    result_list = []
    for _, row in result.iterrows():
        result_list.append({'title': row['title'], 'total_citations': int(row['total_citations'])})
else:
    result_list = []

out = json.dumps(result_list)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NXMOHSVqm5ZoaMYRx3HwbIeQ': 'file_storage/call_NXMOHSVqm5ZoaMYRx3HwbIeQ.json', 'var_call_qvGEa7SRtYRBHSYe3VlVDTre': 'file_storage/call_qvGEa7SRtYRBHSYe3VlVDTre.json'}

exec(code, env_args)
