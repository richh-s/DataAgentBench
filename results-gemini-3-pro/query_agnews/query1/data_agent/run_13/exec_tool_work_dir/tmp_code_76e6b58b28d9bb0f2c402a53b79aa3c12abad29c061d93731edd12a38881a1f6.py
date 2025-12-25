code = """import json
import re

file_path = locals()['var_function-call-11980837049529818020']
with open(file_path, 'r') as f:
    data = json.load(f)

# Regex for keywords to ensure word boundaries
sports_keywords = [
    r"\bbaseball\b", r"\bbasketball\b", r"\bfootball\b", r"\bsoccer\b", r"\btennis\b", r"\bhockey\b", r"\bgolf\b", r"\brugby\b", r"\bcricket\b", r"\bboxing\b", r"\bwrestling\b", r"\bathletics\b", r"\bswimming\b", r"\bgymnastics\b",
    r"\bolympics\b", r"\bolympic\b", r"\bmedal\b", r"\bgold\b", r"\bsilver\b", r"\bbronze\b",
    r"\bnba\b", r"\bnfl\b", r"\bmlb\b", r"\bnhl\b", r"\bfifa\b", r"\buefa\b", r"\bnascar\b", r"\bf1\b", r"\bformula one\b", r"\bgrand prix\b",
    r"\bwimbledon\b", r"\bus open\b", r"\bfrench open\b", r"\baustralian open\b",
    r"\bsuper bowl\b", r"\bworld cup\b", r"\bchampionship\b", r"\btournament\b", r"\bplayoff\b", r"\bstanley cup\b", r"\bworld series\b",
    r"\bquarterback\b", r"\btouchdown\b", r"\bhomerun\b", r"\bshutout\b", r"\bhat-trick\b",
    r"\blakers\b", r"\bbulls\b", r"\bknicks\b", r"\bceltics\b", r"\byankees\b", r"\bred sox\b", r"\bdodgers\b", r"\bgiants\b", r"\bpatriots\b", r"\bcowboys\b", r"\beagles\b", r"\bpackers\b", r"\bred wings\b", r"\bmaple leafs\b", r"\bcanadiens\b", r"\brangers\b", r"\breal madrid\b", r"\bbarcelona\b", r"\bmanchester united\b", r"\bchelsea\b", r"\barsenal\b", r"\bliverpool\b", r"\bac milan\b", r"\bjuventus\b", r"\bbayern munich\b",
    r"\bagassi\b", r"\bfederer\b", r"\broddick\b", r"\bwilliams\b", r"\bsharapova\b", r"\bwoods\b", r"\bmickelson\b", r"\barmstrong\b", r"\bschumacher\b", r"\bphelps\b", r"\bthorpe\b", r"\bbryant\b", r"\boneal\b", r"\bduncan\b", r"\bgarnett\b", r"\bjames\b", r"\bmanning\b", r"\bbrady\b", r"\bvick\b", r"\bowens\b", r"\bbonds\b", r"\bsosa\b", r"\bmcgwire\b", r"\bjeter\b", r"\brodriguez\b", r"\bmartinez\b", r"\bschilling\b", r"\bjohnson\b", r"\blemieux\b", r"\bgretzky\b", r"\bbeckham\b", r"\bronaldo\b", r"\bzidane\b", r"\bhenry\b",
    r"\bcoach\b", r"\bathlete\b", r"\bstadium\b", r"\bwinning streak\b", r"\blosing streak\b", r"\bvarsity\b", r"\bsport\b", r"\bsports\b"
]

def is_sports(text):
    text = text.lower()
    for k in sports_keywords:
        if re.search(k, text):
            return True, k
    return False, None

# Sort by description length
sorted_data = sorted(data, key=lambda x: len(x.get('description', '')), reverse=True)

candidates = []
for d in sorted_data:
    text = (d.get('title', '') + " " + d.get('description', ''))
    is_sp, key = is_sports(text)
    if is_sp:
        # Check for false positives: e.g. "sport" in "sport utility vehicle"
        if key == r"\bsport\b" and "utility" in text:
            continue
            
        candidates.append({
            'title': d.get('title'),
            'len': len(d.get('description', '')),
            'matched_keyword': key,
            'description': d.get('description')[:100] + "..." # truncated for display
        })
        if len(candidates) >= 10:
            break

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-14235117254003200453': [{'_id': '69446cc2ebf4f4e141509be9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-14235117254003203414': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2404915057031312117': [{'_id': '69446cc2ebf4f4e141509be9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446cc2ebf4f4e141509bea', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446cc2ebf4f4e141509beb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446cc2ebf4f4e141509bec', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446cc2ebf4f4e141509bed', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6997860476864382213': [{'COUNT(*)': '127600'}], 'var_function-call-2820495118632274692': [], 'var_function-call-12963950434809988779': [{'_id': '69446cc2ebf4f4e141511119', 'article_id': '30000', 'title': 'Kerry Accuses Bush of Hiding the Truth About Iraq', 'description': 'Senator Kerry leveled his charges in a speech prepared for delivery later today before the National Guard Association in Las Vegas.'}], 'var_function-call-10886045983183967928': [{'_id': '69446cc2ebf4f4e141518649', 'article_id': '60000', 'title': 'BYTE OF THE APPLE', 'description': 'Apple lost one war to Microsoft by not licensing its Mac operating system. It may repeat the error with its iPod and music software.'}], 'var_function-call-17957036424541502436': [{'_id': '69446cc3ebf4f4e14151fb79', 'article_id': '90000', 'title': "Davenport's Victory Over Williams May Not Be Enough", 'description': ' LOS ANGELES (Reuters) - Top-ranked Lindsay Davenport pulled  off a stunning 3-6, 7-5, 6-1 win over Serena Williams at the  WTA Tour Championships Saturday, but her battling effort may  still might not be enough to get her into the semifinals.'}], 'var_function-call-11980837049529818020': 'file_storage/function-call-11980837049529818020.json', 'var_function-call-1987934744290743192': [{'title': "'Trustworthiness' still a goal for Microsoft", 'len': 925, 'matched_keyword': 'sport', 'description': 'January 15, 2005 -- a Saturday -- will almost certainly pass quietly on the bucolic Redmond, Washington, campus of Microsoft Corp. But for those in the field of information technology security, who often make a sport of following the company\'s struggles to secure its products, the date is certain to attract some notice: it\'s the third anniversary of a now-famous internal Microsoft e-mail dubbed the "Trustworthy Computing" memo.&lt;p&gt;ADVERTISEMENT&lt;/p&gt;&lt;p&gt;&lt;img src="http://ad.doubleclick.net/ad/idg.us.ifw.general/sbcspotrssfeed;sz=1x1;ord=200301151450?" width="1" height="1" border="0"/&gt;&lt;a href="http://ad.doubleclick.net/clk;9228975;9651165;a?http://www.infoworld.com/spotlights/sbc/main.html?lpid0103035400730000idlp"&gt;SBC Case Study: Crate   Barrel&lt;/a&gt;&lt;br/&gt;What sold them on improving their network? A system that could cut management costs from the get-go. Find out more.&lt;/p&gt;'}, {'title': 'Bush Visits Canada On Fence-Mending Tour', 'len': 894, 'matched_keyword': 'nfl', 'description': "US President George Bush is visiting Ottawa today, his first stop on a fence-mending tour that takes him to Europe early next year. This is his first official visit to Canada since becoming president four years ago. He skipped Canada in favour of visiting Mexico at the start of his first term in office, and cancelled a state visit to Canada last year, after Canadians got vocal about their opposition to the Iraq conflict.  As CBC News reports, the purpose of this visit may be to smooth relations damaged by the war in Iraq and trade disputes over Canadian beef and softwood lumber. Bush is also expected to ask Martin for a stronger and longer commitment to peacekeeping in Afghanistan and help with organizing elections and rebuilding political institutions in Iraq. CBC News also speculates that Bush may offer a more definitive timetable for reopening the U.S. border to Canada's cattle."}, {'title': ' quot;Hobbits quot; Found In Indonesia', 'len': 838, 'matched_keyword': 'henry', 'description': 'Exploding through the newsnets is the discovery of the remains of seven members of a tiny, previously unknown human species that survived until at least 13,000 years ago, and perhaps co-existed with modern humans right up to the present day.  Adult Homo Florensiensis, nicknamed "Hobbits" by the dig workers who helped uncover the remains at the Liang Bua cave on the island of Flores in Indonesia, were about the size of a three-year-old modern human child, but had a brain one-third the size. Stone tools and pygmy elephant bones found at the site indicate that these "Hobbits" hunted co-operatively together in groups, meaning that they must have had language. "The whole idea that you need a particular brain size to do anything intelligent is completely blown away by this find," commented Dr Henry Gee of Nature magazine to the BBC.'}]}

exec(code, env_args)
