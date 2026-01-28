code = """import json

# Compose final answer details using previous results stored in variables
contents_top = var_call_nsHD7L2UvuH2i9pq4WbWMPya
lang = var_call_8AXOvH9wyuZaFXrump4pCdnv
repos = var_call_OH6JlxmoD99OoU0KpcYKIRiP
lic = var_call_f4HPrJXDM8pwzdvRDtrfRQ9i
contents_rec = var_call_Lxmo6MtT5LCtLgdxIJlH3ahA[0]

answer = {
    'repository': 'uacaps/PageMenu',
    'primary_languages_description': lang[0]['language_description'] if lang else None,
    'watch_count': int(repos[0]['watch_count']) if repos else None,
    'license': lic[0]['license'] if lic else None,
    'most_copied_swift_file_id': contents_top['top_files'][0]['id'],
    'most_copied_swift_file_path': contents_rec['sample_path'],
    'copies_in_dataset': contents_top['max_copies']
}

import json
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_oSkPWzXihTqO9vvcpWCglOps': [], 'var_call_rbHOFgBtBvkb2IDJvshCTvd0': ['commits', 'contents', 'files'], 'var_call_R1k4AIpVxOEdsxHIEMKDMRNy': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'copies': '4'}, {'id': 'd67714b2a25908fbc4e6b00531862cc62265bf75', 'copies': '2'}, {'id': '0191f88060e6994e1095478da21798fd2c0a9dcb', 'copies': '2'}, {'id': 'e94c45ffe619fbd39e7f5df78a590bd33893d64a', 'copies': '2'}, {'id': 'a1615a71d1bdbb036d1dde0a94b8285fa8fca084', 'copies': '2'}, {'id': '53496cde05c660feb3ab3335e825b363aa68a51a', 'copies': '2'}, {'id': 'd1b6baa8d0bd3ac28e0765482e204e33340ccf8c', 'copies': '2'}, {'id': '8af9111216436874eecfaa475d5c2f3ac650e3bc', 'copies': '2'}, {'id': '6066caa5e76b60fbd0f7bc2a096c6fd7c023609f', 'copies': '2'}, {'id': '3252bbf919d2fb7d0f3fd9a3841f44f5f699c0c2', 'copies': '2'}, {'id': 'f260ac370354b6dc8e5fb92da276cf587dd2d4d7', 'copies': '2'}, {'id': 'f64ee245678dcb26d658600708e2996a7608fc6e', 'copies': '2'}, {'id': '731d202c0c486ce8daf377f2c6a7389cc9bc20fa', 'copies': '2'}, {'id': '75c9123b0b91ca99402ed40efe80d21cb6bc3f90', 'copies': '2'}, {'id': '49f5eda9ac693bf61324ee7f65a15d704f7f3411', 'copies': '2'}, {'id': 'a1a7098f21fbd20afe3098e33bb8e0c93b14179e', 'copies': '1'}, {'id': 'b577774bae4db39fa8a2a5c8e4b61b654085919d', 'copies': '1'}, {'id': '37104c1cea94b28d00a2c564dcd09e8f542f5ef6', 'copies': '1'}, {'id': 'ef1ba022ec64bc9c7fdbba5156a7d6eec3068e33', 'copies': '1'}, {'id': '89a00ca864c3e205b522deb9533c921cf3c1243d', 'copies': '1'}], 'var_call_59Hcnp9AAdp0opDoiQpoStl8': [], 'var_call_SVjJRBCzTSAwIFjZy3Lm8Ers': [], 'var_call_4Hs4co1epdSoWn1wbwNko0Jp': [], 'var_call_q8fwIyRYAp5c5Hv1wl7PRIyZ': 'file_storage/call_q8fwIyRYAp5c5Hv1wl7PRIyZ.json', 'var_call_nsHD7L2UvuH2i9pq4WbWMPya': {'max_copies': 38, 'top_files': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.', 'copies': 38}]}, 'var_call_8AXOvH9wyuZaFXrump4pCdnv': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_call_uBAJ1RTiY930XzBTxS4qkJMI': [], 'var_call_Lxmo6MtT5LCtLgdxIJlH3ahA': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.', 'content': '//\n//  ContactTableViewCell.swift\n//  PageMenuDemoTabbar\n//\n//  Created by Niklas Fahl on 1/9/15.\n//  Copyright (c) 2015 Niklas Fahl. All rights reserved.\n//\n\nimport UIKit\n\nclass ContactTableViewCell: UITableViewCell {\n\n    @IBOutlet var photoImageView: UIImageView!\n    @IBOutlet var nameLabel: UILabel!\n    @IBOutlet weak var starButton: UIButton!\n    \n    override func awakeFromNib() {\n        super.awakeFromNib()\n        // Initialization code\n    \n        photoImageView.layer.cornerRadius = 15\n    }\n    \n    override func setSelected(selected: Bool, animated: Bool) {\n        super.setSelected(selected, animated: animated)\n        \n        // Configure the view for the selected state\n    }\n    \n}\n'}], 'var_call_OH6JlxmoD99OoU0KpcYKIRiP': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}], 'var_call_f4HPrJXDM8pwzdvRDtrfRQ9i': [{'license': 'bsd-3-clause'}]}

exec(code, env_args)
