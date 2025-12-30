code = """import re, json, pandas as pd

with open(var_call_uLJTeZlWKZHjQvuNomf3W3Tj, 'r') as f:
    papers = json.load(f)

year_pattern = re.compile(r'\b(20[0-2][0-9])\b')

records = []
for doc in papers:
    text = doc.get('text', '')
    # Heuristic: look for a contributions section listing 'empirical'
    if 'empirical' not in text.lower():
        continue
    years = [int(y) for y in year_pattern.findall(text)]
    year = min(years) if years else None
    if year is None or year <= 2016:
        continue
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_uLJTeZlWKZHjQvuNomf3W3Tj': 'file_storage/call_uLJTeZlWKZHjQvuNomf3W3Tj.json', 'var_call_YQ0mViRvzGEZnCPDnLPVtPTJ': 'file_storage/call_YQ0mViRvzGEZnCPDnLPVtPTJ.json', 'var_call_GWsKSRemnbtjYoacLgJwe6K0': {'papers_sample': [], 'citation_cols': ['title', 'total_citations'], 'cites_sample': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'total_citations': '313'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '390'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'total_citations': '368'}, {'title': 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'total_citations': '277'}]}}

exec(code, env_args)
