code = """import json

# Load paper_docs (larger set)
with open(locals()['var_function-call-16958740794073155916'], 'r') as f:
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
                # snippet from start of keywords
                snippet = text_lower[start_idx:start_idx+600]
                # Try to stop at next section (double newline or specific headers)
                # We stop at double newline to be safe
                end_idx = snippet.find(double_newline)
                if end_idx != -1:
                    snippet = snippet[:end_idx]
                
                # Also stop if we hit "Introduction" or "Abstract" (unlikely after keywords but possible)
                if "introduction" in snippet:
                    snippet = snippet.split("introduction")[0]
                
                if 'food' in snippet:
                    is_food = True
                    break
        
    if not is_food:
        # Check abstract
        start_idx = text_lower.find("abstract")
        if start_idx != -1:
            snippet = text_lower[start_idx:start_idx+2000]
            # Stop at Introduction
            end_idx = snippet.find("introduction")
            if end_idx != -1:
                snippet = snippet[:end_idx]
            
            # Additional stop at "General Terms" or "Keywords" if abstract comes before them
            k_idx = snippet.find("author keywords")
            if k_idx != -1:
                snippet = snippet[:k_idx]

            # In abstract, be more specific? Or just "food"?
            # Hint says "Common domains include: 'food'".
            # So likely "food" will be explicitly mentioned.
            if 'food' in snippet:
                is_food = True

    if is_food:
        food_papers.append(title)

# Filter citations
total_citations = 0
food_papers_set = set(food_papers)

# Debug: print found food papers
# print("DEBUG: Found food papers:", food_papers)

for cit in citations:
    if cit['title'] in food_papers_set:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({"food_papers_count": len(food_papers), "food_papers_titles": food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-8528399130518209876': ['paper_docs'], 'var_function-call-8528399130518209403': ['Citations', 'sqlite_sequence'], 'var_function-call-5911009850598284906': 'file_storage/function-call-5911009850598284906.json', 'var_function-call-5911009850598284323': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-8131891965155681043': 'file_storage/function-call-8131891965155681043.json', 'var_function-call-9545123832461402324': 'file_storage/function-call-9545123832461402324.json', 'var_function-call-16177678008665017919': {'food_papers_count': 0, 'food_papers_titles': [], 'total_citations': 0}, 'var_function-call-9443954233437372911': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'context': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'context': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'context': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-7379546396970470087': {'count': 5, 'titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-16958740794073155916': 'file_storage/function-call-16958740794073155916.json', 'var_function-call-13973086622616753670': {'count': 99}}

exec(code, env_args)
