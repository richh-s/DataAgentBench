code = """import json
import re

# Get file paths from local variables
citations_path = locals()['var_function-call-14555610858560358239']
papers_path = locals()['var_function-call-11640274332636556525']

# Load data
with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Regex to find Author Keywords section
    # Use raw string for regex, but escape backslashes for JSON transport if needed
    # We look for "Author Keywords" or "Keywords", followed by optional whitespace/newline,
    # capturing content until double newline or a capitalized header line.
    keywords_match = re.search(r'(?:Author Keywords|Keywords)\s*\n(.*?)(?:\n\n|\n[A-Z ]{5,}\n)', text, re.DOTALL | re.IGNORECASE)
    
    keywords_text = ""
    if keywords_match:
        keywords_text = keywords_match.group(1)
    
    keywords_text_lower = keywords_text.lower()
    title_lower = title.lower()
    
    is_food = False
    
    # Check keywords list
    kw_list = [k.strip() for k in re.split(r'[;,\n]', keywords_text_lower) if k.strip()]
    
    for kw in kw_list:
        if 'food' in kw:
            is_food = True
            break
            
    if not is_food and 'food' in title_lower:
        is_food = True
        
    if is_food:
        food_papers.append(title)

total_citations = 0

for c in citations:
    c_title = c.get('title', '')
    if c_title in food_papers:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-13801611410000855703': 'file_storage/function-call-13801611410000855703.json', 'var_function-call-13801611410000858480': ['Citations', 'sqlite_sequence'], 'var_function-call-14555610858560358239': 'file_storage/function-call-14555610858560358239.json', 'var_function-call-11640274332636556525': 'file_storage/function-call-11640274332636556525.json'}

exec(code, env_args)
