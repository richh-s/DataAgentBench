code = """import json
import re

# Load data
with open(locals()['var_function-call-17971925795973344162'], 'r') as f:
    docs = json.load(f)

with open(locals()['var_function-call-17971925795973342135'], 'r') as f:
    citations = json.load(f)

food_titles = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Try to find keywords section
    # Pattern: "Author Keywords" or "Keywords" followed by content, until double newline or next major section
    # We'll grab a chunk after the keyword label
    
    match = re.search(r'(?:Author Keywords|Keywords|Index Terms)\s*[:\n](.*?)(?:\n\n|\n[A-Z]+ [A-Z]+)', text, re.DOTALL | re.IGNORECASE)
    
    is_food = False
    if match:
        keywords = match.group(1).lower()
        if 'food' in keywords:
            is_food = True
    else:
        # Fallback: check if 'food' is in the first 2000 characters (metadata area) but be careful
        # Or checking if 'food' appears in a line starting with "Keywords"
        # Let's try a simpler approach if the regex failed: look for lines containing "Keywords" and "food" close by
        pass
    
    # Debugging: let's print if we find food
    if is_food:
        food_titles.append(title)

# Calculate citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({"food_titles": food_titles, "total_citations": total_citations}))"""

env_args = {'var_function-call-8748244462217434689': ['paper_docs'], 'var_function-call-8748244462217434842': ['Citations', 'sqlite_sequence'], 'var_function-call-10817664668211665430': 'file_storage/function-call-10817664668211665430.json', 'var_function-call-4112176734939169200': 'file_storage/function-call-4112176734939169200.json', 'var_function-call-17971925795973344162': 'file_storage/function-call-17971925795973344162.json', 'var_function-call-17971925795973342135': 'file_storage/function-call-17971925795973342135.json'}

exec(code, env_args)
