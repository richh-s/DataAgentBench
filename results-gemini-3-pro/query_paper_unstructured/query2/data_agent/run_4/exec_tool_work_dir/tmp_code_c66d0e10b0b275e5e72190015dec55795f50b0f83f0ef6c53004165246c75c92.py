code = """import json

# Paths
citations_path = locals()['var_function-call-14649324199470214251']
papers_path = locals()['var_function-call-5323787067724034665']

# Load citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers
paper_map = {}
try:
    with open(papers_path, 'r') as f:
        papers_data = json.load(f)
        for p in papers_data:
            paper_map[p['filename']] = p['text']
except Exception as e:
    print(f"Error loading papers: {e}")

acm_citation_counts = []

for cit in citations:
    title = cit['title']
    filename = title + ".txt"
    
    if filename in paper_map:
        text = paper_map[filename]
        # Robust check: ACM in the first 3000 chars
        header = text[:3000]
        if "ACM" in header:
            acm_citation_counts.append(int(cit['citation_count']))
    else:
        pass

if len(acm_citation_counts) > 0:
    avg = sum(acm_citation_counts) / len(acm_citation_counts)
    print("__RESULT__:")
    print(json.dumps(avg))
else:
    print("__RESULT__:")
    print(json.dumps(0))"""

env_args = {'var_function-call-14649324199470214251': 'file_storage/function-call-14649324199470214251.json', 'var_function-call-1435401735284119985': 'file_storage/function-call-1435401735284119985.json', 'var_function-call-14005966684331283554': 'file_storage/function-call-14005966684331283554.json', 'var_function-call-5323787067724034665': 'file_storage/function-call-5323787067724034665.json', 'var_function-call-14065168965893616449': 68.5}

exec(code, env_args)
