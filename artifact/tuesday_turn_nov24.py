council = None  # Tuesday Nov 24 morning full-pass day turn
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, ('REP COUNT', old[:70], c, n)
    s = s.replace(old, new)

# ---------- 1. ages, highest first ----------
rep('day seventy-eight', 'day seventy-nine', 3)
rep('day seventy-seven', 'day seventy-eight', 3)
rep('night seventy', 'night seventy-one', 2)
rep('day sixty-nine', 'day seventy', 1)
rep('seventy-two days past', 'seventy-three days past', 4)
rep('sixty-two days past', 'sixty-three days past', 1)
rep('day forty-three', 'day forty-four', 2)
rep('Forty days past', 'Forty-one days past', 2)
rep('forty days past', 'forty-one days past', 2)
rep('(forty days)', '(forty-one days)', 2)
rep('day thirty-five', 'day thirty-six', 2)
rep('Day thirty-five', 'Day thirty-six', 2)
rep('98 days', '99 days', 1)
rep('Ages as of Nov 23', 'Ages as of Nov 24', 1)
rep('twenty-five days past due', 'twenty-six days past due', 4)
rep('is nineteen days old', 'is twenty days old', 1)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-23T21:07:00-06:00', '2026-11-24T06:12:00-06:00', 2)
rep('Monday, November 23', 'Tuesday, November 24', 1)
rep('<b>Brief compiled</b> Mon 6:12 AM &middot; data checked Mon 9:07 PM CT',
    '<b>Brief compiled</b> Tue 6:12 AM &middot; data checked Tue 6:12 AM CT', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. masthead splice ----------
i = s.index('Monday opens the holiday-short week')
j = s.index('No reactions saved.</p>')
new_masthead = (
 'Tuesday is the last full call day before the holiday: <b>Izzy check-in at 10</b> (the Tim '
 'record is at <b>day thirty-six</b> and the rewrite is still unstaged &mdash; the only window '
 'is before 10), then ATS 10:30, GamifyOS noon, <b>Iris training at 1</b>, TTT at 2 &mdash; '
 'eight hours, touching the line. Overnight, <b>Chandler implemented the connection</b> (the PHP '
 'and the Dial Translation) and sent his config with questions the doc doesn&rsquo;t cover '
 '&mdash; <b>he is waiting on a review to proceed</b>. Emilio at <b>Smart City checked in '
 'Monday</b> asking for updates. The <b>Exit Code ACH is on its fourth day</b> with no re-send, '
 'the <b>Kimberly note is eleven days old</b>, Drafts is empty, and the <b>$5,000 invoice is '
 'twenty-six days past due</b>. '
)
s = s[:i] + new_masthead + s[j:]

# ---------- 4. ledger: close Monday, open Tuesday ----------
rep('The overnight into Monday was busy: <b>three failures through 5:19 AM</b>, a <b>success at 5:08</b> and a <b>failure at 5:48</b>, then a <b>fifth failure at 7:28</b>. The afternoon stayed quiet, but a <b>needs-attention at 7:25 PM</b> kept the evening streak alive &mdash; fourteen days now &mdash; <b>5&ndash;1&ndash;1 by 9:07, window open</b>.',
    'The overnight into Monday was busy &mdash; five failures and a success, all before 7:30 AM &mdash; then nothing until a <b>needs-attention at 7:25 PM</b> kept the evening streak alive, fourteen days now. <b>Monday closes 5&ndash;1&ndash;1</b> &mdash; seven events, verified Tuesday morning with trash included. The overnight into Tuesday was quiet &mdash; <b>0&ndash;0&ndash;0 by 6:12, window open</b>.', 1)

# ---------- 5. todaynote + todaysched ----------
rep('Monday &mdash; Sync 8, DW Engineering 10&ndash;2 with the Threshold demo 1&ndash;2 inside, TTT 2&ndash;3 &mdash; 6.75h',
    'Tuesday &mdash; Izzy 10, ATS 10:30, GamifyOS noon, Iris 1, all inside DW Client 10&ndash;2, TTT 2&ndash;3 &mdash; 8h', 1)
a = s.index('<div class="card sched" id="todaysched">')
b = s.index('</section>', a)
new_sched = ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot free"><div class="t">7:00&ndash;10:00</div><div class="w">Open morning<small>The one window before the calls: <b>rewrite the Tim record</b>, the <b>Exit Code re-send</b> (fourth day), and <b>Chandler&rsquo;s config review</b></small></div></div>\n'
 '        <div class="slot"><div class="t">10:00&ndash;10:30</div><div class="w">Izzy Weekly Checkin<small>Tim, Adam, Jr &mdash; the Oracle record is the open promise</small></div></div>\n'
 '        <div class="slot"><div class="t">10:30&ndash;11:00</div><div class="w">ATS/Voxtell catch-up<small>Michael Wheelock&rsquo;s team &mdash; &ldquo;doing this tomorrow&rdquo; is twenty days old</small></div></div>\n'
 '        <div class="slot"><div class="t">11:00&ndash;12:00</div><div class="w">DW Client + Admin + Sales<small>The one quiet hour inside the block</small></div></div>\n'
 '        <div class="slot"><div class="t">12:00&ndash;1:00</div><div class="w">GamifyOS Sync<small>Weekly client sync</small></div></div>\n'
 '        <div class="slot"><div class="t">1:00&ndash;2:00</div><div class="w">Iris Training<small>SpectrumVoIP &mdash; how to sell Iris, Laura&rsquo;s team</small></div></div>\n'
 '        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Transition, Talking, Triage<small>The <b>Kimberly note</b> (eleven days) and a <b>Smart City update for Emilio</b></small></div></div>\n'
 '        <div class="slot free"><div class="t">3:00&ndash;8:00</div><div class="w">Open evening<small>Clear &mdash; Thanksgiving is Thursday</small></div></div>\n'
 '      </div>\n    ')
