code = """import json
import re

# Load citations
with open(locals()['var_function-call-389901141376174398'], 'r') as f:
    citations_data = json.load(f)
citation_map = {item['title']: int(item['total_citations']) for item in citations_data}

# Load papers
with open(locals()['var_function-call-389901141376172653'], 'r') as f:
    papers_data = json.load(f)

print("Debug Info:")
for i, paper in enumerate(papers_data[:5]):
    filename = paper.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    
    match = re.search(r'20\d{2}', text[:1000])
    year = int(match.group(0)) if match else 0
    
    has_empirical = 'empirical' in text.lower()
    in_citations = title in citation_map
    
    print(f"Paper {i}: Title='{title}'")
    print(f"  Year found: {year}")
    print(f"  Has 'empirical': {has_empirical}")
    print(f"  In citation map: {in_citations}")
    print(f"  Snippet: {text[:200].replace(chr(10), ' ')}")
    print("-" * 20)

print("__RESULT__:")
print("[]")"""

env_args = {'var_function-call-11261961701334828073': ['paper_docs'], 'var_function-call-11261961701334829364': 'file_storage/function-call-11261961701334829364.json', 'var_function-call-11261961701334830655': ['Citations', 'sqlite_sequence'], 'var_function-call-11261961701334827850': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-8802837961524065341': 'file_storage/function-call-8802837961524065341.json', 'var_function-call-389901141376174398': 'file_storage/function-call-389901141376174398.json', 'var_function-call-389901141376172653': 'file_storage/function-call-389901141376172653.json', 'var_function-call-8584235094798493494': []}

exec(code, env_args)
