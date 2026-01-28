code = """import json
import pandas as pd
import re

# Load previous tool results from storage paths
citations_path = var_call_qlghjVs0sQlhCjm8wTqftdZ9
papers_path = var_call_9pNnhRX6y4RU1qSXaRGhEq9S

citations = pd.read_json(citations_path)
papers = pd.read_json(papers_path)

# Normalize and convert citation counts to int
citations['total_citations'] = citations['total_citations'].astype(int)

# Extract title from filename
papers['title'] = papers['filename'].str.replace(r'\.txt$', '', regex=True)

# Function to detect CHI venue in text
def is_chi(text):
    if not isinstance(text, str):
        return False
    patterns = [r"\bCHI\b", r"SIGCHI", r"Proceedings of the SIGCHI", r"ACM CHI"]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False

papers['is_chi'] = papers['text'].apply(is_chi)

# Merge citations with papers on title
merged = citations.merge(papers[['title','is_chi']], on='title', how='inner')
# Filter to CHI papers
chi_cited_2020 = merged[merged['is_chi'] == True].copy()
chi_cited_2020['total_citations'] = chi_cited_2020['total_citations'].astype(int)
chi_cited_2020 = chi_cited_2020.sort_values('total_citations', ascending=False)

# Prepare result
result = chi_cited_2020[['title','total_citations']].to_dict(orient='records')

# Print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qlghjVs0sQlhCjm8wTqftdZ9': 'file_storage/call_qlghjVs0sQlhCjm8wTqftdZ9.json', 'var_call_EjIl9KBepE0GJDg9EzYrlrDO': ['paper_docs'], 'var_call_9pNnhRX6y4RU1qSXaRGhEq9S': 'file_storage/call_9pNnhRX6y4RU1qSXaRGhEq9S.json'}

exec(code, env_args)
