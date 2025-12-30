code = """import json
import os

citations_var = locals()['var_function-call-2106421940036629061']
chi_papers_var = locals()['var_function-call-12904116397288956253']

# Load citations data
if isinstance(citations_var, str) and os.path.exists(citations_var):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

# Load CHI papers data
if isinstance(chi_papers_var, str) and os.path.exists(chi_papers_var):
    with open(chi_papers_var, 'r') as f:
        chi_papers = json.load(f)
else:
    chi_papers = chi_papers_var

# Create a set of CHI titles
chi_titles = set()
for p in chi_papers:
    fname = p.get('filename', '')
    if fname.endswith('.txt'):
        chi_titles.add(fname[:-4])
    else:
        chi_titles.add(fname)

# Filter citations and sum
total_citations = 0
count = 0
matched_titles = []

for record in citations_data:
    title = record['title']
    if title in chi_titles:
        try:
            val = int(record['citation_count'])
            total_citations += val
            count += 1
            matched_titles.append(title)
        except ValueError:
            pass

print(f"Number of CHI papers cited in 2020: {count}")
print(f"Total citation count: {total_citations}")
print(f"Matched titles: {matched_titles}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-2106421940036629061': 'file_storage/function-call-2106421940036629061.json', 'var_function-call-10975034147027654622': {'count': 188, 'filenames_preview': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"]}, 'var_function-call-8410670422247250246': 'file_storage/function-call-8410670422247250246.json', 'var_function-call-16527945425029861293': 'file_storage/function-call-16527945425029861293.json', 'var_function-call-3942142969729170768': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-13646251503415477728': 243, 'var_function-call-12522816240389371249': 'file_storage/function-call-12522816240389371249.json', 'var_function-call-9399173173343595409': 'file_storage/function-call-9399173173343595409.json', 'var_function-call-12904116397288956253': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
