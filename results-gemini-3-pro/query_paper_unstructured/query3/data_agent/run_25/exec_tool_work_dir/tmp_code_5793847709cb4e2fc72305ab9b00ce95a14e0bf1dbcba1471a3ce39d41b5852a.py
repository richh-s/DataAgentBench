code = """import json
import re

with open(locals()['var_function-call-4539730163481461020'], 'r') as f:
    docs = json.load(f)

papers = []
for doc in docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract year
    # Look in the first 1000 characters
    header = text[:1000]
    years = re.findall(r"(20\d{2})", header)
    year = int(years[0]) if years else 0
    
    # Check for empirical
    # Check full text
    text_lower = text.lower()
    has_empirical = "empirical" in text_lower
    has_study = "study" in text_lower or "studies" in text_lower
    has_participants = "participant" in text_lower
    
    papers.append({
        "title": title,
        "year": year,
        "has_empirical": has_empirical,
        "has_study": has_study,
        "has_participants": has_participants
    })

# Filter
filtered = [p for p in papers if p['year'] > 2016]

print("__RESULT__:")
print(json.dumps({
    "total_docs": len(docs),
    "docs_after_2016": len(filtered),
    "docs_after_2016_with_empirical": len([p for p in filtered if p['has_empirical']]),
    "docs_after_2016_with_study": len([p for p in filtered if p['has_study']]),
    "examples_empirical": [p['title'] for p in filtered if p['has_empirical']][:5]
}))"""

env_args = {'var_function-call-4403390195297864469': 'file_storage/function-call-4403390195297864469.json', 'var_function-call-5079307557547688021': ['paper_docs'], 'var_function-call-3097430276196367090': 'file_storage/function-call-3097430276196367090.json', 'var_function-call-5206321841837773326': {'has_empirical': False, 'has_survey': True, 'has_interview': True, 'has_study': True}, 'var_function-call-3687296208506163854': [], 'var_function-call-5857355116469077971': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-4539730163481461020': 'file_storage/function-call-4539730163481461020.json'}

exec(code, env_args)
