code = """import json

path = locals()['var_function-call-16668750805844990908']
with open(path, 'r') as f:
    citations_data = json.load(f)

filenames = [x['title'] + ".txt" for x in citations_data]

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-16668750805844990908': 'file_storage/function-call-16668750805844990908.json', 'var_function-call-6116269667237026537': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"], 'var_function-call-8320557006357925662': 'file_storage/function-call-8320557006357925662.json', 'var_function-call-12101616537043613350': 188}

exec(code, env_args)
