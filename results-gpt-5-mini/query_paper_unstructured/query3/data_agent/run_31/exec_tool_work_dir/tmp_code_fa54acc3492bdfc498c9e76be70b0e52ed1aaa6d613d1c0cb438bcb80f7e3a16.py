code = """import json, re

# Load large results if they are file paths
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

papers = load_var(var_call_3mSpFF6qoRBZlFtIAupKikmz)
citations = load_var(var_call_CKIrJUzHQxE69MsihJviRv1R)

# Build citation map: normalized lower -> total_citations (int)
def normalize_title(t):
    if t is None:
        return ''
    s = t.strip()
    # remove surrounding quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1].strip()
    # collapse whitespace
    s = re.sub(r"\s+", " ", s)
    return s

cit_map = {}
for rec in citations:
    raw_title = rec.get('title')
    norm = normalize_title(raw_title).lower()
    try:
        total = int(rec.get('total_citations'))
    except Exception:
        try:
            total = int(float(rec.get('total_citations')))
        except Exception:
            total = 0
    # if duplicates, keep max
    if norm in cit_map:
        cit_map[norm] = max(cit_map[norm], total)
    else:
        cit_map[norm] = total

# Process papers to find empirical contributions after 2016
results = []
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    # derive title from filename
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    title = title.strip()
    text_lower = text.lower()
    # find year
    year = None
    years = re.findall(r"\b(?:19|20)\d{2}\b", text)
    if years:
        try:
            year = int(years[0])
        except:
            year = None
    else:
        # try pattern like '\'15' -> 2015
        m = re.search(r"'(?P<yy>\d{2})\b", text)
        if m:
            yy = int(m.group('yy'))
            year = 2000 + yy if yy <= 30 else 1900 + yy
    # determine empirical contribution
    is_empirical = 'empirical' in text_lower
    if year is not None and year > 2016 and is_empirical:
        # find matching citation total
        tnorm = normalize_title(title).lower()
        total = None
        if tnorm in cit_map:
            total = cit_map[tnorm]
        else:
            # fuzzy search
            for cit_title, cit_total in cit_map.items():
                if tnorm == cit_title or tnorm in cit_title or cit_title in tnorm:
                    total = cit_total
                    break
        if total is None:
            total = 0
        results.append({'title': title, 'total_citations': total, 'year': year})

# Sort results by total_citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Prepare JSON-serializable output (remove year or keep; include year may be helpful)
out = [{'title': r['title'], 'total_citations': r['total_citations'], 'year': r['year']} for r in results]

print("__RESULT__:")
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_gz1g6vEvnM5xZiRL7edRw0qJ': ['paper_docs'], 'var_call_3mSpFF6qoRBZlFtIAupKikmz': 'file_storage/call_3mSpFF6qoRBZlFtIAupKikmz.json', 'var_call_CKIrJUzHQxE69MsihJviRv1R': 'file_storage/call_CKIrJUzHQxE69MsihJviRv1R.json'}

exec(code, env_args)
