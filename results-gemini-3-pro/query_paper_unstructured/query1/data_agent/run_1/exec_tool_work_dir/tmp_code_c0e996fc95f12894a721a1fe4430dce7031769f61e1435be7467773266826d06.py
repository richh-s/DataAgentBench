code = """import json
import re

citations_file = locals()['var_function-call-1796445934379117253']
papers_file = locals()['var_function-call-4873793932197398139']

with open(citations_file, 'r') as f:
    citations = json.load(f)
with open(papers_file, 'r') as f:
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
    
    if 'food' in title.lower():
        is_food = True

    if not is_food:
        header_chunk = text[:5000]
        pattern = "(Author\\s+Keywords|Keywords|Index\\s+Terms|General\\s+Terms)[\\s\\S]*?(?=INTRODUCTION|ABSTRACT|ACM\\s+Classification)"
        match = re.search(pattern, header_chunk, re.IGNORECASE)
        
        if match:
            keywords_text = match.group(0)
            if 'food' in keywords_text.lower():
                is_food = True
    
    if is_food:
        food_titles.append(title)

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
