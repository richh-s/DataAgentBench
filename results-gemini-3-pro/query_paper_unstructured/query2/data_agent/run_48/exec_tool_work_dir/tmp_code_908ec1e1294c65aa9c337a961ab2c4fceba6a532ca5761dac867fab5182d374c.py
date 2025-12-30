code = """import json

# Load citations
citations_path = locals()['var_function-call-2553281828849054275']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers
papers_path = locals()['var_function-call-17732932705077824943']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Create a dictionary for quick lookup of paper text by filename
# Note: citation title matches filename without .txt
papers_dict = {p['filename']: p['text'] for p in papers}

acm_citations = []
missing_papers = 0

for c in citations:
    title = c['title']
    filename = title + ".txt"
    
    if filename in papers_dict:
        text = papers_dict[filename]
        # Check for ACM publisher
        # Common indicators: "ACM", "Association for Computing Machinery"
        # Often appearing in copyright notices or headers/footers
        if "ACM" in text or "Association for Computing Machinery" in text:
            acm_citations.append(int(c['citation_count']))
    else:
        missing_papers += 1

if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
else:
    avg_citation = 0

print(f"Total citations processed: {len(citations)}")
print(f"Papers found in MongoDB: {len(citations) - missing_papers}")
print(f"ACM papers found: {len(acm_citations)}")
print(f"Average citation count: {avg_citation}")

print("__RESULT__:")
print(json.dumps(avg_citation))"""

env_args = {'var_function-call-2553281828849054275': 'file_storage/function-call-2553281828849054275.json', 'var_function-call-11306034102406453313': 158, 'var_function-call-12620038734802007538': 'file_storage/function-call-12620038734802007538.json', 'var_function-call-6192357641571030232': 5, 'var_function-call-14030373234983643704': 'file_storage/function-call-14030373234983643704.json', 'var_function-call-17732932705077824943': 'file_storage/function-call-17732932705077824943.json'}

exec(code, env_args)
