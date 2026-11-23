council = None  # Monday Nov 24 full morning turn: close Sunday 8-3-5, drafts deleted, demo day
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, ('REP COUNT', old[:70], c, n)
    s = s.replace(old, new)

# ---------- 1. ages, highest first ----------
rep('day seventy-seven', 'day seventy-eight', 3)
rep('day seventy-six', 'day seventy-seven', 3)
rep('night sixty-nine', 'night seventy', 2)
rep('day sixty-eight', 'day sixty-nine', 1)
rep('seventy-one days past', 'seventy-two days past', 4)
rep('sixty-one days past', 'sixty-two days past', 1)
rep('day forty-two', 'day forty-three', 2)
rep('Thirty-nine days past', 'Forty days past', 2)
rep('thirty-nine days past', 'forty days past', 2)
rep('(thirty-nine days)', '(forty days)', 2)
rep('day thirty-four', 'day thirty-five', 3)
rep('Day thirty-four', 'Day thirty-five', 2)
rep('97 days', '98 days', 1)
rep('Ages as of Nov 22', 'Ages as of Nov 23', 1)
rep('twenty-four days past due', 'twenty-five days past due', 3)
rep('is eighteen days old', 'is nineteen days old', 2)
rep('nine days old', 'ten days old', 1)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-22T21:07:00-06:00', '2026-11-23T06:12:00-06:00', 2)
rep('Sunday, November 22', 'Monday, November 23', 1)
rep('<b>Brief compiled</b> Fri 6:11 AM &middot; data checked Sun 9:07 PM CT',
    '<b>Brief compiled</b> Mon 6:12 AM &middot; data checked Mon 6:12 AM CT', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. masthead splice ----------
i = s.index('Sunday is a recovery day')
j = s.index('No reactions saved.</p>')
new_masthead = (
 'Monday opens the holiday-short week with the <b>Threshold demo at 1</b> &mdash; Chandler, Brent '
 'and Jeff, with Jr alongside; countersignature is the last step. Before it: sync at 8, Deep Work '
 '10&ndash;2 wrapped around the demo. Two items need two minutes each: <b>the $3,000 Exit Code ACH '
 'to Valera still shows no re-send</b>, three days after Friday&rsquo;s bounce, and the <b>Kimberly '
 'note is ten days old</b>. The weekend emptied Drafts the hard way: <b>all four drafts were '
 'deleted unsent</b> &mdash; the Tim record (day thirty-five) has nothing staged and the Izzy '
 'check-in is tomorrow at 10. The pager had a loud Sunday &mdash; <b>sixteen events, eight of them '
 'failures</b> &mdash; and the overnight into Monday added four more failures. The <b>$5,000 '
 'invoice is twenty-five days past due</b> unless the ACH cleared it. '
)
s = s[:i] + new_masthead + s[j:]

# ---------- 4. ledger: close Sunday, open Monday ----------
rep('an <b>eighth failure at 5:39</b> and a <b>needs-attention at 8:04</b> &mdash; the thirteenth straight evening with events &mdash; <b>8&ndash;3&ndash;5 by 9:07, window open</b>.',
    'an <b>eighth failure at 5:39</b> and a <b>needs-attention at 8:04</b> &mdash; the thirteenth straight evening with events. <b>Sunday closes 8&ndash;3&ndash;5</b> &mdash; sixteen events, tying Thursday, verified Monday morning with trash included. The overnight into Monday was busy: <b>three failures through 5:19 AM</b>, a <b>success at 5:08</b> and a <b>failure at 5:48</b> &mdash; <b>4&ndash;0&ndash;1 by 6:12, window open</b>.', 1)

# ---------- 5. todaynote + todaysched ----------
rep('Sunday &mdash; Pilates 9:30, Recovery Red Light 10:30 &mdash; 2h',
    'Monday &mdash; Sync 8, DW Engineering 10&ndash;2 with the Threshold demo 1&ndash;2 inside, TTT 2&ndash;3 &mdash; 6.75h', 1)
a = s.index('<div class="card sched" id="todaysched">')
b = s.index('</section>', a)
new_sched = ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot free"><div class="t">7:00&ndash;8:00</div><div class="w">Open morning<small><b>Re-send the Exit Code payment</b> before the sync (three days since the bounce); the <b>Kimberly note</b> (ten days)</small></div></div>\n'
 '        <div class="slot"><div class="t">8:00&ndash;8:45</div><div class="w">Weekly Product Sync<small>Eelco and Jr</small></div></div>\n'
 '        <div class="slot free"><div class="t">8:45&ndash;10:00</div><div class="w">Open<small>Demo prep: Threshold runs Inteliquent; countersignature is the last step</small></div></div>\n'
 '        <div class="slot"><div class="t">10:00&ndash;2:00</div><div class="w">Deep Work (Engineering)<small>Illia&rsquo;s Pipedrive review (voxai-851) lives here; the <b>Threshold demo sits inside at 1&ndash;2</b> &mdash; Chandler, Brent, Jeff, with Jr</small></div></div>\n'
 '        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Transition, Talking, Triage<small>Rewrite the Tim record &mdash; the draft is gone, and the Izzy check-in is tomorrow at 10</small></div></div>\n'
 '      </div>\n    ')
