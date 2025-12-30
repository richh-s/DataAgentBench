code = """import json
import re

file_path = locals()['var_function-call-1805963749802490353']
with open(file_path, 'r') as f:
    papers = json.load(f)

target_title = "Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt"
target_paper = next((p for p in papers if p['filename'] == target_title), None)

print("__RESULT__:")
if target_paper:
    text = target_paper['text']
    header = text[:5000]
    
    # Check Copyright regex
    copyright_pattern = re.compile(r"(Copyright|©)\s*(held by.*|ACM|IEEE)?\s*2016", re.IGNORECASE)
    match_c = copyright_pattern.search(header)
    
    # Check Venue regex
    venue_pattern = re.compile(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*('16|2016)", re.IGNORECASE)
    match_v = venue_pattern.search(header)
    
    # Check Domain regex
    domain_pattern = re.compile(r"physical activity", re.IGNORECASE)
    match_d = domain_pattern.search(target_title) or domain_pattern.search(header)
    
    print(json.dumps({
        "copyright_match": str(match_c) if match_c else "None",
        "venue_match": str(match_v) if match_v else "None",
        "domain_match": str(match_d) if match_d else "None",
        "copyright_snippet": text[match_c.start():match_c.end()] if match_c else "N/A"
    }))
else:
    print("Target paper not found.")"""

env_args = {'var_function-call-13658712290201137078': 'file_storage/function-call-13658712290201137078.json', 'var_function-call-1805963749802490353': 'file_storage/function-call-1805963749802490353.json', 'var_function-call-10638941931328606069': [], 'var_function-call-17350073314681680537': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'header_snippet': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'header_snippet': 'Beyond Behavior: The Coach’s Perspective \n on Technology in Health Coaching \n\nHeleen Rutjes \n Human-Technology Interaction \n Eindhoven University of Technology \n Eindhoven, the Netherlands \n H.Rutjes@tue.nl \n\nMartijn C. Willemsen \n Human-Technology Interaction \n Eindhoven University of Technology \n '}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'header_snippet': 'Charting Design Preferences on Wellness Wearables  \n\nJuho Rantakari1, Virve Inget2, Ashley Colley1, Jonna Häkkilä1 \n\n1University of Lapland \nYliopistokatu 8 \n96400 Rovaniemi, Finland \nfirstname.lastname@ulapland.fi \n\n2Center for Ubiquitous Computing \nP.O Box 4500 \n90014 University of Oulu, Finland \n'}], 'var_function-call-3264491478001736579': [], 'var_function-call-9028487827674499251': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'snippets': ['ng, François\n\nGuimbetiere, and Tanzeem Choudhury. 2016.\nEmotionCheck: leveraging bodily signals and ', 'k to regulate our emotions. In Proceedings of the\n2016 ACM International Joint Conference on Pervasi', 'l\nStorytelling. Springer, 38–43.\n\n24. Akane Sano. 2016. Measuring college students’ sleep,\nstress, m']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippets': ['Paul  Dendale,  Kris  Luyten  and  Karin \nConinx. 2016. Back on bike: the BoB mobile cycling app for', "Lumsden,  Rachel Shaw   and  Dympna  O'Sullivan. \n2016.  A  longitudinal evaluation  of  the  accept", 'ia Jacobs, James Clawson and Elizabeth D. Mynatt. 2016. A Cancer \nJourney  Framework:  Guiding  the ']}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'snippets': ["ons from Permissions@acm.org. \nCHI'16, May 07-12, 2016, San Jose, CA, USA  \n© 2016 ACM. ISBN 978-1-4", ". \nCHI'16, May 07-12, 2016, San Jose, CA, USA  \n© 2016 ACM. ISBN 978-1-4503-3362-7/16/05…$15.00  \nht", 'nsation).  Of  640 \n\nLiving Healthy#chi4good, CHI 2016, San Jose, CA, USA1109 \n \n \n\x0ccompleted  surve']}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'snippets': ['g \n\nonline \n\nand \n\nThe interviews, held in spring 2016, were semi-structured, \nand  conducted  by  o', ', UKPaper 670Page 5 \n\x0csession,  held  in  autumn  2016,  lasted  2  hours  and  was \nfacilitated  by', 'll  Dutch  student  sports \ncenters,  in  autumn  2016.  Two  clients,  recruited  by  the \nauthors,']}, {'title': 'Charting Design Preferences on Wellness Wearables.txt', 'snippets': ['Request permissions from Permissions@acm.org. \nAH 2016, February 25-27, 2016, Geneva, Switzerland \n©', 'om Permissions@acm.org. \nAH 2016, February 25-27, 2016, Geneva, Switzerland \n© 2016 ACM. ISBN 978-1-', '016, February 25-27, 2016, Geneva, Switzerland \n© 2016 ACM. ISBN 978-1-4503-3680-2/16/02…$15.00 \nDOI']}], 'var_function-call-1410797014628049251': []}

exec(code, env_args)
