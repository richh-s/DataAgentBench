code = """import json, re
# Load the paper_docs query result
pd_path = var_call_PXFJFUAWbkatsTSRln5Fzxb6
with open(pd_path, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Load the citations aggregated result
cit_path = var_call_q3fRohL6dfYLUpdNcEng2Q3T
with open(cit_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a map of title -> total_citations (as int)
cit_map = {}
for rec in citations:
    title = rec.get('title')
    tc = rec.get('total_citations')
    try:
        tc_int = int(tc)
    except:
        try:
            tc_int = int(float(tc))
        except:
            tc_int = 0
    cit_map[title] = tc_int

# Find paper_docs that mention 'physical activity' and appear to be published in 2016
matches = []
for rec in paper_docs:
    text = rec.get('text','')
    if not re.search(r'physical activity', text, re.I):
        continue
    # heuristics for publication year 2016: look for standalone '2016' or venue with 2016
    if re.search(r'\b2016\b', text):
        filename = rec.get('filename','')
        title = filename[:-4] if filename.endswith('.txt') else filename
        matches.append(title)

# Deduplicate and sort
matches = sorted(list(dict.fromkeys(matches)))

# Prepare output list with citation counts
output = []
for t in matches:
    # Titles in citations DB may have differences in punctuation; try direct match, then case-insensitive
    if t in cit_map:
        tc = cit_map[t]
    else:
        # attempt case-insensitive match
        tc = 0
        for k,v in cit_map.items():
            if k.lower() == t.lower():
                tc = v
                break
    output.append({"title": t, "total_citations": tc})

# Print result in required format
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_8FYthHJvjhDSYs9BfJ0YBmBx': 'file_storage/call_8FYthHJvjhDSYs9BfJ0YBmBx.json', 'var_call_oOocD6aMAYGkkKk6tGFYyHgQ': [], 'var_call_PXFJFUAWbkatsTSRln5Fzxb6': 'file_storage/call_PXFJFUAWbkatsTSRln5Fzxb6.json', 'var_call_q3fRohL6dfYLUpdNcEng2Q3T': 'file_storage/call_q3fRohL6dfYLUpdNcEng2Q3T.json'}

exec(code, env_args)
