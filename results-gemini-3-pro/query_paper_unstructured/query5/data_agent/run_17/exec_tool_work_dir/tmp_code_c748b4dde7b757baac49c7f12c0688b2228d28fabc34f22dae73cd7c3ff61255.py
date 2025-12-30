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
debug_headers = []

for paper in papers:
    fname = paper.get('filename')
    if fname in citation_map:
        text = paper.get('text', '')
        header = text[:1000]
        
        # Check for CHI
        # Patterns: "CHI '15", "CHI 2015", "Proceedings of the ... CHI ...", "Conference on Human Factors..."
        # Using a broader check
        
        is_chi = False
        if "CHI" in header:
            # Validate if it's really CHI venue
            if "Conference on Human Factors in Computing Systems" in header:
                is_chi = True
            elif re.search(r"CHI\s*['\u2019]?\d{2}", header):
                 is_chi = True
            elif re.search(r"CHI\s*20\d{2}", header):
                 is_chi = True
            elif "CHI Conference" in header:
                 is_chi = True
        
        if is_chi:
            chi_papers.append((fname, citation_map[fname]))
        else:
            if len(debug_headers) < 5:
                debug_headers.append((fname, header[:200].replace('\n', ' ')))

print("Found CHI papers:", len(chi_papers))
for p in chi_papers:
    print(p)

print("Sample non-CHI headers:")
for h in debug_headers:
    print(h)

total = sum(c for _, c in chi_papers)
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16}

exec(code, env_args)
