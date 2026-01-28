code = """import json
import re

papers_file = 'var_function-call-7300462932011158786.json'

try:
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    debug_info = []
    for i, doc in enumerate(papers[:10]):
        text = doc.get('text', '')
        header = text[:1000]
        
        # Check Year
        # Loose regex for any year-like number
        years_found = re.findall(r'\b(20\d{2})\b', header)
        short_years_found = re.findall(r"'(\d{2})\b", header)
        
        # Check Empirical
        has_empirical = "empirical" in text.lower()
        
        debug_info.append({
            "filename": doc['filename'],
            "years_found": years_found,
            "short_years_found": short_years_found,
            "has_empirical": has_empirical,
            "text_preview": text[:200].replace('\n', ' ')
        })

    print("__RESULT__:")
    print(json.dumps(debug_info))
    
except Exception as e:
    print(f"Error: {e}")
    print("__RESULT__:")
    print(json.dumps("error"))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete', 'var_function-call-17779314564341058459': []}

exec(code, env_args)
