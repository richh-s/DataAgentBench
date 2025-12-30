code = """import json
import re

# Load papers
with open(locals()['var_function-call-4358244583942540599'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-5959858908206975424'], 'r') as f:
    citations = json.load(f)

food_papers_titles = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Extract Author Keywords
    # Pattern: Look for "Author Keywords" and capture until "ACM Classification" or "INTRODUCTION" or 2 newlines
    # Case insensitive for the header search
    keywords_match = re.search(r'Author Keywords\s*(.*?)(?:\n\n|ACM Classification|INTRODUCTION)', text, re.IGNORECASE | re.DOTALL)
    keywords_text = ""
    if keywords_match:
        keywords_text = keywords_match.group(1)
    
    # Check for 'food' in title or keywords
    is_food = False
    if 'food' in title.lower():
        is_food = True
    elif 'food' in keywords_text.lower():
        is_food = True
    
    # Just in case, let's print the title and whether it was found, for debugging (I can capture stdout)
    # But I should verify logic. 
    # Let's also check if "food" is mentioned in the first 500 chars, maybe it's in the Abstract?
    # But "domain" usually implies a category.
    
    if is_food:
        food_papers_titles.append(title)

# Filter citations
total_citations = 0
matched_citation_records = 0

food_titles_set = set(food_papers_titles)

for c in citations:
    c_title = c.get('title')
    count = int(c.get('citation_count', 0))
    if c_title in food_titles_set:
        total_citations += count
        matched_citation_records += 1

result = {
    "food_papers_found": food_papers_titles,
    "total_citations": total_citations,
    "matched_citation_records": matched_citation_records
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4625483642172775665': 'file_storage/function-call-4625483642172775665.json', 'var_function-call-4600237865366959545': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5959858908206975424': 'file_storage/function-call-5959858908206975424.json', 'var_function-call-4358244583942540599': 'file_storage/function-call-4358244583942540599.json'}

exec(code, env_args)
