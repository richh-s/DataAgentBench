code = """import json
import re

citations_file = locals()['var_function-call-17226783687381058868']
papers_file = locals()['var_function-call-439047016334957359']
with open(citations_file, 'r') as f:
    citations = json.load(f)
with open(papers_file, 'r') as f:
    papers = json.load(f)

paper_map = {p['filename']: p['text'] for p in papers}
total = 0

for c in citations:
    fname = c['title'] + ".txt"
    if fname in paper_map:
        text = paper_map[fname]
        head = text[:3000]
        
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in head:
            is_chi = True
        elif re.search(r'CHI\s+\d{4}', head): 
            is_chi = True
        elif re.search(r'CHI\s+\'\d{2}', head): 
            is_chi = True
        
        if is_chi:
            total += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-17226783687381058868': 'file_storage/function-call-17226783687381058868.json', 'var_function-call-11445110573427865236': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"], 'var_function-call-12469297253673424923': 'file_storage/function-call-12469297253673424923.json', 'var_function-call-13349597544077869875': 'file_storage/function-call-13349597544077869875.json', 'var_function-call-5125539185123063334': {'count': 5}, 'var_function-call-7904490856032329911': 'file_storage/function-call-7904490856032329911.json', 'var_function-call-15190824524824419371': 0, 'var_function-call-2112808822247239442': 'file_storage/function-call-2112808822247239442.json', 'var_function-call-439047016334957359': 'file_storage/function-call-439047016334957359.json', 'var_function-call-3475495459262312372': 99, 'var_function-call-6871933481051541043': 'file_storage/function-call-6871933481051541043.json', 'var_function-call-4961367800834471654': 308, 'var_function-call-11368717807113238927': 68, 'var_function-call-2015243156271664619': 99, 'var_function-call-14727053952157562846': 'file_storage/function-call-14727053952157562846.json', 'var_function-call-17980830366504486511': '694f5530284b10b11dc0a8cb', 'var_function-call-18169912269323847632': [], 'var_function-call-13134514996454948942': [], 'var_function-call-4045758357375057140': ['A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Toward Health Information Technology That Supports Overweight/Obese Women in Addressing Emotion- and Stress-Related Eating.txt', 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study.txt'], 'var_function-call-7671210134703816620': [], 'var_function-call-1113903658818502583': [], 'var_function-call-13980772725484035801': 308, 'var_function-call-382763045374906216': 'Done'}

exec(code, env_args)
