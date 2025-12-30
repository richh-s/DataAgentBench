code = """import json
import re

# Load citations and papers
citations_path = locals()['var_function-call-2553281828849054275']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-17732932705077824943']
with open(papers_path, 'r') as f:
    papers = json.load(f)

papers_dict = {p['filename']: p['text'] for p in papers}

acm_citations_strict = []
acm_citations_loose = []

for c in citations:
    title = c['title']
    filename = title + ".txt"
    
    if filename in papers_dict:
        text = papers_dict[filename]
        
        # Loose check
        if "ACM" in text:
            acm_citations_loose.append(int(c['citation_count']))
            
        # Strict check
        # Check for copyright notice or permission or classification
        is_acm = False
        if "permissions@acm.org" in text:
            is_acm = True
        elif "ACM Classification Keywords" in text:
            is_acm = True
        elif re.search(r"Copyright.*ACM", text, re.IGNORECASE):
            is_acm = True
        elif re.search(r"©.*ACM", text):
            is_acm = True
            
        if is_acm:
            acm_citations_strict.append(int(c['citation_count']))

avg_loose = sum(acm_citations_loose)/len(acm_citations_loose) if acm_citations_loose else 0
avg_strict = sum(acm_citations_strict)/len(acm_citations_strict) if acm_citations_strict else 0

print(f"Loose count: {len(acm_citations_loose)}, Avg: {avg_loose}")
print(f"Strict count: {len(acm_citations_strict)}, Avg: {avg_strict}")

print("__RESULT__:")
print(json.dumps(avg_strict))"""

env_args = {'var_function-call-2553281828849054275': 'file_storage/function-call-2553281828849054275.json', 'var_function-call-11306034102406453313': 158, 'var_function-call-12620038734802007538': 'file_storage/function-call-12620038734802007538.json', 'var_function-call-6192357641571030232': 5, 'var_function-call-14030373234983643704': 'file_storage/function-call-14030373234983643704.json', 'var_function-call-17732932705077824943': 'file_storage/function-call-17732932705077824943.json', 'var_function-call-15397100873994922973': 59.36363636363637}

exec(code, env_args)
