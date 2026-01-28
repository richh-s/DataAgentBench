code = """import json
import re

# Load citations data (with counts)
citations_data_path = locals()['var_function-call-1858146419099260835']
with open(citations_data_path, 'r') as f:
    citations_data = json.load(f)

# Map filename -> count (convert to int)
citation_map = {}
for item in citations_data:
    try:
        count = int(item['citation_count'])
    except ValueError:
        count = 0
    citation_map[item['title'] + ".txt"] = count

# Load paper docs
papers_path = locals()['var_function-call-9448533248759791427']
with open(papers_path, 'r') as f:
    papers = json.load(f)

total_citations = 0
chi_papers = []

for paper in papers:
    fname = paper.get('filename')
    if fname in citation_map:
        text = paper.get('text', '')
        header = text[:2000]
        
        # Enhanced CHI detection
        is_chi = False
        # Matches CHI '15, CHI '99, CHI 2015, CHI 2020
        # Case sensitive "CHI" to avoid false positives in lower case text
        if re.search(r"\bCHI\s*['\u2019]?\s*\d{2,4}\b", header): 
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif "CHI Conference" in header:
            is_chi = True
        # Fallback: Check if "CHI" is alone on a line or with specific location info
        # e.g. "CHI 2013, April 27–May 2, 2013, Paris, France"
        elif re.search(r"\bCHI\b.*(?:April|May|June|July|August|September|October|November|December)", header):
            is_chi = True
            
        if is_chi:
            count = citation_map[fname]
            total_citations += count
            chi_papers.append(fname)

print(f"Found {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
# print(f"CHI papers: {chi_papers}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-1858146419099260835': 'file_storage/function-call-1858146419099260835.json', 'var_function-call-15380122331926952136': 'file_storage/function-call-15380122331926952136.json', 'var_function-call-9448533248759791427': 'file_storage/function-call-9448533248759791427.json'}

exec(code, env_args)
