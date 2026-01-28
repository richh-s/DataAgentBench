code = """import json
import re

# Load citations
with open(locals()['var_function-call-4239113770536719479'], 'r') as f:
    citations = json.load(f)

# Load paper docs
with open(locals()['var_function-call-2195288999403441372'], 'r') as f:
    papers = json.load(f)

# Create a map of filename -> text
paper_map = {p['filename']: p['text'] for p in papers}

total_citations = 0
chi_papers = []

for citation in citations:
    title = citation['title']
    filename = title + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        # Check venue in the header (first 2000 chars)
        header = text[:2000]
        
        # Check for CHI venue
        # CHI usually appears as "CHI 'XX" or "CHI 20XX" or "Conference on Human Factors in Computing Systems"
        # Using regex to find "CHI" as a whole word
        is_chi = False
        if re.search(r'\bCHI\b', header):
            is_chi = True
        elif "Human Factors in Computing Systems" in header:
            is_chi = True
        
        if is_chi:
            total_citations += citation['citation_count']
            chi_papers.append(title)
            
print(f"Found {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_papers_count": len(chi_papers)}))"""

env_args = {'var_function-call-4239113770536719479': 'file_storage/function-call-4239113770536719479.json', 'var_function-call-5140237096160835583': 'file_storage/function-call-5140237096160835583.json', 'var_function-call-13183044506038404940': 'file_storage/function-call-13183044506038404940.json', 'var_function-call-17837509656361549464': 'file_storage/function-call-17837509656361549464.json', 'var_function-call-11481915050006868588': {'total_citations': 0, 'missing_count': 184}, 'var_function-call-2195288999403441372': 'file_storage/function-call-2195288999403441372.json'}

exec(code, env_args)
