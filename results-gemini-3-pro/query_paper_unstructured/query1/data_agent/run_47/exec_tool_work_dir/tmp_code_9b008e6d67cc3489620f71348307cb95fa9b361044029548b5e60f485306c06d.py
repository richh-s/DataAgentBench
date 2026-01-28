code = """import json

papers_path = locals()['var_function-call-15077613833019679981']
with open(papers_path, 'r') as f:
    papers = json.load(f)

keywords_list = []
food_in_keywords_count = 0

for p in papers:
    text_lower = p['text'].lower()
    idx = text_lower.find("author keywords")
    if idx == -1:
        idx = text_lower.find("index terms")
    
    if idx != -1:
        # Extract next 300 chars
        snippet = p['text'][idx:idx+300]
        keywords_list.append(snippet)
        if "food" in snippet.lower():
            food_in_keywords_count += 1

print("__RESULT__:")
print(json.dumps({
    "sample_keywords": keywords_list[:5],
    "total_papers_with_keywords": len(keywords_list),
    "food_in_keywords_count": food_in_keywords_count
}))"""

env_args = {'var_function-call-14405582414403684106': ['paper_docs'], 'var_function-call-14405582414403686195': ['Citations', 'sqlite_sequence'], 'var_function-call-1273577479453038261': 'file_storage/function-call-1273577479453038261.json', 'var_function-call-1273577479453039900': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15077613833019679981': 'file_storage/function-call-15077613833019679981.json', 'var_function-call-15077613833019680274': 'file_storage/function-call-15077613833019680274.json', 'var_function-call-3637328086309733464': 0, 'var_function-call-3175997620453810825': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'context': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti', 'keywords': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation '}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'context': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr', 'keywords': 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGenera'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'context': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo', 'keywords': ''}]}

exec(code, env_args)
