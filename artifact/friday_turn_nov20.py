council = None  # Friday Nov 20 full-pass day turn. Precedent: thursday_turn_nov19.py
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, ('REP COUNT', old[:70], c, n)
    s = s.replace(old, new)

# ---------- 1. ages, highest first ----------
rep('day seventy-four', 'day seventy-five', 3)
rep('day seventy-three', 'day seventy-four', 3)
rep('night sixty-six', 'night sixty-seven', 2)
rep('day sixty-five', 'day sixty-six', 1)
rep('sixty-eight days past', 'sixty-nine days past', 4)
rep('fifty-eight days past', 'fifty-nine days past', 1)
rep('day thirty-nine', 'day forty', 1)
rep('Thirty-six days past', 'Thirty-seven days past', 2)
rep('thirty-six days past', 'thirty-seven days past', 2)
rep('(thirty-six days)', '(thirty-seven days)', 2)
rep('day thirty-one', 'day thirty-two', 3)
rep('Day thirty-one', 'Day thirty-two', 2)
rep('94 days', '95 days', 1)
rep('Ages as of Nov 19', 'Ages as of Nov 20', 1)
rep('twenty-one days past due', 'twenty-two days past due', 3)
rep('is fifteen days old', 'is sixteen days old', 2)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-19T21:07:00-06:00', '2026-11-20T06:11:00-06:00', 2)
rep('Thursday, November 19', 'Friday, November 20', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)
rep('<b>Brief compiled</b> Thu 6:11 AM &middot; data checked Thu 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:11 AM &middot; data checked Fri 6:11 AM CT', 1)

# ---------- 3. masthead splice ----------
i = s.index('Thursday is a partner-facing day')
j = s.index('No reactions saved.</p>')
new_masthead = (
 'Friday is a light one &mdash; three commitments, 2.5 hours: <b>Pitch and Run at 8</b>, the '
 '<b>Gevity pizza party 12:30&ndash;1:30</b>, and <b>Nicole Berry of Access Systems at 1:30</b> '
 '(Jr joins) &mdash; a 500-customer reseller asking about white-labeling, booked back-to-back with '
 'the pizza party, so leave by 1:25. Thursday earned the quiet: <b>Exit Code&rsquo;s $3,000 went '
 'out a day early</b>, <b>Nortec went from DNS question to confirmed-good in under four hours</b> '
 '(Steve asked at 2:00, the CNAME went back at 2:19, he ran the onboarding end to end by 2:43, and '
 '&ldquo;the DNS and the connection are good&rdquo; closed it at 5:58), and <b>Jordan&rsquo;s Test '
 'Suite failure was reported at 1:54 and fixed by 3:03</b>. The <b>GigTel walkthrough ran '
 '2&ndash;3</b> &mdash; a transfer issue surfaced during live testing, FreeSwitch integration came '
 'up, and you sent Tanner the onboarding guide at 3:35; the Nov 9 GigTel draft is now moot but '
 'still sits in Drafts. <b>Heart-Led&rsquo;s first GamifyOS session ran 11&ndash;12</b> '
 '(dashboards, the coaching assistant now live, Wiz upgrades), and the morning&rsquo;s '
 '<b>future-proofing session</b> sketched the Spectrum-risk response and Jr&rsquo;s FreeSwitch '
 'prototype. The <b>billing-kickoff question answered itself</b>: Jr followed up with Michael '
 'Ruggiere Thursday afternoon asking for the requirements list &mdash; the shell is already being '
 'framed around Rev&rsquo;s data. Chandler answered the SMS question too &mdash; <b>Threshold uses '
 'Inteliquent</b>, same as Nortec &mdash; and his <b>demo is Monday 1&ndash;2</b>, countersignature '
 'the last step. Still open: the <b>Kimberly note is seven days old</b>; <b>four drafts sit '
 'unsent</b> (the Tim draft is sixteen days old, the record at day thirty-two); the <b>$5,000 '
 'invoice is twenty-two days past due</b> unless the ACH cleared it. Friday opens '
 '<b>0&ndash;0&ndash;0</b> on a quiet overnight &mdash; nothing fired after 7:57 PM. '
)
s = s[:i] + new_masthead + s[j:]

# ---------- 4. ledger splice (close Thursday, open Friday) ----------
a = s.index('The overnight into Thursday stayed quiet',
            s.index('Wednesday closes 6&ndash;0&ndash;2'))
b = s.index('window open</b>.', a) + len('window open</b>.')
new_ledger = (
 'The overnight into Thursday stayed quiet, then Thursday ran heavy: a <b>needs-attention at '
 '6:30 AM</b>, <b>failures at 7:06, 7:25 and 11:29</b> with <b>needs-attention at 7:29 and '
 '11:31</b>, then a ninth-straight evening window that was also the heaviest &mdash; a '
 '<b>needs-attention at 6:02</b>, the day&rsquo;s only <b>success at 6:26</b>, two more '
 'needs-attention through 6:53, and six failures through 7:57. <b>Thursday closes '
 '9&ndash;6&ndash;1</b> &mdash; sixteen events, one shy of the seventeen-event record, verified '
 'Friday morning with trash included. The overnight into Friday stayed quiet &mdash; '
 '<b>0&ndash;0&ndash;0 by 6:11, window open</b>.'
)
s = s[:a] + new_ledger + s[b:]

