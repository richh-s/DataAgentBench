code = """import json

file_path = locals()['var_function-call-9186032532350029848']
with open(file_path, 'r') as f:
    papers = json.load(f)

print("Total papers:", len(papers))

food_titles_keywords = []
food_titles_text = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    text_lower = text.lower()
    
    # Keyword extraction
    keywords = ""
    start_idx = text_lower.find('author keywords')
    if start_idx == -1:
        start_idx = text_lower.find('index terms')
    
    if start_idx != -1:
        chunk = text_lower[start_idx:start_idx+1000]
        end_candidates = ['acm classification keywords', 'introduction', 'general terms', 'abstract']
        min_end = 1000
        for cand in end_candidates:
            end_idx = chunk.find(cand, 15)
            if end_idx != -1 and end_idx < min_end:
                min_end = end_idx
        keywords = chunk[:min_end]
        
    if 'food' in keywords:
        food_titles_keywords.append(title)
        
    if 'food' in text_lower:
        food_titles_text.append(title)

print("__RESULT__:")
print(json.dumps({
    "count_keywords": len(food_titles_keywords),
    "titles_keywords": food_titles_keywords,
    "count_text": len(food_titles_text),
    "titles_text_sample": food_titles_text[:5]
}))"""

env_args = {'var_function-call-16691690145892377259': 'file_storage/function-call-16691690145892377259.json', 'var_function-call-2784456045421474973': 'file_storage/function-call-2784456045421474973.json', 'var_function-call-6442636259754716830': [], 'var_function-call-18030104582321491684': {'food_in_text_count': 3, 'food_in_text_samples': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'], 'keyword_samples': ['Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation ', 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGenera', 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe development of mobile phone technology and biological\nsensors is enabling individuals to sel']}, 'var_function-call-16698546098495853563': 5, 'var_function-call-9186032532350029848': 'file_storage/function-call-9186032532350029848.json'}

exec(code, env_args)
