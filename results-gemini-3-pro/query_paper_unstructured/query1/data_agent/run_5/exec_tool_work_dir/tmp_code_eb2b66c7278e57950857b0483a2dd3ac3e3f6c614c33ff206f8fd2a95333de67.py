code = """import json
import re

# Load data
with open(locals()['var_function-call-17959813920400142644'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-14824333924694724411'], 'r') as f:
    citations = json.load(f)

food_papers = []
debug_info = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract keywords
    # Look for "Author Keywords" or "Keywords"
    # and capture text until next section (Introduction, ACM Classification, or double newline followed by uppercase?)
    
    # Normalize text for easier search
    lower_text = text.lower()
    
    start_indices = [m.start() for m in re.finditer(r'(author\s+)?keywords', lower_text)]
    
    is_food = False
    keywords_found = ""
    
    for start in start_indices:
        # Check if it's a real header (e.g., at start of line or preceded by newline)
        # and extract until next likely header
        # simple heuristic: take next 500 chars
        snippet = lower_text[start:start+500]
        # remove the "keywords" part
        snippet = re.sub(r'^(author\s+)?keywords', '', snippet).strip()
        
        # split by newlines and take the first block that looks like keywords
        # usually keywords are terminated by a blank line or a new section
        # in the sample: "Author Keywords \nLived Informatics... Location. \n\nACM Classification Keywords"
        
        # Let's try to cut at "acm classification" or "introduction" or "abstract"
        end_match = re.search(r'(acm classification|introduction|abstract|general terms)', snippet)
        if end_match:
            keywords_block = snippet[:end_match.start()]
        else:
            keywords_block = snippet # fallback
        
        if 'food' in keywords_block:
            is_food = True
            keywords_found = keywords_block
            break
            
    if is_food:
        food_papers.append(title)
    
    # For debugging, let's print if we found food
    if is_food:
        debug_info.append(f"Found FOOD paper: {title} (Keywords: {keywords_found[:100]}...)")

# Now calculate citations
total_citations = 0
citation_rows = 0
for cit in citations:
    if cit['title'] in food_papers:
        try:
            total_citations += int(cit['citation_count'])
            citation_rows += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers),
    "food_papers": food_papers,
    "total_citations": total_citations,
    "debug_info": debug_info
}))"""

env_args = {'var_function-call-12772568682444921532': 'file_storage/function-call-12772568682444921532.json', 'var_function-call-268740664748096753': 'file_storage/function-call-268740664748096753.json', 'var_function-call-17959813920400142644': 'file_storage/function-call-17959813920400142644.json', 'var_function-call-14824333924694724411': 'file_storage/function-call-14824333924694724411.json'}

exec(code, env_args)
