code = """import json
import re

# Load data
with open(locals()['var_function-call-1796445934379117253'], 'r') as f:
    citations = json.load(f)
with open(locals()['var_function-call-4873793932197398139'], 'r') as f:
    papers = json.load(f)

food_titles = []

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.append(title)
        continue

    # Extract Keywords
    # Regex to find keywords section. 
    # Usually starts with "Author Keywords", "Keywords", "Index Terms"
    # Ends with "ACM Classification", "INTRODUCTION", "ABSTRACT" or just distinct newline structure
    
    # Simple approach: find "Author Keywords" or "Keywords" and take the next 500 characters or until a major header
    match = re.search(r'(Author\s+Keywords|Index\s+Terms|Keywords)\s*[:\n](.*?)(?=(ACM\s+Classification|INTRODUCTION|ABSTRACT|\n\n[A-Z]))', text, re.IGNORECASE | re.DOTALL)
    
    keywords_text = ""
    if match:
        keywords_text = match.group(2)
    else:
        # Fallback: sometimes keywords are just after Abstract
        pass
        
    if 'food' in keywords_text.lower():
        food_titles.append(title)

# Filter citations
total_citations = 0
found_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        try:
            count = int(cit['citation_count'])
            total_citations += count
            found_citations += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_paper_count": len(food_titles), "matched_citations": found_citations}))"""

env_args = {'var_function-call-2863254843670531231': 'file_storage/function-call-2863254843670531231.json', 'var_function-call-14615599340757939529': ['Citations', 'sqlite_sequence'], 'var_function-call-1796445934379117253': 'file_storage/function-call-1796445934379117253.json', 'var_function-call-4873793932197398139': 'file_storage/function-call-4873793932197398139.json'}

exec(code, env_args)
