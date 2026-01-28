code = """import json

# Get file paths
citations_path = locals()['var_function-call-14555610858560358239']
papers_path = locals()['var_function-call-71872959294259411']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    text_lower = text.lower()
    
    # Try to find keywords section
    keywords_start = text_lower.find('author keywords')
    if keywords_start == -1:
        keywords_start = text_lower.find('keywords')
    
    extracted_keywords = ""
    if keywords_start != -1:
        # Start searching after the label
        start_idx = keywords_start + 15 # approx len
        chunk = text_lower[start_idx:start_idx+1000]
        # Split by double newline using chr(10)
        parts = chunk.split(chr(10) + chr(10))
        extracted_keywords = parts[0]
        
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    # Check keywords for 'food' or 'diet' or 'nutrition' or 'eating'
    # The prompt specifically asked for 'food' domain.
    # The description lists "food" as a domain.
    # So I should look for the string "food" in the keywords.
    # I will also check for "diet", "nutrition" just in case.
    
    relevant = ['food'] # Strictly "food" based on description? 
    # Description: "Common domains include: 'food', 'physical activity'..."
    # So 'food' is the label.
    
    if not is_food:
        # Check keywords properly
        kws = [k.strip() for k in extracted_keywords.replace(';', ',').split(',')]
        for k in kws:
            if 'food' in k:
                is_food = True
                break
    
    if is_food:
        food_papers.append(title)

total_citations = 0
found_citations_count = 0
for c in citations:
    if c.get('title') in food_papers:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
            found_citations_count += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations,
    "paper_count": len(papers),
    "food_papers_count": len(food_papers),
    "food_papers_list": food_papers
}))"""

env_args = {'var_function-call-13801611410000855703': 'file_storage/function-call-13801611410000855703.json', 'var_function-call-13801611410000858480': ['Citations', 'sqlite_sequence'], 'var_function-call-14555610858560358239': 'file_storage/function-call-14555610858560358239.json', 'var_function-call-11640274332636556525': 'file_storage/function-call-11640274332636556525.json', 'var_function-call-9036090035766421574': 0, 'var_function-call-13667839510535967665': {'food_titles': [], 'sample_keywords': [{'title': 'A Lived Informatics Model of Personal Informatics', 'kw': ' \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity; finances; location. '}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'kw': ' \npersonal informatics, collection, reflection, model, barriers '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'kw': '\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'kw': ' \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; overactive bladder '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'kw': ' \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  '}], 'full_text_food_count': 3}, 'var_function-call-11646218085687772138': {'keywords_found': [], 'titles_found': [], 'total_unique_keywords_count': 28}, 'var_function-call-13565125768838552930': {'paper_count': 5, 'sample_texts_start': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali']}, 'var_function-call-71872959294259411': 'file_storage/function-call-71872959294259411.json'}

exec(code, env_args)
