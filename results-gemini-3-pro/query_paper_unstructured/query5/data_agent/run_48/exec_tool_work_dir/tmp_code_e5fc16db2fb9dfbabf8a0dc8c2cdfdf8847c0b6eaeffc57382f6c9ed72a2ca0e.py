code = """import json
import re

# Load citations
with open(locals()['var_function-call-264858034059979045'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_function-call-8351315325764085192'], 'r') as f:
    papers_list = json.load(f)

paper_map = {p['filename']: p['text'] for p in papers_list}

total_citations = 0
chi_papers = []

for cite in citations:
    title = cite['title']
    filename = title + ".txt"
    text = paper_map.get(filename, "")
    
    if not text:
        continue
        
    # Increase header size
    header = text[:3000]
    
    is_chi = False
    
    # Check for CHI patterns
    # Match "CHI 20xx" or "CHI 'xx" or "CHI ' xx"
    if re.search(r"CHI\s+['’]?\s*\d{2,4}", header):
        is_chi = True
    elif "Conference on Human Factors in Computing Systems" in header:
        is_chi = True
        
    # Filters
    if re.search(r"OzCHI", header, re.IGNORECASE):
        is_chi = False
    if re.search(r"CHI Play", header, re.IGNORECASE):
        is_chi = False
    
    if is_chi:
        chi_papers.append(title)
        total_citations += int(cite['citation_count'])

print(f"Found {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
print(f"Sample CHI papers: {chi_papers[:5]}")

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "num_papers": len(chi_papers)}))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json', 'var_function-call-1959921926523090950': {'total_citations': 0, 'num_papers': 0}, 'var_function-call-8389437484024645991': 'Done', 'var_function-call-2898140987180465692': 'Done'}

exec(code, env_args)
