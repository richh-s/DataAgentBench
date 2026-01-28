code = """import json
import re

# Load data
with open(locals()['var_function-call-753594386774760790'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-753594386774761341'], 'r') as f:
    citations = json.load(f)

food_titles = []

for p in papers:
    text = p['text']
    filename = p['filename']
    
    # Simpler extraction logic
    keywords = ""
    lower_text = text.lower()
    
    # Try to find the keyword section
    if "author keywords" in lower_text:
        start_idx = lower_text.find("author keywords") + len("author keywords")
        # take next 500 chars
        candidate = lower_text[start_idx:start_idx+500]
        # stop at next section header (usually double newline or 'acm classification' or 'introduction')
        # We'll just look for 'acm classification' or 'introduction' or '\n\n'
        stop_markers = ["acm classification", "introduction", "\n\n\n"]
        min_stop = len(candidate)
        for marker in stop_markers:
            idx = candidate.find(marker)
            if idx != -1 and idx < min_stop:
                min_stop = idx
        keywords = candidate[:min_stop]
    elif "index terms" in lower_text:
        start_idx = lower_text.find("index terms") + len("index terms")
        candidate = lower_text[start_idx:start_idx+500]
        stop_markers = ["introduction", "\n\n\n"]
        min_stop = len(candidate)
        for marker in stop_markers:
            idx = candidate.find(marker)
            if idx != -1 and idx < min_stop:
                min_stop = idx
        keywords = candidate[:min_stop]
    
    # Check for 'food'
    if "food" in keywords:
        title = filename.rsplit('.', 1)[0]
        food_titles.append(title)

# Sum citations
total_citations = 0
for c in citations:
    if c['title'] in food_titles:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_paper_count": len(food_titles)}))"""

env_args = {'var_function-call-14816162912546968424': 'file_storage/function-call-14816162912546968424.json', 'var_function-call-15665473937794536591': ['paper_docs'], 'var_function-call-15665473937794537994': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-17092646585437206863': 'file_storage/function-call-17092646585437206863.json', 'var_function-call-753594386774760790': 'file_storage/function-call-753594386774760790.json', 'var_function-call-753594386774761341': 'file_storage/function-call-753594386774761341.json'}

exec(code, env_args)
