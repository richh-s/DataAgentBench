code = """import json

def load_var(v):
    # load if file path
    if isinstance(v, str):
        try:
            with open(v, 'r') as f:
                return json.load(f)
        except Exception:
            return v
    return v

# load symbols and descriptions
data = load_var(var_call_N4LMQAANlnNwmoz7cJSdm7gW)
symbols = data['symbols']
desc_map = data['descriptions']

# list of keys from the parallel query results in the same order
keys = [
'var_call_9AlZPA0Q8bteER3sm3Ly8F4t','var_call_nEIV8UrR1fMyltO8Fsn3HjGw','var_call_uBOXBu2dlqXj9XVFmrk1OcT2',
'var_call_DMEjvrX3k7RSxZhtWWaS4Olo','var_call_bcavzZHLdzpnHhmbUz3egk2J','var_call_cYAiNi5i3mrxPFNrlVZ8FhCw',
'var_call_TLEI0GQ0t27M9rFLRe0PzI08','var_call_WPKCO0XCerS49ziI3nx8cl3d','var_call_ThJQb0CkS6X64GpLxogSzkTk',
'var_call_IqNvMDIh9WYWzPqqiqLQogfw','var_call_1SFYynqARey8xpztNZ6AcuF2','var_call_FIAcN0bDhPQXcmrmnoAkCE7S',
'var_call_vpmbAhczGb1RBYnTOxAyFdpD','var_call_1l58TW8G5oc7onKzaCxhIk9e','var_call_xS1SZC9RkbY708CF26aUyam6',
'var_call_wITS7xYPXECSpHkCFlgv20SM','var_call_SZiEqk1t3LjVHd8StN04JgFA','var_call_LgMM4U8eD2haiGheLo1ehOzV',
'var_call_I2G04YcPGjmaOelP9mxNoEOP','var_call_AG0mFOf1Iw2Cp7ohURBiwetJ','var_call_XUA9lCtP4gpCFt0KEkXBT4UP',
'var_call_nhsNyrVKlCjtiOUvYPQzA3R3','var_call_vN9WjseP0LHRZadJ1Pmc0976','var_call_tGKVtFPlQpMrZ5MrOyrtmtg3',
'var_call_o09f2Ihocg3o2M9gX06nlLaw','var_call_WSYONq9gdIPO6oP92yiBXrXd','var_call_l2njJd7nEZ3xN2WofFi6DOTY',
'var_call_XIZCle1lP6Wt4G66Gv5Q4Iar','var_call_8843dOh2wfB2LyhdDuepdiHj','var_call_9fJoACAz84AV2O3HkZfsE6Mo',
'var_call_cZbeMScMaiAOjmztHJPybdeT','var_call_ydEdEZuvEQcZg1J84AlpcT2y','var_call_RfcoKK6fXlEbVw4ItqKsq2TA',
'var_call_y7fruvA37kwcywx7F4BGK1ql','var_call_SlZoIrGT55JtayYyQMC9i4cc','var_call_su74ksQ5CBVVx5MvmLGnUSNT',
'var_call_guRyQt3yWUmDzoIaY6yUHd8S','var_call_WyDRRbxenbOtdi2EWfxHzbHg','var_call_gPScaOZNCVpunxoZOfQApp7U',
'var_call_kPbellbX5hryd4KCraNY3h8B','var_call_BcOUc7jSvsEbTxbNDKiIkeQs','var_call_GmxC7MmJnaZcwlkkOKgcmnhw',
'var_call_W2JmnJ8d9aikZJwNb7Prx1aK','var_call_H7H0y5A3Of25arzmE1hcic8Q','var_call_UDpKBgG4CyAfgeBvCxjArPQF',
'var_call_HkKoGRaFmF8VSFsSIcVdDuDi','var_call_JyUSlOpdC6KLyfavmIvYr3WR','var_call_FSv6H34ZoJJwRZ30O7Duiljg',
'var_call_VP5c4N9vIlYq74dulFxxrKv0','var_call_GA9cCJAXQGbUuzLoeWxZdRXU','var_call_u2JzB358VOzkotOZx1ei8rFv',
'var_call_Z7GAVxLYOwzbUmH517O6GKp8','var_call_6XFRW1FLbLbyY2lwuE3vHk4Q','var_call_dyAHGr6De4MkrcEkkOMlrMpx',
'var_call_Rt6elK66BLoFnmNYblW4UTlg','var_call_JM6OxGJnF0FW3nBt1cXZfBDq','var_call_d2NVgpYeOvzHT9km1k5LHPVL',
'var_call_ccRsjQdzQaqkmAtpTi2y9tPF','var_call_XitvMOyHuy7UVecj9MZ5R2rm','var_call_MY8VbinWQ8XcijSAXZRxBtld',
'var_call_Q12YJgzmUJl9NUc8JjELYMTf','var_call_b9KUQczgfYRxfalSrIgdkWwk','var_call_IQHyIeywXFidrn5155NjchX9',
'var_call_1gveNP5m1LJ7N5UICjP46Z0A','var_call_bxwkQFRkzzZRAS6QVASqLUb3','var_call_61lsVD3JLeZV9vUkTw3XF5o8',
'var_call_CZulgmQqMCnubLdfA7CvVF0d','var_call_M4EkGvsGwCw5sKLpQtRZNLnK','var_call_Ixca49as3vqVIuiJXjIrYLbX',
'var_call_V6xFIAcEEjtJS3zsonnMLxoR','var_call_x8tQobTtag3Z0qDbATCJW4RF','var_call_YY8R3LMeXbzKM5WgMb6LCBml',
'var_call_vl0J0ZfsWBoX4vJwrzbNPm1K','var_call_sb7lk03pjKz0btbliMsRDm9f','var_call_PhR10JyFC97gXWOwAcprXxA7',
'var_call_Lt2UZkbbqUfbTEtjhmC0SDWX','var_call_E8GuyEDxG0X2OPWR5QtGECeC','var_call_u7R26D9eiy2cwE6WRb71fL3F',
'var_call_PVn0WE0EroetGduZlvDAe8Se','var_call_3Xkvw9GNOskSk9dJhpECb97j','var_call_GxUieoKLkMwnPMi9rp3jjciv',
'var_call_OXsuOFE1OWN2gjBlnsI3PSa3','var_call_zsIHXcJx4hJy8Lii0b6lCe5X','var_call_9n9suSIUAs4k8XuRqTloJcLX',
'var_call_JjkyobShdu48Vsz6o0BMuVpo','var_call_UnZUFUyLScr1qETEzGTlI4yo'
]

# collect counts
pairs = []
for i, key in enumerate(keys):
    # guard index
    if i >= len(symbols):
        break
    sym = symbols[i]
    val = globals().get(key)
    val = load_var(val)
    cnt = 0
    try:
        if isinstance(val, list) and len(val) > 0 and 'cnt' in val[0]:
            cnt = int(val[0]['cnt'])
        elif isinstance(val, dict) and 'cnt' in val:
            cnt = int(val['cnt'])
        elif isinstance(val, str):
            # try parse
            parsed = json.loads(val)
            if isinstance(parsed, list) and len(parsed)>0 and 'cnt' in parsed[0]:
                cnt = int(parsed[0]['cnt'])
    except Exception:
        cnt = 0
    pairs.append((sym, cnt))

# sort and get top 5
pairs_sorted = sorted(pairs, key=lambda x: x[1], reverse=True)
top5 = pairs_sorted[:5]

# function to extract company name from description
import re
def extract_name(desc):
    if not desc:
        return ''
    # common markers
    markers = [' specializes', ' is ', ' provides', ' operates', ' focuses', ' based', ' - ', ',']
    idx = None
    for m in markers:
        p = desc.find(m)
        if p != -1:
            idx = p
            break
    if idx is None:
        # try split by period
        p = desc.find('.')
        if p!=-1:
            idx = p
    if idx is None:
        name = desc
    else:
        name = desc[:idx]
    # strip trailing connectors
    name = name.strip()
    # remove corporate suffixes if they appear at end redundantly
    return name

result_names = []
for sym, cnt in top5:
    desc = desc_map.get(sym, '')
    name = extract_name(desc)
    if not name:
        name = sym
    result_names.append({'Symbol': sym, 'Company Name': name, 'Count': cnt})

print('__RESULT__:')
print(json.dumps(result_names))"""

