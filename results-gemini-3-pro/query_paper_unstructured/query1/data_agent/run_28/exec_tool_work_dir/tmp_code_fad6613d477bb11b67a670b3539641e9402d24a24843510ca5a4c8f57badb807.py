code = """import json
import re

citations_path = locals()['var_function-call-12816615437608771062']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-10208889887629651499']
with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers_titles = set()

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    text_lower = text.lower()
    
    # Check Title
    if 'food' in title.lower():
        is_food = True
    
    # Check Keywords
    # Locate "Author Keywords" or "Index Terms"
    # Extract ~500 chars after that
    
    if not is_food:
        # Find start index
        start_indices = []
        for kw_marker in ["author keywords", "index terms"]:
            idx = text_lower.find(kw_marker)
            if idx != -1:
                start_indices.append(idx + len(kw_marker))
        
        for start in start_indices:
            # content after marker
            chunk = text_lower[start:start+500]
            # Stop at common next section headers to avoid false positives from body text
            # e.g. "introduction", "abstract", "acm classification"
            stop_markers = ["introduction", "abstract", "acm classification", "general terms", "ccs concepts"]
            min_stop = len(chunk)
            for stop in stop_markers:
                stop_idx = chunk.find(stop)
                if stop_idx != -1 and stop_idx < min_stop:
                    min_stop = stop_idx
            
            clean_chunk = chunk[:min_stop]
            if 'food' in clean_chunk:
                is_food = True
                break
    
    if is_food:
        food_papers_titles.add(title)

# Sum citations
total_citations = 0
count_food_papers = len(food_papers_titles)

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
