code = """import json
import re
import pandas as pd

# Load the two stored results from the previous query_db calls
# var_call_SB2mS1sYxq5FJ9oU82So96qs and var_call_3ey4XApfW9pioL2TAv8w2ENR

data_path = var_call_SB2mS1sYxq5FJ9oU82So96qs
citations_path = var_call_3ey4XApfW9pioL2TAv8w2ENR

# If the variables are file paths (strings), load the JSON; otherwise assume they are lists
if isinstance(data_path, str):
    with open(data_path, 'r', encoding='utf-8') as f:
        papers = json.load(f)
else:
    papers = data_path

if isinstance(citations_path, str):
    with open(citations_path, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = citations_path

# Build DataFrame for citations and normalize
cit_df = pd.DataFrame(citations)
if 'total_citations' in cit_df.columns:
    cit_df['total_citations'] = cit_df['total_citations'].astype(int)
else:
    # If summed column named differently, attempt to find numeric column
    for col in cit_df.columns:
        if cit_df[col].dtype == object:
            try:
                cit_df[col] = cit_df[col].astype(int)
            except:
                pass

# Process papers: extract title from filename and year from text, filter empirical and year>2016
rows = []
for doc in papers:
    filename = doc.get('filename', '')
    if not filename:
        continue
    title = filename.rsplit('.txt', 1)[0]
    text = doc.get('text', '') or ''
    # Check for 'empirical' contribution (case-insensitive substring)
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        # Find all 4-digit years in the text
        years = re.findall(r"\b(20\d{2})\b", text)
        year_found = None
        if years:
            # Convert to ints and prefer the first occurrence that is >2016
            yrs_int = [int(y) for y in years]
            for y in yrs_int:
                if y > 2016:
                    year_found = y
                    break
            # if none >2016, leave as None
        if year_found and year_found > 2016:
            rows.append({'title': title, 'year': year_found})

papers_df = pd.DataFrame(rows)

# Join with citations on title
if not papers_df.empty:
    merged = papers_df.merge(cit_df, left_on='title', right_on='title', how='left')
else:
    merged = pd.DataFrame(columns=['title', 'year', 'total_citations'])

# Prepare results: title and total_citations (as int, 0 if missing)
results = []
for _, r in merged.iterrows():
    tc = r.get('total_citations')
    try:
        tc = int(tc) if not pd.isna(tc) else 0
    except:
        tc = 0
    results.append({'title': r['title'], 'total_citations': tc})

# Sort results by total_citations descending
results = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Print in required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_cssq7TM9Lb9mcDYNrJdXWaNx': ['paper_docs'], 'var_call_NoWVcXEf50YyN9gDZeLvFtuL': ['Citations', 'sqlite_sequence'], 'var_call_SB2mS1sYxq5FJ9oU82So96qs': 'file_storage/call_SB2mS1sYxq5FJ9oU82So96qs.json', 'var_call_3ey4XApfW9pioL2TAv8w2ENR': 'file_storage/call_3ey4XApfW9pioL2TAv8w2ENR.json'}

exec(code, env_args)
