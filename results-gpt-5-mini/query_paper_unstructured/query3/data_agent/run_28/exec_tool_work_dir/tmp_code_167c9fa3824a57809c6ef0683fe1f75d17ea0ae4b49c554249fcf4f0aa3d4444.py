code = """import json, re

# Load data from storage-provided file paths
papers = json.load(open(var_call_s4Y0c3KrmsdgEEjFDJJdS7vc, 'r'))
citations = json.load(open(var_call_qd8ghf56ina4oLgVSTtgHAEe, 'r'))

# Build citation lookup: normalize titles by stripping surrounding quotes and whitespace
def norm_title(t):
    if t is None:
        return ''
    t = t.strip()
    # strip matching leading and trailing quotes (single or double)
    if len(t) >= 2 and ((t[0] == '"' and t[-1] == '"') or (t[0] == "'" and t[-1] == "'")):
        t = t[1:-1].strip()
    return re.sub(r"\s+"," ", t).lower()

cit_map = {}
for c in citations:
    t = c.get('title')
    total = c.get('total_citations')
    # ensure int
    try:
        total_int = int(total)
    except:
        try:
            total_int = int(float(total))
        except:
            total_int = 0
    cit_map[norm_title(t)] = total_int

# Process papers
matches = []
for p in papers:
    filename = p.get('filename','')
    text = p.get('text','') or ''
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    # find publication year: first 4-digit year between 2000 and 2026 in the header area (first 400 chars preferred)
    head = text[:800]
    years = re.findall(r"\b(19|20)\d{2}\b", head)
    # re.findall with groups returns only group; instead find all 4-digit
    years_all = re.findall(r"\b(19|20)\d{2}\b", text[:800])
    years_all = re.findall(r"\b(19|20)\d{2}\b", head)
    # better: find all matches
    years_all = re.findall(r"\b(19|20)\d{2}\b", head)
    # Using a different approach to get full year strings
    years_all = re.findall(r"\b(?:19|20)\d{2}\b", head)
    pub_year = None
    for y in years_all:
        try:
            yi = int(y)
            if yi >= 1900 and yi <= 2026:
                pub_year = yi
                break
        except:
            continue
    # fallback: search whole text
    if pub_year is None:
        years_all = re.findall(r"\b(?:19|20)\d{2}\b", text)
        for y in years_all:
            yi = int(y)
            if yi >= 1900 and yi <= 2026:
                pub_year = yi
                break

    if pub_year is None:
        continue

    # check contribution: case-insensitive substring 'empirical'
    if 'empirical' in text.lower():
        if pub_year > 2016:
            # find citation total
            total = cit_map.get(norm_title(title), None)
            # attempt alternative title forms: sometimes citations have quotes or different punctuation
            if total is None:
                # try with surrounding double quotes
                total = cit_map.get(norm_title('"' + title + '"'), None)
            if total is None:
                # try with single quotes
                total = cit_map.get(norm_title("'" + title + "'"), None)
            if total is None:
                # try exact lower
                total = cit_map.get(title.lower(), 0)
            if total is None:
                total = 0
            matches.append({'title': title, 'total_citations': int(total), 'year': pub_year})

# Sort matches by title
matches = sorted(matches, key=lambda x: x['title'].lower())

# Build plain-text answer
if not matches:
    plain = 'No matching papers found.'
else:
    lines = []
    for m in matches:
        lines.append(f"{m['title']} - {m['total_citations']}")
    plain = '\n'.join(lines)

import json
print("__RESULT__:")
print(json.dumps(plain))"""

env_args = {'var_call_qd8ghf56ina4oLgVSTtgHAEe': 'file_storage/call_qd8ghf56ina4oLgVSTtgHAEe.json', 'var_call_y7ScKsSvVOgLH8cgVecmeKns': ['paper_docs'], 'var_call_s4Y0c3KrmsdgEEjFDJJdS7vc': 'file_storage/call_s4Y0c3KrmsdgEEjFDJJdS7vc.json'}

exec(code, env_args)
