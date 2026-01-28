code = """import json

citations_file = locals()['var_function-call-8931525846963248243']
with open(citations_file, 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]
# deduplicate
filenames = list(set(filenames))

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-8931525846963248243': 'file_storage/function-call-8931525846963248243.json', 'var_function-call-17301308444494823963': {'count': 188, 'filenames': ['Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'SweatAtoms: Materializing Physical Activity.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Personal Informatics for Sport: Meaning, Body, and Social Relations in Amateur and Elite Athletes.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Crafting a View of Self-Tracking Data in the Clinical Visit.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations.txt']}}

exec(code, env_args)
