code = """import json
import re

# Load papers
with open(locals()['var_function-call-14023155913287027792'], 'r') as f:
    papers_data = json.load(f)

print("__RESULT__:")
print(f"Total papers: {len(papers_data)}")
if len(papers_data) > 0:
    print(f"Keys in a doc: {papers_data[0].keys()}")

count_year_found = 0
count_year_gt_2016 = 0
count_empirical = 0
count_empirical_and_gt_2016 = 0

examples = []

for doc in papers_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Extract Year
    year = None
    copy_match = re.search(r'Copyright\s.*?(\d{4})', text[:5000], re.IGNORECASE)
    if copy_match:
        year = int(copy_match.group(1))
    
    if not year:
        # Check specific conference pattern
        # e.g. "CHI '19"
        header_match = re.search(r"[A-Z]+\s+'(\d{2})", text[:500])
        if header_match:
            y_short = int(header_match.group(1))
            year = 2000 + y_short

    if not year:
        year_match = re.search(r'\b(20\d\d)\b', text[:1000])
        if year_match:
            year = int(year_match.group(1))

    # Extract Contribution
    is_empirical = "empirical" in text.lower()
    
    if year:
        count_year_found += 1
        if year > 2016:
            count_year_gt_2016 += 1
    
    if is_empirical:
        count_empirical += 1
        
    if year and year > 2016 and is_empirical:
        count_empirical_and_gt_2016 += 1
        examples.append({"title": title, "year": year, "is_empirical": is_empirical})

print(f"Years found: {count_year_found}")
print(f"Years > 2016: {count_year_gt_2016}")
print(f"Empirical found: {count_empirical}")
print(f"Both found: {count_empirical_and_gt_2016}")
print(f"Example matches: {examples[:3]}")

# Check if 'empirical' is the right word.
# Maybe I should check for 'contribution: empirical' specifically?
# Let's check a paper that has 'empirical' in text but maybe year is wrong or vice versa."""

env_args = {'var_function-call-15870197178321181346': 'file_storage/function-call-15870197178321181346.json', 'var_function-call-15870197178321180761': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-5877010014911458978': 'file_storage/function-call-5877010014911458978.json', 'var_function-call-15161005825129355678': 'file_storage/function-call-15161005825129355678.json', 'var_function-call-14023155913287027792': 'file_storage/function-call-14023155913287027792.json', 'var_function-call-14333893458989342011': []}

exec(code, env_args)
