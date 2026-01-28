code = """import json, re
# Load data from previous query_db calls stored as variables
# Variables: var_call_YLM54NRtEWUx8N4fylA9Ll6U and var_call_xVI5j7X8zkf9tJ86ha1vzS7q

def load_var(v):
    if isinstance(v, str):
        # it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

citations = load_var(var_call_YLM54NRtEWUx8N4fylA9Ll6U)
papers = load_var(var_call_xVI5j7X8zkf9tJ86ha1vzS7q)

# Build mapping from title (filename without .txt) to extracted metadata
title_to_meta = {}
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = doc.get('text', '')
    # extract year: find first 4-digit number between 1990 and 2026
    years = re.findall(r"(19|20)\d{2}", text)
    year = None
    # years regex gives '19' or '20' groups; instead find all full matches
    years_full = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    for y in years_full:
        yi = int(y)
        if 1900 <= yi <= 2026:
            year = yi
            break
    # extract source: look for 'ACM', 'IEEE', 'PubMed' (case-insensitive)
    src = None
    txt_lower = text.lower()
    if 'acm' in text or '© acm' in txt_lower or '\u00a9 acm' in txt_lower:
        src = 'ACM'
    elif 'ieee' in text:
        src = 'IEEE'
    elif 'pubmed' in txt_lower:
        src = 'PubMed'
    # store
    title_to_meta[title.strip()] = {'year': year, 'source': src}

# Now iterate over citations for 2018 (these are the ones we queried)
matched_counts = []
matched_titles = []
for rec in citations:
    title = rec.get('title', '').strip()
    # find matching paper
    meta = title_to_meta.get(title)
    if not meta:
        # sometimes title may have slight whitespace differences; try case-insensitive match
        meta = title_to_meta.get(title.strip())
        if not meta:
            # try other normalization: remove multiple spaces
            key = ' '.join(title.split())
            meta = title_to_meta.get(key)
    if meta and meta.get('source') == 'ACM':
        # parse citation_count
        cc = rec.get('citation_count')
        try:
            cc_int = int(str(cc))
            matched_counts.append(cc_int)
            matched_titles.append(title)
        except:
            continue

count = len(matched_counts)
avg = None
if count > 0:
    avg = sum(matched_counts) / count
    # round to 3 decimal places
    avg = round(avg, 3)

result = {'average_citation_count': avg, 'paper_count': count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YLM54NRtEWUx8N4fylA9Ll6U': 'file_storage/call_YLM54NRtEWUx8N4fylA9Ll6U.json', 'var_call_xVI5j7X8zkf9tJ86ha1vzS7q': 'file_storage/call_xVI5j7X8zkf9tJ86ha1vzS7q.json'}

exec(code, env_args)
