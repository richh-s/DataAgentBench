code = """import json

file_path = locals()['var_function-call-13998873614656470167']
with open(file_path, 'r') as f:
    papers = json.load(f)

food_titles = []
total_papers = len(papers)

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    if 'food' in title.lower():
        food_titles.append(title)
        continue
        
    lower_text = text.lower()
    
    kw_idx = lower_text.find("author keywords")
    if kw_idx == -1:
        kw_idx = lower_text.find(chr(10) + "keywords")
        if kw_idx == -1:
             kw_idx = lower_text.find(" keywords")
    
    if kw_idx != -1:
        snippet = lower_text[kw_idx:kw_idx+1000]
        
        end_idx = 1000
        for marker in ["introduction", "acm classification", "general terms", "abstract", chr(10)+chr(10)]:
             m_idx = snippet.find(marker)
             if m_idx != -1 and m_idx > 10:
                 end_idx = min(end_idx, m_idx)
        
        keywords = snippet[:end_idx]
        if 'food' in keywords:
            food_titles.append(title)

result = {
    "total_papers": total_papers,
    "food_titles": food_titles
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1852344882916152676': 'file_storage/function-call-1852344882916152676.json', 'var_function-call-1852344882916155297': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-17858895574398346247': 'file_storage/function-call-17858895574398346247.json', 'var_function-call-7066089185120334334': [], 'var_function-call-10665992474686830857': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-13998873614656470167': 'file_storage/function-call-13998873614656470167.json'}

exec(code, env_args)
