code = """import json, re
papers = json.load(open(var_call_s4Y0c3KrmsdgEEjFDJJdS7vc, 'r'))
citations = json.load(open(var_call_qd8ghf56ina4oLgVSTtgHAEe, 'r'))

def norm_title(t):
    if not t:
        return ''
    s = str(t).strip()
    if len(s) >= 2 and s[0] in ('"', "'") and s[-1] == s[0]:
        s = s[1:-1].strip()
    s = re.sub(r'\s+', ' ', s)
    return s.lower()

cit_map = {}
for c in citations:
    t = c.get('title')
    total = c.get('total_citations', 0)
    try:
        total_int = int(total)
    except:
        try:
            total_int = int(float(total))
        except:
            total_int = 0
    cit_map[norm_title(t)] = total_int

results = []
for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '') or ''
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    # find first 4-digit year
    m = re.search(r"\b(?:19|20)\d{2}\b", text[:800])
    pub_year = None
    if m:
        try:
            pub_year = int(m.group(0))
        except:
            pub_year = None
    if pub_year is None:
        m = re.search(r"\b(?:19|20)\d{2}\b", text)
        if m:
            try:
                pub_year = int(m.group(0))
            except:
                pub_year = None
    if pub_year is None:
        continue
    if 'empirical' in text.lower() and pub_year > 2016:
        key = norm_title(title)
        total = cit_map.get(key)
        if total is None:
            total = cit_map.get(title.lower(), 0)
        if total is None:
            total = 0
        results.append({"title": title, "total_citations": int(total), "year": pub_year})

# sort by title
results = sorted(results, key=lambda x: x['title'].lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_qd8ghf56ina4oLgVSTtgHAEe': 'file_storage/call_qd8ghf56ina4oLgVSTtgHAEe.json', 'var_call_y7ScKsSvVOgLH8cgVecmeKns': ['paper_docs'], 'var_call_s4Y0c3KrmsdgEEjFDJJdS7vc': 'file_storage/call_s4Y0c3KrmsdgEEjFDJJdS7vc.json'}

exec(code, env_args)
