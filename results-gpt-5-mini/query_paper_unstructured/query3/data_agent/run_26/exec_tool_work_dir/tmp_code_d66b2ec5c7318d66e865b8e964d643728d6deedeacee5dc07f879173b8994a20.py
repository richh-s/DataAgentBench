code = """import json, re, os
# Paths to mongo query result files (from previous calls)
paths = []
for key in ['var_call_NdlxHcu3fDHa7h5jPPnFPD3Y','var_call_sZ8QRMzxnj4hHRAuaAUs7og6','var_call_mB4p9sAq4lpFrwci3VV5sX6H','var_call_qdPezJyiGQ882BWNhhrL3cAR']:
    if key in globals():
        paths.append(globals()[key])

# Load citations aggregated totals
citations = []
if 'var_call_Q3vcQuNUCPTeDpy7DuZax7iu' in globals():
    with open(var_call_Q3vcQuNUCPTeDpy7DuZax7iu, 'r', encoding='utf-8') as f:
        citations = json.load(f)
title_to_citations = {c['title']: int(c['total_citations']) for c in citations}

found = []
seen_titles = set()
for path in paths:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        try:
            records = json.load(f)
        except Exception as e:
            continue
    for r in records:
        filename = r.get('filename','')
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        if title in seen_titles:
            continue
        seen_titles.add(title)
        text = r.get('text','') or ''
        # search for contribution mentions near 'contribution' or 'we contribute' lines
        empirical = False
        if re.search(r'\b(empir|empirical|empirically)\b', text, re.IGNORECASE):
            empirical = True
        # search for explicit 'Contribution' section
        contrib_section = None
        m = re.search(r'(?s)(contribution[s]?|we contribute|contributions)[:\s\-\n]+(.{0,500})', text, re.IGNORECASE)
        if m:
            contrib_section = m.group(0)
            if re.search(r'\b(empir|empirical|empirically)\b', contrib_section, re.IGNORECASE):
                empirical = True
        # find year occurrence 2017-2024 - pick earliest occurrence
        my = re.search(r'20(1[7-9]|2[0-4])', text)
        year = int(my.group(0)) if my else None
        if empirical and year and year>2016:
            total_cit = title_to_citations.get(title, 0)
            found.append({'title': title, 'year': year, 'total_citations': total_cit})

# Deduplicate and sort
found_sorted = sorted(found, key=lambda x: (-x['total_citations'], x['title']))

print('__RESULT__:')
print(json.dumps(found_sorted))"""

env_args = {'var_call_a50SROerJh7cg2CaFPe5HUSq': ['paper_docs'], 'var_call_8DV18aV221C1QGLy9PTJoWRD': ['Citations', 'sqlite_sequence'], 'var_call_qdPezJyiGQ882BWNhhrL3cAR': 'file_storage/call_qdPezJyiGQ882BWNhhrL3cAR.json', 'var_call_bMZXN2lTUc5GRRtVj2EHltEd': [], 'var_call_mB4p9sAq4lpFrwci3VV5sX6H': 'file_storage/call_mB4p9sAq4lpFrwci3VV5sX6H.json', 'var_call_HGxkZwdlqYp7msjXWFNaJEEP': [], 'var_call_kMdGe3WrYqAfYtDfi7WKRa1Q': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'empirical_found': False, 'year_found': 2019, 'preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'empirical_found': False, 'year_found': None, 'preview': 'Barriers and Negative Nudges:  \nExploring Challenges in Food Journaling   \nFelicia Cordeiro1, Daniel A. Epstein1, Edison Thomaz3, Elizabeth Bales1,2, \nArvind K. Jagannathan3, Gregory D. Abowd3, James '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'empirical_found': False, 'year_found': None, 'preview': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastna'}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'empirical_found': False, 'year_found': None, 'preview': 'Closing the Gap: Supporting Patients’ Transition  \nto Self-Management after Hospitalization \n Ari H Pollack1,2, Uba Backonja4, Andrew D. Miller4, Sonali R. Mishra3, Maher Khelifi4,  \nLogan Kendall4, a'}, {'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Common Barriers to the Use of Patient-Generated Data\nAcross Clinical Settings\nPeter West1, Max Van Kleek2, Richard Giordano1, Mark J. Weal3, Nigel Shadbolt2\n2Dept. of Computer Science\nUniversity of Ox'}, {'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'empirical_found': False, 'year_found': 2019, 'preview': 'Communicating Uncertainty in Fertility Prognosis\n\nHanna Schneider\nLMU Munich\nhanna.schneider@ifi.lmu.de\n\nMariam Hassib\nBundeswehr University Munich\nmariam.hassib@unibw.de\n\nJulia Wayrauther\nLMU Munich\n'}, {'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'empirical_found': False, 'year_found': 2017, 'preview': 'Computational Approaches Toward\nIntegrating Quantiﬁed Self Sensing and Social Media\nMunmun De Choudhury\nMrinal Kumar\nGeorgia Institute of\nGeorgia Institute of\nTechnology\nTechnology\nAtlanta, GA 30332 U'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Does Journaling Encourage Healthier Choices?\nAnalyzing Healthy Eating Behaviors of Food Journalers\n\nPalakorn Achananuparp\nSingapore Management University\nSingapore, Singapore\npalakorna@smu.edu.sg\n\nEe-'}, {'filename': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Entangled with Numbers: Quantified Self  \nand Others in a Team-Based Online Game  \n\nYUBO KOU, Florida State University, USA \nXINNING GUI, University of California, Irvine, USA \n\nQuantification  is  a '}], 'var_call_NdlxHcu3fDHa7h5jPPnFPD3Y': 'file_storage/call_NdlxHcu3fDHa7h5jPPnFPD3Y.json', 'var_call_sZ8QRMzxnj4hHRAuaAUs7og6': 'file_storage/call_sZ8QRMzxnj4hHRAuaAUs7og6.json', 'var_call_Q3vcQuNUCPTeDpy7DuZax7iu': 'file_storage/call_Q3vcQuNUCPTeDpy7DuZax7iu.json', 'var_call_QVgYaD7kBOFABEcLSmn0WbD6': [], 'var_call_M5XBGOSI05fheXtlGhWrkoID': [{'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study', 'total_citations': '231'}], 'var_call_oEysfBicsEI3ZEGo6lNzJBDK': [], 'var_call_H3Q0lCRr0WOaiYuNbQIKcss7': [], 'var_call_w7bjIj4MznfHdxIb3Q5G6gRh': []}

exec(code, env_args)
