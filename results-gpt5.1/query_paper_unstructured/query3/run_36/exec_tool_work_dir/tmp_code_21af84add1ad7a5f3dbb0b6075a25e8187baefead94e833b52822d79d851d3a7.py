code = """import re, json, pandas as pd

paper_path = var_call_S0PTExgxghOnm3uoZgX1mD5E
cites_path = var_call_W8cOEzND1SanxVZ9MIkWkbzn

with open(paper_path, 'r') as f:
    paper_docs = json.load(f)
with open(cites_path, 'r') as f:
    citations = json.load(f)

year_pattern = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    years = re.findall(year_pattern, text)
    years_int = []
    for y in years:
        if isinstance(y, tuple):
            years_int.append(int(''.join(y)))
        else:
            years_int.append(int(y))
    return max(years_int) if years_int else None

records = []
for doc in paper_docs:
    text = doc.get('text', '') or ''
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not re.search(r"empirical", text, re.I):
        continue
    title = (doc.get('filename') or '').replace('.txt','')
    if not title:
        continue
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cites_df = pd.DataFrame(citations)

cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = papers_df.merge(cites_df, on='title', how='left')

result = merged[['title', 'total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S0PTExgxghOnm3uoZgX1mD5E': 'file_storage/call_S0PTExgxghOnm3uoZgX1mD5E.json', 'var_call_W8cOEzND1SanxVZ9MIkWkbzn': 'file_storage/call_W8cOEzND1SanxVZ9MIkWkbzn.json', 'var_call_SAYRfjpWGTl0eNagZVqFmlhb': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}]}

exec(code, env_args)
