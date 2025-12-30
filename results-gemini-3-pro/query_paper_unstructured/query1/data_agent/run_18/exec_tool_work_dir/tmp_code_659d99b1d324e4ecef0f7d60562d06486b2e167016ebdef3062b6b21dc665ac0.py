code = """import json
import pandas as pd
import re

citations_path = locals()['var_function-call-12584433843491866400']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)

papers_path = locals()['var_function-call-12191250202053504981']
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

newline = chr(10)
pattern = "Author Keywords(.*?)(?:ACM Classification|INTRODUCTION|General Terms|Index Terms|" + newline + newline + newline + ")"

food_titles = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    is_food = False
    
    # Check Title
    if 'food' in title.lower():
        is_food = True
    else:
        # Check Keywords
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            kw = match.group(1).lower()
            if 'food' in kw:
                is_food = True
    
    if is_food:
        food_titles.append(title)

food_citations = citations_df[citations_df['title'].isin(food_titles)]
total_citations = food_citations['citation_count'].sum()

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_titles),
    "total_citations": int(total_citations),
    "sample_titles": food_titles[:5]
}))"""

env_args = {'var_function-call-3783672913394696319': ['paper_docs'], 'var_function-call-3783672913394696700': ['Citations', 'sqlite_sequence'], 'var_function-call-272073867596597133': 'file_storage/function-call-272073867596597133.json', 'var_function-call-272073867596596742': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9679994414761045024': 'file_storage/function-call-9679994414761045024.json', 'var_function-call-12584433843491866400': 'file_storage/function-call-12584433843491866400.json', 'var_function-call-12584433843491866597': 'file_storage/function-call-12584433843491866597.json', 'var_function-call-3836062097239578025': {'food_paper_count': 0, 'total_citations': 0, 'sample_titles': []}, 'var_function-call-1933883333484097501': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'keywords_found': 'Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Locat', 'is_food': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'keywords_found': 'Personal informatics, collection, reflection, model, barriers', 'is_food': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'keywords_found': 'Personalization; animation; emotion; engagement; empathy; self-reﬂection.', 'is_food': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'keywords_found': 'None', 'is_food': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'keywords_found': 'Wearable technology; dashboard; information visualization;  stroke rehabilitation; occupational ther', 'is_food': False}], 'var_function-call-15046315751179438460': {'food_paper_count': 0, 'total_citations': 0, 'sample_titles': []}, 'var_function-call-11438704676541415212': {'count_title': 0, 'count_keywords': 0, 'count_abstract': 0, 'count_text': 3, 'sample_text_match_title': 'A Lived Informatics Model of Personal Informatics'}, 'var_function-call-1234210617771924849': ['_id', 'filename', 'text'], 'var_function-call-2172777175667348485': {'extracted_count': 4, 'top_keywords': [['personal informatics', 2], ['lived informatics', 1], ['self-tracking', 1], ['lapsing', 1], ['physical activity', 1], ['finances', 1], ['location.', 1], ['collection', 1], ['reflection', 1], ['model', 1], ['barriers', 1], ['personalization', 1], ['animation', 1], ['emotion', 1], ['engagement', 1], ['empathy', 1], ['self-reﬂection.', 1], ['wearable technology', 1], ['dashboard', 1], ['information visualization', 1], ['stroke rehabilitation', 1], ['occupational therapy', 1]], 'food_keyword_exact_count': 0, 'food_related_keywords': []}, 'var_function-call-17537928508705641539': 5, 'var_function-call-4523878923744202522': 1405, 'var_function-call-12191250202053504981': 'file_storage/function-call-12191250202053504981.json'}

exec(code, env_args)
