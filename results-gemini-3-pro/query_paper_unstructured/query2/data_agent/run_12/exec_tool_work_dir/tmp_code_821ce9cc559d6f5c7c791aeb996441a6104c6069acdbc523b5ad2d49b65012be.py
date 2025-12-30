code = """import json

mongo_res = locals()['var_function-call-5679702400551775489']
info = {}
info['mongo_type'] = str(type(mongo_res))
if isinstance(mongo_res, list):
    info['mongo_len'] = len(mongo_res)
    info['mongo_sample'] = mongo_res[0] if len(mongo_res) > 0 else None
elif isinstance(mongo_res, str):
    info['mongo_val_preview'] = mongo_res[:100]

sqlite_res_path = locals()['var_function-call-3465492661884944588']
info['sqlite_type'] = str(type(sqlite_res_path))

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-3465492661884944588': 'file_storage/function-call-3465492661884944588.json', 'var_function-call-5093555136357275627': 'file_storage/function-call-5093555136357275627.json', 'var_function-call-9313904331850907827': {'count': 158, 'filenames_preview': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt']}, 'var_function-call-13887185202303649787': 'file_storage/function-call-13887185202303649787.json', 'var_function-call-5679702400551775489': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-12282390523872244281': 'Debug done'}

exec(code, env_args)