# ---------- 5. todaynote + todaysched ----------
rep('Thursday &mdash; DW 8:30&ndash;12:30 with Heart-Led 11&ndash;12 inside it, GigTel walkthrough 2&ndash;3, Reserved 3:30, Scott 4 &mdash; 7.5h',
    'Friday &mdash; Pitch and Run 8&ndash;9, Gevity pizza 12:30&ndash;1:30, Nicole Berry 1:30&ndash;2 &mdash; 2.5h', 1)
a = s.index('<div class="card sched" id="todaysched">')
b = s.index('</section>', a)
new_sched = ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot free"><div class="t">6:15&ndash;8:00</div><div class="w">Open morning<small>Send the <b>Kimberly note</b> (seven days) and the <b>LeVarr-and-Alex draft</b> before the day starts moving</small></div></div>\n'
 '        <div class="slot"><div class="t">8:00&ndash;9:00</div><div class="w">Pitch and Run ATX<small>Codependent Cocktails + Coffee &mdash; all paces welcome</small></div></div>\n'
 '        <div class="slot free"><div class="t">9:00&ndash;12:30</div><div class="w">Open block<small>The day&rsquo;s biggest stretch: the <b>Tim draft</b> (sixteen days), the <b>GigTel transfer-issue follow-up</b> from the walkthrough, and the <b>assistant behind the failure stream</b> &mdash; sixteen alert events Thursday makes that five-minute look worth it</small></div></div>\n'
 '        <div class="slot"><div class="t">12:30&ndash;1:30</div><div class="w">Gevity Pizza Party<small>Sammataro at the club &mdash; Nicole Berry starts the minute it ends, so leave by 1:25</small></div></div>\n'
 '        <div class="slot"><div class="t">1:30&ndash;2:00</div><div class="w">Nicole Berry &mdash; Access Systems<small>500-customer reseller, white-label interest; Jr accepted; from the UGM conversation</small></div></div>\n'
 '        <div class="slot free"><div class="t">2:00&ndash;6:00</div><div class="w">Open afternoon<small>Clear runway into the weekend &mdash; Friendsgiving moved to Saturday, so tonight is free</small></div></div>\n'
 '      </div>\n    ')
s = s[:a] + new_sched + s[b:]

# ---------- 6. chart ----------
a = s.index('<div class="plot" id="plot">')
b = s.index('<div class="xaxis"', a)
def bar(tot, pct, segs):
    inner = ''.join('<div class="seg %s" style="height:%s%%"></div>' % (k, v) for k, v in segs)
    return ('          <div class="bar"><div class="tot" style="bottom:calc(%s%% + 6px)">%s</div>\n'
            '            %s</div>\n' % (pct, tot, inner))
new_plot = ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 + bar('2.5', '17.86', [('m', '3.57'), ('p', '14.29')])
 + bar('5.5', '39.29', [('p', '39.29')])
 + bar('2', '14.29', [('p', '14.29')])
 + bar('6.75', '48.21', [('m', '12.5'), ('f', '35.71')])
 + bar('8', '57.14', [('m', '21.43'), ('f', '35.71')])
 + bar('6.5', '46.43', [('m', '7.14'), ('f', '35.71'), ('p', '3.57')])
 + bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')])
 + '        </div>\n        ')
s = s[:a] + new_plot + s[b:]
rep('<div><b>Thu</b>19</div><div><b>Fri</b>20</div>\n          <div><b>Sat</b>21</div><div><b>Sun</b>22</div><div><b>Mon</b>23</div><div><b>Tue</b>24</div><div><b>Wed</b>25</div>',
    '<div><b>Fri</b>20</div><div><b>Sat</b>21</div>\n          <div><b>Sun</b>22</div><div><b>Mon</b>23</div><div><b>Tue</b>24</div><div><b>Wed</b>25</div><div><b>Thu</b>26</div>', 1)
rep('Thu Nov 19 &ndash; Wed Nov 25', 'Fri Nov 20 &ndash; Thu Nov 26', 1)

# ---------- 7. Today flag ----------
rep('<span class="pill warn">Today</span> Exit Code is paid &mdash; Nortec&rsquo;s setup finished today</h3>',
    '<span class="pill warn">Today</span> A light Friday &mdash; one reseller call, and the Kimberly note turns seven days old</h3>', 1)