s = s[:a] + new_sched + s[b:]

# ---------- 6. chart roll Tue 24 - Mon 30 ----------
a = s.index('<div class="plot" id="plot">')
b = s.index('<div class="xaxis"', a)
def bar(tot, pct, segs):
    inner = ''.join('<div class="seg %s" style="height:%s%%"></div>' % (k, v) for k, v in segs)
    return ('          <div class="bar"><div class="tot" style="bottom:calc(%s%% + 6px)">%s</div>\n'
            '            %s</div>\n' % (pct, tot, inner))
new_plot = ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 + bar('8', '57.14', [('m', '21.43'), ('f', '35.71')])
 + bar('6', '42.86', [('m', '7.14'), ('f', '35.71')])
 + bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')])
 + bar('0', '0', [])
 + bar('0', '0', [])
 + bar('2', '14.29', [('p', '14.29')])
 + bar('5.75', '41.07', [('m', '5.36'), ('f', '35.71')])
 + '        </div>\n        ')
s = s[:a] + new_plot + s[b:]
rep('<div><b>Mon</b>23</div><div><b>Tue</b>24</div>\n          <div><b>Wed</b>25</div><div><b>Thu</b>26</div><div><b>Fri</b>27</div><div><b>Sat</b>28</div><div><b>Sun</b>29</div>',
    '<div><b>Tue</b>24</div><div><b>Wed</b>25</div>\n          <div><b>Thu</b>26</div><div><b>Fri</b>27</div><div><b>Sat</b>28</div><div><b>Sun</b>29</div><div><b>Mon</b>30</div>', 1)
rep('Mon Nov 23 &ndash; Sun Nov 29', 'Tue Nov 24 &ndash; Mon Nov 30', 1)

# ---------- 7. Today flag ----------
a = s.index('The Exit Code ACH bounced &mdash; the $3,000 payment needs a re-send</h3>')
b = s.index('</p>', a) + 4
new_flag = ('The Izzy check-in is at 10 &mdash; the Tim record has to be rewritten this '
 'morning</h3>\n           <p>All four drafts died unsent over the weekend, so the <b>Oracle '
 'record rewrite (day thirty-six)</b> has exactly one window: <b>before the 10 AM check-in</b>. '
 'Two more fit the same window: the <b>Exit Code re-send</b> &mdash; four days on, the invoice '
 'twenty-six days past due &mdash; and a reply to <b>Chandler</b>, who implemented the '
 'connection overnight and sent his config with questions the doc doesn&rsquo;t cover; <b>he is '
 'waiting on a review to proceed</b>.</p>')
