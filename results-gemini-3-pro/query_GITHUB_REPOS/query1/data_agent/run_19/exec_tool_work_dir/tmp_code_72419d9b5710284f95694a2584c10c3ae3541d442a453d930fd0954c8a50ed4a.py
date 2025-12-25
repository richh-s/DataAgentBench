code = """import json

# IDs of READMEs in Non-Python repos
target_ids_file = locals()['var_function-call-1997626725569329320']
with open(target_ids_file, 'r') as f:
    target_ids = json.load(f)

# IDs of contents with "Copyright"
copyright_ids_file = locals()['var_function-call-15435963703617651368']
with open(copyright_ids_file, 'r') as f:
    copyright_ids_list = json.load(f)

copyright_ids_set = set(item['id'] for item in copyright_ids_list)

# Count intersection
count_copyright = 0
for tid in target_ids:
    if tid in copyright_ids_set:
        count_copyright += 1

total = len(target_ids)
proportion = count_copyright / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "count_copyright": count_copyright,
    "total": total,
    "proportion": proportion
}))"""

env_args = {'var_function-call-15690208722106533545': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1317426344979526180': 'file_storage/function-call-1317426344979526180.json', 'var_function-call-3833117249716137549': [{'COUNT(*)': '3325634'}], 'var_function-call-8139088797049422320': [{'count_star()': '195'}], 'var_function-call-8232077413265731152': [{'sample_path': 'assets/readme/home.jpg'}, {'sample_path': 'rtrouton_scripts/Casper_Scripts/install_company_canon_printer_drivers/README.md'}, {'sample_path': 'api/docs/README.md'}, {'sample_path': 'manager/README.txt'}, {'sample_path': 'README.md'}, {'sample_path': 'centos7.mongodb24/examples/replica/README.md'}, {'sample_path': 'README.md'}, {'sample_path': '022. Balanced Binary Tree/README.md'}, {'sample_path': 'examples/python/README.md'}, {'sample_path': 'lib/ehstorguids/README.md'}, {'sample_path': 'README.md'}, {'sample_path': 'art/readme_pic.png'}, {'sample_path': 'gwt/src/Timeline/README'}, {'sample_path': 'node_modules/base64url/node_modules/concat-stream/readme.md'}, {'sample_path': 'edu-services/cm-service/xdocs/db-demo-2.4.x-fix/readme.txt'}, {'sample_path': 'ppapi/tests/clang/README'}, {'sample_path': 'modoboa/bower_components/eonasdan-bootstrap-datetimepicker/README.md'}, {'sample_path': 'labs/architecture-examples/cujo/bower_components/curl/src/curl/plugin/README.md'}, {'sample_path': 'cluster/juju/layers/kubernetes/README.md'}, {'sample_path': 'tools/ckeditor/README.md'}], 'var_function-call-14761839733299388913': [{'count_star()': '524077'}], 'var_function-call-6371081823174223180': [{'count_star()': '3086'}], 'var_function-call-6023538620865391951': 'file_storage/function-call-6023538620865391951.json', 'var_function-call-11949558034636123156': 'file_storage/function-call-11949558034636123156.json', 'var_function-call-10034288392245374241': 'file_storage/function-call-10034288392245374241.json', 'var_function-call-8466893061163724252': 60149, 'var_function-call-1624657722700064077': 'file_storage/function-call-1624657722700064077.json', 'var_function-call-16857281004801262279': [{'COUNT(*)': '550905'}], 'var_function-call-6254358590231921713': 'file_storage/function-call-6254358590231921713.json', 'var_function-call-18341112339036593908': 'file_storage/function-call-18341112339036593908.json', 'var_function-call-13686227570124530061': 'file_storage/function-call-13686227570124530061.json', 'var_function-call-10728758801601727368': 'file_storage/function-call-10728758801601727368.json', 'var_function-call-1997626725569329320': 'file_storage/function-call-1997626725569329320.json', 'var_function-call-18400844015156351596': 2540, 'var_function-call-7545383215971464552': 'file_storage/function-call-7545383215971464552.json', 'var_function-call-3849935128326863551': 'file_storage/function-call-3849935128326863551.json', 'var_function-call-16576260064087752653': [{'count_star()': '24286'}], 'var_function-call-15435963703617651368': 'file_storage/function-call-15435963703617651368.json'}

exec(code, env_args)
