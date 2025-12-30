code = """import json
import re

# Load Citations
citations_path = locals()['var_function-call-12816615437608771062']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load Paper Docs
papers_path = locals()['var_function-call-6011285741143756461']
with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers_titles = set()

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    if not is_food:
        # Check Author Keywords
        # Try to find the block
        match = re.search(r"Author Keywords\s*(.*?)\s*(?:ACM Classification Keywords|INTRODUCTION|Index Terms|ABSTRACT|General Terms)", text, re.DOTALL | re.IGNORECASE)
        if match:
            keywords = match.group(1).lower()
            if 'food' in keywords:
                is_food = True
        else:
            # Fallback: sometimes Abstract is before keywords or keywords are at the end?
            # Let's try to just look for "Author Keywords" and take next 500 chars if end marker not found
            match_start = re.search(r"Author Keywords", text, re.IGNORECASE)
            if match_start:
                start_idx = match_start.end()
                keywords = text[start_idx:start_idx+500].lower()
                # Use a heuristic to stop at double newline or next section
                # But simple check might be enough
                if 'food' in keywords:
                    # Double check if it's really in keywords (e.g. separated by semicolons or commas)
                    # This is a bit loose but likely accurate enough given the hint.
                    is_food = True

    if is_food:
        food_papers_titles.add(title)

# Filter Citations
total_citations = 0
for c in citations:
    c_title = c.get('title')
    c_count = c.get('citation_count')
    
    if c_title in food_papers_titles:
        try:
            total_citations += int(c_count)
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-1408029875395216778': 'file_storage/function-call-1408029875395216778.json', 'var_function-call-12816615437608771062': 'file_storage/function-call-12816615437608771062.json', 'var_function-call-6011285741143756461': 'file_storage/function-call-6011285741143756461.json'}

exec(code, env_args)
