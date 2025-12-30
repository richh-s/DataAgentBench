code = """import json
from collections import Counter

try:
    with open(locals()['var_function-call-17235522576117083875'], 'r') as f:
        papers = json.load(f)

    total_papers = len(papers)
    keyword_counter = Counter()

    for p in papers:
        text = p.get('text', '').lower()
        kwd_start = text.find('author keywords')
        if kwd_start == -1:
            kwd_start = text.find('keywords \n') # try with newline
        
        if kwd_start != -1:
            candidates = []
            for marker in ['acm classification', 'introduction', 'general terms', 'abstract', 'ccs concepts', '\n\n']:
                idx = text.find(marker, kwd_start + 15)
                if idx != -1:
                    candidates.append(idx)
            
            if candidates:
                kwd_end = min(candidates)
            else:
                kwd_end = kwd_start + 300
                
            block = text[kwd_start:kwd_end]
            # simple cleanup
            clean_block = ""
            for char in block:
                if char.isalnum() or char in [';', ',', ' ', '\n', '-']:
                    clean_block += char
            
            parts = clean_block.replace('author keywords', '').replace('keywords', '').replace('\n', ';').replace(',', ';').split(';')
            for part in parts:
                k = part.strip()
                if len(k) > 2:
                    keyword_counter[k] += 1

    print("__RESULT__:")
    print(json.dumps({
        "total_papers": total_papers,
        "top_keywords": keyword_counter.most_common(50)
    }))
except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-5786904885440834537': 'file_storage/function-call-5786904885440834537.json', 'var_function-call-5786904885440834028': ['Citations', 'sqlite_sequence'], 'var_function-call-17235522576117083875': 'file_storage/function-call-17235522576117083875.json', 'var_function-call-17235522576117081446': 'file_storage/function-call-17235522576117081446.json', 'var_function-call-10431991474880319321': {'food_paper_count': 0, 'total_citations': 0, 'matched_citation_records': 0, 'sample_food_titles': []}, 'var_function-call-3610987394290696059': {'count_food_in_text': 3, 'examples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'food_snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti', 'keywords_snippet': 'keywords \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. \n\nacm classification keywords \nh.5.m. information interfaces and presentation (e.g., '}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'food_snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr', 'keywords_snippet': 'keywords \npersonal informatics, collection, reflection, model, barriers \n\nacm classification keywords \nh5.m.  information  interfaces  and  presentation  (e.g.,  hci): \nmiscellaneous.  \n\ngeneral terms'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'food_snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo', 'keywords_snippet': 'keywords \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder \n\nacm reference format: \n\nana-maria  salai  and  lynne  baillie.  2019.  a  wee  '}]}}

exec(code, env_args)
