code = """import json

with open(locals()['var_function-call-10170891781232486104'], 'r') as f:
    papers = json.load(f)

results = []
for p in papers:
    idx = p['text'].find('2016')
    if idx != -1 and idx < 5000:
        # Get context
        start = max(0, idx - 50)
        end = min(len(p['text']), idx + 50)
        context = p['text'][start:end]
        results.append({"filename": p['filename'], "context": context})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3386748849417591379': 'file_storage/function-call-3386748849417591379.json', 'var_function-call-10170891781232486104': 'file_storage/function-call-10170891781232486104.json', 'var_function-call-3802665463089483117': [], 'var_function-call-1764232359799178053': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'snippet': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'}], 'var_function-call-1572118856094614173': [], 'var_function-call-13823077288244029395': [], 'var_function-call-6093602271974842484': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'index_of_2016': 49375, 'total_length': 54376}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'index_of_2016': 65587, 'total_length': 74850}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'index_of_2016': 3015, 'total_length': 30774}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'index_of_2016': 13642, 'total_length': 85065}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'index_of_2016': 3195, 'total_length': 19552}]}

exec(code, env_args)
