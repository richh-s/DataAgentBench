code = """import json
import re

# Load citations data
path_citations = locals().get('var_function-call-7498192109235549923')
with open(path_citations, 'r') as f:
    citations_data = json.load(f)

# Create a map: title -> citation_count
citation_map = {c['title']: int(c['citation_count']) for c in citations_data}
cited_titles = set(citation_map.keys())

# Load paper docs
path_docs = locals().get('var_function-call-7995451070674360072')
with open(path_docs, 'r') as f:
    docs = json.load(f)

print(f"Total docs loaded: {len(docs)}")

chi_citations = 0
chi_papers = []

for doc in docs:
    fname = doc['filename']
    title = fname.replace('.txt', '')
    
    if title in cited_titles:
        text = doc['text']
        header = text[:1000] # Check first 1000 chars
        
        # Check for CHI venue
        is_chi = False
        
        # Regex patterns for CHI venue
        # 1. "CHI 'XX" or "CHI 20XX"
        if re.search(r"CHI\s+'?\d{2,4}", header):
            is_chi = True
        # 2. "Conference on Human Factors in Computing Systems"
        elif "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        # 3. "CHI Conference"
        elif "CHI Conference" in header:
            is_chi = True
        # 4. Strict "CHI" followed by date/location line often found in ACM headers
        # e.g. "CHI 2011, May 7-12, 2011, Vancouver, BC, Canada"
        elif re.search(r"CHI\s+\d{4}\s*,", header):
            is_chi = True
            
        if is_chi:
            chi_citations += citation_map[title]
            chi_papers.append(title)

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"Sample CHI papers: {chi_papers[:5]}")
print(f"Total citation count: {chi_citations}")
print("__RESULT__:")
print(json.dumps(chi_citations))"""

env_args = {'var_function-call-7498192109235549923': 'file_storage/function-call-7498192109235549923.json', 'var_function-call-1495859486444725251': 'file_storage/function-call-1495859486444725251.json', 'var_function-call-6405304347776267640': 188, 'var_function-call-15965521281973898392': 'file_storage/function-call-15965521281973898392.json', 'var_function-call-6154840779900112772': 'file_storage/function-call-6154840779900112772.json', 'var_function-call-4693824508147823644': 'file_storage/function-call-4693824508147823644.json', 'var_function-call-9895404596539580614': 16, 'var_function-call-7995451070674360072': 'file_storage/function-call-7995451070674360072.json'}

exec(code, env_args)
