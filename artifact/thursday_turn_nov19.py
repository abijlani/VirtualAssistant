# Thursday Nov 20... (Nov 19) full-pass day turn.
# Facts: Wednesday closed 6-0-2 (eight events; failures 5:41a/6:44a/11:33a/7:06p
# + two through 7:55p, successes 1:11p/7:15p; eighth straight 6-9 evening; both
# senders live all day). Thursday opens 0-0-0, overnight quiet. Overnight: PR
# #1228 (dial-by-name/directory fix) MERGED into main; Chandler reported setup
# "completed" and his demo is Monday 1-2; Nortec awaiting DNS/firewall specs;
# a FOURTH draft appeared (LeVarr+Alex cc Laura, onboarding follow-up). Exit Code
# $3,000 due TOMORROW. Week rolls Thu 19 - Wed 25. Hazards: 'hit day thirty'
# frozen; 'day thirty-eight' substring of 'day thirty'; ledger anchored on
# 'Overnight the alerts <b>switched'; chart scale 14 (1h = 7.142857%).
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f'{old[:60]!r}: expected {n}, found {c}'
    s = s.replace(old, new)

# ---------- 1. ages (highest first; day-thirty family handled with care) ----------
rep('day seventy-three', 'day seventy-four', 3)
rep('day seventy-two', 'day seventy-three', 3)
rep('night sixty-five', 'night sixty-six', 2)
rep('day sixty-four', 'day sixty-five', 1)
rep('sixty-seven days past', 'sixty-eight days past', 4)
rep('fifty-seven days past', 'fifty-eight days past', 1)
rep('day thirty-eight', 'day thirty-nine', 1)
rep('Thirty-five days past', 'Thirty-six days past', 2)
rep('thirty-five days past', 'thirty-six days past', 2)
rep('(thirty-five days)', '(thirty-six days)', 2)
rep('hit day thirty', '@@FROZEN@@', 1)
assert len(re.findall(r'day thirty(?!-)', s)) == 7
s = re.sub(r'day thirty(?!-)', 'day thirty-one', s)
assert len(re.findall(r'Day thirty(?!-)', s)) == 2
s = re.sub(r'Day thirty(?!-)', 'Day thirty-one', s)
rep('@@FROZEN@@', 'hit day thirty', 1)
rep('93 days', '94 days', 1)
rep('Ages as of Nov 18', 'Ages as of Nov 19', 1)
rep('twenty days past due', 'twenty-one days past due', 3)
rep('is fourteen days old', 'is fifteen days old', 1)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-18T21:07:00-06:00', '2026-11-19T06:11:00-06:00', 2)
rep('<b>Brief compiled</b> Wed 6:11 AM', '<b>Brief compiled</b> Thu 6:11 AM', 1)
rep('data checked Wed 9:07 PM CT', 'data checked Thu 6:11 AM CT', 1)
rep('Wednesday, November 18', 'Thursday, November 19', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. masthead ----------
i = s.index('Wednesday is kickoff day')
j = s.index('No reactions saved.</p>')
masthead = (
    'Thursday is a partner-facing day: <b>Heart-Led Wellness&rsquo;s first GamifyOS '
    'session runs 11&ndash;12</b> inside Deep Work 8:30&ndash;12:30, the <b>GigTel '
    'platform walkthrough with Tanner is 2&ndash;3</b>, and Scott is at 4. Overnight '
    'brought real closure: <b>the dial-by-name fix merged into main</b> &mdash; the '
    'v45 directory regression that broke Environmental Pest Control&rsquo;s AI Assist '
    'lookup now has its fix shipped; tell Jordan once it deploys. '
    '<b>Chandler wrote &ldquo;this has been completed&rdquo;</b> on his setup thread '
    'and his <b>Threshold demo is locked for Monday 1&ndash;2</b> (Jeff and Brent '
    'invited) &mdash; countersignature is the last step on the usage-only deal. '
    '<b>Nortec is waiting on you</b>: Steve finished his side and asked what DNS and '
    'firewall changes are needed &mdash; that answer is the only thing between Nortec '
    'and deployment. Wednesday also produced an Eelco working session (SmartKonnect '
    'brand and integration approvals, knowledge-base pricing, a customer-success '
    'hire to scope), a full Iris onboarding call with LeVarr, Alex, Laura and Donna '
    '(training mode, warm transfers, the drip campaign, a Square MCP integration '
    'idea, video testimonials) with a <b>Dec 1 follow-up booked</b>, and a <b>fourth '
    'draft</b> &mdash; an onboarding follow-up to LeVarr and Alex, cc Laura, sitting '
    'unsent beside the Affiliated Tech, GigTel and Tim drafts. <b>Exit Code&rsquo;s '
    '$3,000 is due tomorrow.</b> The <b>Kimberly note is six days old</b>. The '
    '<b>$5,000 invoice is twenty-one days past due</b> unless the ACH cleared it. '
    'And nothing in mail or calendar confirms the billing kickoff actually convened '
    'Wednesday &mdash; worth one line to Jr. Thursday opens <b>0&ndash;0&ndash;0</b> '
    'on a quiet overnight. '
)
s = s[:i] + masthead + s[j:]

# ---------- 4. ledger: close Wednesday, open Thursday ----------
i = s.index('Overnight the alerts <b>switched')
j = s.index('not counted).') + len('not counted).')
ledger = (
    'Overnight the alerts <b>began arriving from the new Smart Konnect notification '
    'sender</b> while the old one kept firing &mdash; both pipes live all day, plus a '
    'new <b>&ldquo;Alert: Positive&rdquo;</b> subject format. Wednesday took '
    '<b>failures at 5:41 and 6:44 AM and 11:33</b>, a <b>success at 1:11 PM</b>, then '
    'the <b>6&ndash;9 window&rsquo;s eighth straight evening: a failure at 7:06, a '
    'success at 7:15, and two more failures through 7:55</b>. <b>Wednesday closes '
    '6&ndash;0&ndash;2</b> &mdash; eight events, verified Thursday morning with trash '
    'included (a demo instance also fired twice around 10:58 during the Stratus '
    're-demo &mdash; not counted). The overnight into Thursday stayed quiet &mdash; '
    '<b>0&ndash;0&ndash;0 by 6:11, window open</b>.'
)
s = s[:i] + ledger + s[j:]

# ---------- 5. todaynote + todaysched ----------
rep('Wednesday &mdash; Recover 9, SustAmb 9:30, White Fences call 10:30, DW 11&ndash;3 '
    '(the billing kickoff likely lands here), Iris Onboarding 3&ndash;4, then card, '
    'flowers and the Lady pickup &mdash; 7.75h',
    'Thursday &mdash; DW 8:30&ndash;12:30 with Heart-Led 11&ndash;12 inside it, GigTel '
    'walkthrough 2&ndash;3, Reserved 3:30, Scott 4 &mdash; 7.5h', 1)

i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i)
sched = '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">6:15&ndash;8:30</div><div class="w">Open morning<small><b>Exit Code&rsquo;s $3,000 is due tomorrow</b> &mdash; queue the payment; send the <b>Kimberly note</b> (six days); answer <b>Steve&rsquo;s DNS and firewall question</b> so Nortec can deploy</small></div></div>
        <div class="slot"><div class="t">8:30&ndash;12:30</div><div class="w">Deep Work: Project Engineering<small>The fourth unsent draft (LeVarr and Alex) and Jordan&rsquo;s directory-fix confirmation fit in here</small></div></div>
        <div class="slot"><div class="t">11:00&ndash;12:00</div><div class="w">GamifyOS x Heart-Led Wellness<small>First session &mdash; Ashlyn and Taylor; phase 1 dashboards, phase 2 employees</small></div></div>
        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">GigTel Platform Walkthrough<small>Tanner (Jr optional) &mdash; demo account refresher, tools setup, next steps; the Nov 9 GigTel draft is probably moot after this</small></div></div>
        <div class="slot"><div class="t">3:30&ndash;4:00</div><div class="w">Reserved</div></div>
        <div class="slot"><div class="t">4:00&ndash;5:00</div><div class="w">Call with Scott Van Camp</div></div>
      </div>
    '''
s = s[:i] + sched + s[j:]

# ---------- 6. chart roll Thu 19 - Wed 25 ----------
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"')
plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(17.86% + 6px)">2.5</div>
            <div class="seg m" style="height:3.57%"></div><div class="seg p" style="height:14.29%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(39.29% + 6px)">5.5</div>
            <div class="seg p" style="height:39.29%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg p" style="height:14.29%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(57.14% + 6px)">8</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
        </div>
        '''
