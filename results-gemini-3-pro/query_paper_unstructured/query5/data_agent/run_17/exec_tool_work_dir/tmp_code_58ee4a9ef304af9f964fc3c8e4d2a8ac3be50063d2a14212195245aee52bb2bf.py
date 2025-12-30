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
        # Only check the first 500 chars to avoid false positives later in text
        header = text[:500] 
        
        is_chi = False
        # Match "CHI 20xx", "CHI 'xx", "CHI'xx", "CHI 'xx"
        # Using dot `.` to match potential apostrophe or space
        if re.search(r"CHI\s*.?\d{2}", header): 
            # Check context to ensure it's the venue, not just a reference
            # Usually venue appears at the start, or in "Proceedings of..."
            # For this exercise, assuming header presence is strong indicator
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        
        if is_chi:
            chi_papers.append((fname, citation_map[fname]))
        else:
            if len(debug_headers) < 3:
                # Store sample header
                debug_headers.append(header[:100].replace('\n', ' '))

print("Matches:", len(chi_papers))
for p in chi_papers:
    print(p)

print("Non-matches sample:")
for h in debug_headers:
    print(h)

total = sum(c for _, c in chi_papers)
print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json', 'var_function-call-4705747550331622406': 16}

exec(code, env_args)
