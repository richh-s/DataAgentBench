code = """import json
import re

# Load citations
with open(locals()['var_function-call-10411215990845860402'], 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for quick lookup: title -> citation_count
# Also normalize citation_count to int
citations_map = {}
for c in citations_data:
    citations_map[c['title']] = int(c['citation_count'])

# Load papers from MongoDB regex result
with open(locals()['var_function-call-14195249221485692358'], 'r') as f:
    papers_data = json.load(f)

acm_citation_counts = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # Remove .txt
    
    # Check if this paper was cited in 2018
    if title in citations_map:
        text = paper.get('text', '')
        # strict check for ACM
        # Common patterns:
        # "Copyright ... ACM"
        # "Permission ... ACM"
        # "permissions@acm.org"
        # "ACM Classification Keywords"
        
        is_acm = False
        if "Copyright" in text and "ACM" in text:
            # Check proximity or just existence? 
            # Given the regex pre-filter, existence is likely enough, but let's be safe.
            # "Copyright 2015 © ACM"
            if re.search(r'Copyright.*ACM', text) or re.search(r'Permission.*ACM', text):
                is_acm = True
        elif "permissions@acm.org" in text:
            is_acm = True
        elif "ACM Classification Keywords" in text:
            is_acm = True
            
        if is_acm:
            acm_citation_counts.append(citations_map[title])

# Calculate average
if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-10411215990845860402': 'file_storage/function-call-10411215990845860402.json', 'var_function-call-10411215990845858223': 'file_storage/function-call-10411215990845858223.json', 'var_function-call-17822327619243240138': [{'count(*)': '158'}], 'var_function-call-17822327619243238473': 'file_storage/function-call-17822327619243238473.json', 'var_function-call-8942426573761665136': 'file_storage/function-call-8942426573761665136.json', 'var_function-call-14541227782143213915': 'file_storage/function-call-14541227782143213915.json', 'var_function-call-14195249221485692358': 'file_storage/function-call-14195249221485692358.json'}

exec(code, env_args)
