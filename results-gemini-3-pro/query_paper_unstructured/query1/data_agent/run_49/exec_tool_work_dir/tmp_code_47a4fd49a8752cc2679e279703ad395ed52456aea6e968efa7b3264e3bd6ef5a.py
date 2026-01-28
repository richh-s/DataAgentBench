code = """import json

key_papers = 'var_function-call-211035955538813966'
key_citations = 'var_function-call-5010856936099612049'

with open(locals()[key_papers], 'r') as f:
    papers = json.load(f)
with open(locals()[key_citations], 'r') as f:
    citations = json.load(f)

debug_info = {}
debug_info['total_papers'] = len(papers)
debug_info['total_citations'] = len(citations)

food_titles_cit = [c['title'] for c in citations if 'food' in c['title'].lower()]
debug_info['food_titles_in_citations'] = food_titles_cit[:5]

food_filenames = [p['filename'] for p in papers if 'food' in p['filename'].lower()]
debug_info['food_filenames'] = food_filenames[:5]

# Check keywords extraction on first paper
if papers:
    text = papers[0]['text']
    lower = text.lower()
    idx = lower.find("author keywords")
    debug_info['first_paper_keywords_idx'] = idx
    if idx != -1:
        debug_info['first_paper_snippet'] = text[idx:idx+200]

# Check how many papers have 'food' in keywords area
count_food = 0
for p in papers:
    text = p['text'].lower()
    idx = text.find('author keywords')
    if idx != -1:
        snippet = text[idx:idx+500]
        if 'food' in snippet:
            count_food += 1
debug_info['papers_with_food_in_keywords'] = count_food

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6408765231398554984': ['paper_docs'], 'var_function-call-6408765231398555607': ['Citations', 'sqlite_sequence'], 'var_function-call-15918017667196444195': 'file_storage/function-call-15918017667196444195.json', 'var_function-call-15918017667196440718': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-211035955538813966': 'file_storage/function-call-211035955538813966.json', 'var_function-call-5010856936099612049': 'file_storage/function-call-5010856936099612049.json', 'var_function-call-9151466501287581759': 0, 'var_function-call-4949709722104029505': 'debug_done'}

exec(code, env_args)
