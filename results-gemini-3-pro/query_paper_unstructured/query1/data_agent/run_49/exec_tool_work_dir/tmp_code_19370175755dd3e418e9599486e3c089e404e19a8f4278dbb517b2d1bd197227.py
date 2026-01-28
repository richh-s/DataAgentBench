code = """import json

# keys provided by the system
key_papers = 'var_function-call-211035955538813966'
key_citations = 'var_function-call-5010856936099612049'

with open(locals()[key_papers], 'r') as f:
    papers = json.load(f)

with open(locals()[key_citations], 'r') as f:
    citations = json.load(f)

food_titles = set()

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # 1. Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # 2. Check Author Keywords
    lower_text = text.lower()
    # Find start of keywords
    # Variations: "Author Keywords", "Keywords"
    start_idx = lower_text.find("author keywords")
    if start_idx == -1:
        start_idx = lower_text.find("keywords")
        # Be careful not to match "keywords" in text body. Usually keywords are at the start/meta.
        # But for now let's assume "Author Keywords" is the standard as per hint/sample.
    
    if start_idx != -1:
        # Extract a window
        window = lower_text[start_idx:start_idx+600]
        # Try to find the end of the keywords section
        # Common next sections: "ACM Classification Keywords", "INTRODUCTION", "ABSTRACT" (if keywords are after abstract?)
        # In the sample: Abstract -> Author Keywords -> ACM Classification -> Introduction
        end_markers = ["acm classification", "introduction", "general terms"]
        end_idx = 600
        for marker in end_markers:
            idx = window.find(marker)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        keywords_text = window[:end_idx]
        if 'food' in keywords_text:
            food_titles.add(title)

# Filter citations
total_count = 0
for c in citations:
    if c['title'] in food_titles:
        try:
            total_count += int(c['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_count))"""

env_args = {'var_function-call-6408765231398554984': ['paper_docs'], 'var_function-call-6408765231398555607': ['Citations', 'sqlite_sequence'], 'var_function-call-15918017667196444195': 'file_storage/function-call-15918017667196444195.json', 'var_function-call-15918017667196440718': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-211035955538813966': 'file_storage/function-call-211035955538813966.json', 'var_function-call-5010856936099612049': 'file_storage/function-call-5010856936099612049.json'}

exec(code, env_args)
