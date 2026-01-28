code = """import json
import re

# Load papers
with open(locals()['var_function-call-3535475471263660703'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-3656629748920796517'], 'r') as f:
    citations = json.load(f)

# Organize citations by title
citation_map = {}
for cit in citations:
    t = cit['title']
    c = cit['citation_count']
    if t not in citation_map:
        citation_map[t] = 0
    citation_map[t] += int(c)

results = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain: "physical activity" in text (case insensitive)
    # The prompt implies domain extraction. 
    # Usually keywords are in the first page. Let's check first 5000 chars.
    header_text = text[:5000].lower()
    
    if "physical activity" in header_text:
        # Check year 2016
        # Look for 2016 in the first 1000 chars (header)
        # We look for "2016" or "'16" associated with a venue or date.
        # But simply "2016" in the header is a strong signal of publication year.
        # Be careful of citations to 2016 papers in the text, but citations usually appear later or in small font (footnotes).
        # Headers usually are at the very top.
        top_text = text[:1000]
        # Regex for 2016.
        if "2016" in top_text:
            # We have a candidate.
            total_citations = citation_map.get(title, 0)
            results.append({"title": title, "total_citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3353327849135623283': ['paper_docs'], 'var_function-call-3353327849135620318': ['Citations', 'sqlite_sequence'], 'var_function-call-869967969559808981': 'file_storage/function-call-869967969559808981.json', 'var_function-call-869967969559806992': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3535475471263660703': 'file_storage/function-call-3535475471263660703.json', 'var_function-call-3656629748920796517': 'file_storage/function-call-3656629748920796517.json'}

exec(code, env_args)
