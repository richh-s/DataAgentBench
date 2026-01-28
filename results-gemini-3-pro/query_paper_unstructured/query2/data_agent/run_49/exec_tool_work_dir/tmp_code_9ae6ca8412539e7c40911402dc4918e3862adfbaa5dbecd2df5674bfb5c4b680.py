code = """import json

# Load citations (from SQLite query result)
# Key: var_function-call-2409786745775470204
try:
    with open(locals()['var_function-call-2409786745775470204'], 'r') as f:
        citations = json.load(f)
except:
    # If the key is not available (e.g. lost context), we might be in trouble. 
    # But usually it persists.
    citations = []

# Load papers (from MongoDB query result)
# Key: var_function-call-6014529169566715250
try:
    with open(locals()['var_function-call-6014529169566715250'], 'r') as f:
        papers = json.load(f)
except:
    papers = []

# Create a map of title -> paper_text
paper_map = {p['filename'].replace('.txt', ''): p['text'] for p in papers}

acm_citation_counts = []

for c in citations:
    title = c['title']
    if title in paper_map:
        text = paper_map[title]
        # Check for ACM source
        # Heuristic: Check first 3000 chars for specific ACM patterns
        header = text[:5000]
        
        is_acm = False
        if "ACM" in header:
            if "Copyright" in header and "ACM" in header:
                is_acm = True
            elif "Permission" in header and "ACM" in header:
                is_acm = True
            elif "Association for Computing Machinery" in header:
                is_acm = True
            elif "ACM Classification Keywords" in header:
                is_acm = True
            elif "ISBN" in header and "ACM" in header:
                is_acm = True
        
        if is_acm:
            try:
                count = int(c['citation_count'])
                acm_citation_counts.append(count)
            except ValueError:
                pass

if acm_citation_counts:
    avg_citation = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg_citation = 0

print(f"Found {len(acm_citation_counts)} ACM papers.")
print(f"Average citation count: {avg_citation}")

print("__RESULT__:")
print(json.dumps(avg_citation))"""

env_args = {'var_function-call-2409786745775470204': 'file_storage/function-call-2409786745775470204.json', 'var_function-call-12345480976137177995': 'file_storage/function-call-12345480976137177995.json', 'var_function-call-13418569887635270290': 'file_storage/function-call-13418569887635270290.json', 'var_function-call-6164372942284620757': {'citations_count': 158, 'papers_count': 5, 'matched_count': 2}, 'var_function-call-1092466089989068117': 'file_storage/function-call-1092466089989068117.json', 'var_function-call-6014529169566715250': 'file_storage/function-call-6014529169566715250.json'}

exec(code, env_args)
