code = """import json

docs_key = "var_function-call-4014968237340429633"

with open(locals()[docs_key], "r") as f:
    docs_data = json.load(f)

target = "Malibu Park Drainage Improvements"
found_text = "Not Found"

for d in docs_data:
    if target in d["text"]:
        # Extract the relevant block crudely
        start = d["text"].find(target)
        found_text = d["text"][start:start+500]
        break

print("__RESULT__:")
print(json.dumps([found_text]))"""

env_args = {'var_function-call-1448852997668966591': ['civic_docs'], 'var_function-call-1448852997668967958': ['Funding'], 'var_function-call-4014968237340428108': 'file_storage/function-call-4014968237340428108.json', 'var_function-call-4014968237340429633': 'file_storage/function-call-4014968237340429633.json', 'var_function-call-2811947825801822237': {'matches': ['Malibu Park Drainage Improvements', 'Permanent Skate Park', 'Bluffs Park Shade Structure'], 'total': 135000}, 'var_function-call-2620570463614741313': {'matches': ['Malibu Park Drainage Improvements', 'Bluffs Park Shade Structure'], 'total': 38000}}

exec(code, env_args)