env_args = {'var_call_obofffwTil0kays857PB0osJ': 'file_storage/call_obofffwTil0kays857PB0osJ.json', 'var_call_GWxju3cF897Xt8p4q6hk2Rmi': 'file_storage/call_GWxju3cF897Xt8p4q6hk2Rmi.json', 'var_call_N4LMQAANlnNwmoz7cJSdm7gW': 'file_storage/call_N4LMQAANlnNwmoz7cJSdm7gW.json', 'var_call_77byU4CkUXpGTf3PtUNC8hYk': {'num_symbols': 86, 'symbols_count_preview': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_call_9AlZPA0Q8bteER3sm3Ly8F4t': [{'cnt': '13'}], 'var_call_nEIV8UrR1fMyltO8Fsn3HjGw': [{'cnt': '0'}], 'var_call_uBOXBu2dlqXj9XVFmrk1OcT2': [{'cnt': '0'}], 'var_call_DMEjvrX3k7RSxZhtWWaS4Olo': [{'cnt': '0'}], 'var_call_bcavzZHLdzpnHhmbUz3egk2J': [{'cnt': '15'}], 'var_call_cYAiNi5i3mrxPFNrlVZ8FhCw': [{'cnt': '0'}], 'var_call_TLEI0GQ0t27M9rFLRe0PzI08': [{'cnt': '10'}], 'var_call_WPKCO0XCerS49ziI3nx8cl3d': [{'cnt': '21'}], 'var_call_ThJQb0CkS6X64GpLxogSzkTk': [{'cnt': '16'}], 'var_call_IqNvMDIh9WYWzPqqiqLQogfw': [{'cnt': '0'}], 'var_call_1SFYynqARey8xpztNZ6AcuF2': [{'cnt': '3'}], 'var_call_FIAcN0bDhPQXcmrmnoAkCE7S': [{'cnt': '0'}], 'var_call_vpmbAhczGb1RBYnTOxAyFdpD': [{'cnt': '5'}], 'var_call_1l58TW8G5oc7onKzaCxhIk9e': [{'cnt': '23'}], 'var_call_xS1SZC9RkbY708CF26aUyam6': [{'cnt': '13'}], 'var_call_wITS7xYPXECSpHkCFlgv20SM': [{'cnt': '0'}], 'var_call_SZiEqk1t3LjVHd8StN04JgFA': [{'cnt': '3'}], 'var_call_LgMM4U8eD2haiGheLo1ehOzV': [{'cnt': '0'}], 'var_call_I2G04YcPGjmaOelP9mxNoEOP': [{'cnt': '0'}], 'var_call_AG0mFOf1Iw2Cp7ohURBiwetJ': [{'cnt': '14'}], 'var_call_XUA9lCtP4gpCFt0KEkXBT4UP': [{'cnt': '10'}], 'var_call_nhsNyrVKlCjtiOUvYPQzA3R3': [{'cnt': '0'}], 'var_call_vN9WjseP0LHRZadJ1Pmc0976': [{'cnt': '16'}], 'var_call_tGKVtFPlQpMrZ5MrOyrtmtg3': [{'cnt': '0'}], 'var_call_o09f2Ihocg3o2M9gX06nlLaw': [{'cnt': '0'}], 'var_call_WSYONq9gdIPO6oP92yiBXrXd': [{'cnt': '1'}], 'var_call_l2njJd7nEZ3xN2WofFi6DOTY': [{'cnt': '0'}], 'var_call_XIZCle1lP6Wt4G66Gv5Q4Iar': [{'cnt': '0'}], 'var_call_8843dOh2wfB2LyhdDuepdiHj': [{'cnt': '18'}], 'var_call_9fJoACAz84AV2O3HkZfsE6Mo': [{'cnt': '23'}], 'var_call_cZbeMScMaiAOjmztHJPybdeT': [{'cnt': '1'}], 'var_call_ydEdEZuvEQcZg1J84AlpcT2y': [{'cnt': '0'}], 'var_call_RfcoKK6fXlEbVw4ItqKsq2TA': [{'cnt': '21'}], 'var_call_y7fruvA37kwcywx7F4BGK1ql': [{'cnt': '0'}], 'var_call_SlZoIrGT55JtayYyQMC9i4cc': [{'cnt': '42'}], 'var_call_su74ksQ5CBVVx5MvmLGnUSNT': [{'cnt': '0'}], 'var_call_guRyQt3yWUmDzoIaY6yUHd8S': [{'cnt': '0'}], 'var_call_WyDRRbxenbOtdi2EWfxHzbHg': [{'cnt': '0'}], 'var_call_gPScaOZNCVpunxoZOfQApp7U': [{'cnt': '0'}], 'var_call_kPbellbX5hryd4KCraNY3h8B': [{'cnt': '2'}], 'var_call_BcOUc7jSvsEbTxbNDKiIkeQs': [{'cnt': '1'}], 'var_call_GmxC7MmJnaZcwlkkOKgcmnhw': [{'cnt': '15'}], 'var_call_W2JmnJ8d9aikZJwNb7Prx1aK': [{'cnt': '0'}], 'var_call_H7H0y5A3Of25arzmE1hcic8Q': [{'cnt': '1'}], 'var_call_UDpKBgG4CyAfgeBvCxjArPQF': [{'cnt': '0'}], 'var_call_HkKoGRaFmF8VSFsSIcVdDuDi': [{'cnt': '0'}], 'var_call_JyUSlOpdC6KLyfavmIvYr3WR': [{'cnt': '0'}], 'var_call_FSv6H34ZoJJwRZ30O7Duiljg': [{'cnt': '0'}], 'var_call_VP5c4N9vIlYq74dulFxxrKv0': [{'cnt': '0'}], 'var_call_GA9cCJAXQGbUuzLoeWxZdRXU': [{'cnt': '14'}], 'var_call_u2JzB358VOzkotOZx1ei8rFv': [{'cnt': '3'}], 'var_call_Z7GAVxLYOwzbUmH517O6GKp8': [{'cnt': '1'}], 'var_call_6XFRW1FLbLbyY2lwuE3vHk4Q': [{'cnt': '0'}], 'var_call_dyAHGr6De4MkrcEkkOMlrMpx': [{'cnt': '4'}], 'var_call_Rt6elK66BLoFnmNYblW4UTlg': [{'cnt': '1'}], 'var_call_JM6OxGJnF0FW3nBt1cXZfBDq': [{'cnt': '15'}], 'var_call_d2NVgpYeOvzHT9km1k5LHPVL': [{'cnt': '0'}], 'var_call_ccRsjQdzQaqkmAtpTi2y9tPF': [{'cnt': '12'}], 'var_call_XitvMOyHuy7UVecj9MZ5R2rm': [{'cnt': '15'}], 'var_call_MY8VbinWQ8XcijSAXZRxBtld': [{'cnt': '0'}], 'var_call_Q12YJgzmUJl9NUc8JjELYMTf': [{'cnt': '1'}], 'var_call_b9KUQczgfYRxfalSrIgdkWwk': [{'cnt': '0'}], 'var_call_IQHyIeywXFidrn5155NjchX9': [{'cnt': '8'}], 'var_call_1gveNP5m1LJ7N5UICjP46Z0A': [{'cnt': '0'}], 'var_call_bxwkQFRkzzZRAS6QVASqLUb3': [{'cnt': '19'}], 'var_call_61lsVD3JLeZV9vUkTw3XF5o8': [{'cnt': '12'}], 'var_call_CZulgmQqMCnubLdfA7CvVF0d': [{'cnt': '2'}], 'var_call_M4EkGvsGwCw5sKLpQtRZNLnK': [{'cnt': '1'}], 'var_call_Ixca49as3vqVIuiJXjIrYLbX': [{'cnt': '0'}], 'var_call_V6xFIAcEEjtJS3zsonnMLxoR': [{'cnt': '3'}], 'var_call_x8tQobTtag3Z0qDbATCJW4RF': [{'cnt': '51'}], 'var_call_YY8R3LMeXbzKM5WgMb6LCBml': [{'cnt': '1'}], 'var_call_vl0J0ZfsWBoX4vJwrzbNPm1K': [{'cnt': '32'}], 'var_call_sb7lk03pjKz0btbliMsRDm9f': [{'cnt': '11'}], 'var_call_PhR10JyFC97gXWOwAcprXxA7': [{'cnt': '0'}], 'var_call_Lt2UZkbbqUfbTEtjhmC0SDWX': [{'cnt': '0'}], 'var_call_E8GuyEDxG0X2OPWR5QtGECeC': [{'cnt': '40'}], 'var_call_u7R26D9eiy2cwE6WRb71fL3F': [{'cnt': '38'}], 'var_call_PVn0WE0EroetGduZlvDAe8Se': [{'cnt': '1'}], 'var_call_3Xkvw9GNOskSk9dJhpECb97j': [{'cnt': '0'}], 'var_call_GxUieoKLkMwnPMi9rp3jjciv': [{'cnt': '6'}], 'var_call_OXsuOFE1OWN2gjBlnsI3PSa3': [{'cnt': '14'}], 'var_call_zsIHXcJx4hJy8Lii0b6lCe5X': [{'cnt': '0'}], 'var_call_9n9suSIUAs4k8XuRqTloJcLX': [{'cnt': '15'}], 'var_call_JjkyobShdu48Vsz6o0BMuVpo': [{'cnt': '7'}], 'var_call_UnZUFUyLScr1qETEzGTlI4yo': [{'cnt': '4'}]}

exec(code, env_args)
