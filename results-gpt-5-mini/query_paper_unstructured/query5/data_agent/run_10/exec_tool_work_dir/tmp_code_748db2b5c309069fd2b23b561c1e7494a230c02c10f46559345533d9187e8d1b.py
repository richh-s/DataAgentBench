code = """import json
# load variables from previous tool calls
filenames_docs = var_call_icO1Oq4g4SBiRpseWxt76dCq
citations = var_call_5ZpXYXlmWaMZgvcRENJkrQ3P

# extract filenames without .txt
chi_titles = [d['filename'].rsplit('.txt', 1)[0] for d in filenames_docs]
chi_set = set(chi_titles)

# build list of papers cited in 2020 that are CHI papers
results = []
total = 0
for rec in citations:
    title = rec['title']
    count = int(rec['total_citations']) if rec.get('total_citations') is not None else 0
    if title in chi_set:
        results.append({'title': title, 'total_citations_2020': count})
        total += count

output = {'papers_cited_in_2020': results, 'overall_total_citations_2020': total}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_icO1Oq4g4SBiRpseWxt76dCq': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_call_5ZpXYXlmWaMZgvcRENJkrQ3P': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': '77'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '98'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '16'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '52'}]}

exec(code, env_args)
