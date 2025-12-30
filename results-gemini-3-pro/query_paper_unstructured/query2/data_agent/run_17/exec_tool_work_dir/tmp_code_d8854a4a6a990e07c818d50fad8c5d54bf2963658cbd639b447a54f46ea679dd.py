code = """import json

with open(locals()['var_function-call-161273639758194169'], 'r') as f:
    citations_2018 = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations_2018}

with open(locals()['var_function-call-4266321762780779682'], 'r') as f:
    papers = json.load(f)

matched = []
unmatched_samples = []

for p in papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    if title in citation_map:
        text = p.get('text', '')
        if 'ACM' in text:
            matched.append(title)
        else:
            if len(unmatched_samples) < 5:
                unmatched_samples.append({"title": title, "snippet": text[:500]})

print("__RESULT__:")
print(json.dumps({"matched_titles": matched, "unmatched_samples": unmatched_samples}))"""

env_args = {'var_function-call-161273639758194169': 'file_storage/function-call-161273639758194169.json', 'var_function-call-161273639758192992': 'file_storage/function-call-161273639758192992.json', 'var_function-call-13120840873059324966': {'count': 158, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set']}, 'var_function-call-447886293380607187': 'file_storage/function-call-447886293380607187.json', 'var_function-call-7481131308563480348': 'file_storage/function-call-7481131308563480348.json', 'var_function-call-4266321762780779682': 'file_storage/function-call-4266321762780779682.json', 'var_function-call-7357971864467483261': {'average_citations': 50.0, 'count_acm_papers': 1, 'total_citations_2018_papers': 158}}

exec(code, env_args)
