code = """import json
import re

file_path = locals()['var_function-call-1805963749802490353']
with open(file_path, 'r') as f:
    papers = json.load(f)

filtered_titles = []
# Expand search window to 5000 chars to catch copyright at bottom of first page
# Patterns
venue_pattern = re.compile(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*('16|2016)", re.IGNORECASE)
copyright_pattern = re.compile(r"(Copyright|©).{0,50}2016", re.IGNORECASE)
domain_pattern = re.compile(r"physical activity", re.IGNORECASE)

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Check domain in title or first 5000 chars
    if domain_pattern.search(filename) or domain_pattern.search(text[:5000]):
        # Check year in first 5000 chars
        header = text[:5000] 
        
        if venue_pattern.search(header) or copyright_pattern.search(header):
            title = filename.rsplit('.', 1)[0]
            filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-13658712290201137078': 'file_storage/function-call-13658712290201137078.json', 'var_function-call-1805963749802490353': 'file_storage/function-call-1805963749802490353.json', 'var_function-call-10638941931328606069': [], 'var_function-call-17350073314681680537': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header_snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header_snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header_snippet': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'}]}

exec(code, env_args)
