code = """import json
import re

# Load data
with open(locals()['var_function-call-753594386774760790'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-753594386774761341'], 'r') as f:
    citations = json.load(f)

# Identify food papers
food_titles = []
debug_info = []

for p in papers:
    text = p['text']
    filename = p['filename']
    
    # regex to find keywords
    # Looking for "Author Keywords" or "Index Terms" followed by content, until double newline or specific headers
    # The example text has "Author Keywords \nLived Informatics; ... \n\nACM Classification Keywords"
    # So we look for "Author Keywords" then take everything until the next header-like sequence or 2+ newlines
    
    match = re.search(r'(Author Keywords|Index Terms|Keywords)\s*[\r\n]+([\s\S]*?)(\n\n\n|\r\n\r\n\r\n|ACM Classification|INTRODUCTION|ABSTRACT)', text, re.IGNORECASE)
    
    keywords = ""
    if match:
        keywords = match.group(2).strip()
    else:
        # Fallback: sometimes there's just one newline or different formatting. 
        # Let's try a simpler split
        if "Author Keywords" in text:
            try:
                part = text.split("Author Keywords")[1]
                # split by double newline to get the paragraph
                keywords = part.split("\n\n")[0].strip()
                # If strictly followed by header
                if "ACM Classification" in keywords:
                    keywords = keywords.split("ACM Classification")[0].strip()
            except:
                pass
        elif "Index Terms" in text:
             try:
                part = text.split("Index Terms")[1]
                keywords = part.split("\n\n")[0].strip()
             except:
                pass

    # Check if 'food' in keywords
    if 'food' in keywords.lower():
        # Title is filename without .txt
        title = filename.rsplit('.', 1)[0]
        food_titles.append(title)
        debug_info.append({"title": title, "keywords": keywords})

# Filter citations
total_citations = 0
matched_citations = 0
for c in citations:
    if c['title'] in food_titles:
        total_citations += int(c['citation_count'])
        matched_citations += 1

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_paper_count": len(food_titles), "matched_citation_records": matched_citations, "sample_titles": food_titles[:5]}))"""

env_args = {'var_function-call-14816162912546968424': 'file_storage/function-call-14816162912546968424.json', 'var_function-call-15665473937794536591': ['paper_docs'], 'var_function-call-15665473937794537994': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-17092646585437206863': 'file_storage/function-call-17092646585437206863.json', 'var_function-call-753594386774760790': 'file_storage/function-call-753594386774760790.json', 'var_function-call-753594386774761341': 'file_storage/function-call-753594386774761341.json'}

exec(code, env_args)
