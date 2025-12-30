code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-9827945916294781673']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create a dictionary of title -> citation_count for year 2020
citation_map = {}
for rec in citations:
    # Convert citation_count to int
    try:
        count = int(rec['citation_count'])
    except:
        count = 0
    citation_map[rec['title']] = count

# Load papers
papers_path = locals()['var_function-call-15113855768220925357']
with open(papers_path, 'r') as f:
    papers = json.load(f)

total_citations = 0
chi_papers_count = 0

for paper in papers:
    title = paper.get('filename', '').replace('.txt', '')
    if title in citation_map:
        text = paper.get('text', '')
        header_text = text[:5000] 
        
        is_chi = False
        
        # Check for CHI venue
        if "Conference on Human Factors in Computing Systems" in header_text:
            is_chi = True
        elif re.search(r"\bCHI\s+'?\d{2,4}", header_text):
            is_chi = True
        elif "CHI Conference" in header_text:
            is_chi = True
        elif re.search(r"Proceedings of the .*CHI", header_text, re.IGNORECASE):
            is_chi = True
        # Specific check for CHI appearing in headers like "CHI 2019, May 4-9..."
        elif re.search(r"\bCHI\s+20\d{2}", header_text):
            is_chi = True
        
        # Check against "Chi" as part of a word (already handled by regex \b)
        
        if is_chi:
            total_citations += citation_map[title]
            chi_papers_count += 1

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "paper_count": chi_papers_count}))"""

env_args = {'var_function-call-9827945916294781673': 'file_storage/function-call-9827945916294781673.json', 'var_function-call-15113855768220925357': 'file_storage/function-call-15113855768220925357.json'}

exec(code, env_args)
