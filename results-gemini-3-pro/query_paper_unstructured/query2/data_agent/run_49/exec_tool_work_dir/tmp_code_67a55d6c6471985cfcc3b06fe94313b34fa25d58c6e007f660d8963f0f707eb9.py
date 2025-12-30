code = """import json

# Load citations
with open(locals()['var_function-call-2409786745775470204'], 'r') as f:
    citations = json.load(f)

# Load papers
# The file from the second query_db call (the accidental 'find all')
with open(locals()['var_function-call-13418569887635270290'], 'r') as f:
    papers = json.load(f)

print(f"Total citations loaded: {len(citations)}")
print(f"Total papers loaded: {len(papers)}")

# Check if we have enough coverage
citation_titles = set(c['title'] for c in citations)
paper_titles = set(p['filename'].replace('.txt', '') for p in papers)

intersection = citation_titles.intersection(paper_titles)
print(f"Number of matched papers: {len(intersection)}")

# Check if we need to fetch more papers.
# If len(papers) is, say, 100, and intersection is small, maybe we missed some.
# But if len(papers) is large (e.g. 1000), likely we have most.

# Also, let's implement the logic to calculate the answer if we have enough data.
# Identification logic for ACM:
# Search for "ACM" in the first 3000 chars of text.

acm_citations = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    if title in citation_titles:
        text_start = p['text'][:5000] # Check first 5000 chars
        # Simple heuristic: look for ACM in copyright or publisher context
        # "Copyright ... ACM"
        # "Association for Computing Machinery"
        # "© ACM"
        # "ACM" might be enough if we are careful. 
        # Let's check for "ACM" and manually verify a few in the output if possible, 
        # or stick to a safer heuristic.
        is_acm = "ACM" in text_start or "Association for Computing Machinery" in text_start
        
        if is_acm:
            # Find the citation count
            # Citations list might have duplicates if multiple years, but here we filtered by year=2018
            # The citations list is [{'title': '...', 'citation_count': '...', ...}]
            # We need to find the specific record.
            
            # Optimization: Create a map for citations
            pass

# Let's just print the counts for now to verify.
print("__RESULT__:")
print(json.dumps({"citations_count": len(citations), "papers_count": len(papers), "matched_count": len(intersection)}))"""

env_args = {'var_function-call-2409786745775470204': 'file_storage/function-call-2409786745775470204.json', 'var_function-call-12345480976137177995': 'file_storage/function-call-12345480976137177995.json', 'var_function-call-13418569887635270290': 'file_storage/function-call-13418569887635270290.json'}

exec(code, env_args)
