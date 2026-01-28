code = """import json

file_path = locals()['var_function-call-7710092852733637321']
with open(file_path, 'r') as f:
    papers = json.load(f)

results = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    snippet = text[:300].replace('\n', ' ')
    has_2016 = '2016' in text
    has_pa = 'physical activity' in text.lower()
    results.append({
        "filename": filename,
        "snippet": snippet,
        "has_2016": has_2016,
        "has_pa": has_pa
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8028739805573563198': ['paper_docs'], 'var_function-call-8028739805573566195': ['Citations', 'sqlite_sequence'], 'var_function-call-12468047497345130248': 'file_storage/function-call-12468047497345130248.json', 'var_function-call-7710092852733637321': 'file_storage/function-call-7710092852733637321.json', 'var_function-call-2111382860012225725': [], 'var_function-call-13155499083960998977': {'total': 5, 'year_2016_count': 0, 'domain_pa_count': 4, 'both_count': 0, 'headers_sample': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-']}, 'var_function-call-2086119536635628987': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
