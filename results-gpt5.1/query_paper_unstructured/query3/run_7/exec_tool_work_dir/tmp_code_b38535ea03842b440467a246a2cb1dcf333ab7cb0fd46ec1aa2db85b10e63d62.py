code = """import re, json
import pandas as pd

# Load full Mongo result
path = var_call_AOr0c5mpgw70eRNQe74zo8by
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Load SQL aggregation result
sql_records = var_call_CUvfUDUJxN5sHaGFsgk9VbsL

# Extract year from text
empirical_papers = []
for doc in mongo_records:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    # require 'contribution' info: look for 'contribution' and 'empirical' near each other or explicit phrase
    if re.search(r'empirical', text, re.I):
        # heuristic year: first 4-digit year between 1990-2025
        years = re.findall(r'(19\d{2}|20\d{2})', text)
        pub_year = None
        for y in years:
            y_int = int(y)
            if 1990 <= y_int <= 2025:
                pub_year = y_int
                break
        if pub_year and pub_year > 2016:
            title = re.sub(r'\.txt$', '', filename)
            empirical_papers.append({'title': title, 'year': pub_year})

emp_df = pd.DataFrame(empirical_papers).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(sql_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, left_on='title', right_on='title', how='left')

result = merged[['title', 'total_citations']].fillna(0).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_AOr0c5mpgw70eRNQe74zo8by': 'file_storage/call_AOr0c5mpgw70eRNQe74zo8by.json', 'var_call_CUvfUDUJxN5sHaGFsgk9VbsL': 'file_storage/call_CUvfUDUJxN5sHaGFsgk9VbsL.json'}

exec(code, env_args)