s = s[:i] + plot + s[j:]

rep('''<div><b>Wed</b>18</div><div><b>Thu</b>19</div>
          <div><b>Fri</b>20</div><div><b>Sat</b>21</div><div><b>Sun</b>22</div><div><b>Mon</b>23</div><div><b>Tue</b>24</div>''',
    '''<div><b>Thu</b>19</div><div><b>Fri</b>20</div>
          <div><b>Sat</b>21</div><div><b>Sun</b>22</div><div><b>Mon</b>23</div><div><b>Tue</b>24</div><div><b>Wed</b>25</div>''', 1)

rep('Wed Nov 18 &ndash; Tue Nov 24', 'Thu Nov 19 &ndash; Wed Nov 25', 1)

# ---------- 7. Today flag ----------
pill = '<span class="pill warn">Today</span>'
i = s.index(pill) + len(pill)
j = s.index('</p>', i) + 4
flag = (
    ' Exit Code&rsquo;s $3,000 is due tomorrow &mdash; and Nortec is waiting on one '
    'email</h3>\n          <p>Two small sends unblock real money and a real deployment: '
    '<b>queue the Exit Code payment today</b> so Friday&rsquo;s due date passes '
    'quietly, and <b>answer Steve Myhre&rsquo;s DNS-and-firewall question</b> &mdash; '
    'he finished his side Wednesday afternoon and Nortec&rsquo;s deployment now waits '
    'entirely on Voxtell. The <b>Kimberly note is six days old</b>: one line owning '
    'the miss, two concrete times. And <b>four drafts now sit unsent</b> &mdash; the '
    'new LeVarr-and-Alex onboarding follow-up is fresh enough to send in two minutes, '
    'the Tim draft is fifteen days old with the record at day thirty-one, and the '
    'GigTel draft is likely mooted by today&rsquo;s 2 PM walkthrough.</p>'
)
s = s[:i] + flag + s[j:]

