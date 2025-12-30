code = """import json
import re

# Load citations
with open(locals()['var_function-call-4239113770536719479'], 'r') as f:
    citations = json.load(f)

# Load paper docs
with open(locals()['var_function-call-2195288999403441372'], 'r') as f:
    papers = json.load(f)

paper_map = {p['filename']: p['text'] for p in papers}

missed_headers = []
count = 0

for citation in citations:
    title = citation['title']
    filename = title + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        header = text[:500]
        
        # Re-run detection to filter out the one we found
        is_chi = False
        if re.search(r'Human Factors in Computing Systems', header, re.IGNORECASE):
            is_chi = True
        elif re.search(r'\bCHI\b', header):
             is_chi = True
             
        if not is_chi:
            missed_headers.append(f"Title: {title}\nHeader: {header}\n")
            count += 1
            if count >= 5:
                break

print("__RESULT__:")
print(json.dumps(missed_headers))"""

env_args = {'var_function-call-4239113770536719479': 'file_storage/function-call-4239113770536719479.json', 'var_function-call-5140237096160835583': 'file_storage/function-call-5140237096160835583.json', 'var_function-call-13183044506038404940': 'file_storage/function-call-13183044506038404940.json', 'var_function-call-17837509656361549464': 'file_storage/function-call-17837509656361549464.json', 'var_function-call-11481915050006868588': {'total_citations': 0, 'missing_count': 184}, 'var_function-call-2195288999403441372': 'file_storage/function-call-2195288999403441372.json', 'var_function-call-8471152419459222340': {'total_citations': 16, 'chi_papers_count': 1}}

exec(code, env_args)
