code = """import json
# var_call_2N3UiYD5P2T9axKCNxsaJHUD contains path to JSON file with citations results
path = var_call_2N3UiYD5P2T9axKCNxsaJHUD
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Extract titles (unique) and create filenames with .txt
titles = []
for rec in data:
    t = rec.get('title')
    if t is not None:
        titles.append(t)
# Deduplicate while preserving order
seen = set()
unique_titles = []
for t in titles:
    if t not in seen:
        seen.add(t)
        unique_titles.append(t)
# Create filenames list
filenames = [t + '.txt' for t in unique_titles]
# Print result as JSON string
out = json.dumps(filenames)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8vkhaVu1pkGIUfEvd5ODlci0': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_call_2N3UiYD5P2T9axKCNxsaJHUD': 'file_storage/call_2N3UiYD5P2T9axKCNxsaJHUD.json'}

exec(code, env_args)
