council = None  # Wednesday Nov 25 morning full-pass day turn
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, ('REP COUNT', old[:70], c, n)
    s = s.replace(old, new)

# ---------- 1. ages, highest first ----------
rep('day seventy-nine', 'day eighty', 3)
rep('day seventy-eight', 'day seventy-nine', 3)
rep('night seventy-one', 'night seventy-two', 2)
c = len(re.findall(r'day seventy(?!-)', s)); assert c == 1, ('BARE SEVENTY', c)
s = re.sub(r'day seventy(?!-)', 'day seventy-one', s)
rep('seventy-three days past', 'seventy-four days past', 4)
rep('sixty-three days past', 'sixty-four days past', 1)
rep('day forty-four', 'day forty-five', 2)
rep('Forty-one days past', 'Forty-two days past', 2)
rep('forty-one days past', 'forty-two days past', 2)
rep('(forty-one days)', '(forty-two days)', 2)
rep('day thirty-six', 'day thirty-seven', 3)
rep('Day thirty-six', 'Day thirty-seven', 2)
rep('99 days', '100 days', 1)
rep('Ages as of Nov 24', 'Ages as of Nov 25', 1)
rep('twenty-six days past due', 'twenty-seven days past due', 4)
rep('is twenty days old', 'is twenty-one days old', 1)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-24T21:07:00-06:00', '2026-11-25T06:11:00-06:00', 2)
rep('Tuesday, November 24', 'Wednesday, November 25', 1)
rep('<b>Brief compiled</b> Tue 6:12 AM &middot; data checked Tue 9:07 PM CT',
    '<b>Brief compiled</b> Wed 6:11 AM &middot; data checked Wed 6:11 AM CT', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. masthead splice ----------
i = s.index('Tuesday is the last full call day')
j = s.index('No reactions saved.</p>')
new_masthead = (
 'Wednesday is demo day again: <b>Future proofing at 8</b> (Eelco, Jr, Carlos Melo), the '
 '<b>Smart City catch-up at 10</b> &mdash; your reply to Emilio is <b>sitting in Drafts</b>, '
 'written yesterday morning and never sent &mdash; and the <b>Sumo Fiber demo at 11:30</b> '
 '(David Burr, Tuesday&rsquo;s inbound lead). Eight hours, touching the line, with Thanksgiving '
 'tomorrow. Overnight, <b>Chandler hit a snag</b>: the config button is not appearing on his '
 'internal test domain and he is troubleshooting while waiting on a look from your side. '
 '<b>Laura Mathwig asked for help reconciling Lakeland Automall usage charges</b>, <b>Caroline '
 'circled back</b> on the Dec 11 workshop, the <b>Exit Code ACH is on its fifth day</b> with no '
 're-send, and the <b>$5,000 invoice is twenty-seven days past due</b>. '
)
s = s[:i] + new_masthead + s[j:]

# ---------- 4. ledger: close Tuesday, open Wednesday ----------
rep('then nothing until <b>two failures in the evening window</b> (6:19 and 7:01 PM) made it the fifteenth straight evening with events &mdash; <b>2&ndash;1&ndash;1 by 9:07, window open</b>.',
    'then nothing until <b>four evening failures</b> (6:19, 7:01, 10:01 and 10:33 PM) made it the fifteenth straight evening with events. <b>Tuesday closes 4&ndash;1&ndash;1</b> &mdash; six events, the lightest weekday of the stretch, verified Wednesday morning with trash included. The overnight into Wednesday was clean &mdash; <b>0&ndash;0&ndash;0 by 6:11, window open</b>.', 1)

# ---------- 5. todaynote + todaysched ----------
rep('Tuesday &mdash; Izzy 10, ATS 10:30, GamifyOS noon, Iris 1, all inside DW Client 10&ndash;2, TTT 2&ndash;3 &mdash; 8h',
    'Wednesday &mdash; Future proofing 8, Smart City 10, Sumo Fiber demo 11:30 inside DW 11&ndash;3, TTT 3&ndash;4 &mdash; 8h', 1)
a = s.index('<div class="card sched" id="todaysched">')
b = s.index('</section>', a)
new_sched = ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot free"><div class="t">7:00&ndash;8:00</div><div class="w">Open morning<small>Send the <b>Smart City draft</b> before the 10 AM catch-up; the <b>Exit Code re-send</b> (fifth day); a look at <b>Chandler&rsquo;s button issue</b></small></div></div>\n'
 '        <div class="slot"><div class="t">8:00&ndash;9:00</div><div class="w">Future proofing<small>Eelco, Jr and Carlos Melo</small></div></div>\n'
 '        <div class="slot free"><div class="t">9:00&ndash;10:00</div><div class="w">Open hour<small>Buffer &mdash; <b>Laura&rsquo;s Lakeland reconcile ask</b> fits here</small></div></div>\n'
 '        <div class="slot"><div class="t">10:00&ndash;11:00</div><div class="w">Smart City catch-up<small>Emilio and Jr &mdash; the drafted reply covers the update he asked for</small></div></div>\n'
 '        <div class="slot"><div class="t">11:00&ndash;3:00</div><div class="w">Deep Work (Project Engineering)<small>The <b>Sumo Fiber demo runs 11:30&ndash;12:30 inside</b> &mdash; David Burr</small></div></div>\n'
 '        <div class="slot"><div class="t">3:00&ndash;4:00</div><div class="w">Transition, Talking, Triage<small>The <b>Kimberly note</b> (twelve days); replies to <b>Caroline</b> and <b>Laura</b></small></div></div>\n'
 '        <div class="slot free"><div class="t">4:00&ndash;8:00</div><div class="w">Open evening<small>Thanksgiving is tomorrow &mdash; the DW block keep-or-drop is hours away</small></div></div>\n'
 '      </div>\n    ')
