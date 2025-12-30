code = """import json
import re

# Load citations
with open(locals()['var_function-call-12774124181016146207'], 'r') as f:
    citations_data = json.load(f)

# Aggregate citations by title
citation_map = {}
for entry in citations_data:
    title = entry['title'].strip()
    count = entry['citation_count']
    # Ensure count is int
    if isinstance(count, str):
        count = int(count) if count.isdigit() else 0
    citation_map[title] = citation_map.get(title, 0) + count

# Load papers
with open(locals()['var_function-call-12774124181016147194'], 'r') as f:
    papers_data = json.load(f)

total_citations = 0
food_papers_count = 0
matched_titles = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '').strip()
    
    # Check domain
    is_food = False
    
    # 1. Check Title
    if 'food' in title.lower():
        is_food = True
    
    # 2. Check Keywords if not already found
    if not is_food:
        # Regex to find keywords section. 
        # Usually "Author Keywords" or "Keywords" followed by content until next section like "ACM Classification" or "INTRODUCTION"
        # We'll look for the block.
        # Simplification: Find the index of "Keywords" and take the next 500 characters, or until double newline.
        
        # Normalize text for searching
        text_lower = text.lower()
        
        # Find start of keywords
        keyword_indices = [m.start() for m in re.finditer(r'(author\s+keywords|keywords)', text_lower)]
        
        for start_idx in keyword_indices:
            # Check a reasonable window after the keyword label, e.g., 300 chars
            # But stop if we hit "introduction" or "abstract" (though abstract usually comes before)
            # or "acm classification"
            window = text_lower[start_idx:start_idx+500]
            if 'food' in window:
                # Double check that "food" isn't part of "introduction" or something, but "food" is a distinct word
                # Let's simple check.
                is_food = True
                break
    
    if is_food:
        food_papers_count += 1
        citations = citation_map.get(title, 0)
        total_citations += citations
        matched_titles.append(title)

print(f"Matched {food_papers_count} papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(str(total_citations)))"""

env_args = {'var_function-call-2229407460365091455': 'file_storage/function-call-2229407460365091455.json', 'var_function-call-12774124181016146207': 'file_storage/function-call-12774124181016146207.json', 'var_function-call-12774124181016147194': 'file_storage/function-call-12774124181016147194.json'}

exec(code, env_args)
