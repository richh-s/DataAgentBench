code = """import json

# Load paper_docs
with open(locals()['var_function-call-8131891965155681043'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-9545123832461402324'], 'r') as f:
    citations = json.load(f)

food_papers = []

newline = chr(10)
double_newline = newline + newline

for paper in paper_docs:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    text_lower = text.lower()
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    if not is_food:
        # Check keywords
        kw_starts = ["author keywords", "index terms", "keywords"]
        for start_phrase in kw_starts:
            start_idx = text_lower.find(start_phrase)
            if start_idx != -1:
                snippet = text_lower[start_idx:start_idx+500]
                end_idx = snippet.find(double_newline)
                if end_idx != -1:
                    snippet = snippet[:end_idx]
                
                if 'food' in snippet:
                    is_food = True
                    break
        
    if not is_food:
        # Check abstract
        start_idx = text_lower.find("abstract")
        if start_idx != -1:
            snippet = text_lower[start_idx:start_idx+2000]
            end_idx = snippet.find("introduction")
            if end_idx != -1:
                snippet = snippet[:end_idx]
            
            if 'food' in snippet:
                is_food = True

    if is_food:
        food_papers.append(title)

# Filter citations
total_citations = 0
food_papers_set = set(food_papers)

for cit in citations:
    if cit['title'] in food_papers_set:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({"food_papers_count": len(food_papers), "food_papers_titles": food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-8528399130518209876': ['paper_docs'], 'var_function-call-8528399130518209403': ['Citations', 'sqlite_sequence'], 'var_function-call-5911009850598284906': 'file_storage/function-call-5911009850598284906.json', 'var_function-call-5911009850598284323': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-8131891965155681043': 'file_storage/function-call-8131891965155681043.json', 'var_function-call-9545123832461402324': 'file_storage/function-call-9545123832461402324.json'}

exec(code, env_args)
