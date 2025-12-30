code = """import json
import re

file_path = locals()['var_function-call-4838891230296315133']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_list = []
for p in papers:
    text = p.get('text', '')
    chunk = text[:5000]
    years_strs = re.findall(r'\b(20\d{2})\b', chunk)
    years = [int(y) for y in years_strs]
    debug_list.append({"filename": p['filename'], "years_found": years})

print("__RESULT__:")
print(json.dumps(debug_list))"""

env_args = {'var_function-call-12813325699209905495': 'file_storage/function-call-12813325699209905495.json', 'var_function-call-4838891230296315133': 'file_storage/function-call-4838891230296315133.json', 'var_function-call-7940884221126680243': [], 'var_function-call-10237573905537353095': {'count': 5, 'first_paper_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'first_filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, 'var_function-call-3171940235740849659': []}

exec(code, env_args)