s = s[:a] + new_sched + s[b:]

# ---------- 6. chart roll Wed 25 - Tue Dec 1 ----------
a = s.index('<div class="plot" id="plot">')
b = s.index('<div class="xaxis"', a)
def bar(tot, pct, segs):
    inner = ''.join('<div class="seg %s" style="height:%s%%"></div>' % (k, v) for k, v in segs)
    return ('          <div class="bar"><div class="tot" style="bottom:calc(%s%% + 6px)">%s</div>\n'
            '            %s</div>\n' % (pct, tot, inner))
new_plot = ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 + bar('8', '57.14', [('m', '21.43'), ('f', '35.71')])
 + bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')])
 + bar('0', '0', [])
 + bar('0', '0', [])
 + bar('2', '14.29', [('p', '14.29')])
 + bar('5.75', '41.07', [('m', '5.36'), ('f', '35.71')])
 + bar('9.5', '67.86', [('m', '39.29'), ('f', '28.57')])
 + '        </div>\n        ')
s = s[:a] + new_plot + s[b:]
rep('<div><b>Tue</b>24</div><div><b>Wed</b>25</div>\n          <div><b>Thu</b>26</div><div><b>Fri</b>27</div><div><b>Sat</b>28</div><div><b>Sun</b>29</div><div><b>Mon</b>30</div>',
    '<div><b>Wed</b>25</div><div><b>Thu</b>26</div>\n          <div><b>Fri</b>27</div><div><b>Sat</b>28</div><div><b>Sun</b>29</div><div><b>Mon</b>30</div><div><b>Tue</b>1</div>', 1)
rep('Tue Nov 24 &ndash; Mon Nov 30', 'Wed Nov 25 &ndash; Tue Dec 1', 1)

# ---------- 7. Today flag ----------
a = s.index('The morning calls ran &mdash; the Exit Code re-send and Chandler&rsquo;s review are still open</h3>')
b = s.index('worth an answer before the Dec 1 Iris sessions.</p>') + len('worth an answer before the Dec 1 Iris sessions.</p>')
new_flag = ('The Smart City reply is drafted but unsent &mdash; the catch-up is at 10</h3>\n'
 '           <p>You wrote Emilio a reply <b>yesterday at 9:03 AM and it is still in Drafts</b>; '
 'the catch-up runs at 10 with Jr. Two blockers carried in: <b>Chandler is stuck</b> &mdash; the '
 'config button is not appearing on his internal test domain and he is troubleshooting while '
 'waiting on a look from your side &mdash; and the <b>Exit Code re-send is on its fifth day</b>, '
 'the invoice twenty-seven days past due. <b>Laura&rsquo;s Lakeland reconcile ask</b> and '
 '<b>Caroline&rsquo;s second nudge</b> on the Dec 11 workshop both wait for replies.</p>')
s = s[:a] + new_flag + s[b:]

