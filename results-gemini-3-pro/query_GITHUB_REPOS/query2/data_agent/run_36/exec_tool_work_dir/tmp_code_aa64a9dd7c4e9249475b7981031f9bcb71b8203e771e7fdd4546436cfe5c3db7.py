code = """import json
import re

file_path = locals()['var_function-call-2573461402379613798']
with open(file_path, 'r') as f:
    data = json.load(f)

max_count = 38
candidates = []

pattern = re.compile(r'(?:duplicated|appearing|seen|repeated|copied|appears) (\d+) times')

for item in data:
    desc = item.get('repo_data_description', '')
    match = pattern.search(desc)
    if match:
        count = int(match.group(1))
        if count == max_count:
            candidates.append(item)

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-17567642971942000785': ['commits', 'contents', 'files'], 'var_function-call-13361138901660454113': ['languages', 'repos', 'licenses'], 'var_function-call-13259296133069852295': 'file_storage/function-call-13259296133069852295.json', 'var_function-call-15549765763826830593': [{'count_star()': '105'}], 'var_function-call-2573461402379613798': 'file_storage/function-call-2573461402379613798.json', 'var_function-call-5897863258137049831': {'max_id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'max_count': 38, 'description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, 'var_function-call-13530393878731223593': [], 'var_function-call-11846105976845507242': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'content': '//\n//  ContactTableViewCell.swift\n//  PageMenuDemoTabbar\n//\n//  Created by Niklas Fahl on 1/9/15.\n//  Copyright (c) 2015 Niklas Fahl. All rights reserved.\n//\n\nimport UIKit\n\nclass ContactTableViewCell: UITableViewCell {\n\n    @IBOutlet var photoImageView: UIImageView!\n    @IBOutlet var nameLabel: UILabel!\n    @IBOutlet weak var starButton: UIButton!\n    \n    override func awakeFromNib() {\n        super.awakeFromNib()\n        // Initialization code\n    \n        photoImageView.layer.cornerRadius = 15\n    }\n    \n    override func setSelected(selected: Bool, animated: Bool) {\n        super.setSelected(selected, animated: animated)\n        \n        // Configure the view for the selected state\n    }\n    \n}\n', 'sample_repo_name': 'uacaps/PageMenu', 'sample_ref': 'refs/heads/master', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'sample_symlink_target': 'None', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}], 'var_function-call-2823428654436503168': [], 'var_function-call-15044479681614226869': [{'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/fun1_to_proc_par2.ll', 'mode': '40960', 'id': '316ad972693d0355c3504729fff14287419e004d', 'symlink_target': '../all/fun1_to_proc_par2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'tests/failure/wrong_order_par_seq_middle.t/wrong_order_par_seq_middle.ll', 'mode': '40960', 'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'symlink_target': '../../../fixtures/all/wrong_order_par_seq_middle.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/layout_case.ll', 'mode': '40960', 'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'symlink_target': '../all/layout_case.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/merger_loli_Sort.ll', 'mode': '40960', 'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'symlink_target': '../all/merger_loli_Sort.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/infer_recv.ll', 'mode': '40960', 'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'symlink_target': '../all/infer_recv.ll'}], 'var_function-call-14062153406453035240': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}]}

exec(code, env_args)
