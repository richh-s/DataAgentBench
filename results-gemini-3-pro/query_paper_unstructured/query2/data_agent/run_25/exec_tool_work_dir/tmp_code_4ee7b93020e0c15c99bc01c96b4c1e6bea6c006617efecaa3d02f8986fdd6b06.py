code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-7305204029616643362']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for item in citations_data:
    t = item['title'].strip()
    c = item['citation_count']
    if isinstance(c, str):
        c = int(c)
    citation_map[t] = c

# Load papers
papers_file = locals()['var_function-call-13904961243015074840']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

acm_citations = []

def is_acm(text):
    # Check for strong ACM indicators
    # "Copyright 20.. © ACM" or "Copyright ... ACM"
    if re.search(r"Copyright\s+(?:©|\(c\)|20\d\d)\s+ACM", text, re.IGNORECASE):
        return True
    if re.search(r"Copyright\s+.*ACM", text, re.IGNORECASE):
        # Slightly broader but safe if 'ACM' is near copyright
        return True
    if "permissions@acm.org" in text:
        return True
    if "ACM Classification Keywords" in text:
        return True
    # If "ACM" is in the first few lines? (Header often has "UbiComp '15... ACM...")
    # But references also have ACM.
    # Check for "Permission to make ... ACM"
    if "Permission to make digital or hard copies" in text and "ACM" in text:
        return True
    return False

# Count how many papers we found
found_papers_count = 0
acm_papers_count = 0

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    
    title = filename[:-4] # remove .txt
    text = paper.get('text', '')
    
    # Check if this paper was cited in 2018
    if title in citation_map:
        found_papers_count += 1
        if is_acm(text):
            acm_citations.append(citation_map[title])
            acm_papers_count += 1

if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps({
    "average_citations": avg_citations,
    "count_acm_papers": acm_papers_count,
    "total_matched_papers": found_papers_count,
    "total_citations_processed": len(citations_data),
    "total_docs": len(papers_data)
}))"""

env_args = {'var_function-call-7305204029616643362': 'file_storage/function-call-7305204029616643362.json', 'var_function-call-7305204029616640165': 'file_storage/function-call-7305204029616640165.json', 'var_function-call-1861457914652662446': 'file_storage/function-call-1861457914652662446.json', 'var_function-call-14956387571741996022': 'file_storage/function-call-14956387571741996022.json', 'var_function-call-10954416611530653513': {'average_citations': 68.5, 'count_acm_papers': 2, 'total_papers_checked': 5, 'debug_sample': [{'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50, 'is_acm': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 87, 'is_acm': True}]}, 'var_function-call-13904961243015074840': 'file_storage/function-call-13904961243015074840.json'}

exec(code, env_args)
