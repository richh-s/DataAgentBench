code = """import re, json, pandas as pd
from pathlib import Path

# Load full mongo results
mongo_path = Path(var_call_XQRvymkPYcgnAqwlgBRycBJ9)
with mongo_path.open() as f:
    mongo_records = json.load(f)

# Extract title (filename without .txt), year, and check domain
papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    # year: look for 2016 explicitly
    year_match = re.search(r"2016", text)
    if not year_match:
        continue
    # domain: look for 'physical activity' substring case-insensitive
    if re.search(r"physical activity", text, re.IGNORECASE) is None:
        continue
    filename = doc.get('filename', '') or ''
    title = re.sub(r"\.txt$", "", filename)
    papers.append({'title': title, 'year': 2016})

# Deduplicate titles
paper_df = pd.DataFrame(papers).drop_duplicates(subset=['title'])

# Load citations aggregate
cit_path = Path(var_call_7PG1DUTb8i8sD8tdR8EpSaBU)
with cit_path.open() as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = paper_df.merge(cit_df, on='title', how='left')

result = merged[['title', 'total_citations']].fillna(0).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_XQRvymkPYcgnAqwlgBRycBJ9': 'file_storage/call_XQRvymkPYcgnAqwlgBRycBJ9.json', 'var_call_7PG1DUTb8i8sD8tdR8EpSaBU': 'file_storage/call_7PG1DUTb8i8sD8tdR8EpSaBU.json'}

exec(code, env_args)
