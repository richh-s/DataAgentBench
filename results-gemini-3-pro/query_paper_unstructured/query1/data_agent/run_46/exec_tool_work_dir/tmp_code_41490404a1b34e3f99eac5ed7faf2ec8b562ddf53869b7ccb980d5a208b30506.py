code = """import json

# Load data
with open(locals()['var_function-call-753594386774760790'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-753594386774761341'], 'r') as f:
    citations = json.load(f)

food_titles = []
newline = chr(10)
double_newline = newline + newline

for p in papers:
    text = p['text']
    filename = p['filename']
    
    keywords = ""
    lower_text = text.lower()
    
    # helper to extract
    def get_keywords(anchor):
        if anchor in lower_text:
            start = lower_text.find(anchor) + len(anchor)
            sub = lower_text[start:start+1000] # grab a chunk
            # truncate at next double newline or section header
            # markers
            markers = ["acm classification", "introduction", "abstract", double_newline]
            end = len(sub)
            for m in markers:
                idx = sub.find(m)
                if idx != -1 and idx < end:
                    end = idx
            return sub[:end]
        return ""

    k1 = get_keywords("author keywords")
    k2 = get_keywords("index terms")
    
    # Combine found keywords
    keywords = k1 + " " + k2
    
    # Check for 'food'
    if "food" in keywords:
        # Check if it is a standalone word or part of a phrase?
        # substring matching is requested.
        title = filename.rsplit('.', 1)[0]
        food_titles.append(title)

total_citations = 0
for c in citations:
    if c['title'] in food_titles:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-14816162912546968424': 'file_storage/function-call-14816162912546968424.json', 'var_function-call-15665473937794536591': ['paper_docs'], 'var_function-call-15665473937794537994': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-17092646585437206863': 'file_storage/function-call-17092646585437206863.json', 'var_function-call-753594386774760790': 'file_storage/function-call-753594386774760790.json', 'var_function-call-753594386774761341': 'file_storage/function-call-753594386774761341.json'}

exec(code, env_args)
