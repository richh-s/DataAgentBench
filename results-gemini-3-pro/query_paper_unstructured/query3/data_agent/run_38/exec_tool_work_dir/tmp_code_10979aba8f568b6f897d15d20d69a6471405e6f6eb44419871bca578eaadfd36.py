code = """import json

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

check_titles = [
    "Anxiety and Autism: Towards Personalized Digital Health",
    "Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use",
    "Everybody Knows What You'Re Doing: A Critical Design Approach to Personal Informatics"
]

print("Checking specific papers:")
for t_check in check_titles:
    paper = next((p for p in papers if t_check in p['filename']), None)
    if paper:
        text = paper['text']
        print(f"Title: {t_check}")
        print(f"  Has 'empirical': {'empirical' in text.lower()}")
        print(f"  Has 2017+: {any(y in text for y in ['2017', '2018', '2019', '2020'])}")
        # Print year context
        for y in ['2015', '2016', '2017', '2018']:
            if y in text:
                print(f"  Found {y}")
    else:
        print(f"Paper not found: {t_check}")

print("__RESULT__:")
print("[]")"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': [], 'var_function-call-10123482125703570852': [], 'var_function-call-4464588429009855954': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-12260434194863203705': [], 'var_function-call-14033479952836946442': [], 'var_function-call-4699397698012979875': {'sample_cit_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics'], 'sample_paper_titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'], 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'empirical': False, 'years_found': ['2015']}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'empirical': False, 'years_found': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'empirical': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'empirical': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'empirical': False, 'years_found': []}]}, 'var_function-call-15181580171572275167': [], 'var_function-call-3140197388063378270': [], 'var_function-call-9328806422664267485': {'paper_filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'paper_has_2018': True, 'paper_has_empirical': True, 'cit_title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'titles_equal': True}, 'var_function-call-16118670276403361957': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citation_count': 265}]}

exec(code, env_args)
