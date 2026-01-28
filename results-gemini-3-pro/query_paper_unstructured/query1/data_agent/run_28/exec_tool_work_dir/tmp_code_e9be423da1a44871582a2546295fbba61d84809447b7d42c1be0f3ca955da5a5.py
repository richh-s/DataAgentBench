code = """import json
import re

citations_path = locals()['var_function-call-12816615437608771062']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-10208889887629651499']
with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers_titles = set()
debug_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # Check Title
    if 'food' in title.lower():
        is_food = True
    
    # Check Keywords
    if not is_food:
        # Regex to capture text between "Author Keywords" and the next section
        # Look for "Author Keywords" followed by content, then stopped by one of the headers
        # or end of file.
        match = re.search(r"Author Keywords\s*[:\n]\s*(.*?)(?=\n\n|\n[A-Z ]{5,}|ACM Classification|INTRODUCTION|ABSTRACT|Index Terms|General Terms|CCS Concepts)", text, re.DOTALL | re.IGNORECASE)
        
        if match:
            keywords = match.group(1).lower()
            if 'food' in keywords:
                is_food = True
        else:
             # Fallback: look for "Author Keywords" and take a chunk
             match_start = re.search(r"Author Keywords", text, re.IGNORECASE)
             if match_start:
                 start = match_start.end()
                 # Take next 300 chars
                 chunk = text[start:start+300].lower()
                 # If "food" is in this chunk
                 if 'food' in chunk:
                     is_food = True
    
    # Also check "Index Terms"
    if not is_food:
        match_idx = re.search(r"Index Terms\s*[:\n]\s*(.*?)(?=\n\n|\n[A-Z ]{5,}|INTRODUCTION)", text, re.DOTALL | re.IGNORECASE)
        if match_idx:
            keywords = match_idx.group(1).lower()
            if 'food' in keywords:
                is_food = True

    if is_food:
        food_papers_titles.add(title)
        debug_titles.append(title)

# Sum citations
total_citations = 0
for c in citations:
    c_title = c.get('title')
    c_count = c.get('citation_count')
    
    if c_title in food_papers_titles:
        try:
            total_citations += int(c_count)
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-1408029875395216778': 'file_storage/function-call-1408029875395216778.json', 'var_function-call-12816615437608771062': 'file_storage/function-call-12816615437608771062.json', 'var_function-call-6011285741143756461': 'file_storage/function-call-6011285741143756461.json', 'var_function-call-4970845110660497664': 0, 'var_function-call-11335810610248278387': 'debug done', 'var_function-call-9994269108278680187': {'paper_titles_sample': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'], 'citation_titles_sample': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'], 'food_in_text_count': 3, 'examples_with_food_in_text': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'is_food_identified': False, 'keyword_extraction_snippet': 'Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Locat'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'is_food_identified': False, 'keyword_extraction_snippet': 'Personal informatics, collection, reflection, model, barriers'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'is_food_identified': False, 'keyword_extraction_snippet': 'N/A'}], 'identified_food_papers_count': 0}, 'var_function-call-6857057513310862422': {'total_papers': 5, 'filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'keyword_counts': {'food': 3, 'diet': 2, 'nutrition': 0, 'eating': 4, 'meal': 4}}, 'var_function-call-10208889887629651499': 'file_storage/function-call-10208889887629651499.json'}

exec(code, env_args)
