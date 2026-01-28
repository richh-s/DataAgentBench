code = """import json
# Load variables from previous calls
ids_records = var_call_Z3v7rE4NpIywiT9yxcRY0vFm
docs1 = var_call_saXqoH8a74y2dHkSYh2k1vdt
docs2 = var_call_BV5l4rbfgW2Kn6ReqTcMTX8j
docs3 = var_call_YikVNZzmzXWj637lrLJmwQ1V
docs4 = var_call_JCMhLuoHto2D9H5PoCxDyzS6
docs5 = var_call_ffP044jrNZ8qGYqPYJ3VY4iq
# Combine docs
all_docs = []
for d in (docs1 + docs2 + docs3 + docs4 + docs5):
    all_docs.append({
        'article_id': int(d.get('article_id')),
        'title': d.get('title',''),
        'description': d.get('description','')
    })
# Build lookup
doc_map = {d['article_id']: d for d in all_docs}
# list of all ids
all_ids = [int(r['article_id']) for r in ids_records]
# classification keywords
sci_kw = ['science','technology','research','lab','electricity','machine','gyro-gen','gameboy','micro-games','micro games','siemens westinghouse','ocean','ocean oversight','ocean research','mobile phone','wireless','fcc','computer']
sports_kw = ['olympic','grand prix','gp','u.s. open','u.s. open','soccer','goal','race','semi-final','defeating','defeat','win','wins','won','match','team','pro bowl','cornerback','wide receiver','broncos','capriati','tennis','formula one','drivers','cycling']
biz_kw = ['stock','stocks','oil','prices','profits','merger','company','companies','trade','exports','wto','market','economic','economy','crude','wireless phone','mobile groups','merger','bank']
# classify
counts = {'Science/Technology':0,'Sports':0,'Business':0,'World':0}
classification = {}
for aid in all_ids:
    text = ''
    doc = doc_map.get(aid)
    if doc:
        text = (doc['title'] + ' ' + doc['description']).lower()
    else:
        text = ''
    cat = None
    # science first
    for kw in sci_kw:
        if kw in text:
            cat = 'Science/Technology'
            break
    if not cat:
        for kw in sports_kw:
            if kw in text:
                cat = 'Sports'
                break
    if not cat:
        for kw in biz_kw:
            if kw in text:
                cat = 'Business'
                break
    if not cat:
        cat = 'World'
    counts[cat] += 1
    classification[aid] = {'category': cat, 'title': doc['title'] if doc else None}
# totals
total = len(all_ids)
sci = counts['Science/Technology']
# fraction
from fractions import Fraction
fr = Fraction(sci, total)
percent = round(100.0 * sci / total, 2) if total>0 else None
result = {
    'science_count': sci,
    'total_count': total,
    'fraction': f"{fr.numerator}/{fr.denominator}",
    'percentage': percent,
    'counts_by_category': counts
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mAfZspeiAlikbNab0gG0xqYa': ['articles'], 'var_call_T7E4bu7rAI55IbxqXsdZvD4i': [{'author_id': '218'}], 'var_call_Z3v7rE4NpIywiT9yxcRY0vFm': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_yyokxzbz0iZSbFRQH8rnGktZ': {'chunks': [[192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918], [62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058], [116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]]}, 'var_call_saXqoH8a74y2dHkSYh2k1vdt': [{'_id': '69598f492f8bd77d09ddf35a', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69598f492f8bd77d09ddfb0b', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69598f492f8bd77d09ddfdb6', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69598f492f8bd77d09ddfe45', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69598f492f8bd77d09de0015', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_call_BV5l4rbfgW2Kn6ReqTcMTX8j': [{'_id': '69598f492f8bd77d09de021c', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}, {'_id': '69598f492f8bd77d09de03f9', 'article_id': '4447', 'title': 'Even in win, nasty vibes', 'description': 'ATHENS -- As you saw yesterday, they #39;re fighting back now. Not with the world, but with themselves. When you #39;ve been humiliated at your own game, ridiculed and laughed at back home and can #39;t intimidate Australia anymore, someone #39;s bound to mope. '}, {'_id': '69598f492f8bd77d09de0784', 'article_id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'description': 'AFP - A Belgian gas explosion in which 20 people were killed may have resulted from a combination of a halt in the gas circulation in a pipeline and existing damage to the main, Belgian television said.'}, {'_id': '69598f492f8bd77d09de0ccb', 'article_id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'description': 'French Prime Minister Jean-Pierre Raffarin declared Sunday that  quot;France will be extremely severe against those who perpetrate anti-semitism, quot; after visiting the Jewish social '}, {'_id': '69598f492f8bd77d09de0d6f', 'article_id': '6869', 'title': 'Somalians sworn in', 'description': 'NAIROBI International mediators swore in members of Somalia #39;s new Parliament on Sunday, a move seen as a crucial step toward establishing the first central government in the country since 1991.'}], 'var_call_YikVNZzmzXWj637lrLJmwQ1V': [{'_id': '69598f492f8bd77d09de159c', 'article_id': '8962', 'title': 'Muenzer races for gold', 'description': 'Athens - Edmonton #39;s Lori-Ann Muenzer moved to within one win of Olympic gold Tuesday, defeating Australian Anna Meares in the semi-final of the sprint cycling.'}, {'_id': '69598f492f8bd77d09de1867', 'article_id': '9677', 'title': 'Israelis to Expand West Bank Settlements', 'description': 'Description: Israeli Prime Minister Ariel Sharon says he is committed to dismantling Jewish settlements in Gaza. But Israel says it will continue to expand Jewish settlements in the West Bank, and cites the tacit approval of the Bush administration.'}, {'_id': '69598f492f8bd77d09de191c', 'article_id': '9858', 'title': 'Stocks End Up as Oil Prices Fall', 'description': 'US stocks ended higher on Wednesday, as a drop in oil prices boosted investor confidence about the economy, but thin volume meant dealers were skeptical about the strength of the rally.'}, {'_id': '69598f492f8bd77d09de2ca7', 'article_id': '14861', 'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'description': " GENEVA (Reuters) - The World Trade Organization's (WTO) top  trade court on Monday rejected a U.S. appeal against a ruling  exonerating the export policies of the Canadian Wheat Board,  diplomats and trade sources said."}, {'_id': '69598f492f8bd77d09de2d96', 'article_id': '15100', 'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'description': ' NEW YORK (Reuters) - Crowd favorite Jennifer Capriati  flirted with disaster before scrambling past Czech Denisa  Chladkova 2-6, 6-1, 6-2 to reach the second round of the U.S.  Open on Monday.'}], 'var_call_JCMhLuoHto2D9H5PoCxDyzS6': [{'_id': '69598f4a2f8bd77d09df05fc', 'article_id': '70498', 'title': 'Owenagainlifts Real Madrid from the doldrums', 'description': 'MADRID, Spain - Michael Owen scored his first Spanish soccer league goal on Saturday to lead Real Madrid over defending champion Valencia, 1-0.'}, {'_id': '69598f4a2f8bd77d09df066a', 'article_id': '70608', 'title': 'Brazilian GP Race Report: Montoya claims first win of 2004', 'description': 'Juan Pablo Montoya held off the charging Kimi Raikkonen to claim Sunday #39;s Brazilian GP, his first win of the season. In wet-dry conditions the Williams driver put in a very impressive performance to win the '}, {'_id': '69598f4a2f8bd77d09df0de7', 'article_id': '72525', 'title': 'Clinton jumps into campaign, as missing explosives force Bush on defensive (AFP)', 'description': 'AFP - Democratic candidate John Kerry charged President George W. Bush with  quot;incredible incompetence quot; over the disappearance of powerful explosives in Iraq, while Bush accused his rival of offering a  quot;strategy of pessimism and retreat quot; in Iraq.'}, {'_id': '69598f4a2f8bd77d09df0fdb', 'article_id': '73025', 'title': 'FCC Approves Merger, Wireless Giant Created', 'description': 'WASHINGTON -- The nation #39;s largest wireless phone company is created by the deal approved Tuesday by the Federal Communications Commission.'}, {'_id': '69598f4a2f8bd77d09df126e', 'article_id': '73684', 'title': 'Crude prices fall after good news from Norway', 'description': ': Crude oil futures fell today as workers in Norway conceded to Government demands to end a strike that could have threatened exports from the world #39;s third-largest supplier.'}], 'var_call_ffP044jrNZ8qGYqPYJ3VY4iq': [{'_id': '69598f4b2f8bd77d09dfba74', 'article_id': '116698', 'title': 'US mobile groups confirm merger', 'description': 'Sprint and Nextel agree to merge in a deal which will create the third largest mobile phone operator in the US.'}, {'_id': '69598f4b2f8bd77d09dfc5fd', 'article_id': '119651', 'title': 'Bush Ordering Better Ocean Oversight (AP)', 'description': "AP - President Bush is creating a White House committee to oversee the nation's ocean policies, with plans to improve research, manage fisheries better and regulate pollution caused by boats."}, {'_id': '69598f4b2f8bd77d09dfc70a', 'article_id': '119920', 'title': 'Indonesian extremists influence Thai Muslims, prime minister says &lt;b&gt;...&lt;/b&gt;', 'description': 'Militants behind the ongoing violence in Thailand #39;s Muslim-majority far south have been indoctrinated by extremists in nearby Indonesia, Prime Minister Thaksin Shinawatra said Saturday.'}, {'_id': '69598f4b2f8bd77d09dfc7db', 'article_id': '120129', 'title': 'Peace delegation leaves Najaf empty-handed as fighting continues', 'description': 'BAGHDAD, Iraq - A national political conference #39;s bid to end the fighting in the Shiite Muslim holy city of Najaf appeared to have failed Tuesday. '}, {'_id': '69598f4b2f8bd77d09dfca57', 'article_id': '120765', 'title': 'Schumacher in uncharted territory', 'description': 'MICHAEL Schumacher doesn #39;t need to win the Belgian Grand Prix on Sunday to nail his unprecedented seventh Formula One drivers title.'}]}

exec(code, env_args)
