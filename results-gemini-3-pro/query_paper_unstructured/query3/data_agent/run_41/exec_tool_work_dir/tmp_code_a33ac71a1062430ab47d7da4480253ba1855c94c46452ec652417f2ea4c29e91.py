code = """import json
import re

papers_path = locals()['var_function-call-7300462932011158786']

info = {}

try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)

    info["total_papers"] = len(papers)
    
    if len(papers) > 0:
        doc = papers[0]
        text = doc.get('text', '')
        header = text[:500]
        info["header_repr"] = repr(header)
        
        matches = re.findall(r'\b20\d{2}\b', header)
        info["matches_20xx"] = matches
        
        matches_short = re.findall(r"'(\d{2})\b", header)
        info["matches_short"] = matches_short

except Exception as e:
    info["error"] = str(e)

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete', 'var_function-call-17779314564341058459': [], 'var_function-call-14079571341064099093': {'error': "[Errno 2] No such file or directory: 'var_function-call-7300462932011158786.json'"}, 'var_function-call-1918080602887774637': {'year_counts': {}, 'empirical_count': 2, 'after_2016_count': 0, 'both_count': 0}, 'var_function-call-7311144611923919482': 'debug_done'}

exec(code, env_args)