# ---------- 8. markers ----------
m = s.index('The week&rsquo;s markers</h4>')
mp = s.index('<p ', m)
pe = s.index('>', mp) + 1
j = s.index('</p>', pe)
markers = (
    'Wednesday closed <b>6&ndash;0&ndash;2</b> &mdash; eight events: morning failures '
    'at 5:41, 6:44 and 11:33, a 1:11 success, then the <b>6&ndash;9 window&rsquo;s '
    'eighth straight evening</b> (failure 7:06, success 7:15, two failures through '
    '7:55). The <b>alert cutover is live</b>: both senders fired all day and the new '
    'platform added an &ldquo;Alert: Positive&rdquo; format. Pipeline: <b>Threshold '
    '&mdash; Chandler&rsquo;s setup is complete and the demo is Monday 1&ndash;2</b>, '
    'countersignature the last step; <b>Nortec &mdash; deployment waits on the DNS '
    'and firewall answer</b>; <b>the dial-by-name fix merged overnight</b>, closing '
    'the v45 directory regression Jordan hit; <b>Access Systems &mdash; Nicole Berry '
    'Friday 1:30</b>, a 500-customer reseller interested in white-labeling; '
    '<b>Stratus expressed interest</b>; <b>Crexendo&rsquo;s NDA is countersigning</b> '
    'with the EVP intro to schedule; <b>Caroline&rsquo;s workshop reply</b> sits with '
    'you and Taylor; <b>Illia&rsquo;s reviews need an owner</b> (#996 closed, #1228 '
    'merged &mdash; #886 and #799 remain); <b>Vitaly interviewed</b>. <b>Exit Code '
    '$3,000 due Friday</b>; the <b>Dec 1 Iris onboarding follow-up</b> is booked; '
    'the billing kickoff&rsquo;s Wednesday outcome is unconfirmed &mdash; ask Jr.'
)
s = s[:pe] + markers + s[j:]

# ---------- 9. coming up ----------
rep('A kickoff Wednesday, a stacked Thursday, then Friendsgiving',
    'A partner-heavy Thursday, then the weekend carries Friendsgiving', 1)
c = s.index('A partner-heavy Thursday, then the weekend carries Friendsgiving')
cp = s.index('<p ', c)
pe = s.index('>', cp) + 1
j = s.index('</p>', pe)
coming = (
    'Today &mdash; 7.5h: DW 8:30&ndash;12:30 with <b>Heart-Led&rsquo;s first session '
    '11&ndash;12 inside it</b>, the <b>GigTel walkthrough 2&ndash;3</b>, Reserved '
    '3:30, <b>Scott Van Camp 4</b>. Friday Nov 20 &mdash; 2.5h: <b>Pitch and Run '
    '8</b>, <b>Gevity pizza party 12:30</b>, then <b>Nicole Berry of Access Systems '
    '1:30</b> (Jr accepted) &mdash; and the <b>Exit Code invoice is due</b>. Saturday '
    '&mdash; 5.5h: <b>Lady Bird trail cleanup 9:30&ndash;12</b>, then '
    '<b>Friendsgiving at Ashlyn&rsquo;s 5&ndash;8</b>. Sunday: Pilates 9:30 and the '
    'red-light bed. Monday Nov 23 &mdash; 6.75h: sync 8, DW Engineering 10&ndash;2 '
    'with <b>the Threshold demo 1&ndash;2 inside it</b>, TTT 2. Tuesday Nov 24 '
    '&mdash; 8h, touching the line: Izzy 10, <b>ATS catch-up 10:30</b>, <b>GamifyOS '
    'Sync noon</b>, <b>Iris training 1</b> inside DW Client 10&ndash;2, TTT 2. '
    'Wednesday Nov 25 &mdash; 6.5h: Recover 9, SustAmb 9:30, DW 11&ndash;3, TTT 3. '
    'Carried: <b>the Cathy call</b> (thirty-six days), <b>the CCI booking</b>, the '
    'drip and performance reports, the ATS five, the Whova trio, the Sahiti intro, '
    'the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-one days past '
    'due unless the ACH cleared it</b>.'
)
s = s[:pe] + coming + s[j:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-19T06:11:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1 and s.count('thirty-three days now') == 1
assert s.count('Wednesday, November 18') == 0 and s.count('@@FROZEN@@') == 0
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr',
            'fK9Bn7og', 'quoter.com', 'smartkonnect.app', 'jY9Li67u']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('thursday turn OK', len(s))
