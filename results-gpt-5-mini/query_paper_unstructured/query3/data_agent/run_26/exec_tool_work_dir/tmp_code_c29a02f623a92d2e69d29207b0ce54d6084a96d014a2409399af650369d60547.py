code = """import json
# Load high-citation titles
cpath = var_call_Fbew8OIrgqmwayysk6deEoHM
with open(cpath, 'r', encoding='utf-8') as f:
    high_cit = json.load(f)

# We'll attempt to find among these which have 'empirical' in their corresponding paper_docs
# Load one of the earlier mongo dumps to search
m_path = var_call_mB4p9sAq4lpFrwci3VV5sX6H
with open(m_path, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)

import re
matches = []
for entry in high_cit:
    title = entry['title']
    # find mongo record by filename
    fname = title + '.txt'
    rec = next((r for r in mongo_records if r.get('filename')==fname), None)
    if not rec:
        # try case-insensitive
        rec = next((r for r in mongo_records if r.get('filename','').lower()==fname.lower()), None)
    if rec:
        text = rec.get('text','')
        if re.search(r'\b(empir|empirical|empirically)\b', text, re.IGNORECASE):
            # find year
            my = re.search(r'20(1[7-9]|2[0-4])', text)
            year = int(my.group(0)) if my else None
            if year and year>2016:
                matches.append({'title': title, 'year': year, 'total_citations': int(entry['total_citations'])})

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_a50SROerJh7cg2CaFPe5HUSq': ['paper_docs'], 'var_call_8DV18aV221C1QGLy9PTJoWRD': ['Citations', 'sqlite_sequence'], 'var_call_qdPezJyiGQ882BWNhhrL3cAR': 'file_storage/call_qdPezJyiGQ882BWNhhrL3cAR.json', 'var_call_bMZXN2lTUc5GRRtVj2EHltEd': [], 'var_call_mB4p9sAq4lpFrwci3VV5sX6H': 'file_storage/call_mB4p9sAq4lpFrwci3VV5sX6H.json', 'var_call_HGxkZwdlqYp7msjXWFNaJEEP': [], 'var_call_kMdGe3WrYqAfYtDfi7WKRa1Q': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'empirical_found': False, 'year_found': 2019, 'preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'empirical_found': False, 'year_found': None, 'preview': 'Barriers and Negative Nudges:  \nExploring Challenges in Food Journaling   \nFelicia Cordeiro1, Daniel A. Epstein1, Edison Thomaz3, Elizabeth Bales1,2, \nArvind K. Jagannathan3, Gregory D. Abowd3, James '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'empirical_found': False, 'year_found': None, 'preview': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastna'}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'empirical_found': False, 'year_found': None, 'preview': 'Closing the Gap: Supporting Patients’ Transition  \nto Self-Management after Hospitalization \n Ari H Pollack1,2, Uba Backonja4, Andrew D. Miller4, Sonali R. Mishra3, Maher Khelifi4,  \nLogan Kendall4, a'}, {'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Common Barriers to the Use of Patient-Generated Data\nAcross Clinical Settings\nPeter West1, Max Van Kleek2, Richard Giordano1, Mark J. Weal3, Nigel Shadbolt2\n2Dept. of Computer Science\nUniversity of Ox'}, {'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'empirical_found': False, 'year_found': 2019, 'preview': 'Communicating Uncertainty in Fertility Prognosis\n\nHanna Schneider\nLMU Munich\nhanna.schneider@ifi.lmu.de\n\nMariam Hassib\nBundeswehr University Munich\nmariam.hassib@unibw.de\n\nJulia Wayrauther\nLMU Munich\n'}, {'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'empirical_found': False, 'year_found': 2017, 'preview': 'Computational Approaches Toward\nIntegrating Quantiﬁed Self Sensing and Social Media\nMunmun De Choudhury\nMrinal Kumar\nGeorgia Institute of\nGeorgia Institute of\nTechnology\nTechnology\nAtlanta, GA 30332 U'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Does Journaling Encourage Healthier Choices?\nAnalyzing Healthy Eating Behaviors of Food Journalers\n\nPalakorn Achananuparp\nSingapore Management University\nSingapore, Singapore\npalakorna@smu.edu.sg\n\nEe-'}, {'filename': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'empirical_found': False, 'year_found': 2018, 'preview': 'Entangled with Numbers: Quantified Self  \nand Others in a Team-Based Online Game  \n\nYUBO KOU, Florida State University, USA \nXINNING GUI, University of California, Irvine, USA \n\nQuantification  is  a '}], 'var_call_NdlxHcu3fDHa7h5jPPnFPD3Y': 'file_storage/call_NdlxHcu3fDHa7h5jPPnFPD3Y.json', 'var_call_sZ8QRMzxnj4hHRAuaAUs7og6': 'file_storage/call_sZ8QRMzxnj4hHRAuaAUs7og6.json', 'var_call_Q3vcQuNUCPTeDpy7DuZax7iu': 'file_storage/call_Q3vcQuNUCPTeDpy7DuZax7iu.json', 'var_call_QVgYaD7kBOFABEcLSmn0WbD6': [], 'var_call_M5XBGOSI05fheXtlGhWrkoID': [{'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study', 'total_citations': '231'}], 'var_call_oEysfBicsEI3ZEGo6lNzJBDK': [], 'var_call_H3Q0lCRr0WOaiYuNbQIKcss7': [], 'var_call_w7bjIj4MznfHdxIb3Q5G6gRh': [], 'var_call_VJJa9iMv6S5MKxG80tn6ARWM': [], 'var_call_Fbew8OIrgqmwayysk6deEoHM': 'file_storage/call_Fbew8OIrgqmwayysk6deEoHM.json'}

exec(code, env_args)
