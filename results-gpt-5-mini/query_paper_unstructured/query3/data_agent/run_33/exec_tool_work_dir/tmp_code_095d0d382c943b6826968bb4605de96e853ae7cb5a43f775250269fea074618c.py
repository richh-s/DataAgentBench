code = """import json, re

# Load data from storage-provided file paths
p1 = var_call_szo3DZnkacnfUUG0guney58x
p2 = var_call_odTaHe9vZWdxEq1yFvPxk0Xv

data1 = json.load(open(p1, 'r', encoding='utf-8'))
data2 = json.load(open(p2, 'r', encoding='utf-8'))

# Build citation lookup
cit = {}
for r in data2:
    t = r.get('title')
    tc = r.get('total_citations')
    try:
        tc_i = int(tc)
    except:
        try:
            tc_i = int(float(tc))
        except:
            tc_i = 0
    cit[t] = tc_i

results = []
for doc in data1:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    header = text[:800]
    year = None
    m = re.search(r"\b(20\d{2})\b", header)
    if m:
        year = int(m.group(1))
    else:
        m2 = re.search(r"'(\d{2})", header)
        if m2:
            yy = int(m2.group(1))
            if 0 <= yy <= 26:
                year = 2000 + yy
    if year is None:
        m = re.search(r"\b(20\d{2})\b", text)
        if m:
            year = int(m.group(1))
    if year is None:
        continue
    if year <= 2016:
        continue
    if 'empirical' in text.lower():
        tc = cit.get(title)
        if tc is None:
            # try exact case-insensitive match
            for k,v in cit.items():
                if k.strip().lower() == title.strip().lower():
                    tc = v
                    break
        if tc is None:
            # try substring match
            for k,v in cit.items():
                if title.strip().lower() in k.strip().lower() or k.strip().lower() in title.strip().lower():
                    tc = v
                    break
        if tc is None:
            tc = 0
        results.append({'title': title, 'total_citations': tc})

results_sorted = sorted(results, key=lambda x: x['title'])

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print(json.dumps(results_sorted))")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_szo3DZnkacnfUUG0guney58x': 'file_storage/call_szo3DZnkacnfUUG0guney58x.json', 'var_call_odTaHe9vZWdxEq1yFvPxk0Xv': 'file_storage/call_odTaHe9vZWdxEq1yFvPxk0Xv.json'}

exec(code, env_args)
