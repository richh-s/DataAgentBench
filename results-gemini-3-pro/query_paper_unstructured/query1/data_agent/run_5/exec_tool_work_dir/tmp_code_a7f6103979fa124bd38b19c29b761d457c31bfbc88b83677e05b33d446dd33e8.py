code = """import json
import re

# Load data
with open(locals()['var_function-call-9389645785727102603'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-14824333924694724411'], 'r') as f:
    citations = json.load(f)

food_papers = []
debug_info = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    lower_text = text.lower()
    
    # Try to find the keyword section
    match = re.search(r'(author\s+keywords|index\s+terms|keywords)', lower_text)
    
    is_food = False
    
    if match:
        start_pos = match.end()
        chunk = lower_text[start_pos:start_pos+1000]
        
        # Stop at next section
        stop_match = re.search(r'(introduction|acm classification|general terms)', chunk)
        if stop_match:
            keywords_text = chunk[:stop_match.start()]
        else:
            keywords_text = chunk
            
        # Check for 'food' as a whole word
        if re.search(r'\bfood\b', keywords_text):
            is_food = True
            debug_info.append(f"Found in keywords: {title}")
    
    # Also check if 'food' is in the title (just in case)
    if 'food' in title.lower():
         is_food = True
         debug_info.append(f"Found in title: {title}")

    if is_food:
        food_papers.append(title)

# Calculate citations
total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        try:
            total_citations += int(cit['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_papers_count": len(food_papers),
    "food_papers": food_papers,
    "total_citations": total_citations,
    "debug_info": debug_info
}))"""

env_args = {'var_function-call-12772568682444921532': 'file_storage/function-call-12772568682444921532.json', 'var_function-call-268740664748096753': 'file_storage/function-call-268740664748096753.json', 'var_function-call-17959813920400142644': 'file_storage/function-call-17959813920400142644.json', 'var_function-call-14824333924694724411': 'file_storage/function-call-14824333924694724411.json', 'var_function-call-6392359925411315977': {'food_papers_count': 0, 'food_papers': [], 'total_citations': 0}, 'var_function-call-4098618634540306182': {'debug_snippets': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_snippet': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci). \n\n'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_snippet': ' \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms \ndesign'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_snippet': '\nh.5.1. information interfaces and presentation (e.g., hci):\nanimations.\n\nauthor keywords\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nintroduction\nthe development of mob'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_snippet': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  bit  mor'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_snippet': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., hci): \nm'}], 'food_in_title': [], 'food_in_text_count': 3}, 'var_function-call-13263391832275722096': [], 'var_function-call-17173017883691100249': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-2160170955041264999': {'related_term_matches': 5, 'sample_related': [{'title': 'A Lived Informatics Model of Personal Informatics', 'found_terms': ['eating', 'meal', 'cooking']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'found_terms': ['eating', 'meal']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'found_terms': ['eating']}], 'physical_activity_papers_count': 1, 'physical_activity_papers': ['A Lived Informatics Model of Personal Informatics']}, 'var_function-call-9725508084601224667': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-3940284529366789218': 5, 'var_function-call-9389645785727102603': 'file_storage/function-call-9389645785727102603.json'}

exec(code, env_args)
