code = """import json

paper_file = locals()['var_function-call-1166448778177815195']
with open(paper_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers loaded: {len(papers)}")
print(f"First 5 filenames: {[p.get('filename') for p in papers[:5]]}")

# Check for Sundroid
sundroid = "Sundroid: Solar Radiation Awareness with Smartphones.txt"
found = any(p.get('filename') == sundroid for p in papers)
print(f"Sundroid found: {found}")

print("__RESULT__:")
print(len(papers))"""

env_args = {'var_function-call-5680722423366514432': ['Citations', 'sqlite_sequence'], 'var_function-call-5680722423366516433': 'file_storage/function-call-5680722423366516433.json', 'var_function-call-5680722423366514338': 'file_storage/function-call-5680722423366514338.json', 'var_function-call-1825670630710000632': 'file_storage/function-call-1825670630710000632.json', 'var_function-call-1380767849587936819': 188, 'var_function-call-5679032680150065306': 'file_storage/function-call-5679032680150065306.json', 'var_function-call-15107492987324530466': 'file_storage/function-call-15107492987324530466.json', 'var_function-call-1166448778177815195': 'file_storage/function-call-1166448778177815195.json', 'var_function-call-9559692353416114931': 16, 'var_function-call-7715102912328110353': {'total_cited_titles': 188, 'papers_found_in_mongo': 4, 'skipped_samples': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}]}}

exec(code, env_args)
