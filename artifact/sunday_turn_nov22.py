council = None  # Sunday Nov 22 weekend day turn (light-tick day turn; no full-pass brief)
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, ('REP COUNT', old[:70], c, n)
    s = s.replace(old, new)

# ---------- 1. ages, highest first ----------
rep('day seventy-six', 'day seventy-seven', 3)
rep('day seventy-five', 'day seventy-six', 3)
rep('night sixty-eight', 'night sixty-nine', 2)
rep('day sixty-seven', 'day sixty-eight', 1)
rep('seventy days past', 'seventy-one days past', 4)
rep('sixty days past', 'sixty-one days past', 1)
rep('day forty-one', 'day forty-two', 2)
rep('Thirty-eight days past', 'Thirty-nine days past', 2)
rep('thirty-eight days past', 'thirty-nine days past', 2)
rep('(thirty-eight days)', '(thirty-nine days)', 2)
rep('day thirty-three', 'day thirty-four', 3)
rep('Day thirty-three', 'Day thirty-four', 2)
rep('96 days', '97 days', 1)
rep('Ages as of Nov 21', 'Ages as of Nov 22', 1)
rep('twenty-three days past due', 'twenty-four days past due', 3)
rep('is seventeen days old', 'is eighteen days old', 2)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-21T21:07:00-06:00', '2026-11-22T07:07:00-06:00', 2)
rep('Saturday, November 21', 'Sunday, November 22', 1)
rep('<b>Brief compiled</b> Fri 6:11 AM &middot; data checked Sat 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:11 AM &middot; data checked Sun 7:07 AM CT', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. masthead splice ----------
i = s.index('Saturday is for the neighborhood')
j = s.index('No reactions saved.</p>')
new_masthead = (
 'Sunday is a recovery day: <b>Pilates at 9:30</b> and the <b>red-light bed at 10:30</b>, then '
 'nothing on the calendar. The one piece of business still standing: <b>the $3,000 Exit Code ACH '
 'to Valera bounced Friday at 4:41 PM</b> and nothing since shows a re-send &mdash; two minutes '
 'from the couch clears it. The <b>Kimberly note is nine days old</b> and travels fine on a '
 'Sunday. Quiet motion elsewhere: Steve Myhre wrote Saturday afternoon offering to send Jr the '
 'sandbox files, so <b>Nortec is moving on its own</b>. Going into the holiday week: <b>four '
 'drafts sit unsent</b> (the Tim draft is eighteen days old, the record now at day thirty-four), '
 'and the <b>$5,000 invoice is twenty-four days past due</b> unless the ACH cleared it. '
)
s = s[:i] + new_masthead + s[j:]

# ---------- 4. ledger: close Saturday, open Sunday ----------
rep('the twelfth straight evening with events &mdash; <b>2&ndash;2&ndash;1 by 9:07, window open</b>.',
    'the twelfth straight evening with events. <b>Saturday closes 2&ndash;2&ndash;1</b> &mdash; five events, verified Sunday morning with trash included. The overnight into Sunday was quiet &mdash; <b>0&ndash;0&ndash;0 by 7:07, window open</b>.', 1)

# ---------- 5. todaynote + todaysched ----------
rep('Saturday &mdash; Lady Bird trail cleanup 9:30&ndash;12, Friendsgiving at Ashlyn&rsquo;s 5&ndash;8 &mdash; 5.5h',
    'Sunday &mdash; Pilates 9:30, Recovery Red Light 10:30 &mdash; 2h', 1)
a = s.index('<div class="card sched" id="todaysched">')
b = s.index('</section>', a)
new_sched = ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot free"><div class="t">7:00&ndash;9:30</div><div class="w">Open morning<small><b>Re-send the Exit Code payment</b> (two days since the bounce); the <b>Kimberly note</b> (nine days) travels fine on a Sunday</small></div></div>\n'
 '        <div class="slot"><div class="t">9:30&ndash;10:30</div><div class="w">Pilates<small>Reformer class</small></div></div>\n'
 '        <div class="slot"><div class="t">10:30&ndash;11:30</div><div class="w">Recovery Red Light<small>The weekly reset</small></div></div>\n'
 '        <div class="slot free"><div class="t">11:30&ndash;8:00</div><div class="w">Open rest of day<small>Nothing scheduled &mdash; the holiday-short week starts Monday</small></div></div>\n'
 '      </div>\n    ')
