code = """import json
import re

# Load papers (filtered by regex 'food' from DB)
with open(locals()['var_function-call-18282859333790879824'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
debug_list = []
for p in papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '').strip()
    text = p.get('text', '')
    
    # Check title
    if 'food' in title.lower():
        continue # Already matched
        
    # Check keywords (re-run logic to debug)
    text_lower = text.lower()
    start_match = re.search(r'(author keywords|keywords|index terms|general terms)', text_lower)
    if start_match:
        start_idx = start_match.end()
        chunk = text_lower[start_idx:start_idx+1000]
        stop_words = ['introduction', 'acm classification', 'categories and subject descriptors']
        min_stop_idx = len(chunk)
        for sw in stop_words:
            idx = chunk.find(sw)
            if idx != -1 and idx < min_stop_idx:
                min_stop_idx = idx
        keywords = chunk[:min_stop_idx]
        
        if 'food' not in keywords:
             debug_list.append({"title": title, "extracted_keywords": keywords})
    else:
        debug_list.append({"title": title, "reason": "No keywords found"})

print(json.dumps(debug_list[:5]))"""

env_args = {'var_function-call-14800347907700836141': 'file_storage/function-call-14800347907700836141.json', 'var_function-call-1190130121296070370': 'file_storage/function-call-1190130121296070370.json', 'var_function-call-1190130121296070935': 'file_storage/function-call-1190130121296070935.json', 'var_function-call-16405168858787139098': {'total_citations': 0, 'food_paper_count': 0, 'matched_citations_records': 0, 'matched_papers_in_citations': 0}, 'var_function-call-18164685780746731910': {'total_papers': 5, 'sample_titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'food_titles_sample': [], 'sample_keyword_chunk': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\nintroduction \npersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent.  personal \ninformatics can serve a goal-driven purpose, such as tracking \nweight loss, increasing physical activity, having a record of \nplaces  visited,  or  tracking  s'}, 'var_function-call-18282859333790879824': 'file_storage/function-call-18282859333790879824.json', 'var_function-call-10652170075689648479': {'total_citations': 270, 'food_paper_count': 1, 'matched_papers_list': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling']}}

exec(code, env_args)
