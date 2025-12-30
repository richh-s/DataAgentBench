code = """import json
import re

# Load paper_docs
try:
    with open('var_function-call-1279721563085973081.json', 'r') as f:
        papers = json.load(f)
except FileNotFoundError:
    # If the file for the second call doesn't exist, maybe it was the first one?
    # But the first one was limit 1.
    # The previous turn said the result is stored in var_function-call-1279721563085973081.
    # I'll assume it exists.
    print("Error loading papers file")
    papers = []

# Load citations
try:
    with open('var_function-call-10463220630905116945.json', 'r') as f:
        citations = json.load(f)
except:
    print("Error loading citations file")
    citations = []

food_papers = []
debug_info = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # Try to find keywords
    # Pattern: Look for "Keywords" or "Author Keywords", take until next major section or double newline
    # Common next sections: "ACM Classification", "INTRODUCTION", "ABSTRACT" (if keywords are at end?) usually keywords are after abstract.
    
    # Simple strategy: Find "Keywords" and take the next 500 chars, check for "food"
    keywords_match = re.search(r'(?:Author\s+)?Keywords\s*[:\n](.*?)(?:ACM Classification|INTRODUCTION|ABSTRACT|\n\n\n)', text, re.IGNORECASE | re.DOTALL)
    
    is_food = False
    extracted_keywords = ""
    if keywords_match:
        extracted_keywords = keywords_match.group(1).lower()
        if 'food' in extracted_keywords:
            is_food = True
    
    # Fallback: check title
    if not is_food:
        if 'food' in title.lower():
            is_food = True
            
    # Fallback 2: If keywords section not found or empty, search for "food" in the first 2000 chars (abstract/intro) 
    # but be careful. 
    # Actually, if "food" is in the text, let's verify if it's a domain.
    # "Common domains include: 'food'". 
    # Maybe check for "Domain: food" or similar if the description implies extracted fields.
    # But since I have to extract, and hints list domains, I'll rely on Keywords and Title.
    
    if is_food:
        food_papers.append(title)
        debug_info.append({"title": title, "keywords": extracted_keywords})

# Calculate citations
total_citations = 0
for c in citations:
    if c['title'] in food_papers:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps({"food_papers_count": len(food_papers), "food_papers": food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json'}

exec(code, env_args)
