code = """import json
import collections

# Load data
order_items_data = locals()['var_function-call-14034936189066484870']
cases_data = locals()['var_function-call-8033806652815484324']

# Helper to clean IDs
def clean_id(id_val):
    if not id_val:
        return ""
    # Remove leading '#'
    s = str(id_val).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Create set of target OrderItem IDs
target_order_item_ids = set()
for item in order_items_data:
    target_order_item_ids.add(clean_id(item['Id']))

# Count issues
issue_counts = collections.Counter()
matched_count = 0

for case in cases_data:
    raw_oi_id = case.get('orderitemid__c')
    if raw_oi_id:
        clean_oi_id = clean_id(raw_oi_id)
        if clean_oi_id in target_order_item_ids:
            # We found a match
            matched_count += 1
            issue_id = case.get('issueid__c')
            if issue_id:
                issue_counts[issue_id] += 1

print(f"Matched Cases: {matched_count}")
print(f"Issue Counts: {issue_counts}")

if issue_counts:
    most_common_issue = issue_counts.most_common(1)[0][0]
else:
    most_common_issue = "No issues found"

print("__RESULT__:")
print(json.dumps(most_common_issue))"""

env_args = {'var_function-call-12494898268608421575': [], 'var_function-call-14387351882542337170': [], 'var_function-call-10216368036279649201': [], 'var_function-call-506291646177773946': [], 'var_function-call-11536859067425183255': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'Phone': '000-111-2222', 'Industry': 'Navigation Technology', 'Description': 'NaviCorp Tech excels in developing advanced navigation technologies, with a focus on precision and power efficiency. Utilizing CircuitAI Innovator alongside OptiPower Manager, they deliver solutions that redefine navigation systems, enhancing accuracy and operational excellence.', 'NumberOfEmployees': '800.0', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'Phone': '333-987-6543', 'Industry': 'Technology Manufacturing', 'Description': 'FusionTech Systems stands out in technology manufacturing by integrating AI and cloud-based solutions. With products like AI Cirku-Tech and CloudLink Designer, they commit to providing innovative manufacturing processes. Their dedication to tech-driven manufacturing ensures high-quality, reliable outputs.', 'NumberOfEmployees': '760.0', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'Phone': '839-393-9393', 'Industry': 'Aerospace Engineering', 'Description': "BlueSky Aerospace excels in aerospace engineering through innovative simulation and circuit design tools. With QuantumPCB Modeler and SimuFlow Xtreme, they develop precise and advanced aerospace components. Their continuous pursuit of innovation drives aerospace technology's evolution.", 'NumberOfEmployees': '980.0', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'Phone': '444-333-4444', 'Industry': 'Artificial Intelligence', 'Description': 'NeuralWave Technologies leads advancements in AI-driven solutions for various applications. Using products like AI Cirku-Tech and Workflow Genius, they optimize design processes and enhance power management in AI systems. Focused on innovation, they continue to push the boundaries of artificial intelligence capabilities.', 'NumberOfEmployees': '950.0', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'Phone': '111-222-3334', 'Industry': 'Drones & Aviation', 'Description': 'SkyNet Technologies pioneers in drone development and aviation technology, combining precision design with advanced cloud capabilities. Through QuantumPCB Modeler and CloudLink Designer, they produce innovative and efficient aviation systems. Their contributions set standards in the modernization of aerial technology.', 'NumberOfEmployees': '700.0', 'ShippingState': 'MO'}], 'var_function-call-8027979050295522500': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}], 'var_function-call-14034936189066484870': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}], 'var_function-call-8033806652815484324': [{'id': '#500Wt00000DDYpHIAX', 'orderitemid__c': '802Wt00000790mNIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'id': '#500Wt00000DDZtKIAX', 'orderitemid__c': '802Wt00000799mPIAQ', 'issueid__c': 'a03Wt00000JqzPSIAZ'}, {'id': '500Wt00000DDfx8IAD', 'orderitemid__c': '802Wt00000798K5IAI', 'issueid__c': 'a03Wt00000JqvNUIAZ'}, {'id': '500Wt00000DDg20IAD', 'orderitemid__c': '802Wt00000793bTIAQ', 'issueid__c': 'a03Wt00000JqhItIAJ'}, {'id': '500Wt00000DDxScIAL', 'orderitemid__c': '802Wt00000790WEIAY', 'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'id': '500Wt00000DDxduIAD', 'orderitemid__c': '802Wt00000790WEIAY', 'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'id': '#500Wt00000DDyznIAD', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB'}, {'id': '#500Wt00000DDzJ8IAL', 'orderitemid__c': '802Wt0000079A4AIAU', 'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'id': '#500Wt00000DDzXeIAL', 'orderitemid__c': '802Wt00000798olIAA', 'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'id': '500Wt00000DE0K1IAL', 'orderitemid__c': '802Wt00000798olIAA', 'issueid__c': 'a03Wt00000JqnHwIAJ'}]}

exec(code, env_args)
