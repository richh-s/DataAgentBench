code = """import json

with open(locals()['var_function-call-9700206069512387348'], 'r') as f:
    citations_data = json.load(f)

target_title = "A Stage-based Model of Personal Informatics Systems"
found_entry = None
for entry in citations_data:
    if entry['title'].lower() == target_title.lower():
        found_entry = entry
        break

sample_titles = [x['title'] for x in citations_data[:3]]

result = {
    "found_entry": found_entry,
    "sample_titles": sample_titles
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9042960770956765793': ['Citations', 'sqlite_sequence'], 'var_function-call-9042960770956765216': ['paper_docs'], 'var_function-call-9700206069512387348': 'file_storage/function-call-9700206069512387348.json', 'var_function-call-9700206069512385745': 'file_storage/function-call-9700206069512385745.json', 'var_function-call-15345152852245153349': 'file_storage/function-call-15345152852245153349.json', 'var_function-call-13303026502511534090': 0, 'var_function-call-15942213445478257079': 'done', 'var_function-call-14752460078601264173': {'first_5_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'chi_count_in_500_chars': 0, 'sample_header': ''}, 'var_function-call-10672173907971338002': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'var_function-call-16401888427703134563': {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'matches': ['quires  prior  specific permission and/or a fee.  CHI 2010, April 10–15, 2010, Atlanta, Georgia, USA', 'demonstrate the use of the model for diagnosing   CHI 2010: Performance, Stagecraft, and MagicApril ', 'a  web  site  where  people  can  report  their   CHI 2010: Performance, Stagecraft, and MagicApril ', 'lly and manually collected by the participants.   CHI 2010: Performance, Stagecraft, and MagicApril ', '  selection  would  have   instead.  When   she   CHI 2010: Performance, Stagecraft, and MagicApril ', 'ion barriers.   Table 3. Integration barriers.    CHI 2010: Performance, Stagecraft, and MagicApril ', 'ing personal changes that might be necessary.”    CHI 2010: Performance, Stagecraft, and MagicApril ', 'e,  the  BodyMedia  SenseWear  armband  is  uni-  CHI 2010: Performance, Stagecraft, and MagicApril ', 'nts  that  the  system  will  integrate.    The   CHI 2010: Performance, Stagecraft, and MagicApril ', '  technologies  to  collect  various  types  of   CHI 2010: Performance, Stagecraft, and MagicApril ']}, 'var_function-call-2920365897182027897': 'done', 'var_function-call-6256095471512962597': {'index': 2811, 'text_length': 63309, 'first_500': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, 'var_function-call-9141583539315528318': 'done', 'var_function-call-12997066912359879032': 'CHI not found in first 5000 chars of Ubicomp paper.', 'var_function-call-399027980345313131': {'total_citations': 0, 'chi_papers_count': 0, 'sample_chi_titles': []}, 'var_function-call-7510368112678129086': 'done'}

exec(code, env_args)
