code = """import json
import os

citations_var = locals()['var_function-call-2106421940036629061']
if isinstance(citations_var, str) and os.path.exists(citations_var):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

filenames = [r['title'] + ".txt" for r in citations_data]

query = {
    "collection": "paper_docs",
    "filter": {
        "filename": {"$in": filenames}
    },
    "projection": {"filename": 1, "text": 1} 
}
# projection text is needed to check for CHI

print("__RESULT__:")
print(json.dumps(json.dumps(query)))"""

env_args = {'var_function-call-2106421940036629061': 'file_storage/function-call-2106421940036629061.json', 'var_function-call-10975034147027654622': {'count': 188, 'filenames_preview': ['Sundroid: Solar Radiation Awareness with Smartphones.txt', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"]}, 'var_function-call-8410670422247250246': 'file_storage/function-call-8410670422247250246.json', 'var_function-call-16527945425029861293': 'file_storage/function-call-16527945425029861293.json', 'var_function-call-3942142969729170768': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-13646251503415477728': 243, 'var_function-call-12522816240389371249': 'file_storage/function-call-12522816240389371249.json', 'var_function-call-9399173173343595409': 'file_storage/function-call-9399173173343595409.json', 'var_function-call-12904116397288956253': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-1371638022713717313': 243, 'var_function-call-4517137375640038223': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-9210819965335981316': 243, 'var_function-call-5763721864485763841': 'file_storage/function-call-5763721864485763841.json', 'var_function-call-9703409222628890210': 'file_storage/function-call-9703409222628890210.json'}

exec(code, env_args)
