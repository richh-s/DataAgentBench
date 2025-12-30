code = """import json
import re

# Load data
with open(locals()['var_function-call-4534989108856043984'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-280795814972665149'], 'r') as f:
    citations = json.load(f)

# Identify target papers
target_papers = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    # Domain: "physical activity"
    if 'physical activity' not in text.lower():
        continue
        
    # Check year
    # We look for 2016 in the text.
    # To be safer, we look for 2016 in the first 2000 characters (header/intro) or near "Copyright" or "Permission".
    # Or just check if "2016" exists. If it's a 2016 paper, it almost certainly mentions 2016 in the header.
    # However, a 2015 paper might cite a 2016 paper (unlikely) or mention "expected in 2016".
    # But usually headers like "CHI 2016" or "UbiComp '16" are clear.
    # Let's search for "2016" in the first 3000 chars.
    
    header_text = text[:3000]
    # Regex for year in typical conference header or copyright
    # e.g. "CHI '16", "September ... 2016", "Copyright 2016"
    if '2016' in header_text:
        target_papers.append(title)
    else:
        # Fallback: check full text for specific patterns if strictly needed, 
        # but 2016 usually appears at the top.
        # Let's double check if 2016 appears later near "Copyright".
        # If not found in header, maybe check specifically for "Copyright 2016" anywhere?
        if "Copyright 2016" in text or "copyright 2016" in text.lower():
            target_papers.append(title)

# Calculate citations
results = []
for title in target_papers:
    total_citations = 0
    found = False
    for cit in citations:
        if cit['title'].strip() == title.strip():
            found = True
            try:
                total_citations += int(cit['citation_count'])
            except:
                pass
    
    # Only add if we found citations? The question asks "title and total citation count".
    # If a paper has no citations recorded, count is 0.
    # However, if it's in the DB but has 0 citations, fine. 
    # If it's not in the DB, maybe we should still list it with 0?
    # Usually "total citation count" implies we report what we know.
    results.append({"title": title, "citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8115990490355926110': 'file_storage/function-call-8115990490355926110.json', 'var_function-call-15132226113380290757': 'file_storage/function-call-15132226113380290757.json', 'var_function-call-4534989108856043984': 'file_storage/function-call-4534989108856043984.json', 'var_function-call-280795814972665149': 'file_storage/function-call-280795814972665149.json'}

exec(code, env_args)
