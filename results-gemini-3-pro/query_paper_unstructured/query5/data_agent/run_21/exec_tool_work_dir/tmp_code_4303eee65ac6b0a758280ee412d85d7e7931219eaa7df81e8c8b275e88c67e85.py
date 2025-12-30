code = """import json
import re

# Load citations
with open(locals()['var_function-call-12669116658095172213'], 'r') as f:
    citations_data = json.load(f)

# Map title -> citation_count
title_to_citations = {item['title']: item['citation_count'] for item in citations_data}

# Load papers
with open(locals()['var_function-call-14587470179612253185'], 'r') as f:
    papers_data = json.load(f)

print(f"Loaded {len(citations_data)} citation records and {len(papers_data)} papers.")

chi_citation_sum = 0
chi_papers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    if title in title_to_citations:
        text = paper.get('text', '')
        # Check for CHI in the first 5000 characters
        header_text = text[:5000]
        
        # Regex for CHI conference patterns
        # Matches: "CHI 2012", "CHI '12", "CHI '12", "CHI12", "Conference on Human Factors in Computing Systems"
        is_chi = False
        if re.search(r'\bCHI\s*\'?\d{2,4}\b', header_text, re.IGNORECASE):
            is_chi = True
        elif "Conference on Human Factors in Computing Systems" in header_text:
            is_chi = True
        elif "CHI Conference" in header_text:
            is_chi = True
        
        if is_chi:
            count = title_to_citations[title]
            chi_citation_sum += count
            chi_papers.append((title, count))

print(f"Found {len(chi_papers)} CHI papers.")
print(f"Total citations: {chi_citation_sum}")
print("__RESULT__:")
print(json.dumps(chi_citation_sum))"""

env_args = {'var_function-call-8178165909663735325': ['Citations', 'sqlite_sequence'], 'var_function-call-8178165909663733532': ['paper_docs'], 'var_function-call-12669116658095172213': 'file_storage/function-call-12669116658095172213.json', 'var_function-call-5093665862301701388': 'file_storage/function-call-5093665862301701388.json', 'var_function-call-8517320496163722169': 'file_storage/function-call-8517320496163722169.json', 'var_function-call-17402942825836254338': 188, 'var_function-call-2848340252119990655': 'file_storage/function-call-2848340252119990655.json', 'var_function-call-1958255929289842492': 5, 'var_function-call-14587470179612253185': 'file_storage/function-call-14587470179612253185.json'}

exec(code, env_args)
