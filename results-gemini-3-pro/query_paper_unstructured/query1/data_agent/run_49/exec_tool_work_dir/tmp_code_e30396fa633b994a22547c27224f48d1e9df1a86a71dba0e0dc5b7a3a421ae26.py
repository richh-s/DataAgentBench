code = """import json

key_papers = 'var_function-call-211035955538813966'
key_citations = 'var_function-call-5010856936099612049'

with open(locals()[key_papers], 'r') as f:
    papers = json.load(f)

with open(locals()[key_citations], 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(papers)}")
print(f"Total citations records: {len(citations)}")

# Check for "food" in titles in citations
food_in_citation_titles = [c['title'] for c in citations if 'food' in c['title'].lower()]
print(f"Citations with 'food' in title: {len(food_in_citation_titles)}")
if food_in_citation_titles:
    print(f"Sample citation titles: {food_in_citation_titles[:3]}")

# Check for "food" in paper filenames
food_in_filenames = [p['filename'] for p in papers if 'food' in p['filename'].lower()]
print(f"Papers with 'food' in filename: {len(food_in_filenames)}")
if food_in_filenames:
    print(f"Sample filenames: {food_in_filenames[:3]}")

# Check keywords extraction
# Let's inspect the text around 'Author Keywords' for the first paper
if len(papers) > 0:
    text = papers[0]['text']
    lower = text.lower()
    idx = lower.find("author keywords")
    print(f"Index of 'author keywords' in first paper: {idx}")
    if idx != -1:
        print(f"Snippet: {text[idx:idx+200]}")
    else:
        print("Author keywords not found in first paper.")

# Check for any "food" in any text keywords area
count_food_keywords = 0
for p in papers:
    text = p['text'].lower()
    if 'author keywords' in text:
        idx = text.find('author keywords')
        snippet = text[idx:idx+500]
        if 'food' in snippet:
            count_food_keywords += 1

print(f"Papers with 'food' in Author Keywords area: {count_food_keywords}")

print("__RESULT__:")
print(json.dumps("debug_done"))"""

env_args = {'var_function-call-6408765231398554984': ['paper_docs'], 'var_function-call-6408765231398555607': ['Citations', 'sqlite_sequence'], 'var_function-call-15918017667196444195': 'file_storage/function-call-15918017667196444195.json', 'var_function-call-15918017667196440718': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-211035955538813966': 'file_storage/function-call-211035955538813966.json', 'var_function-call-5010856936099612049': 'file_storage/function-call-5010856936099612049.json', 'var_function-call-9151466501287581759': 0}

exec(code, env_args)
