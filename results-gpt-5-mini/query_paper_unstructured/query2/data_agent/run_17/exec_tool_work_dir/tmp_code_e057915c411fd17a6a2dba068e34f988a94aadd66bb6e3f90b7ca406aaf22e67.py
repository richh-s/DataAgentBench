code = """import json
import math

# Load the query results from storage variables
# var_call_FKNInrG0ECMlrRlBy5EaW8z5 and var_call_cJZFkIvROBu9E2j2Ld47Qqch are provided by the tool storage

# Helper to load possibly-large results stored as a JSON file path

def load_var(v):
    if isinstance(v, str):
        # assume it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_FKNInrG0ECMlrRlBy5EaW8z5)
paper_docs = load_var(var_call_cJZFkIvROBu9E2j2Ld47Qqch)

# Build set of titles from paper_docs filenames (remove .txt extension)
paper_titles = set()
for d in paper_docs:
    fn = d.get('filename') or d.get('file') or ''
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    paper_titles.add(title)

# Filter citations for titles in paper_titles and compute average citation_count
match_count = 0
citation_sum = 0
matched_records = []
for rec in citations:
    title = rec.get('title')
    ccount = rec.get('citation_count')
    # convert citation_count to int if possible
    try:
        c = int(ccount)
    except Exception:
        # skip non-numeric
        continue
    if title in paper_titles:
        match_count += 1
        citation_sum += c
        matched_records.append({'title': title, 'citation_count': c})

if match_count > 0:
    average = citation_sum / match_count
    # round to 4 decimals
    average = round(average, 4)
else:
    average = None

result = {
    'average_citation_count_acm_papers_cited_in_2018': average,
    'matching_paper_count': match_count,
    'total_citation_sum': citation_sum
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FKNInrG0ECMlrRlBy5EaW8z5': 'file_storage/call_FKNInrG0ECMlrRlBy5EaW8z5.json', 'var_call_cJZFkIvROBu9E2j2Ld47Qqch': 'file_storage/call_cJZFkIvROBu9E2j2Ld47Qqch.json'}

exec(code, env_args)
