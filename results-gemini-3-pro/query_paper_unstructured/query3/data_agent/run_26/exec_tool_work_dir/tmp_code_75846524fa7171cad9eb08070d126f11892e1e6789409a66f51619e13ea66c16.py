code = """import json
import re

# Load paper_docs
with open(locals()['var_function-call-1844431421063330575'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-11864637065263499194'], 'r') as f:
    citations = json.load(f)

# Helper to extract year
def extract_year(text):
    # Look for 4 digit year in first 2000 chars
    head = text[:3000]
    # Regex for year 2000-2029. 
    # Often appears as "CHI '18" -> need to handle that?
    # "UBICOMP '15"
    # "Copyright 2015"
    # "September 7-11, 2015"
    
    # Strategy 1: Find 4 digit years
    years = re.findall(r'\b(20[0-2][0-9])\b', head)
    if years:
        # Return the first reasonable year found?
        # Sometimes the first one is the copyright year, which is usually the publication year.
        return int(years[0])
    
    # Strategy 2: Find 'YY (e.g. '15)
    # This is risky as '15 could be anything. But usually "Conference 'YY"
    return None

# Helper to check contribution
def check_contribution(text):
    return "empirical" in text.lower()

# Process papers
matching_titles = []
debug_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    year = extract_year(text)
    is_empirical = check_contribution(text)
    
    if year is not None and year > 2016 and is_empirical:
        matching_titles.append(title)
        debug_info.append({"title": title, "year": year, "empirical": is_empirical})

# Filter citations
citation_counts = {}
for cit in citations:
    t = cit['title']
    c = int(cit['citation_count'])
    if t in matching_titles:
        citation_counts[t] = citation_counts.get(t, 0) + c

# Format result
result = []
for title in matching_titles:
    result.append({
        "title": title,
        "total_citation_count": citation_counts.get(title, 0)
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14741953591797828167': ['paper_docs'], 'var_function-call-14741953591797829382': ['Citations', 'sqlite_sequence'], 'var_function-call-2114113704500066494': 'file_storage/function-call-2114113704500066494.json', 'var_function-call-2114113704500064987': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-1844431421063330575': 'file_storage/function-call-1844431421063330575.json', 'var_function-call-11864637065263499194': 'file_storage/function-call-11864637065263499194.json'}

exec(code, env_args)
