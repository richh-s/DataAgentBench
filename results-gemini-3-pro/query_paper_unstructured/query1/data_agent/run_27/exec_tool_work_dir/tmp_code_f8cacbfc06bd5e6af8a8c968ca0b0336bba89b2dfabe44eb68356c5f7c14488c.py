code = """import json
import re

# Load papers
try:
    with open('var_function-call-16923378931810091090.json', 'r') as f:
        papers = json.load(f)
except Exception as e:
    print(json.dumps({"error": f"Failed to load papers: {str(e)}"}))
    papers = []

# Load citations
try:
    with open('var_function-call-10009206756418749160.json', 'r') as f:
        citations = json.load(f)
except Exception as e:
    print(json.dumps({"error": f"Failed to load citations: {str(e)}"}))
    citations = []

food_papers = []

# Debug: Print all keywords found to see if I am missing something
debug_keywords = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # Check Keywords section
    # Regex: Look for "Keywords" or "Author Keywords", followed by content, until a section header
    # Section headers are usually uppercase or follow a pattern.
    # I'll try to capture up to 500 chars after "Keywords"
    
    match = re.search(r'(?:Author\s+)?Keywords[:\s](.{0,500})', text, re.IGNORECASE | re.DOTALL)
    keywords_text = ""
    if match:
        # split by newline to stop at next paragraph or section?
        # usually keywords are one block. 
        # let's assume they might be until double newline or "INTRODUCTION"
        raw_kws = match.group(1)
        # cut off at "INTRODUCTION" or "ABSTRACT" or "ACM Classification"
        end_idx = len(raw_kws)
        for stop in ["INTRODUCTION", "ABSTRACT", "ACM Classification", "\n\n\n"]:
            idx = raw_kws.upper().find(stop)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        keywords_text = raw_kws[:end_idx].strip().lower()
        
    debug_keywords.append({"title": title, "kws": keywords_text})
    
    is_food = False
    if 'food' in keywords_text:
        is_food = True
    elif 'food' in title.lower():
        is_food = True
    
    if is_food:
        food_papers.append(title)

# Calculate citations
total_citations = 0
citation_details = {}
for c in citations:
    if c['title'] in food_papers:
        cnt = int(c['citation_count'])
        total_citations += cnt
        if c['title'] not in citation_details:
            citation_details[c['title']] = 0
        citation_details[c['title']] += cnt

print("__RESULT__:")
print(json.dumps({
    "food_papers": food_papers,
    "total_citations": total_citations,
    "debug_keywords": debug_keywords[:5], # Show first 5 to check
    "citation_details": citation_details
}))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}, 'var_function-call-4486819615144744261': 'file_storage/function-call-4486819615144744261.json', 'var_function-call-16923378931810091090': 'file_storage/function-call-16923378931810091090.json', 'var_function-call-10009206756418749160': 'file_storage/function-call-10009206756418749160.json'}

exec(code, env_args)
