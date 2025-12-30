code = """import re, json
import pandas as pd

with open(var_call_KnqHJJ9V657Bwgo93MPhPsCQ, 'r') as f:
    mongo_records = json.load(f)

papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    filename = doc.get('filename', '') or ''
    if not filename:
        continue
    title = filename.replace('.txt', '')

    m = re.search(r'(19|20)\d{2}', text[:1500])
    year = int(m.group(0)) if m else None

    is_empirical = False
    if re.search(r'\bempirical\b', text, re.I):
        is_empirical = True
    else:
        if re.search(r'\b(participants?|interviews?|survey|study|studies|experiment|fieldwork|ethnograph|trial)\b', text, re.I):
            is_empirical = True

    if year and year > 2016 and is_empirical:
        papers.append({'title': title, 'year': year})

with open(var_call_ljjyHD8mSS5ZOtYJgynOZbj8, 'r') as f:
    citation_records = json.load(f)

cit_df = pd.DataFrame(citation_records)

cit_df['title_clean'] = cit_df['title'].str.replace('"', '', regex=False)

papers_df = pd.DataFrame(papers)

merged = papers_df.merge(cit_df, left_on='title', right_on='title_clean', how='left')

result = merged[['title', 'year', 'total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KnqHJJ9V657Bwgo93MPhPsCQ': 'file_storage/call_KnqHJJ9V657Bwgo93MPhPsCQ.json', 'var_call_ljjyHD8mSS5ZOtYJgynOZbj8': 'file_storage/call_ljjyHD8mSS5ZOtYJgynOZbj8.json', 'var_call_UbgQ5PLo7vO1fKKU1cd3NlHv': {'cols': ['title', 'total_citations'], 'sample': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}]}}

exec(code, env_args)
