code = """import json

citations_path = locals()['var_function-call-14555610858560358239']
papers_path = locals()['var_function-call-11640274332636556525']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

keywords_of_interest = []
titles_of_interest = []

all_keywords = set()

relevant_terms = ['food', 'diet', 'nutrition', 'eating', 'meal', 'cooking']

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    text_lower = text.lower()
    
    # Extract keywords
    kw_header = 'author keywords'
    kw_start = text_lower.find(kw_header)
    offset = len(kw_header)
    if kw_start == -1:
        kw_header = 'keywords'
        kw_start = text_lower.find(kw_header)
        offset = len(kw_header)
    
    extracted_keywords = ""
    if kw_start != -1:
        start_idx = kw_start + offset
        chunk = text_lower[start_idx:start_idx+1000]
        parts = chunk.split(chr(10) + chr(10))
        extracted_keywords = parts[0]
        
        # Split individual keywords
        kws = [k.strip() for k in extracted_keywords.replace(';', ',').split(',')]
        for k in kws:
            all_keywords.add(k)
            for term in relevant_terms:
                if term in k:
                    keywords_of_interest.append({'title': title, 'keyword': k})
    
    # Check title
    for term in relevant_terms:
        if term in title.lower():
            titles_of_interest.append(title)

print("__RESULT__:")
print(json.dumps({
    "keywords_found": keywords_of_interest,
    "titles_found": titles_of_interest,
    "total_unique_keywords_count": len(all_keywords)
}))"""

env_args = {'var_function-call-13801611410000855703': 'file_storage/function-call-13801611410000855703.json', 'var_function-call-13801611410000858480': ['Citations', 'sqlite_sequence'], 'var_function-call-14555610858560358239': 'file_storage/function-call-14555610858560358239.json', 'var_function-call-11640274332636556525': 'file_storage/function-call-11640274332636556525.json', 'var_function-call-9036090035766421574': 0, 'var_function-call-13667839510535967665': {'food_titles': [], 'sample_keywords': [{'title': 'A Lived Informatics Model of Personal Informatics', 'kw': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. '}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'kw': ' \npersonal informatics, collection, reflection, model, barriers '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'kw': '\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'kw': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'kw': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  '}], 'full_text_food_count': 3}}

exec(code, env_args)