s = s[:a] + new_sched + s[b:]

# ---------- 6. chart roll Mon 23 - Sun 29 ----------
a = s.index('<div class="plot" id="plot">')
b = s.index('<div class="xaxis"', a)
def bar(tot, pct, segs):
    inner = ''.join('<div class="seg %s" style="height:%s%%"></div>' % (k, v) for k, v in segs)
    return ('          <div class="bar"><div class="tot" style="bottom:calc(%s%% + 6px)">%s</div>\n'
            '            %s</div>\n' % (pct, tot, inner))
new_plot = ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 + bar('6.75', '48.21', [('m', '12.5'), ('f', '35.71')])
 + bar('8', '57.14', [('m', '21.43'), ('f', '35.71')])
 + bar('6.5', '46.43', [('m', '7.14'), ('f', '35.71'), ('p', '3.57')])
 + bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')])
 + bar('0', '0', [])
 + bar('0', '0', [])
 + bar('2', '14.29', [('p', '14.29')])
 + '        </div>\n        ')
s = s[:a] + new_plot + s[b:]
rep('<div><b>Sun</b>22</div><div><b>Mon</b>23</div>\n          <div><b>Tue</b>24</div><div><b>Wed</b>25</div><div><b>Thu</b>26</div><div><b>Fri</b>27</div><div><b>Sat</b>28</div>',
    '<div><b>Mon</b>23</div><div><b>Tue</b>24</div>\n          <div><b>Wed</b>25</div><div><b>Thu</b>26</div><div><b>Fri</b>27</div><div><b>Sat</b>28</div><div><b>Sun</b>29</div>', 1)
rep('Sun Nov 22 &ndash; Sat Nov 28', 'Mon Nov 23 &ndash; Sun Nov 29', 1)

# ---------- 7. Today flag ----------
a = s.index('<p><b>Mercury flagged the $3,000 ACH to Valera at 4:41 PM Friday</b>')
b = s.index('</p>', a) + 4
new_flag = ('<p><b>Mercury flagged the $3,000 ACH to Valera at 4:41 PM Friday</b> &mdash; three days '
 'on, nothing shows a re-send, and the invoice it was paying is twenty-five days past due. It is a '
 'two-minute Mercury task before the 8 AM sync. The other fixed point today: <b>the Threshold demo '
 'at 1</b>, inside the Deep Work block &mdash; countersignature is the last step.</p>')
s = s[:a] + new_flag + s[b:]

