code = """import json
from statistics import mean

# Load the MongoDB paper_docs results (stored as a .json file path)
with open(var_call_ltyIBqRa1mvcgKUYP99C8rf2, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Load the Citations query results (stored as a .json file path)
with open(var_call_QutiidaqH2Z9b5n6IYgjpHHK, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a mapping from title (filename without .txt) to document text
title_to_text = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    title_to_text[title] = doc.get('text', '')

# For each citation in 2018, if the corresponding paper's text indicates publisher ACM, include its citation_count
matched_counts = []
matched_titles = []
for cit in citations:
    title = cit.get('title')
    if title in title_to_text:
        text = title_to_text[title] or ''
        if 'acm' in text.lower():
            # parse citation_count
            raw = cit.get('citation_count')
            try:
                count = int(raw)
            except Exception:
                try:
                    count = int(float(raw))
                except Exception:
                    # try extract digits
                    import re
                    m = re.search(r"(\d+)", str(raw))
                    count = int(m.group(1)) if m else None
            if count is not None:
                matched_counts.append(count)
                matched_titles.append(title)

if matched_counts:
    avg = sum(matched_counts)/len(matched_counts)
else:
    avg = None

output = {
    'average_citation_count': avg,
    'num_acm_papers_in_2018_citations': len(matched_counts)
}

import json as _json
print("__RESULT__:")
print(_json.dumps(output))"""

env_args = {'var_call_HFc4Z4C5pmBI2tRzQHJ19iVL': ['paper_docs'], 'var_call_ltyIBqRa1mvcgKUYP99C8rf2': 'file_storage/call_ltyIBqRa1mvcgKUYP99C8rf2.json', 'var_call_F4uFUuGZKQZNJQi6BDgP0Ncv': ['Citations', 'sqlite_sequence'], 'var_call_QutiidaqH2Z9b5n6IYgjpHHK': 'file_storage/call_QutiidaqH2Z9b5n6IYgjpHHK.json'}

exec(code, env_args)
