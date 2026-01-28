code = """import json, re, os
# Load variables from previous tool calls
# var_call_4i9iNrTQb04kPTTxpzCeJEll and var_call_lWcutxA6rZ7NIqKbTy4TfXBe are provided in storage
p_docs_var = var_call_4i9iNrTQb04kPTTxpzCeJEll
cit_var = var_call_lWcutxA6rZ7NIqKbTy4TfXBe

# Load JSON content if variables are file paths
if isinstance(p_docs_var, str) and p_docs_var.endswith('.json') and os.path.exists(p_docs_var):
    with open(p_docs_var, 'r', encoding='utf-8') as f:
        papers = json.load(f)
else:
    papers = p_docs_var

if isinstance(cit_var, str) and cit_var.endswith('.json') and os.path.exists(cit_var):
    with open(cit_var, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_var

# Build citation map
cit_map = {}
for c in citations:
    title = c.get('title')
    tc = c.get('total_citations')
    try:
        tc_int = int(tc)
    except Exception:
        try:
            tc_int = int(float(tc))
        except Exception:
            tc_int = None
    cit_map[title] = tc_int

results = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = doc.get('text','') or ''
    # Ensure contribution mentions 'empirical'
    if not re.search(r"\bempirical\b", text, re.IGNORECASE):
        continue
    # Find year (first 4-digit year between 1900 and 2099)
    years = re.findall(r"\b(?:19\d{2}|20\d{2})\b", text)
    year = None
    for y in years:
        try:
            yi = int(y)
            if yi >= 1900 and yi <= 2099:
                year = yi
                break
        except:
            continue
    if year is None:
        continue
    if year <= 2016:
        continue
    # Join with citation totals
    if title in cit_map and cit_map[title] is not None:
        results.append({"title": title, "total_citations": cit_map[title], "year": year})

# Sort results by total_citations descending
results.sort(key=lambda x: x['total_citations'] if x['total_citations'] is not None else 0, reverse=True)

# Prepare JSON-serializable output (remove year if not needed, but include)
out = results

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_rHBdx8o9E7ydtdCdLzUhwueG': ['paper_docs'], 'var_call_4i9iNrTQb04kPTTxpzCeJEll': 'file_storage/call_4i9iNrTQb04kPTTxpzCeJEll.json', 'var_call_lWcutxA6rZ7NIqKbTy4TfXBe': 'file_storage/call_lWcutxA6rZ7NIqKbTy4TfXBe.json'}

exec(code, env_args)
