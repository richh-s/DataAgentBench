code = """import json
import re

# Load citations
citation_file = locals()['var_function-call-5680722423366516433']
with open(citation_file, 'r') as f:
    citations = json.load(f)

# Create map: title -> count
# Since the query was WHERE citation_year = 2020, all records are for 2020.
cited_papers = {}
for c in citations:
    # Handle potential duplicates if any (though usually unique per year per title)
    # But wait, citations table might have multiple entries? No, unique id.
    # We sum if multiple entries? Assuming one entry per paper per year.
    count = int(c['citation_count'])
    title = c['title']
    cited_papers[title] = count

# Load papers
paper_file = locals()['var_function-call-1166448778177815195']
with open(paper_file, 'r') as f:
    papers = json.load(f)

total_citations = 0
chi_papers = []
non_chi_matched = []

def is_chi(text):
    # Check first 2000 chars
    header = text[:2000]
    
    # Pattern 1: CHI 'YY or CHI 20YY
    # \bCHI matches "CHI" word boundary. 
    # \s* matches optional space.
    # ['\u2019]? matches optional apostrophe (standard or curly).
    # \s* matches optional space.
    # \d{2,4} matches year (15, 2015).
    if re.search(r"\bCHI\s*['\u2019]?\s*\d{2,4}\b", header, re.IGNORECASE):
        return True
        
    # Pattern 2: Full conference name
    if re.search(r"Conference on Human Factors in Computing Systems", header, re.IGNORECASE):
        return True
        
    return False

for p in papers:
    # Extract title from filename
    title = p['filename'].rsplit('.', 1)[0]
    
    if title in cited_papers:
        if is_chi(p['text']):
            total_citations += cited_papers[title]
            chi_papers.append(title)
        else:
            non_chi_matched.append(title)

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"First 5 CHI papers: {chi_papers[:5]}")
print(f"Skipped {len(non_chi_matched)} non-CHI papers.")
print(f"First 5 Skipped papers: {non_chi_matched[:5]}")
print(f"Total citations: {total_citations}")

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-5680722423366514432': ['Citations', 'sqlite_sequence'], 'var_function-call-5680722423366516433': 'file_storage/function-call-5680722423366516433.json', 'var_function-call-5680722423366514338': 'file_storage/function-call-5680722423366514338.json', 'var_function-call-1825670630710000632': 'file_storage/function-call-1825670630710000632.json', 'var_function-call-1380767849587936819': 188, 'var_function-call-5679032680150065306': 'file_storage/function-call-5679032680150065306.json', 'var_function-call-15107492987324530466': 'file_storage/function-call-15107492987324530466.json', 'var_function-call-1166448778177815195': 'file_storage/function-call-1166448778177815195.json'}

exec(code, env_args)
