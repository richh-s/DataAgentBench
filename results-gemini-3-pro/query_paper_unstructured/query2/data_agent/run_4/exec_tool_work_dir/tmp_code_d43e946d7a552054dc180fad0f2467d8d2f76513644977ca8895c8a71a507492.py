code = """import json

# Paths
citations_path = locals()['var_function-call-14649324199470214251'] # Citations with counts
papers_path = locals()['var_function-call-5323787067724034665'] # Papers dump

# Load citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers
# Using a dictionary for faster lookup: filename -> text
paper_map = {}
try:
    with open(papers_path, 'r') as f:
        papers_data = json.load(f)
        for p in papers_data:
            paper_map[p['filename']] = p['text']
except Exception as e:
    print(f"Error loading papers: {e}")

# Process
acm_citation_counts = []
missing_papers = 0

for cit in citations:
    title = cit['title']
    filename = title + ".txt"
    
    if filename in paper_map:
        text = paper_map[filename]
        # Check for ACM. 
        # Hints say "Common sources... include: 'ACM'".
        # I'll check for "ACM" string. 
        # To be safe, I'll check if it appears in the first 2000 characters (header) or last 2000 (footer/references) or just anywhere? 
        # The preview showed "Copyright 2015 ACM".
        # Let's check if "ACM" is in the text. 
        if "ACM" in text:
            acm_citation_counts.append(int(cit['citation_count']))
    else:
        missing_papers += 1

print(f"Total citations processed: {len(citations)}")
print(f"Papers found in Mongo: {len(citations) - missing_papers}")
print(f"ACM Papers found: {len(acm_citation_counts)}")

if len(acm_citation_counts) > 0:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
    print("__RESULT__:")
    print(json.dumps(avg_citations))
else:
    print("__RESULT__:")
    print(json.dumps(0))"""

env_args = {'var_function-call-14649324199470214251': 'file_storage/function-call-14649324199470214251.json', 'var_function-call-1435401735284119985': 'file_storage/function-call-1435401735284119985.json', 'var_function-call-14005966684331283554': 'file_storage/function-call-14005966684331283554.json', 'var_function-call-5323787067724034665': 'file_storage/function-call-5323787067724034665.json'}

exec(code, env_args)
