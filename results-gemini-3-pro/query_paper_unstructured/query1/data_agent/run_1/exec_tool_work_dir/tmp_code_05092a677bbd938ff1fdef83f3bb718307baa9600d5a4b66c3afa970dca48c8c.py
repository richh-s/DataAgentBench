code = """import json
import re

# Load data
with open(locals()['var_function-call-1796445934379117253'], 'r') as f:
    citations = json.load(f)
with open(locals()['var_function-call-4873793932197398139'], 'r') as f:
    papers = json.load(f)

food_titles = []
seen_titles = set()

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    if title in seen_titles:
        continue
    seen_titles.add(title)
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True

    if not is_food:
        # Extract Keywords
        # Look for keywords section in first 5000 chars
        header_chunk = text[:5000]
        # Regex: Keywords... until...
        # Using double backslash for safety in tool call string
        pattern = r'(Author\s+Keywords|Keywords|Index\s+Terms|General\s+Terms)[\s\S]*?(?=INTRODUCTION|ABSTRACT|ACM\s+Classification|\n\n\n)'
        match = re.search(pattern, header_chunk, re.IGNORECASE)
        
        if match:
            keywords_text = match.group(0)
            if 'food' in keywords_text.lower():
                is_food = True
    
    if is_food:
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
print(json.dumps({"total_citations": total_citations, "food_paper_count": len(food_titles), "matched_citations": found_citations, "sample_titles": food_titles[:3]}))"""

env_args = {'var_function-call-2863254843670531231': 'file_storage/function-call-2863254843670531231.json', 'var_function-call-14615599340757939529': ['Citations', 'sqlite_sequence'], 'var_function-call-1796445934379117253': 'file_storage/function-call-1796445934379117253.json', 'var_function-call-4873793932197398139': 'file_storage/function-call-4873793932197398139.json'}

exec(code, env_args)
