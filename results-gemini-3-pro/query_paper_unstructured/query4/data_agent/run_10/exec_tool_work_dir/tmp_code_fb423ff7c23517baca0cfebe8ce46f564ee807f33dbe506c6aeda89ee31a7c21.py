code = """import json

with open(locals()['var_function-call-14412117665521451328'], 'r') as f:
    papers = json.load(f)

count_domain = 0
count_year_1000 = 0
count_both = 0

sample_domain_matches = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '')
    
    has_domain = "physical activity" in text.lower()
    has_year = "2016" in text[:1000]
    
    if has_domain:
        count_domain += 1
        if len(sample_domain_matches) < 5:
            sample_domain_matches.append({"title": title, "header": text[:200]})
            
    if has_year:
        count_year_1000 += 1
        
    if has_domain and has_year:
        count_both += 1

print("__RESULT__:")
print(json.dumps({
    "count_domain": count_domain,
    "count_year_1000": count_year_1000,
    "count_both": count_both,
    "samples": sample_domain_matches
}))"""

env_args = {'var_function-call-16010210468405756630': 'file_storage/function-call-16010210468405756630.json', 'var_function-call-16010210468405758491': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10417048927437287642': 'file_storage/function-call-10417048927437287642.json', 'var_function-call-14412117665521451328': 'file_storage/function-call-14412117665521451328.json', 'var_function-call-14412117665521453199': 'file_storage/function-call-14412117665521453199.json', 'var_function-call-12849824086341018331': []}

exec(code, env_args)
