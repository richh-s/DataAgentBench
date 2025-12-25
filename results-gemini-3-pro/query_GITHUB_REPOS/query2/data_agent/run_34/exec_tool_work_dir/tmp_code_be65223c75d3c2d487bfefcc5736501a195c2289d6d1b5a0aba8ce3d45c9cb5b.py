code = """import json
import re

file_path = locals()['var_function-call-1622377898261970536']
with open(file_path, 'r') as f:
    data = json.load(f)

patterns = [
    r"duplicated (\d+) times",
    r"appearing (\d+) times",
    r"seen (\d+) times",
    r"repeated (\d+) times",
    r"copied (\d+) times"
]

max_copies = -1
target_id = None
debug_list = []

for item in data:
    desc = item.get('repo_data_description', '')
    # Ensure it's non-binary. The description contains "non-binary".
    if 'non-binary' not in desc.lower():
        continue
    
    count = 0
    for pat in patterns:
        m = re.search(pat, desc)
        if m:
            count = int(m.group(1))
            break
            
    if count > max_copies:
        max_copies = count
        target_id = item['id']
    
    debug_list.append((item['id'], count))

debug_list.sort(key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps({
    "target_id": target_id,
    "max_copies": max_copies,
    "top_5": debug_list[:5]
}))"""

env_args = {'var_function-call-202814163877997822': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'copy_count': '4'}, {'id': '75c9123b0b91ca99402ed40efe80d21cb6bc3f90', 'copy_count': '2'}, {'id': 'd1b6baa8d0bd3ac28e0765482e204e33340ccf8c', 'copy_count': '2'}, {'id': '6066caa5e76b60fbd0f7bc2a096c6fd7c023609f', 'copy_count': '2'}, {'id': 'e94c45ffe619fbd39e7f5df78a590bd33893d64a', 'copy_count': '2'}], 'var_function-call-2310690157930696608': [], 'var_function-call-11781882774561093865': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'content': '// Copyright 2015 The Chromium Authors. All rights reserved.\n// Use of this source code is governed by a BSD-style license that can be\n// found in the LICENSE file.\n\nmodule device;\n\nenum NFCErrorType {\n  SECURITY,\n  NOT_SUPPORTED,\n  DEVICE_DISABLED,\n  NOT_FOUND,\n  INVALID_MESSAGE,\n  OPERATION_CANCELLED,\n  TIMER_EXPIRED,\n  CANNOT_CANCEL,\n  IO_ERROR\n};\n\nenum NFCRecordType {\n  EMPTY,\n  TEXT,\n  URL,\n  JSON,\n  OPAQUE_RECORD\n};\n\nenum NFCPushTarget {\n  TAG,\n  PEER,\n  ANY\n};\n\nenum NFCWatchMode {\n  WEBNFC_ONLY,\n  ANY\n};\n\nstruct NFCError {\n  NFCErrorType error_type;\n};\n\nstruct NFCRecord {\n  NFCRecordType recordType;\n  string? mediaType;\n  array<uint8> data;\n};\n\nstruct NFCMessage {\n  array<NFCRecord> data;\n  string? url;\n};\n\nstruct NFCPushOptions {\n  NFCPushTarget target;\n  double timeout;\n  bool ignoreRead;\n};\n\nstruct NFCRecordTypeFilter {\n  NFCRecordType recordType;\n};\n\nstruct NFCWatchOptions {\n  string? url;\n  NFCRecordTypeFilter? recordFilter;\n  string? mediaType;\n  NFCWatchMode mode;\n};\n\ninterface NFC {\n  SetClient(NFCClient client);\n  Push(NFCMessage message, NFCPushOptions? options) => (NFCError? error);\n  CancelPush(NFCPushTarget target) => (NFCError? error);\n  Watch(NFCWatchOptions options) => (uint32 id, NFCError? error);\n  CancelWatch (uint32 id) => (NFCError? error);\n  CancelAllWatches () => (NFCError? error);\n  SuspendNFCOperations();\n  ResumeNFCOperations();\n};\n\ninterface NFCClient {\n  OnWatch(uint32 id, NFCMessage message);\n};\n', 'sample_repo_name': 'nwjs/chromium.src', 'sample_ref': 'refs/heads/nw15', 'sample_path': 'device/nfc/nfc.mojom', 'sample_symlink_target': 'None', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}], 'var_function-call-1556214950733105289': 'file_storage/function-call-1556214950733105289.json', 'var_function-call-6934053472163489181': [{'count_star()': '105'}], 'var_function-call-1622377898261970536': 'file_storage/function-call-1622377898261970536.json'}

exec(code, env_args)
