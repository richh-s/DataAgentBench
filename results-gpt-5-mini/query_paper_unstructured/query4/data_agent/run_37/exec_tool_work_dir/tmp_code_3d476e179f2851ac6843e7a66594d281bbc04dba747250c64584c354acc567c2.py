code = """import json, re
# Load MongoDB query result (large file path)
with open(var_call_a7lRT9qkRRvzCoLIoTWBvXFu, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
# Load citations aggregated totals
with open(var_call_I69hr4IoOVcu3F9cpYCfdYmn, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build citations dict: normalize title by stripping
cit_dict = {}
for rec in citations:
    t = rec.get('title','').strip()
    # total_citations may be string, convert to int if possible
    tc = rec.get('total_citations', 0)
    try:
        tc_int = int(tc)
    except:
        try:
            tc_int = int(float(tc))
        except:
            tc_int = 0
    cit_dict[t] = tc_int

results = []

for doc in paper_docs:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    if not filename:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # check domain mention
    if not re.search(r'physical\s*activity', text, flags=re.I):
        continue
    # attempt to find publication year near top of document
    head = text[:800]
    years = re.findall(r"\b(19|20)(\d{2})\b", head)
    year_found = None
    if years:
        # years is list of tuples like ('20','16') -> join
        for y in years:
            y_full = int(y[0]+y[1])
            if 1990 <= y_full <= 2025:
                year_found = y_full
                break
    else:
        # fallback: search anywhere for 2016
        if re.search(r"\b2016\b", text):
            year_found = 2016

    if year_found == 2016:
        total_citations = cit_dict.get(title)
        # try some normalization if not found: some titles in citations may have smart quotes or different punctuation
        if total_citations is None:
            # try to match ignoring punctuation and case
            def norm(s):
                return re.sub(r"[^A-Za-z0-9]", "", s).lower()
            ntitle = norm(title)
            found = False
            for k,v in cit_dict.items():
                if norm(k) == ntitle:
                    total_citations = v
                    found = True
                    break
            if not found:
                total_citations = 0
        results.append({"title": title, "total_citations": total_citations})

# Deduplicate results by title
seen = set()
unique_results = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        unique_results.append(r)

print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_z44fGCrcdv8xi0cJHcIwkqeH': 'file_storage/call_z44fGCrcdv8xi0cJHcIwkqeH.json', 'var_call_9MgAY2bXiWE3HmFw3vDrjYJp': [], 'var_call_a7lRT9qkRRvzCoLIoTWBvXFu': 'file_storage/call_a7lRT9qkRRvzCoLIoTWBvXFu.json', 'var_call_I69hr4IoOVcu3F9cpYCfdYmn': 'file_storage/call_I69hr4IoOVcu3F9cpYCfdYmn.json'}

exec(code, env_args)
