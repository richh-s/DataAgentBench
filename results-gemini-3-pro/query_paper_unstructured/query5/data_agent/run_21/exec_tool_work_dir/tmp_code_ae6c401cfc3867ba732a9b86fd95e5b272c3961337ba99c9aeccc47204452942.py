code = """import json
import re

# Load citations
with open(locals()['var_function-call-12669116658095172213'], 'r') as f:
    citations_data = json.load(f)

title_to_citations = {}
for item in citations_data:
    try:
        title_to_citations[item['title']] = int(item['citation_count'])
    except:
        continue

# Load papers
with open(locals()['var_function-call-14587470179612253185'], 'r') as f:
    papers_data = json.load(f)

chi_citation_sum = 0
found_count = 0

for paper in papers_data:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    if title in title_to_citations:
        text = paper.get('text', '')
        # check first 5000 chars
        head = text[:5000]
        
        # Check for CHI
        # CHI followed by year (2 or 4 digits), optional apostrophe
        if re.search(r"CHI\s*['’]?\d{2,4}", head, re.IGNORECASE) or \
           "Conference on Human Factors in Computing Systems" in head:
            
            chi_citation_sum += title_to_citations[title]
            found_count += 1

print(f"Found {found_count} CHI papers.")
print(f"Total citations: {chi_citation_sum}")
print("__RESULT__:")
print(json.dumps(chi_citation_sum))"""

env_args = {'var_function-call-8178165909663735325': ['Citations', 'sqlite_sequence'], 'var_function-call-8178165909663733532': ['paper_docs'], 'var_function-call-12669116658095172213': 'file_storage/function-call-12669116658095172213.json', 'var_function-call-5093665862301701388': 'file_storage/function-call-5093665862301701388.json', 'var_function-call-8517320496163722169': 'file_storage/function-call-8517320496163722169.json', 'var_function-call-17402942825836254338': 188, 'var_function-call-2848340252119990655': 'file_storage/function-call-2848340252119990655.json', 'var_function-call-1958255929289842492': 5, 'var_function-call-14587470179612253185': 'file_storage/function-call-14587470179612253185.json'}

exec(code, env_args)
