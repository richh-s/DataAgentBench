code = """import json
import os

# Load citations
citations_path = locals()['var_function-call-13908298438428433880']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a map for citations: title -> count
citation_map = {}
for item in citations_data:
    # citation_count might be string or int
    count = int(item['citation_count'])
    citation_map[item['title']] = count

# Load papers
papers_path = locals()['var_function-call-13272072186750426102']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

acm_citations = []

for p in papers_data:
    title = p['filename'].replace('.txt', '')
    
    # Check if paper is in the citation list (cited in 2018)
    if title in citation_map:
        text_head = p['text'][:3000] # Check first 3000 chars for header info
        
        # Check for ACM source
        # "Copyright ... ACM" is a strong signal. 
        # "Permission to make ... ACM" 
        # "Association for Computing Machinery"
        # The prompt says "Common sources ... include: ACM".
        # Based on the sample, "ACM" appears in copyright notice.
        # We'll use a simple check first.
        is_acm = "ACM" in text_head
        
        # To be safer, look for specific phrases if "ACM" is too generic?
        # But "ACM" in the header of an academic paper is almost certainly the publisher/venue.
        # Let's double check if IEEE papers might mention ACM (e.g. in references in the first page?).
        # Unlikely to have references in the first 3000 chars unless it's a very short paper.
        # However, "ACM Classification Keywords" is unique to ACM.
        # "Copyright ... ACM" is unique.
        
        if is_acm:
            acm_citations.append(citation_map[title])

if not acm_citations:
    print("__RESULT__:")
    print(json.dumps("No ACM papers found or no citations."))
else:
    avg_citations = sum(acm_citations) / len(acm_citations)
    print("__RESULT__:")
    print(json.dumps(avg_citations))"""

env_args = {'var_function-call-13908298438428433880': 'file_storage/function-call-13908298438428433880.json', 'var_function-call-13908298438428430929': 'file_storage/function-call-13908298438428430929.json', 'var_function-call-17064019482965131703': 'file_storage/function-call-17064019482965131703.json', 'var_function-call-13272072186750426102': 'file_storage/function-call-13272072186750426102.json'}

exec(code, env_args)
