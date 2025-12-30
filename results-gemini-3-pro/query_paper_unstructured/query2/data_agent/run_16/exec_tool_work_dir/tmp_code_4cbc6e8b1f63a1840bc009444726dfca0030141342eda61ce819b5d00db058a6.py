code = """import json
import pandas as pd

citations_path = locals()['var_function-call-15068442808757462000']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)

papers_path = locals()['var_function-call-3821172634289075047']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

paper_texts = {}
for p in papers_data:
    if 'filename' in p and 'text' in p:
        title = p['filename'].replace('.txt', '')
        paper_texts[title] = p['text']

acm_citations = []
matched_count = 0

for index, row in df_citations.iterrows():
    title = row['title']
    try:
        count = int(row['citation_count'])
    except:
        continue
    
    if title in paper_texts:
        matched_count += 1
        text = paper_texts[title]
        # Check first 5000 chars for "ACM"
        if "ACM" in text[:5000]: 
            acm_citations.append(count)

if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {"average_citation_count": avg_citations, "num_acm_papers": len(acm_citations), "num_matched_papers": matched_count, "total_papers_fetched": len(papers_data)}
else:
    result = {"average_citation_count": 0, "num_acm_papers": 0, "num_matched_papers": matched_count, "total_papers_fetched": len(papers_data)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15068442808757462000': 'file_storage/function-call-15068442808757462000.json', 'var_function-call-15068442808757464883': 'file_storage/function-call-15068442808757464883.json', 'var_function-call-10205754986180600973': {'average_citation_count': 68.5, 'num_papers': 2}, 'var_function-call-15165036157903326656': {'num_citations': 158, 'num_papers': 5, 'sample_citation_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set'], 'sample_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'matching_titles_count': 2}, 'var_function-call-3821172634289075047': 'file_storage/function-call-3821172634289075047.json'}

exec(code, env_args)
