code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-7305204029616643362']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for citations: title -> citation_count
# Assuming titles are unique for year 2018. If not, I should handle it.
citation_map = {}
for item in citations_data:
    t = item['title'].strip()
    c = item['citation_count']
    # c might be string or int in JSON, ensure int
    if isinstance(c, str):
        c = int(c)
    
    if t in citation_map:
        # If duplicate exists, what to do? Usually citation data is unique per year per paper.
        # But if it happens, maybe sum it? Or it's an error?
        # Let's assume unique for now, or just overwrite (likely identical)
        pass
    citation_map[t] = c

# Load papers
papers_file = locals()['var_function-call-14956387571741996022']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

acm_citations = []
debug_info = []

def is_acm(text):
    # Check for strong ACM indicators
    # "Copyright 20.. © ACM"
    # "permissions@acm.org"
    # "ACM Classification Keywords"
    if "permissions@acm.org" in text:
        return True
    if "ACM Classification Keywords" in text:
        return True
    if re.search(r"Copyright\s+\d{4}\s+©\s+ACM", text, re.IGNORECASE):
        return True
    if re.search(r"©\s+ACM\s+\d{4}", text, re.IGNORECASE):
        return True
    return False

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    
    title = filename[:-4] # remove .txt
    text = paper.get('text', '')
    
    # Check if this paper was cited in 2018
    if title in citation_map:
        # Check if published by ACM
        if is_acm(text):
            acm_citations.append(citation_map[title])
            debug_info.append({"title": title, "count": citation_map[title], "is_acm": True})
        else:
            # Maybe check weak indicators?
            # "ACM" appears in text?
            if "ACM" in text:
                 # Potentially ACM but missed by regex?
                 # Let's not count it to avoid FPs (e.g. references to ACM)
                 pass

# Calculate average
if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps({
    "average_citations": avg_citations,
    "count_acm_papers": len(acm_citations),
    "total_papers_checked": len(papers_data),
    "debug_sample": debug_info[:5]
}))"""

env_args = {'var_function-call-7305204029616643362': 'file_storage/function-call-7305204029616643362.json', 'var_function-call-7305204029616640165': 'file_storage/function-call-7305204029616640165.json', 'var_function-call-1861457914652662446': 'file_storage/function-call-1861457914652662446.json', 'var_function-call-14956387571741996022': 'file_storage/function-call-14956387571741996022.json'}

exec(code, env_args)
