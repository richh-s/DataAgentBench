code = """import json

# Load papers
with open(locals()['var_function-call-14019670930518450301'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-14019670930518453728'], 'r') as f:
    citations = json.load(f)

print(f"Total papers loaded: {len(papers)}")

food_titles = set()

for p in papers:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    text_lower = text.lower()
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    # Check keywords if not found in title
    if not is_food:
        kwd_start = text_lower.find('author keywords')
        if kwd_start == -1:
            kwd_start = text_lower.find('keywords')
            
        if kwd_start != -1:
            # Find end of block
            candidates = []
            for marker in ['acm classification', 'introduction', 'general terms', 'abstract', 'ccs concepts', '\n\n\n']:
                idx = text_lower.find(marker, kwd_start + 15)
                if idx != -1:
                    candidates.append(idx)
            
            if candidates:
                kwd_end = min(candidates)
            else:
                kwd_end = kwd_start + 500
                
            block = text_lower[kwd_start:kwd_end]
            if 'food' in block:
                is_food = True
    
    if is_food:
        food_titles.add(title)

print(f"Food papers found: {len(food_titles)}")
print(f"Food titles: {list(food_titles)}")

total_citations = 0
for c in citations:
    if c['title'] in food_titles:
        try:
            total_citations += int(c['citation_count'])
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_titles),
    "total_citations": total_citations
}))"""

env_args = {'var_function-call-5786904885440834537': 'file_storage/function-call-5786904885440834537.json', 'var_function-call-5786904885440834028': ['Citations', 'sqlite_sequence'], 'var_function-call-17235522576117083875': 'file_storage/function-call-17235522576117083875.json', 'var_function-call-17235522576117081446': 'file_storage/function-call-17235522576117081446.json', 'var_function-call-10431991474880319321': {'food_paper_count': 0, 'total_citations': 0, 'matched_citation_records': 0, 'sample_food_titles': []}, 'var_function-call-3610987394290696059': {'count_food_in_text': 3, 'examples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'food_snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti', 'keywords_snippet': 'keywords \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., '}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'food_snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr', 'keywords_snippet': 'keywords \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'food_snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo', 'keywords_snippet': 'keywords \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  '}]}, 'var_function-call-18190992027473448520': {'total_papers': 5, 'first_10_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'food_filenames': []}, 'var_function-call-14019670930518450301': 'file_storage/function-call-14019670930518450301.json', 'var_function-call-14019670930518453728': 'file_storage/function-call-14019670930518453728.json'}

exec(code, env_args)
