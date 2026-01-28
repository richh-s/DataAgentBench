code = """import json
import re

citations_data_path = locals()['var_function-call-1858146419099260835']
with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for item in citations_data:
    try:
        count = int(item['citation_count'])
    except ValueError:
        count = 0
    citation_map[item['title'] + ".txt"] = count

papers_path = locals()['var_function-call-9448533248759791427']
with open(papers_path, 'r') as f:
    papers = json.load(f)

chi_papers = []
debug_info = []

for paper in papers:
    fname = paper.get('filename')
    if fname in citation_map:
        text = paper.get('text', '')
        header = text[:500]
        
        is_chi = False
        if re.search(r"\bCHI\s*['\u2019]?\s*\d{2,4}\b", header): 
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif "CHI Conference" in header:
            is_chi = True
        
        if is_chi:
            chi_papers.append((fname, citation_map[fname]))
        
        # Collect some debug info on non-matching papers to see what their headers look like
        if len(debug_info) < 10:
             debug_info.append({"fname": fname, "header_snippet": header.replace("\n", " ")})

print(f"CHI papers found: {len(chi_papers)}")
print(f"CHI papers details: {chi_papers}")
print("Sample headers from processed papers:")
for d in debug_info:
    print(d)

total = sum(c for _, c in chi_papers)
print(f"Total: {total}")

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16}

exec(code, env_args)