a = s.index('<p><b>The Exit Code payment is done</b>')
b = s.index('</p>', a) + 4
new_flag = ('<p>The only work meeting is <b>Nicole Berry of Access Systems at 1:30</b> &mdash; a '
 '500-customer reseller interested in white-labeling, Jr joining &mdash; and it starts the minute '
 'the pizza party ends, so leave by 1:25. The real work of the day is the backlog: the <b>Kimberly '
 'note is seven days old</b> (one line owning the miss, two concrete times), and <b>four drafts '
 'sit unsent</b> &mdash; the LeVarr-and-Alex follow-up takes two minutes, the Tim draft is sixteen '
 'days old with the record at day thirty-two, and the GigTel draft was mooted by the walkthrough '
 'and can be discarded.</p>')
s = s[:a] + new_flag + s[b:]

# ---------- 8. markers ----------
k = s.index('The week&rsquo;s markers</h4>')
l = s.index('<p ', k)
m = s.index('</p>', l) + 4
new_markers = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Thursday closed '
 '<b>9&ndash;6&ndash;1</b> &mdash; sixteen events, one shy of the seventeen-event record: three '
 'morning failures and three needs-attention, then the <b>ninth straight 6&ndash;9 evening</b> and '
 'the heaviest yet (needs-attention 6:02, the lone success 6:26, two needs-attention through 6:53, '
 'six failures through 7:57). Pipeline: <b>Threshold &mdash; demo Monday 1&ndash;2</b>, '
 'countersignature the last step, and Chandler confirmed they use Inteliquent; <b>Nortec &mdash; '
 'deployed in one afternoon</b>, DNS question to confirmed-good inside four hours; <b>Access '
 'Systems &mdash; Nicole Berry today 1:30</b>, a 500-customer reseller interested in '
 'white-labeling; <b>GigTel &mdash; walkthrough done, onboarding guide sent</b>, one transfer '
 'issue to chase; <b>Stratus expressed interest</b>; <b>Crexendo&rsquo;s NDA is countersigning</b> '
 'with the EVP intro to schedule; <b>Caroline&rsquo;s workshop reply</b> sits with you and Taylor; '
 '<b>Illia&rsquo;s reviews need an owner</b> (#886 and #799 remain); <b>Vitaly interviewed</b>. '
 '<b>Exit Code is paid</b>; the <b>Dec 1 Iris follow-up</b> is booked; and the billing kickoff '
 'moved &mdash; <b>Jr asked Michael Ruggiere for the requirements list</b>, the shell already '
 'framed around Rev&rsquo;s data.</p>')
s = s[:l] + new_markers + s[m:]

# ---------- 9. coming-up ----------
rep('A partner-heavy Thursday, then the weekend carries Friendsgiving',
    'A light Friday into Friendsgiving weekend, then a holiday-short week', 1)
n = s.index('A light Friday into Friendsgiving weekend, then a holiday-short week')
l = s.index('<p ', n)
m = s.index('</p>', l) + 4
new_coming = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 2.5h: '
 '<b>Pitch and Run 8</b>, <b>Gevity pizza party 12:30</b>, then <b>Nicole Berry of Access Systems '
 '1:30</b> (Jr accepted), back-to-back with the pizza. Saturday &mdash; 5.5h: <b>Lady Bird trail '
 'cleanup 9:30&ndash;12</b>, then <b>Friendsgiving at Ashlyn&rsquo;s 5&ndash;8</b>. Sunday: '
 'Pilates 9:30 and the red-light bed. Monday Nov 23 &mdash; 6.75h: sync 8, DW Engineering '
 '10&ndash;2 with <b>the Threshold demo 1&ndash;2 inside it</b>, TTT 2. Tuesday Nov 24 &mdash; 8h, '
 'touching the line: Izzy 10, <b>ATS catch-up 10:30</b>, <b>GamifyOS Sync noon</b>, <b>Iris '
 'training 1</b> inside DW Client 10&ndash;2, TTT 2. Wednesday Nov 25 &mdash; 6.5h: Recover 9, '
 'SustAmb 9:30, DW 11&ndash;3, TTT 3. Thursday Nov 26 is Thanksgiving &mdash; 5.5h still on the '
 'calendar: DW 8:30&ndash;12:30, <b>Scott Van Camp 2</b>, Reserved 3:30 &mdash; worth deciding '
 'whether that Deep Work block survives the holiday. Carried: <b>the Cathy call</b> (thirty-seven '
 'days), <b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, '
 'the Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-two days '
 'past due unless the ACH cleared it</b>.</p>')
s = s[:l] + new_coming + s[m:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-20T06:11:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('Good evening, Bodhi.') == 0
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('Kimberly note is six days') == 0
assert s.count('Friday, November 20') == 1
assert s.count('Fri Nov 20 &ndash; Thu Nov 26') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr', 'fK9Bn7og',
            'quoter.com', 'smartkonnect.app', 'jY9Li67u', 'vercel-dns']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('FRIDAY TURN OK', len(s))
