code = """import json
import pandas as pd

with open(locals()['var_function-call-1526931378206999654'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-543033747280973835'], 'r') as f:
    paper_docs = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce').fillna(0).astype(int)

paper_list = []
start_markers = ["author keywords", "index terms", "keywords"]
end_markers = ["acm classification", "introduction", "abstract", "general terms", "categories and subject"]

for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = doc.get('text', '').lower()
    
    domain_text = ""
    found_start = -1
    for sm in start_markers:
        idx = text.find(sm)
        if idx != -1:
            found_start = idx
            break
            
    if found_start != -1:
        start_search = found_start + 15
        best_end = len(text)
        found_end = False
        for em in end_markers:
            idx = text.find(em, start_search)
            if idx != -1 and idx < best_end:
                best_end = idx
                found_end = True
        
        if not found_end:
             best_end = min(len(text), start_search + 1000)
             
        domain_text = text[found_start:best_end]
    
    paper_list.append({
        'title': title,
        'domain_text': domain_text
    })

df_papers = pd.DataFrame(paper_list)

food_papers = df_papers[df_papers['domain_text'].str.contains('food', na=False)]

merged = pd.merge(food_papers, df_citations, on='title', how='inner')
total_citations = merged['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "total_citations": int(total_citations),
    "docs_processed": len(paper_docs),
    "food_papers_count": len(food_papers),
    "food_papers_titles": food_papers['title'].tolist()
}))"""

env_args = {'var_function-call-1526931378206999654': 'file_storage/function-call-1526931378206999654.json', 'var_function-call-1526931378207000783': 'file_storage/function-call-1526931378207000783.json', 'var_function-call-15304272311676446797': 'file_storage/function-call-15304272311676446797.json', 'var_function-call-11626738571080925771': 0, 'var_function-call-17087876279852164663': {'matches_count': 0, 'first_5_domains': ['author keywords \nlived informatics; personal informatics; self-tracking; \nlapsing; physical activity', 'author keywords \npersonal informatics, collection, reflection, model, barriers \n\n', 'author keywords\npersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\n', 'keywords \nmobile  health  applications;  assistive  technology;  co-design; \ninterviews; usability; ', 'author keywords \nwearable technology; dashboard; information visualization; \nstroke rehabilitation; '], 'total_docs': 5}, 'var_function-call-9193027681353351219': {'citations_count': 1405, 'paper_docs_count': 5, 'paper_titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-543033747280973835': 'file_storage/function-call-543033747280973835.json'}

exec(code, env_args)
