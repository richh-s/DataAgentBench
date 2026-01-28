code = """import json

# Load paper docs
with open('var_function-call-15077613833019679981.json', 'r') as f:
    papers = json.load(f)

# Load citations
with open('var_function-call-15077613833019680274.json', 'r') as f:
    citations = json.load(f)

food_titles = set()

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    if not text: continue
    
    text_lower = text.lower()
    title = filename.replace('.txt', '')
    
    # Check title
    # We want whole word match approximately, but simplest is contains
    # Given the specificity, 'food' is unlikely to be substring of another common domain word
    # except 'seafood' or 'nonfood'. 
    # Let's check for ' food ' or 'food,' or 'food.' or starts/ends with food.
    # To be safe, I'll use a simple "food" check first, but verify boundaries if I can.
    # Actually, let's just use string find for "food".
    
    is_food = False
    if "food" in title.lower().split(): # naive word boundary check
        is_food = True
    elif "food" in title.lower():
        # Check if it's a standalone word?
        # e.g. "Food and ..." -> "food" in split is True.
        # "Seafood" -> "seafood" in split. "food" not in split.
        pass

    if not is_food:
        # Check Keywords
        # Look for "author keywords"
        idx = text_lower.find("author keywords")
        if idx == -1:
            idx = text_lower.find("index terms")
            
        if idx != -1:
            # Check the next 500 chars
            snippet = text_lower[idx:idx+500]
            # Check for "food" in snippet
            # Be careful about matching "food" in "seafood"
            # Let's perform a check: is "food" present surrounded by non-alpha?
            # We can iterate or just simple check
            if "food" in snippet:
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
