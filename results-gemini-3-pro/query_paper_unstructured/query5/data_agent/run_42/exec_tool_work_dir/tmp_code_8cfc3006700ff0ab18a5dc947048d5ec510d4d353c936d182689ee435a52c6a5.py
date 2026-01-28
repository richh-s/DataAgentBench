code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-9827945916294781673']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create a dictionary of title -> citation_count for year 2020
citation_map = {}
for rec in citations:
    citation_map[rec['title']] = rec['citation_count']

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
        # Check for CHI venue
        # Heuristics:
        # 1. "CHI 'YY" or "CHI 20YY"
        # 2. "Conference on Human Factors in Computing Systems"
        # 3. "CHI Conference"
        # 4. In copyright notice "UbiComp" was "UbiComp '15". So "CHI '15"
        
        header_text = text[:3000] # Check first 3000 chars
        is_chi = False
        
        if "Conference on Human Factors in Computing Systems" in header_text:
            is_chi = True
        elif re.search(r"\bCHI\s+'?\d{2,4}", header_text):
            is_chi = True
        elif "CHI Conference" in header_text:
            is_chi = True
        elif re.search(r"Proceedings of the .*CHI", header_text, re.IGNORECASE):
            is_chi = True
        # Check specifically for the example "CHI 20xx" pattern often found
        elif re.search(r"CHI\s+20\d{2}", header_text):
            is_chi = True
            
        if is_chi:
            total_citations += citation_map[title]
            chi_papers_count += 1

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "paper_count": chi_papers_count}))"""

env_args = {'var_function-call-9827945916294781673': 'file_storage/function-call-9827945916294781673.json', 'var_function-call-15113855768220925357': 'file_storage/function-call-15113855768220925357.json'}

exec(code, env_args)
