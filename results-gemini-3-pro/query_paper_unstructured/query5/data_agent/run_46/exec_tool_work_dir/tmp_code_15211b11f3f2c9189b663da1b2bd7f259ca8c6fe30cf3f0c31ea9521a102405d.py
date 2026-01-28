code = """import json
import os

# Load citations
citations_path = locals()['var_function-call-7904474651748754030']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load paper docs
papers_path = locals()['var_function-call-17007904567241461401']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Identify CHI papers
chi_papers = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for CHI in the header (first 500 chars)
    header = text[:500]
    
    # The venue is usually "CHI"
    # Looking at the example: "UBICOMP '15, SEPTEMBER..."
    # CHI papers likely start with "CHI 'YY" or "CHI 20YY" or have "Proceedings of the ... CHI ..."
    # Or just "CHI" in the top block.
    # To be robust, let's look for "CHI" as a whole word in the header.
    # Or "Conference on Human Factors in Computing Systems"
    
    is_chi = False
    if "CHI" in header or "Conference on Human Factors in Computing Systems" in header:
        # Simple check might have false positives (e.g. "CHINA", "ARCHIVE"). 
        # But usually headers are quite distinct.
        # Let's refine: "CHI '" or "CHI 20" or "CHI 19" or "CHI 20"
        # The example has "UBICOMP '15".
        # Let's look for "CHI '" or "CHI 20" or "CHI 1" (for years 10-19)
        # Also just "CHI" followed by year or comma or newline.
        
        # Let's normalize header to check for CHI
        import re
        # Regex for CHI followed by year pattern or just appearing as a standalone token in likely header
        # Pattern: CHI 'YY or CHI 20YY or CHI 19YY. 
        # Also "Proceedings of ... CHI"
        if re.search(r'\bCHI\b', header): 
            is_chi = True
            
    if is_chi:
        chi_papers.append(title)

# Filter citations
total_citations = 0
chi_paper_set = set(chi_papers)

relevant_citations = []
for c in citations:
    if c['title'] in chi_paper_set:
        count = int(c['citation_count'])
        total_citations += count
        relevant_citations.append(c)

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-7904474651748754030': 'file_storage/function-call-7904474651748754030.json', 'var_function-call-7904474651748757041': ['paper_docs'], 'var_function-call-17007904567241461401': 'file_storage/function-call-17007904567241461401.json'}

exec(code, env_args)
