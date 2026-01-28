code = """import json
import re

with open(locals()['var_function-call-17959813920400142644'], 'r') as f:
    paper_docs = json.load(f)

related_terms = ['diet', 'nutrition', 'eating', 'meal', 'cooking']
candidates = []

physical_activity_papers = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    lower_text = text.lower()
    
    # Check for related terms
    found_terms = []
    for term in related_terms:
        if term in lower_text:
            found_terms.append(term)
    
    if found_terms:
        candidates.append({
            "title": filename.replace('.txt', ''),
            "found_terms": found_terms
        })
        
    # Check for Physical Activity in keywords
    # My previous extraction logic:
    match = re.search(r'(author\s+keywords|index\s+terms|keywords)', lower_text)
    if match:
        start = match.end()
        chunk = lower_text[start:start+500]
        if 'physical activity' in chunk:
            physical_activity_papers.append(filename.replace('.txt', ''))

print("__RESULT__:")
print(json.dumps({
    "related_term_matches": len(candidates),
    "sample_related": candidates[:3],
    "physical_activity_papers_count": len(physical_activity_papers),
    "physical_activity_papers": physical_activity_papers[:3]
}))"""

env_args = {'var_function-call-12772568682444921532': 'file_storage/function-call-12772568682444921532.json', 'var_function-call-268740664748096753': 'file_storage/function-call-268740664748096753.json', 'var_function-call-17959813920400142644': 'file_storage/function-call-17959813920400142644.json', 'var_function-call-14824333924694724411': 'file_storage/function-call-14824333924694724411.json', 'var_function-call-6392359925411315977': {'food_papers_count': 0, 'food_papers': [], 'total_citations': 0}, 'var_function-call-4098618634540306182': {'debug_snippets': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_snippet': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\n'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_snippet': ' \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms \ndesign'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_snippet': '\nh.5.1. information interfaces and presentation (e.g., hci):\nanimations.\n\nauthor keywords\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nintroduction\nthe development of mob'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_snippet': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  bit  mor'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_snippet': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci): \nm'}], 'food_in_title': [], 'food_in_text_count': 3}, 'var_function-call-13263391832275722096': [], 'var_function-call-17173017883691100249': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo'}]}

exec(code, env_args)
