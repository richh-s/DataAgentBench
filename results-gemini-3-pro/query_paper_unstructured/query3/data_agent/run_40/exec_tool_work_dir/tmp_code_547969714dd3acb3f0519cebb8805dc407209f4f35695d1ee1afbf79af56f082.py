code = """import re

text = "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN"
# Try original regex
original = re.findall(r'\b(20\d{2})\b', text)
print(f"Original full year: {original}")

# Try improved regex for short year
# Original: \b'([12]\d)\b
# ' is not a word char, so \b' matches ONLY if previous char was a word char? No.
# \b matches position where one side is word char, one is not.
# If text is " '15", previous is space (non-word). Current is ' (non-word). No boundary between space and '.
# Boundary is between ' and 1.
# So \b matches between ' and 1.
# So \b' fails because it expects boundary BEFORE '. 
# Correct: (?:^|\s)'([012]\d)\b
short = re.findall(r"(?:^|\s|'|\")'([012]\d)\b", text) # account for potentially other chars? Just space is usually enough
print(f"Short year: {short}")

# Let's fix the script."""

env_args = {'var_function-call-4642845267965044101': ['paper_docs'], 'var_function-call-4642845267965042778': ['Citations', 'sqlite_sequence'], 'var_function-call-10467492128798022417': 'file_storage/function-call-10467492128798022417.json', 'var_function-call-1634184987777097794': 'file_storage/function-call-1634184987777097794.json', 'var_function-call-15997797269268972557': [], 'var_function-call-522812283828333894': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}

exec(code, env_args)
