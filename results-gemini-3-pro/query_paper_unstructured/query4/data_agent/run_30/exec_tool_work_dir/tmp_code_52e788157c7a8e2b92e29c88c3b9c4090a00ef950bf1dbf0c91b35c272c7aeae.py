code = """import json

with open(locals()['var_function-call-10170891781232486104'], 'r') as f:
    papers = json.load(f)

titles_2016 = []
for p in papers:
    # Check if '2016' is in the first 5000 characters
    # This avoids picking up references at the end
    if '2016' in p['text'][:5000]:
        # Optional: Check if 'physical activity' is in the text (it is, from query)
        # But maybe check if it's in the first part of the text?
        # The prompt says "domain: ... physical activity".
        # I'll keep all papers returned by the query that are from 2016.
        # But I should double check if "physical activity" is actually a domain.
        # Given the query filtered for "physical activity", I'll assume it's relevant.
        titles_2016.append(p['filename'].replace('.txt', ''))

print(f"Found {len(titles_2016)} papers from 2016.")
print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-3386748849417591379': 'file_storage/function-call-3386748849417591379.json', 'var_function-call-10170891781232486104': 'file_storage/function-call-10170891781232486104.json', 'var_function-call-3802665463089483117': [], 'var_function-call-1764232359799178053': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'snippet': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'}], 'var_function-call-1572118856094614173': [], 'var_function-call-13823077288244029395': [], 'var_function-call-6093602271974842484': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'index_of_2016': 49375, 'total_length': 54376}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'index_of_2016': 65587, 'total_length': 74850}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'index_of_2016': 3015, 'total_length': 30774}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'index_of_2016': 13642, 'total_length': 85065}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'index_of_2016': 3195, 'total_length': 19552}], 'var_function-call-13073936229223165813': [{'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'context': "ons from Permissions@acm.org. \nCHI'16, May 07-12, 2016, San Jose, CA, USA  \n© 2016 ACM. ISBN 978-1-4"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'context': 'Request permissions from Permissions@acm.org. \nAH 2016, February 25-27, 2016, Geneva, Switzerland \n©'}]}

exec(code, env_args)
