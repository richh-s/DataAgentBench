code = """import json
import re

# Load citations
with open('var_function-call-14555610858560358239.json', 'r') as f:
    citations = json.load(f)

# Load paper_docs
with open('var_function-call-11640274332636556525.json', 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Keywords
    # Regex to find Author Keywords section
    # We look for "Author Keywords" followed by content, stopping at double newline or next known header
    keywords_match = re.search(r'(?:Author Keywords|Keywords)\s*\n(.*?)(?:\n\n|\n[A-Z ]{5,}\n)', text, re.DOTALL | re.IGNORECASE)
    
    keywords_text = ""
    if keywords_match:
        keywords_text = keywords_match.group(1)
    
    # Normalize
    keywords_text_lower = keywords_text.lower()
    title_lower = title.lower()
    
    # Check for 'food'
    # We check if 'food' is in the keywords or title
    is_food = False
    
    # Check keywords list
    # Split by ; or , or \n
    kw_list = [k.strip() for k in re.split(r'[;,\n]', keywords_text_lower) if k.strip()]
    
    # Check if any keyword contains 'food'
    for kw in kw_list:
        if 'food' in kw:
            is_food = True
            break
            
    # Also check title
    if not is_food and 'food' in title_lower:
        is_food = True
        
    # Also check abstract just in case (optional, but might be safer if keywords are missing)
    # But let's stick to keywords/title first as per "domain" extraction.
    
    if is_food:
        food_papers.append(title)

# Filter citations
total_citations = 0
matched_papers = set()

for c in citations:
    c_title = c.get('title', '')
    if c_title in food_papers:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
            matched_papers.add(c_title)
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-13801611410000855703': 'file_storage/function-call-13801611410000855703.json', 'var_function-call-13801611410000858480': ['Citations', 'sqlite_sequence'], 'var_function-call-14555610858560358239': 'file_storage/function-call-14555610858560358239.json', 'var_function-call-11640274332636556525': 'file_storage/function-call-11640274332636556525.json'}

exec(code, env_args)
