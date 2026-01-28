code = """import json
# var_call_6UNCSElGLs46xvjJRtGANxoR is available
res = var_call_6UNCSElGLs46xvjJRtGANxoR
# Extract AgentId
agent_id = None
if res and isinstance(res, list) and len(res) > 0:
    agent_id = res[0].get('AgentId')
# Prepare JSON-serializable string
output = json.dumps({'AgentId': agent_id})
print("__RESULT__:")
print(output)"""

env_args = {'var_call_AbV0x2MmS60aqzP5LB4R439e': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_6UNCSElGLs46xvjJRtGANxoR': [{'AgentId': '005Wt000003NIXCIA4', 'total_sales': '46919.149999999994'}]}

exec(code, env_args)
