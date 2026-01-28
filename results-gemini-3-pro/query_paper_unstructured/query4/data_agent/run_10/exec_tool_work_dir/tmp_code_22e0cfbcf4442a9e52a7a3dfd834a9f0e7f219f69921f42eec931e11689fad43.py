code = """import json

# Load papers
with open(locals()['var_function-call-14412117665521451328'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-14412117665521453199'], 'r') as f:
    citations = json.load(f)

target_year = "2016"
target_domain = "physical activity"
matched_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check year in first 1000 chars
    # We look for 2016. 
    # To be safer, we can check for "Copyright 2016" or conference headers.
    # But simple check is often sufficient for these datasets.
    header = text[:1000]
    
    # Check domain in full text (case insensitive)
    if target_domain.lower() in text.lower():
        # Check year
        if target_year in header:
             matched_titles.append(title)

# Filter citations
results = {}
for c in citations:
    c_title = c['title']
    if c_title in matched_titles:
        count = int(c['citation_count'])
        if c_title not in results:
            results[c_title] = 0
        results[c_title] += count

# Prepare final list
final_list = []
for title in matched_titles:
    # Use the computed count, or 0 if no citations found
    count = results.get(title, 0)
    final_list.append({"title": title, "citation_count": count})

print("__RESULT__:")
print(json.dumps(final_list))"""

env_args = {'var_function-call-16010210468405756630': 'file_storage/function-call-16010210468405756630.json', 'var_function-call-16010210468405758491': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10417048927437287642': 'file_storage/function-call-10417048927437287642.json', 'var_function-call-14412117665521451328': 'file_storage/function-call-14412117665521451328.json', 'var_function-call-14412117665521453199': 'file_storage/function-call-14412117665521453199.json'}

exec(code, env_args)
