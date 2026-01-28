code = """import json
import re

# Load data from storage file paths
with open(var_call_e5JON5AGCqr2JbDrky5Sihl7, 'r') as f:
    papers = json.load(f)
with open(var_call_rYduxM8rVSUEQXIm9c8v98uf, 'r') as f:
    citations = json.load(f)

# Build citation map
cit_map = {}
for c in citations:
    title = c.get('title', '').strip()
    # Some citation counts may be strings; convert safely
    try:
        tc = int(c.get('total_citations'))
    except Exception:
        try:
            tc = int(str(c.get('total_citations')).replace(',', ''))
        except Exception:
            tc = None
    cit_map[title] = tc

results = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    lower = text.lower()
    # determine contribution by substring matching
    is_empirical = 'empiric' in lower
    if not is_empirical:
        continue
    # find publication year: look for 4-digit 20xx between 2000 and 2025
    years = re.findall(r'(20\d{2})', text)
    pub_year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2025:
            pub_year = yi
            break
    if pub_year is None:
        # try in filename
        m = re.search(r'(20\d{2})', filename)
        if m:
            pub_year = int(m.group(1))
    if pub_year is None:
        continue
    if pub_year > 2016:
        # find citation count by exact or case-insensitive match
        tc = cit_map.get(title)
        if tc is None:
            # try case-insensitive match
            for k, v in cit_map.items():
                if k and k.lower() == title.lower():
                    tc = v
                    break
        if tc is None:
            # try stripping quotes
            key = title.strip(' "')
            tc = cit_map.get(key)
        if tc is None:
            tc = 0
        results.append({'title': title, 'total_citations': tc, 'year': pub_year})

# Sort results by title for consistency
results = sorted(results, key=lambda x: x['title'])

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_FmCFJsvD9LVEak5nCV1AvXMo': ['paper_docs'], 'var_call_e5JON5AGCqr2JbDrky5Sihl7': 'file_storage/call_e5JON5AGCqr2JbDrky5Sihl7.json', 'var_call_c0hwsQCx7NACXiwPZOO2Tea5': ['Citations', 'sqlite_sequence'], 'var_call_rYduxM8rVSUEQXIm9c8v98uf': 'file_storage/call_rYduxM8rVSUEQXIm9c8v98uf.json'}

exec(code, env_args)
