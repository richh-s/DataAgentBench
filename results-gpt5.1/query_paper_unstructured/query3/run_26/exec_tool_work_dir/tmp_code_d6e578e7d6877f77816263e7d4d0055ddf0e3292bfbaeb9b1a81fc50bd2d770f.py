code = """import re, json, pandas as pd

# Load full Mongo and citations results
with open(var_call_uzjJKQEGOkxiNnYlwMAOuxIe, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_9cKZRhGI6XXizXbWJB5czsqU, 'r') as f:
    citations_records = json.load(f)

# Heuristic year extractor
year_regex = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    years = [int(y) for y in year_regex.findall(text)]
    if not years:
        return None
    # choose most recent year as publication year approximation
    return max(years)

papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    year = extract_year(text)
    if year and year > 2016:
        # crude contribution heuristic: require word 'empirical' in text
        if re.search(r'empirical', text, re.IGNORECASE):
            filename = doc.get('filename', '') or ''
            title = filename.rsplit('.txt', 1)[0]
            papers.append({'title': title, 'year': year})

# Build dataframe of empirical post-2016 titles
emp_df = pd.DataFrame(papers).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(citations_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, how='left', left_on='title', right_on='title')

result = merged[['title', 'total_citations']].sort_values('title').to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uzjJKQEGOkxiNnYlwMAOuxIe': 'file_storage/call_uzjJKQEGOkxiNnYlwMAOuxIe.json', 'var_call_9cKZRhGI6XXizXbWJB5czsqU': 'file_storage/call_9cKZRhGI6XXizXbWJB5czsqU.json'}

exec(code, env_args)
