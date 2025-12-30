code = """import json
import re

c_path = locals()['var_function-call-15796312403929804430']
p_path = locals()['var_function-call-93104423649467143']

with open(c_path, 'r') as f:
    c_data = json.load(f)

with open(p_path, 'r') as f:
    p_data = json.load(f)

# Build citation map
c_map = {}
for x in c_data:
    t = x['title']
    count = int(x['citation_count'])
    if t not in c_map:
        c_map[t] = 0
    c_map[t] += count

results = []
debug_info = {"total_papers": len(p_data), "gt_2016": 0, "empirical_match": 0}

for p in p_data:
    text = p['text']
    fname = p['filename']
    title = fname.replace('.txt', '')
    
    # Extract Year
    header = text[:1000]
    years = re.findall(r'20\d\d', header)
    pub_year = 0
    if years:
        y_ints = [int(y) for y in years]
        # Filter for plausible publication years (e.g., 2010-2025)
        # Avoid citation years which might be later, but usually appear in references (end of text)
        # Header years are usually the pub year.
        valid_years = [y for y in y_ints if 2010 <= y <= 2025]
        if valid_years:
            pub_year = min(valid_years)
    
    if pub_year > 2016:
        debug_info["gt_2016"] += 1
        # Check 'empirical'
        if 'empirical' in text.lower():
            debug_info["empirical_match"] += 1
            cit_count = c_map.get(title, 0)
            results.append({
                "title": title,
                "citation_count": cit_count
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7844967085086575341': 'file_storage/function-call-7844967085086575341.json', 'var_function-call-7844967085086573572': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-12278789652942674597': 'file_storage/function-call-12278789652942674597.json', 'var_function-call-15796312403929804430': 'file_storage/function-call-15796312403929804430.json', 'var_function-call-14593713414867433848': [], 'var_function-call-13454756578952752926': {'total_papers': 5, 'year_gt_2016': 0, 'empirical_in_text': 2, 'both': 0}, 'var_function-call-93104423649467143': 'file_storage/function-call-93104423649467143.json'}

exec(code, env_args)
