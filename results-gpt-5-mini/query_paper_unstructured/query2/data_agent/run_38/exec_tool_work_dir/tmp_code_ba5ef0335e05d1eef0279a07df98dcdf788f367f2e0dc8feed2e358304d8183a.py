code = """import json
# Load large results from storage files
with open(var_call_rphCXyuJ53uRipNFtIHu2uar, 'r') as f:
    paper_docs = json.load(f)
with open(var_call_su1FVtn0f1Qq4o6RLciXMWPy, 'r') as f:
    citations_2018 = json.load(f)

# Build set of titles for papers published by ACM
acm_titles = set()
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','') or ''
    text_lower = text.lower()
    # Heuristic: consider as ACM if 'acm' appears and there's also 'copyright' or 'permission to make' or 'acm classification' nearby
    if 'acm' in text_lower and ('copyright' in text_lower or 'permission to make' in text_lower or 'acm classification' in text_lower):
        acm_titles.add(title)

# Match citations to ACM titles and compute average
matched_counts = []
for rec in citations_2018:
    title = rec.get('title')
    cc = rec.get('citation_count')
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            continue
    if title in acm_titles:
        matched_counts.append(cc_int)

if len(matched_counts) == 0:
    result = {"average_citation_count": None, "num_papers": 0}
else:
    avg = sum(matched_counts)/len(matched_counts)
    # Round to 4 decimal places
    result = {"average_citation_count": round(avg,4), "num_papers": len(matched_counts)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rphCXyuJ53uRipNFtIHu2uar': 'file_storage/call_rphCXyuJ53uRipNFtIHu2uar.json', 'var_call_su1FVtn0f1Qq4o6RLciXMWPy': 'file_storage/call_su1FVtn0f1Qq4o6RLciXMWPy.json'}

exec(code, env_args)
