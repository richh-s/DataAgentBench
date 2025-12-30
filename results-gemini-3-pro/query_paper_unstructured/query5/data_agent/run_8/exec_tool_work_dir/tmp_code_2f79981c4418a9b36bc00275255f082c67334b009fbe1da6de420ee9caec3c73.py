code = """import json
import re

with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations}

with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

chi_papers = []
total_citations = 0

for paper in papers:
    title = paper.get('filename', '')[:-4]
    if title in citation_map:
        text = paper.get('text', '')
        # Split at references
        try:
            parts = re.split(r'REFERENCES', text, flags=re.IGNORECASE)
            body = parts[0]
        except:
            body = text
        
        is_chi = False
        # Check patterns
        if "Conference on Human Factors in Computing Systems" in body:
            is_chi = True
        elif re.search(r'CHI \d{4}', body): # CHI 2015
            is_chi = True
        elif re.search(r"CHI '\d{2}", body): # CHI '15
            is_chi = True
        
        if is_chi:
            chi_papers.append(title)
            total_citations += citation_map[title]

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"Total citations: {total_citations}")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16, 'var_function-call-17501030019706782583': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}]}, 'var_function-call-5225444022116205832': [], 'var_function-call-14680094483701822161': [{'title': 'A Lived Informatics Model of Personal Informatics', 'match': 'CHI Year'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'match': 'CHI Year'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'match': 'Full Name'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'match': 'Full Name'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'match': 'Full Name'}], 'var_function-call-7239758174783740011': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  "}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'header': ' Barriers to Engagement with a Personal Informatics  Productivity Tool  Jon Bird  City University Lo'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'header': 'Beyond Abandonment to Next Steps: Understanding and  Designing for Life after Personal Informatics T'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'header': 'Beyond Behavior: The Coach’s Perspective   on Technology in Health Coaching   Heleen Rutjes   Human-'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'header': 'Charting Design Preferences on Wellness Wearables    Juho Rantakari1, Virve Inget2, Ashley Colley1, '}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'header': 'ClimbSense - Automatic Climbing Route Recognition using Wrist-worn Inertia Measurement Units Florian'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'header': 'Closing the Gap: Supporting Patients’ Transition   to Self-Management after Hospitalization   Ari H '}]}

exec(code, env_args)
