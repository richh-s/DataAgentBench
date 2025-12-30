code = """import json
import re

with open(locals()['var_function-call-17959813920400142644'], 'r') as f:
    paper_docs = json.load(f)

candidates = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    lower_text = text.lower()
    
    matches = [m.start() for m in re.finditer(r'\bfood\b', lower_text)]
    if matches:
        contexts = []
        for m in matches:
            start = max(0, m - 50)
            end = min(len(lower_text), m + 50)
            contexts.append(lower_text[start:end])
        
        candidates.append({
            "title": filename.replace('.txt', ''),
            "contexts": contexts
        })

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-12772568682444921532': 'file_storage/function-call-12772568682444921532.json', 'var_function-call-268740664748096753': 'file_storage/function-call-268740664748096753.json', 'var_function-call-17959813920400142644': 'file_storage/function-call-17959813920400142644.json', 'var_function-call-14824333924694724411': 'file_storage/function-call-14824333924694724411.json', 'var_function-call-6392359925411315977': {'food_papers_count': 0, 'food_papers': [], 'total_citations': 0}, 'var_function-call-4098618634540306182': {'debug_snippets': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_snippet': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\n'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_snippet': ' \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms \ndesign'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_snippet': '\nh.5.1. information interfaces and presentation (e.g., hci):\nanimations.\n\nauthor keywords\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nintroduction\nthe development of mob'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_snippet': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  bit  mor'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_snippet': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci): \nm'}], 'food_in_title': [], 'food_in_text_count': 3}}

exec(code, env_args)