# ---------- 8. Tim li card: draft deleted ----------
a = s.index('<h4>The Tim record is drafted')
b = s.index('</div></li>', a) + 11
new_li = ('<h4>The Tim draft is gone &mdash; all four drafts were deleted unsent over the weekend. '
 'The Oracle record has to be rewritten.</h4>\n'
 '          <p class="why">The written record &mdash; the reply naming the <b>four test orders '
 '&mdash; 102813, 102862, 103088, 101356</b> &mdash; validating Izzy against shipped/backorder, '
 'inventory, lensless and kit cases, and wiring his Google sheet into the flow &mdash; no longer '
 'exists: Drafts is empty and nothing reached Sent. The record promise stands <b>at day '
 'thirty-five</b> with nothing staged, and the <b>Izzy check-in is tomorrow at 10</b>. The '
 '<b>Levitt verdict</b> is the thread&rsquo;s other open item &mdash; iz-10dlc stays open until '
 'someone records it.</p>\n'
 '          <div class="meta"><span class="pill crit">Deleted, unsent</span><span class="pill warn">'
 'Day thirty-five &mdash; rewrite before tomorrow&rsquo;s 10 AM</span></div>\n'
 '        </div></li>')
s = s[:a] + new_li + s[b:]

# ---------- 9. markers ----------
rep('Thursday closed <b>9&ndash;6&ndash;1</b> &mdash; sixteen events, one shy of the seventeen-event record: three morning failures and three needs-attention, then the <b>ninth straight 6&ndash;9 evening</b> and the heaviest yet (needs-attention 6:02, the lone success 6:26, two needs-attention through 6:53, six failures through 7:57).',
    'Sunday closed <b>8&ndash;3&ndash;5</b> &mdash; sixteen events, tying Thursday: a clean five-success morning, then <b>eight failures between 11:14 AM and 5:39 PM</b> and the <b>thirteenth straight 6&ndash;9 evening</b> &mdash; a mid-day flip worth a look in the call logs.', 1)
rep('<b>the Tim reply is on day thirty-five in Drafts</b> &mdash; one Send closes it.',
    '<b>the Tim reply was deleted from Drafts unsent</b> &mdash; it has to be rewritten.', 1)
rep('the shell already framed around Rev&rsquo;s data.</p>',
    'the shell already framed around Rev&rsquo;s data. New this morning: <b>Vapi retires the Claude model your assistants run on Nov 30</b> and will auto-migrate them &mdash; worth checking the affected assistants before the holiday.</p>', 1)

# ---------- 10. coming-up ----------
rep('A recovery Sunday, then a holiday-short week', 'Demo day, then Thanksgiving', 1)
n = s.index('Demo day, then Thanksgiving')
l = s.index('<p ', n)
m = s.index('</p>', l) + 4
new_coming = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 6.75h: '
 'sync 8, DW Engineering 10&ndash;2 with <b>the Threshold demo 1&ndash;2 inside it</b>, TTT 2. '
 'Tuesday Nov 24 &mdash; 8h, touching the line: Izzy 10, <b>ATS catch-up 10:30</b>, <b>GamifyOS '
 'Sync noon</b>, <b>Iris training 1</b> inside DW Client 10&ndash;2, TTT 2. Wednesday Nov 25 '
 '&mdash; 6.5h: Recover 9, SustAmb 9:30, DW 11&ndash;3, TTT 3. Thursday Nov 26 is Thanksgiving '
 '&mdash; 5.5h still on the calendar: DW 8:30&ndash;12:30 with <b>Scott Van Camp inside it at '
 '10&ndash;11</b>, Reserved 3:30 &mdash; still worth deciding whether that block survives the '
 'holiday. Friday Nov 27 and Saturday Nov 28 are clear; Sunday Nov 29 is Pilates and the red-light '
 'bed. Dec 1 stacks up: Izzy, ATS, GamifyOS, Iris training, the <b>Iris onboarding follow-up at '
 '2</b> and the <b>BFS x GamifyOS demo at 3</b>. Carried: <b>the Cathy call</b> (forty days), '
 '<b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the '
 'Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-five days past '
 'due unless the ACH cleared it</b>.</p>')
s = s[:l] + new_coming + s[m:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-23T06:12:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('Monday, November 23') == 1
assert s.count('Mon Nov 23 &ndash; Sun Nov 29') == 1
assert s.count('day forty-six') == 1
assert s.count('four drafts sit unsent') == 0
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr', 'fK9Bn7og',
            'quoter.com', 'smartkonnect.app', 'jY9Li67u', 'vercel-dns', 'vee.js',
            'claude-sonnet', 'claude-haiku']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('MONDAY TURN OK', len(s))
