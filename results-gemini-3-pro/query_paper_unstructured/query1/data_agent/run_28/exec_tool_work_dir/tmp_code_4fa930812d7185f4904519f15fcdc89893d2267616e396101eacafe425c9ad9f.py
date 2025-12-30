code = """import json
import re

citations_path = locals()['var_function-call-12816615437608771062']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-6011285741143756461']
with open(papers_path, 'r') as f:
    papers = json.load(f)

debug = {}

debug['paper_titles_sample'] = [p['filename'].replace('.txt', '') for p in papers[:3]]
debug['citation_titles_sample'] = [c['title'] for c in citations[:3]]

food_in_text_count = 0
examples = []

food_papers_titles = set()

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check simple inclusion
    if 'food' in text.lower():
        food_in_text_count += 1
        
    # Logic test
    is_food = False
    keyword_extraction = "N/A"
    
    if 'food' in title.lower():
        is_food = True
    
    # Try Regex
    match = re.search(r"Author Keywords\s*(.*?)\s*(?:ACM Classification Keywords|INTRODUCTION|Index Terms|ABSTRACT|General Terms)", text, re.DOTALL | re.IGNORECASE)
    if match:
        keywords = match.group(1).lower()
        keyword_extraction = match.group(1)[:100]
        if 'food' in keywords:
            is_food = True
    else:
         match_start = re.search(r"Author Keywords", text, re.IGNORECASE)
         if match_start:
             keyword_extraction = text[match_start.end():match_start.end()+100] + "..."
             if 'food' in keyword_extraction.lower():
                 is_food = True
    
    if is_food:
        food_papers_titles.add(title)
        
    if 'food' in text.lower() and len(examples) < 3:
        examples.append({
            "filename": filename,
            "is_food_identified": is_food,
            "keyword_extraction_snippet": keyword_extraction
        })

debug['food_in_text_count'] = food_in_text_count
debug['examples_with_food_in_text'] = examples
debug['identified_food_papers_count'] = len(food_papers_titles)

print("__RESULT__:")
print(json.dumps(debug))"""

env_args = {'var_function-call-1408029875395216778': 'file_storage/function-call-1408029875395216778.json', 'var_function-call-12816615437608771062': 'file_storage/function-call-12816615437608771062.json', 'var_function-call-6011285741143756461': 'file_storage/function-call-6011285741143756461.json', 'var_function-call-4970845110660497664': 0, 'var_function-call-11335810610248278387': 'debug done'}

exec(code, env_args)
