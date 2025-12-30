code = """import re, json
import pandas as pd

# Load full Mongo results
with open(var_call_KnqHJJ9V657Bwgo93MPhPsCQ, 'r') as f:
    mongo_records = json.load(f)

# Extract title and publication year, and check empirical contribution heuristically
papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    filename = doc.get('filename', '') or ''
    title = filename.replace('.txt', '')

    # Year: look for CHI-style year near venue pattern or 20xx in header
    m = re.search(r'CHI\s*(20\d{2})', text[:5000])
    if not m:
        m = re.search(r'(20\d{2})', text[:1000])
    year = int(m.group(1)) if m else None

    # Contribution: mark empirical if word appears near methods/participants phrases
    is_empirical = False
    if re.search(r'\bempirical\b', text, re.I):
        is_empirical = True
    else:
        # heuristic: presence of participants/sample/interview/study etc.
        if re.search(r'\b(participants?|interviews?|survey|study|studies|experiment|fieldwork|ethnograph|trial)\b', text, re.I):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        papers.append({'title': title, 'year': year})

# Load citations
with open(var_call_ljjyHD8mSS5ZOtYJgynOZbj8, 'r') as f:
    citation_records = json.load(f)

cit_df = pd.DataFrame(citation_records)
# Normalize columns
cit_df['title_clean'] = cit_df['title'].str.replace('"', '', regex=False)

papers_df = pd.DataFrame(papers)

# Join on title
merged = papers_df.merge(cit_df, left_on='title', right_on='title_clean', how='left')

result = merged[['title', 'year', 'total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KnqHJJ9V657Bwgo93MPhPsCQ': 'file_storage/call_KnqHJJ9V657Bwgo93MPhPsCQ.json', 'var_call_ljjyHD8mSS5ZOtYJgynOZbj8': 'file_storage/call_ljjyHD8mSS5ZOtYJgynOZbj8.json'}

exec(code, env_args)