s = s[:a] + new_sched + s[b:]

# ---------- 6. chart roll Sun 22 - Sat 28 ----------
a = s.index('<div class="plot" id="plot">')
b = s.index('<div class="xaxis"', a)
def bar(tot, pct, segs):
    inner = ''.join('<div class="seg %s" style="height:%s%%"></div>' % (k, v) for k, v in segs)
    return ('          <div class="bar"><div class="tot" style="bottom:calc(%s%% + 6px)">%s</div>\n'
            '            %s</div>\n' % (pct, tot, inner))
new_plot = ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 + bar('2', '14.29', [('p', '14.29')])
 + bar('6.75', '48.21', [('m', '12.5'), ('f', '35.71')])
 + bar('8', '57.14', [('m', '21.43'), ('f', '35.71')])
 + bar('6.5', '46.43', [('m', '7.14'), ('f', '35.71'), ('p', '3.57')])
 + bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')])
 + bar('0', '0', [])
 + bar('0', '0', [])
 + '        </div>\n        ')
s = s[:a] + new_plot + s[b:]
rep('<div><b>Sat</b>21</div><div><b>Sun</b>22</div>\n          <div><b>Mon</b>23</div><div><b>Tue</b>24</div><div><b>Wed</b>25</div><div><b>Thu</b>26</div><div><b>Fri</b>27</div>',
    '<div><b>Sun</b>22</div><div><b>Mon</b>23</div>\n          <div><b>Tue</b>24</div><div><b>Wed</b>25</div><div><b>Thu</b>26</div><div><b>Fri</b>27</div><div><b>Sat</b>28</div>', 1)
rep('Sat Nov 21 &ndash; Fri Nov 27', 'Sun Nov 22 &ndash; Sat Nov 28', 1)

# ---------- 7. Today flag ----------
a = s.index('<p><b>Mercury flagged the $3,000 ACH to Valera at 4:41 PM Friday</b>')
b = s.index('</p>', a) + 4
new_flag = ('<p><b>Mercury flagged the $3,000 ACH to Valera at 4:41 PM Friday</b> &mdash; the Exit '
 'Code payment bounced on its due date, and two days on nothing shows a re-send. Two minutes from '
 'the couch clears it; the rest of Sunday is <b>Pilates at 9:30</b>, the <b>red-light bed at '
 '10:30</b>, and recovery before the holiday-short week.</p>')
s = s[:a] + new_flag + s[b:]

# ---------- 9. coming-up ----------
rep('Friendsgiving today, then a holiday-short week',
    'A recovery Sunday, then a holiday-short week', 1)
n = s.index('A recovery Sunday, then a holiday-short week')
l = s.index('<p ', n)
m = s.index('</p>', l) + 4
new_coming = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 2h, both '
 'chosen: <b>Pilates 9:30</b>, <b>Recovery Red Light 10:30</b>. Monday Nov 23 &mdash; 6.75h: sync '
 '8, DW Engineering 10&ndash;2 with <b>the Threshold demo 1&ndash;2 inside it</b>, TTT 2. Tuesday '
 'Nov 24 &mdash; 8h, touching the line: Izzy 10, <b>ATS catch-up 10:30</b>, <b>GamifyOS Sync '
 'noon</b>, <b>Iris training 1</b> inside DW Client 10&ndash;2, TTT 2. Wednesday Nov 25 &mdash; '
 '6.5h: Recover 9, SustAmb 9:30, DW 11&ndash;3, TTT 3. Thursday Nov 26 is Thanksgiving &mdash; '
 '5.5h still on the calendar: DW 8:30&ndash;12:30 with <b>Scott Van Camp inside it at '
 '10&ndash;11</b>, Reserved 3:30 &mdash; worth deciding whether that block survives the holiday. '
 'Friday Nov 27 and Saturday Nov 28 are clear. Carried: <b>the Cathy call</b> (thirty-nine days), '
 '<b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the '
 'Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-four days past '
 'due unless the ACH cleared it</b>.</p>')
s = s[:l] + new_coming + s[m:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-22T07:07:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('Sunday, November 22') == 1
assert s.count('Sun Nov 22 &ndash; Sat Nov 28') == 1
assert s.count('day forty-six') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr', 'fK9Bn7og',
            'quoter.com', 'smartkonnect.app', 'jY9Li67u', 'vercel-dns', 'vee.js']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('SUNDAY TURN OK', len(s))