s = s[:a] + new_flag + s[b:]

# ---------- 8. Tim li card pill ----------
rep('Day thirty-six &mdash; rewrite before tomorrow&rsquo;s 10 AM',
    'Day thirty-six &mdash; the check-in is at 10 this morning', 1)

# ---------- 9. markers: Monday close + Threshold pipeline segment ----------
rep('Sunday closed <b>8&ndash;3&ndash;5</b> &mdash; sixteen events, tying Thursday: a clean five-success morning, then <b>eight failures between 11:14 AM and 5:39 PM</b> and the <b>thirteenth straight 6&ndash;9 evening</b> &mdash; a mid-day flip worth a look in the call logs.',
    'Monday closed <b>5&ndash;1&ndash;1</b> &mdash; seven events: five failures and a success, all before 7:30 AM, then silence until a 7:25 PM needs-attention made it the <b>fourteenth straight evening with events</b>. Sunday&rsquo;s mid-day flip (eight failures 11 AM&ndash;5:39 PM) is still worth a look in the call logs.', 1)
rep('<b>Threshold &mdash; the demo ran Monday at 1 and the CNAME went in by 2:08</b> (Chandler: &ldquo;I will let you know if there are any issues&rdquo;), countersignature the last step, Inteliquent confirmed;',
    '<b>Threshold &mdash; onboarding is moving fast</b>: the CNAME is in and <b>Chandler implemented the PHP and the Dial Translation overnight</b>, sending his config with questions the doc doesn&rsquo;t cover &mdash; he is waiting on a review to proceed; countersignature still the last step, Inteliquent confirmed;', 1)

# ---------- 10. coming-up ----------
rep('Demo day, then Thanksgiving', 'A stacked Tuesday, then Thanksgiving', 1)
n = s.index('A stacked Tuesday, then Thanksgiving')
l = s.index('<p ', n)
m = s.index('</p>', l) + 4
new_coming = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 8h, '
 'touching the line: <b>Izzy 10</b>, <b>ATS 10:30</b>, <b>GamifyOS noon</b>, <b>Iris training '
 '1</b>, all inside DW Client 10&ndash;2, TTT 2. Wednesday Nov 25 slimmed down &mdash; '
 '<b>Recover and Sustainable Ambition came off the calendar</b> &mdash; now 6h: <b>Future '
 'proofing at 8</b> (Eelco, Jr, Carlos Melo), DW 11&ndash;3, TTT 3. Thursday Nov 26 is '
 'Thanksgiving &mdash; 5.5h still on the calendar: DW 8:30&ndash;12:30 with <b>Scott Van Camp '
 'inside it at 10&ndash;11</b>, Reserved 3:30 &mdash; still worth deciding whether that block '
 'survives the holiday. Friday Nov 27 and Saturday Nov 28 are clear. Sunday Nov 29 &mdash; '
 'Pilates 9:30, red-light bed 10:30. Monday Nov 30 &mdash; 5.75h: Sync 8, DW Engineering '
 '10&ndash;2, TTT 2. Dec 1 is the real stack &mdash; eight blocks including <b>Heart-Led '
 'Wellness x GamifyOS at 11</b>, the <b>Iris onboarding follow-up at 2</b> and the <b>BFS x '
 'GamifyOS demo at 3</b>. Carried: <b>the Cathy call</b> (forty-one days), <b>the CCI '
 'booking</b>, the drip and performance reports, the ATS five, the Whova trio, the Sahiti '
 'intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-six days past '
 'due</b>.</p>')
s = s[:l] + new_coming + s[m:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-24T06:12:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('Tuesday, November 24') == 1
assert s.count('Tue Nov 24 &ndash; Mon Nov 30') == 1
assert s.count('day forty-six') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr', 'fK9Bn7og',
            'quoter.com', 'smartkonnect.app', 'jY9Li67u', 'vercel-dns', 'vee.js',
            'claude-sonnet', 'claude-haiku', 'spa-jzeq-dqt', '3786223867732', '120836304',
            'televolve', '209.189.202.13', '199.191.62.116']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('TUESDAY TURN OK', len(s))
