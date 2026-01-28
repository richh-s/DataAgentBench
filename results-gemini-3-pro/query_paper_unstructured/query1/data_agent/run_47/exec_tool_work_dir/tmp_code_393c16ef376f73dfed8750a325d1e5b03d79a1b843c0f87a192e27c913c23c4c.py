code = """import json

# Get file paths from local variables
papers_path = locals()['var_function-call-15077613833019679981']
citations_path = locals()['var_function-call-15077613833019680274']

# Load paper docs
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

food_titles = set()

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    if not text: continue
    
    text_lower = text.lower()
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # Check title for whole word 'food'
    # We can use a simple helper to check word boundary
    def has_word(text, word):
        # simple boundary check
        # replace punctuation with space
        cleaned = ''.join(c if c.isalnum() else ' ' for c in text)
        return word in cleaned.split()

    if has_word(title.lower(), "food"):
        is_food = True
    
    if not is_food:
        # Check Keywords
        idx = text_lower.find("author keywords")
        if idx == -1:
            idx = text_lower.find("index terms")
            
        if idx != -1:
            # Check the next 600 chars (approx 5-6 lines)
            snippet = text_lower[idx:idx+600]
            if has_word(snippet, "food"):
                is_food = True
    
    if is_food:
        food_titles.add(title)

# Calculate total citations
total_citations = 0
for c in citations:
    c_title = c.get('title', '')
    if c_title in food_titles:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-14405582414403684106': ['paper_docs'], 'var_function-call-14405582414403686195': ['Citations', 'sqlite_sequence'], 'var_function-call-1273577479453038261': 'file_storage/function-call-1273577479453038261.json', 'var_function-call-1273577479453039900': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15077613833019679981': 'file_storage/function-call-15077613833019679981.json', 'var_function-call-15077613833019680274': 'file_storage/function-call-15077613833019680274.json'}

exec(code, env_args)
