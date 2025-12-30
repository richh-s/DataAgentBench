code = """import re, json, pandas as pd

# Load full Mongo and citations results
with open(var_call_b6zfJjQMFU4boqYcL0wna5Je, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_8qqtPs7KItRmMaIapUJjoBJj, 'r') as f:
    citation_records = json.load(f)

# Heuristic to extract year from text (look for CHI 2018-style or standalone 20xx / 19xx near top)
def extract_year(text):
    head = text[:5000]
    # common ACM pattern e.g., CHI 2018, 2017, April 21–26, 2018
    m = re.search(r'(19|20)\d{2}', head)
    if m:
        year = int(m.group(0))
        if 1900 <= year <= 2100:
            return year
    return None

# Determine if paper has empirical contribution via simple keyword search around "study", "participants", etc.
empirical_keywords = [
    'we conducted a study', 'we conducted an experiment', 'we conducted interviews',
    'we interviewed', 'we conducted a survey', 'we surveyed', 'participants',
    'user study', 'field study', 'study design', 'randomized controlled trial',
    'randomised controlled trial', 'rct', 'qualitative study', 'quantitative study'
]

def is_empirical(text):
    ltxt = text.lower()
    return any(k in ltxt for k in empirical_keywords)

papers = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not is_empirical(text):
        continue
    papers.append({'title': title, 'year': year})

# Build citation dataframe
cit_df = pd.DataFrame(citation_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

paper_df = pd.DataFrame(papers)

if paper_df.empty:
    result = []
else:
    merged = paper_df.merge(cit_df, on='title', how='left')
    merged = merged[['title', 'total_citations']].fillna(0)
    merged['total_citations'] = merged['total_citations'].astype(int)
    result = merged.to_dict(orient='records')

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_b6zfJjQMFU4boqYcL0wna5Je': 'file_storage/call_b6zfJjQMFU4boqYcL0wna5Je.json', 'var_call_8qqtPs7KItRmMaIapUJjoBJj': 'file_storage/call_8qqtPs7KItRmMaIapUJjoBJj.json'}

exec(code, env_args)
