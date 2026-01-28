code = """import json

citations_file = locals()['var_function-call-8931525846963248243']
with open(citations_file, 'r') as f:
    citations = json.load(f)

papers_file = locals()['var_function-call-4192422070354728246']
with open(papers_file, 'r') as f:
    papers = json.load(f)

citation_titles = set([c['title'] for c in citations])

debug_info = []
count = 0
for p in papers:
    title = p['filename'][:-4]
    if title in citation_titles:
        debug_info.append({"title": title, "header": p['text'][:300]})
        count += 1
        if count >= 5:
            break

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-8931525846963248243': 'file_storage/function-call-8931525846963248243.json', 'var_function-call-17301308444494823963': {'count': 188, 'filenames': ['Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'SweatAtoms: Materializing Physical Activity.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Personal Informatics for Sport: Meaning, Body, and Social Relations in Amateur and Elite Athletes.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Crafting a View of Self-Tracking Data in the Clinical Visit.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations.txt']}, 'var_function-call-6838254019764142939': 'file_storage/function-call-6838254019764142939.json', 'var_function-call-4192422070354728246': 'file_storage/function-call-4192422070354728246.json', 'var_function-call-8855315205875236819': {'total_citations': 0, 'chi_paper_count': 0, 'sample_chi_papers': []}}

exec(code, env_args)