# ---------- 8. Tim pill + markers + pipeline tweaks ----------
rep('Day thirty-seven &mdash; the check-in is at 10 this morning',
    'Day thirty-seven &mdash; next check-in Dec 1', 1)
rep('Monday closed <b>5&ndash;1&ndash;1</b> &mdash; seven events: five failures and a success, all before 7:30 AM, then silence until a 7:25 PM needs-attention made it the <b>fourteenth straight evening with events</b>. Sunday&rsquo;s mid-day flip (eight failures 11 AM&ndash;5:39 PM) is still worth a look in the call logs.',
    'Tuesday closed <b>4&ndash;1&ndash;1</b> &mdash; six events, the lightest weekday of the stretch: a success and a needs-attention before 7:15 AM, silence all day, then <b>four failures between 6:19 and 10:33 PM</b>, the fifteenth straight evening with events. The evening cluster is now the dominant shape of the failure run; Sunday&rsquo;s mid-day flip is still worth a look in the call logs.', 1)
rep('<b>Threshold &mdash; onboarding is moving fast</b>: the CNAME is in and <b>Chandler implemented the PHP and the Dial Translation overnight</b>, sending his config with questions the doc doesn&rsquo;t cover &mdash; he is waiting on a review to proceed; countersignature still the last step, Inteliquent confirmed;',
    '<b>Threshold &mdash; Chandler is implementing and hit a snag</b>: the PHP and Dial Translation are in, but the config button is not appearing on his internal test domain and he is troubleshooting while waiting on a look from your side; countersignature still the last step, Inteliquent confirmed;', 1)
rep('<b>Caroline&rsquo;s workshop reply</b> sits with you and Taylor;',
    '<b>Caroline&rsquo;s workshop reply</b> sits with you and Taylor, and she circled back Tuesday;', 1)

# ---------- 9. coming-up ----------
rep('A stacked Tuesday, then Thanksgiving', 'Demo day again, then Thanksgiving', 1)
n = s.index('Demo day again, then Thanksgiving')
l = s.index('<p ', n)
m = s.index('</p>', l) + 4
new_coming = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 8h, '
 'touching the line: <b>Future proofing 8</b>, <b>Smart City 10</b>, the <b>Sumo Fiber demo '
 '11:30</b> inside DW 11&ndash;3, TTT 3. Tomorrow is Thanksgiving &mdash; 5.5h still on the '
 'calendar: DW 8:30&ndash;12:30 with <b>Scott Van Camp inside it at 10&ndash;11</b>, Reserved '
 '3:30 &mdash; the keep-or-drop call is now hours away. Friday Nov 27 and Saturday Nov 28 are '
 'clear. Sunday Nov 29 &mdash; Pilates 9:30, red-light bed 10:30. Monday Nov 30 &mdash; 5.75h: '
 'Sync 8, DW Engineering 10&ndash;2, TTT 2. Tuesday Dec 1 is the <b>peak of the next stretch '
 '&mdash; 9.5h, well over the line</b>: Izzy 10, ATS 10:30, <b>Heart-Led Wellness x GamifyOS '
 '11</b>, GamifyOS noon and <b>Iris training 1</b> inside DW Client 10&ndash;2, then the '
 '<b>Iris onboarding follow-up at 2</b> and the <b>BFS x GamifyOS demo at 3</b>. Wednesday Dec '
 '2 brings Sustainable Ambition back, and Dec 3 holds DW 8:30&ndash;12:30 plus a 2 PM '
 'appointment. Carried: <b>the Cathy call</b> (forty-two days), <b>the CCI booking</b>, the '
 'drip and performance reports, the ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io '
 'sessions ask</b>, and the <b>invoice &mdash; twenty-seven days past due</b>.</p>')
s = s[:l] + new_coming + s[m:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-25T06:11:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('Wednesday, November 25') == 1
assert s.count('Wed Nov 25 &ndash; Tue Dec 1') == 1
assert s.count('day forty-six') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr', 'fK9Bn7og',
            'quoter.com', 'smartkonnect.app', 'jY9Li67u', 'vercel-dns', 'vee.js',
            'claude-sonnet', 'claude-haiku', 'spa-jzeq-dqt', '3786223867732', '120836304',
            'televolve', '209.189.202.13', '199.191.62.116', '275255105845747', 'bE3ze98A',
            'humenetwork.com']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('WEDNESDAY TURN OK', len(s))
