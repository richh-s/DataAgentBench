code = """import json, re

# Load files
citation_path = locals()['var_functions.query_db:6']
paper_path = locals()['var_functions.query_db:34']

with open(citation_path) as cf:
    citation_data = json.load(cf)

with open(paper_path) as pf:
    paper_data = json.load(pf)

# Build citation dictionary
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['total_citations'])

# Process papers
papers_2016 = []

for doc in paper_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check physical activity domain
    if 'physical activity' not in text.lower():
        continue
    
    # Check for 2016 using regex
    has_2016 = bool(re.search(r'2016', text))
    
    # Verify it's actually a 2016 paper by checking for venue/copyright patterns
    if has_2016:
        # Look for copyright 2016
        if re.search(r'copyright.*?2016', text, re.IGNORECASE):
            year = 2016
        # Look for venue 2016
        elif re.search(r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp).*?2016', text, re.IGNORECASE):
            year = 2016
        # Look for 2016 in first 500 chars (often header)
        elif '2016' in text[:500]:
            year = 2016
        else:
            year = None
        
        if year == 2016:
            total_cites = citation_dict.get(title, 0)
            papers_2016.append([title, total_cites])

# Sort by citations descending
papers_2016.sort(key=lambda x: x[1], reverse=True)

# Format output
output = []
for title, cites in papers_2016:
    output.append('Title: ' + title)
    output.append('Total Citations: ' + str(cites))
    output.append('')

result_str = '\n'.join(output).strip() if papers_2016 else 'No papers found'

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'title': "Everybody Knows What You'Re Doing: A Critical Design Approach to Personal Informatics", 'total_citations': '694'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'total_citations': '595'}, {'title': 'See Friendship, Sort of: How Conversation and Digital Traces Might Support Reflection on Friendships', 'total_citations': '593'}, {'title': 'Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'total_citations': '587'}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'total_citations': '557'}, {'title': "It Feels Like I'm Managing Myself: HIV+ People Tracking Their Personal Health Information", 'total_citations': '556'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520'}, {'title': 'Go and Grow: Mapping Personal Data to a Living Plant', 'total_citations': '500'}, {'title': 'Patina Engraver: Visualizing Activity Logs As Patina in Fashionable Trackers', 'total_citations': '497'}, {'title': 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'total_citations': '492'}, {'title': 'Designing for Self-Tracking of Emotion and Experience with Tangible Modality', 'total_citations': '491'}, {'title': "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'total_citations': '489'}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'total_citations': '488'}, {'title': "Toss 'N' Turn: Smartphone As Sleep and Sleep Quality Detector", 'total_citations': '484'}, {'title': 'Personal Informatics in Chronic Illness Management', 'total_citations': '484'}, {'title': 'The Irony and Re-interpretation of Our Quantified Self', 'total_citations': '481'}, {'title': 'Everything We Do, Everything We Press: Data-Driven Remote Performance Management in a Mobile Workplace', 'total_citations': '476'}, {'title': 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors', 'total_citations': '473'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': '467'}, {'title': 'Opportunities for Oral Health Monitoring Technologies Beyond the Dental Clinic', 'total_citations': '466'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'Why We Use and Abandon Smart Devices', 'total_citations': '463'}, {'title': 'Persistent Sharing of Fitness App Status on Twitter', 'total_citations': '462'}, {'title': 'SleepCoacher: A Personalized Automated Self-Experimentation System for Sleep Recommendations', 'total_citations': '461'}, {'title': 'Examining Menstrual Tracking to Inform the Design of Personal Informatics Tools', 'total_citations': '458'}, {'title': 'Implementing Ethics for a Mobile App Deployment', 'total_citations': '457'}, {'title': 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations', 'total_citations': '457'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citations': '452'}, {'title': 'Can SAL Support Self Reflection for Health and Nutrition?', 'total_citations': '450'}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'total_citations': '449'}, {'title': 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'total_citations': '448'}, {'title': 'Investigating the Effectiveness of Cohort-Based Sleep Recommendations', 'total_citations': '446'}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'total_citations': '442'}, {'title': 'VRFit: An Interactive Dashboard for Visualising of Virtual Reality Exercise and Daily Step Data', 'total_citations': '441'}, {'title': 'Exploring the Data Tracking and Sharing Preferences of Wheelchair Athletes', 'total_citations': '435'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Facts, Interactivity and Videotape: Exploring the Design Space of Data in Interactive Video Storytelling', 'total_citations': '430'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': '428'}, {'title': 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures', 'total_citations': '427'}, {'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'total_citations': '426'}, {'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'total_citations': '424'}, {'title': 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'total_citations': '421'}, {'title': 'Bringing New Voices to Design of Exercise Technology: Participatory Design with Vulnerable Young Adults', 'total_citations': '419'}, {'title': 'Understanding Individual Differences for Tailored Smoking Cessation Apps', 'total_citations': '417'}, {'title': 'Lunch Line: Using Public Displays and Mobile Devices to Encourage Healthy Eating in an Organization', 'total_citations': '410'}, {'title': "The Quantified Patient in the Doctor's Office: Challenges & Opportunities", 'total_citations': '404'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}]}

exec(code, env_args)
