code = """import json, re, pandas as pd

# Load the full results from the stored JSON file paths
with open(var_call_iCUHDVbiSw0006lfDawFS6sX, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_AweFdR2rSs65N5Jw4r1U7H0h, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citation mapping
cit_map = {}
for rec in citations:
    title = rec.get('title')
    # Some titles may have surrounding whitespace
    if title is None:
        continue
    title_key = title.strip()
    # citation total might be string; convert to int if possible
    try:
        total = int(rec.get('total_citations'))
    except Exception:
        try:
            total = int(float(rec.get('total_citations')))
        except Exception:
            total = None
    cit_map[title_key] = total

results = []

# Helper to extract year
year_re = re.compile(r"\b(19|20)\d{2}\b")
for doc in papers:
    filename = doc.get('filename','')
    if not filename:
        continue
    title = filename.rstrip('.txt')
    text = doc.get('text','') or ''
    # search for year in the first 800 characters (header)
    header = text[:1200]
    years = year_re.findall(header)
    year = None
    # findall returns tuples because of group; instead use finditer
    it = year_re.finditer(header)
    for m in it:
        y = int(m.group(0))
        if 1990 <= y <= 2026:
            year = y
            break
    if year is None:
        # fallback: search entire text
        it = year_re.finditer(text)
        for m in it:
            y = int(m.group(0))
            if 1990 <= y <= 2026:
                year = y
                break
    # domain detection: check if 'physical activity' appears anywhere (case-insensitive)
    domain = None
    if 'physical activity' in text.lower():
        domain = 'physical activity'
    # also check keywords section for 'Physical Activity' case
    # If year==2016 and domain matches, collect
    if year == 2016 and domain == 'physical activity':
        total_citations = cit_map.get(title, 0)
        if total_citations is None:
            total_citations = 0
        results.append({'title': title, 'total_citations': total_citations})

# If no results found, we may need to try a looser match: titles where text contains 'physical activity' and year 2016
if not results:
    # try again scanning all docs for 'physical activity' and year 2016
    for doc in papers:
        filename = doc.get('filename','')
        if not filename:
            continue
        title = filename.rstrip('.txt')
        text = doc.get('text','') or ''
        header = text[:1200]
        year = None
        it = year_re.finditer(header)
        for m in it:
            y = int(m.group(0))
            if 1990 <= y <= 2026:
                year = y
                break
        if year is None:
            it = year_re.finditer(text)
            for m in it:
                y = int(m.group(0))
                if 1990 <= y <= 2026:
                    year = y
                    break
        if year == 2016 and 'physical activity' in text.lower():
            total_citations = cit_map.get(title, 0)
            if total_citations is None:
                total_citations = 0
            results.append({'title': title, 'total_citations': total_citations})

# Deduplicate results by title
seen = set()
uniq_results = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        uniq_results.append(r)

import json as _json
print("__RESULT__:")
print(_json.dumps(uniq_results))"""

env_args = {'var_call_iCUHDVbiSw0006lfDawFS6sX': 'file_storage/call_iCUHDVbiSw0006lfDawFS6sX.json', 'var_call_AweFdR2rSs65N5Jw4r1U7H0h': 'file_storage/call_AweFdR2rSs65N5Jw4r1U7H0h.json'}

exec(code, env_args)
