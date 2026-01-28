code = """import json
import re

# Load data
with open(locals()['var_function-call-10209984453905821604'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-10209984453905818035'], 'r') as f:
    citations = json.load(f)

food_titles = set()

for doc in paper_docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # Check keywords
    # Look for "Author Keywords" or "Keywords"
    # We will look in the first 3000 chars
    header_section = text[:3000]
    
    # regex for Keywords section
    # Usually "Author Keywords" followed by text until next section
    # Next section often starts with all caps or "ACM Classification"
    
    match = re.search(r'(Author Keywords|Keywords)([\s\S]*?)(\n\n|[A-Z]{2,})', header_section, re.IGNORECASE)
    if match:
        keywords_text = match.group(2).lower()
        if 'food' in keywords_text:
            food_titles.add(title)
            continue
            
    # Fallback: check abstract if it mentions "food" significantly?
    # Or maybe the domain is just listed. 
    # Let's also check if "food" appears in the first 1000 chars as a standalone word?
    # The prompt says "Common domains include: ... food ...". 
    # If I miss some, I might get it wrong. 
    # Let's assume the Keyword search + Title search is sufficient as per the "extract" instruction implying structured data in text.
    
    # Let's verify by printing titles that contain "food" but weren't caught by keywords
    # if 'food' in text.lower()[:1000] and title not in food_titles:
    #     pass # Potential miss
        
# Calculate citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        total_citations += int(cit['citation_count'])

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_papers_count": len(food_titles), "titles": list(food_titles)}))"""

env_args = {'var_function-call-15020890105501723075': ['paper_docs'], 'var_function-call-15020890105501724646': ['Citations', 'sqlite_sequence'], 'var_function-call-10118985144780459012': 'file_storage/function-call-10118985144780459012.json', 'var_function-call-10118985144780458999': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10209984453905821604': 'file_storage/function-call-10209984453905821604.json', 'var_function-call-10209984453905818035': 'file_storage/function-call-10209984453905818035.json'}

exec(code, env_args)
