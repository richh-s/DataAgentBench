code = """import json
import re

with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations}

with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

chi_papers = []
total_citations = 0

debug_titles = []

for paper in papers:
    title = paper.get('filename', '')[:-4]
    if title not in citation_map:
        continue
    
    text = paper.get('text', '')
    
    # Logic:
    # 1. Look for Permission block
    perm_match = re.search(r"Permission to make digital or hard copies", text, re.IGNORECASE)
    venue_found = False
    is_chi = False
    
    if perm_match:
        # Check snippet around permission
        start = perm_match.start()
        # ACM copyright block usually follows. It contains the venue.
        snippet = text[start:start+1500]
        
        # Check for CHI pattern in snippet
        if re.search(r"Conference on Human Factors in Computing Systems", snippet, re.IGNORECASE):
            is_chi = True
            venue_found = True
        elif re.search(r"\bCHI\s*['’]?\d{2,4}", snippet):
            is_chi = True
            venue_found = True
        
        # Double check: if UbiComp is in the snippet, it overrides CHI?
        # (Unless CHI is the main one).
        # But usually they don't mix in the copyright block.
        # If I see "UbiComp", and "CHI" is NOT there, it's false.
        # If "CHI" is there, it's true.
        # Note: "A Lived Informatics Model" has "UbiComp '15" in snippet. It does NOT have "CHI".
        
    if not venue_found:
        # Fallback: Check first 3000 chars (Header/First page)
        # Avoid references which are at the end.
        snippet = text[:3000]
        if re.search(r"Conference on Human Factors in Computing Systems", snippet, re.IGNORECASE):
            is_chi = True
        elif re.search(r"\bCHI\s*['’]?\d{2,4},\s*[A-Z]", snippet):
            # Strict pattern with Date/Month to avoid random "CHI 2015" mentions
            is_chi = True

    if is_chi:
        chi_papers.append(title)
        total_citations += citation_map[title]
        debug_titles.append(title)

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16, 'var_function-call-17501030019706782583': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}]}, 'var_function-call-5225444022116205832': [], 'var_function-call-14680094483701822161': [{'title': 'A Lived Informatics Model of Personal Informatics', 'match': 'CHI Year'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'match': 'CHI Year'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'match': 'Full Name'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'match': 'Full Name'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'match': 'Full Name'}], 'var_function-call-7239758174783740011': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  "}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'header': ' Barriers to Engagement with a Personal Informatics  Productivity Tool  Jon Bird  City University Lo'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'header': 'Beyond Abandonment to Next Steps: Understanding and  Designing for Life after Personal Informatics T'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'header': 'Beyond Behavior: The Coach’s Perspective   on Technology in Health Coaching   Heleen Rutjes   Human-'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'header': 'Charting Design Preferences on Wellness Wearables    Juho Rantakari1, Virve Inget2, Ashley Colley1, '}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'header': 'ClimbSense - Automatic Climbing Route Recognition using Wrist-worn Inertia Measurement Units Florian'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'header': 'Closing the Gap: Supporting Patients’ Transition   to Self-Management after Hospitalization   Ari H '}], 'var_function-call-4365208543066403133': 1893, 'var_function-call-16377022919636549182': 61, 'var_function-call-2847063484787585829': {'sundroid_header': 'Sundroid: Solar Radiation Awareness with Smartphones∗  Thomas Fahrni, Michael Kuhn, Philipp Sommer, Roger Wattenhofer, and Samuel Welten Computer Engineering and Networks Laboratory ETH Zurich, Switzerland ﬁrstname.lastname@tik.ee.ethz.ch  ABSTRACT While the sun is important for our health, overexpo', 'chi_papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'count': 43}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'count': 2}], 'total': 61}, 'var_function-call-1886946324018678199': 'Done', 'var_function-call-4292012880260422153': {'snippet': 'Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for proﬁt or commercial advantage and that copies bear this notice and the full citation on the ﬁrst page. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior speciﬁc permission and/or a fee. UbiComp’11, September 17–21, 2011, Beijing, China. Copyright 2011 ACM 978-1-4503-0630-0/11/0', 'chi_indices': [47792, 48417, 48668, 49229], 'total_chi': 4}, 'var_function-call-15226953928440916861': 0, 'var_function-call-10072067619886650282': [{'title': 'A Lived Informatics Model of Personal Informatics', 'venue_snippet': "FROM_EMAIL: .  UbiComp '15, September 7-11, 2015, Osaka, Japan.  Copyright 2015 © ACM 978-1-4503-3574-4/15/09...$15.00.  http://dx.doi.org/10.1145/2750858.2804250   The first and most commonly used model for unde"}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'venue_snippet': 'FROM_EMAIL: . CHI 2018, April 21–26, 2018, Montréal, QC, Canada © 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM. ISBN 978-1-4503-5620-6/18/04. . . $15.00 DOI: http://dx.doi.org/10'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'venue_snippet': 'FROM_EMAIL: ).  CHI 2019, May 4-9, 2019, Glasgow, Scotland, UK.  © 2019 Copyright is held by the owner/author(s). Publication rights licensed to ACM.  ACM ISBN 978-1-4503-5970-2/19/05...$15.00.  DOI: https://doi.'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'venue_snippet': '.   Request permissions from Permissions@acm.org.    CHI 2015, April 18  - 23 2015, Seoul, Republic of Korea    Copyright 2015 ACM 978-1-4503-3145-6/15/04$15.00    http://dx.doi.org/10.1145/2702123.27'}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'venue_snippet': ".  OZCHI '14, Dec 2-5, 2014, Sydney, Australia  Copyright © 2014 ACM 978-1-4503-0653-9... $15.00  http://dx.doi.org/10.1145/2686612.2686668   370  stressful.   Students  are  the  most  prolific  user"}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'venue_snippet': 'FROM_EMAIL: .  CHI 2015, April 18–23, 2015, Seoul, Republic of Korea.  Copyright is held by the owner/author(s). Publication rights licensed to ACM.  ACM 978-1-4503-3145-6/15/04…$15.00.  http://dx.doi.org/10.1145'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'venue_snippet': 'FROM_EMAIL: .  CHI 2019, May 4–9, 2019, Glasgow, Scotland UK © 2019 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-1-4503-5970-2/19/05. . . $15.00 https://doi.org/10.1145/'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'venue_snippet': '. Request permissions  from Permissions@acm.org.  CHI 2015, April 18 - 23, 2015, Seoul, Republic of Korea  Copyright is held by the owner/author(s). Publication rights licensed to  ACM.  ACM 978-1-450'}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'venue_snippet': 'FROM_EMAIL: .  study to evaluate the usability of the system as well as its potential for individual and collaborative sensemaking of the data.  CCS CONCEPTS • Human-centered computing → Visualization systems and'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'venue_snippet': 'FROM_EMAIL: . © 2018 Association for Computing Machinery. 2474-9567/2018/3-ART37 $15.00 https://doi.org/10.1145/3191769  Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, Vol. 2'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'venue_snippet': 'FROM_EMAIL: . DH’18, April 23–26, 2018, Lyon, France © 2018 Association for Computing Machinery. ACM ISBN 978-1-4503-6493-5/18/04. . . $15.00 https://doi.org/10.1145/3194658.3194663  loss programs [9]. The act of'}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'venue_snippet': 'FROM_EMAIL: . DH’18, April 23–26, 2018, Lyon, France © 2018 Association for Computing Machinery. ACM ISBN 978-1-4503-6493-5/18/04. . . $15.00 https://doi.org/10.1145/3194658.3194662  1 INTRODUCTION Persistent col'}, {'title': 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'venue_snippet': '. Request permissions  from permissions@acm.org.  CHI 2018, April 21–26, 2018, Montréal, QC, Canada.  © 2018 ACM ISBN 978-1-4503-5620-6/18/04...$15.00.   https://doi.org/10.1145/3173574.3173871   Figu'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'venue_snippet': 'FROM_EMAIL: .  UbiComp’13, September 8–12, 2013, Zurich, Switzerland.  Copyright © 2013 ACM 978-1-4503-1770-2/13/09…$15.00.  http://dx.doi.org/10.1145/2493432.2493433   Figure 1. A fine-grained view of daily step'}, {'title': 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'venue_snippet': '. Request permissions from permissions@acm.org.  CSCW 2014, March 14–18, 2015, Vancouver, BC, Canada.  Copyright © 2014 ACM 978-1-4503-2922-4/15/03...$15.00.  http://dx.doi.org/10.1145/2675133.2675135'}, {'title': 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'venue_snippet': '. Request permissions from  Permissions@acm.org. DIS 2017, June 10-14, 2017, Edinburgh, United Kingdom  Copyright is held by the owner/author(s). Publication rights licensed to ACM. ACM 978-1-4503-492'}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'venue_snippet': '. Request permissions from  Permissions@acm.org. Copyright is held by the owner/author(s). Publication rights licensed to Association for Computing Machinery.  2474-9567/2018/9-ART132 $15.00  https://'}, {'title': 'Intelligent Computing in Personal Informatics: Key Design Considerations', 'venue_snippet': 'FROM_EMAIL: . IUI 2015, March 29–April 1, 2015, Atlanta, GA, USA. Copyright is held by the owner/author(s). Publication rights licensed to ACM. ACM 978-1-4503-3306-1/15/03 ...$15.00. http://dx.doi.org/10.1145/267'}, {'title': 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'venue_snippet': 'FROM_EMAIL: . ICTD ’16, June 03-06, 2016, Ann Arbor, Michigan, USA c(cid:13) 2016 ACM. ISBN 978-1-4503-4306-0/16/06. . . $15.00 DOI: http://dx.doi.org/10.1145/2909609.2909664  1.  INTRODUCTION  Approximately 1.3'}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'venue_snippet': '. Request  permissions from Permissions@acm.org.  CHI 2017, May 06-11, 2017, Denver, CO, USA   © 2017 ACM. ISBN 978-1-4503-4655-9/17/05…$15.00   DOI: http://dx.doi.org/10.1145/3025453.3025557   Despit'}], 'var_function-call-812912343305407643': 1551}

exec(code, env_args)
