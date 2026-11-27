# Friday Nov 27 morning full turn.
# Thanksgiving closed 0-0-0 (zero events, verified with trash) - sixteen-day
# evening streak ends. Friday calendar completely clear; Sunday Pilates/red-light
# came off. Dan Lievens: old Smart Oracle version dies this weekend.
# Order: content splices first, then age bumps, then asserts, then write.
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f"count {c}!={n} for {old[:70]!r}"
    s = s.replace(old, new)

# ---------- SECTION A: content splices ----------

# A1. Stamps / brief line / eyebrow / greeting
rep('2026-11-26T21:07:00-06:00', '2026-11-27T06:11:00-06:00', 2)
rep('Brief compiled</b> Thu 6:11 AM &middot; data checked Thu 9:07 PM CT',
    'Brief compiled</b> Fri 6:11 AM &middot; data checked Fri 6:11 AM CT', 1)
rep('Thursday, November 26', 'Friday, November 27', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# A2. Masthead splice
i = s.index('Thanksgiving, and the calendar kept its morning:')
j = s.index('No reactions saved.</p>')
assert i < j
new_masthead = (
    'The quiet day finally came: <b>Thanksgiving closed 0&ndash;0&ndash;0</b> &mdash; not a single '
    'ledger event, ending the sixteen-day evening streak &mdash; and today&rsquo;s calendar is '
    '<b>completely clear</b>, with the <b>Sunday Pilates and red-light slots off the calendar too</b>, '
    'so the whole long weekend is open. Both written replies are <b>still in Drafts</b> (Caroline, cc '
    'Ellie, and Smart City). One small deadline: <b>Dan Lievens wrote that the old Smart Oracle version '
    'stops working this weekend</b> &mdash; update the app before Saturday. The <b>Exit Code ACH is on '
    'its seventh day</b> with no re-send, the <b>$5,000 invoice is twenty-nine days past due</b>, and '
    '<b>Vapi&rsquo;s model retirement is Monday</b>. No reactions saved.</p>'
)
s = s[:i] + new_masthead + s[j + len('No reactions saved.</p>'):]

# A3. Ledger: close Thanksgiving, open Friday
rep('The overnight into Thanksgiving was clean &mdash; <b>0&ndash;0&ndash;0 by 9:07, window open</b>.',
    'The overnight into Thanksgiving was clean, and the day stayed that way. <b>Thanksgiving closes '
    '0&ndash;0&ndash;0</b> &mdash; zero events, the first silent day on the ledger and the end of the '
    'sixteen-day evening streak, verified Friday morning with trash included. The overnight into Friday '
    'was clean too &mdash; <b>0&ndash;0&ndash;0 by 6:11, window open</b>.', 1)

# A4. Today flag (h3 + p) - replace Thursday's flag verbatim
old_flag = ('<h3><span class="pill warn">Today</span> Two written replies are sitting in Drafts &mdash; '
            'Caroline and Smart City</h3>\n           <p>The <b>Caroline workshop reply went into Drafts '
            'Wednesday at 9:01 AM</b> (cc Ellie) and has not gone out &mdash; her Dec 11 workshop ask is '
            'now answered on paper only. The <b>Smart City reply to Emilio is still in Drafts too</b>; the '
            'catch-up it was written for already ran Wednesday at 10, so send it as the recap or let the '
            'meeting stand as the answer. <b>Chandler&rsquo;s snag is answered</b>: you replied Wednesday '
            'morning and <b>Jr followed with a config guide at 9:49</b> &mdash; the ball is with '
            'Threshold. Still open: the <b>Exit Code re-send (sixth day)</b> and the <b>Iris audit</b> '
            'you promised Laura ahead of the Dec 1 sessions.</p>')
new_flag = ('<h3><span class="pill warn">Today</span> A clear day &mdash; two drafts to send and one '
            'weekend app deadline</h3>\n           <p>Nothing is on the calendar today. The <b>Caroline '
            'workshop reply</b> (drafted Wednesday 9:01 AM, cc Ellie) and the <b>Smart City reply to '
            'Emilio</b> are both still sitting in Drafts &mdash; each is one click from sent. New and '
            'small: <b>Dan Lievens wrote Wednesday afternoon that the old Smart Oracle version stops '
            'working this weekend</b> &mdash; update the app from the App Store before Saturday. Still '
            'open: the <b>Exit Code re-send (seventh day)</b>, the <b>Iris audit</b> you promised Laura '
            'ahead of the Dec 1 sessions, and <b>Vapi&rsquo;s Monday model retirement</b> &mdash; the '
            'weekend is the last window to check the affected assistants.</p>')
rep(old_flag, new_flag, 1)

# A5. Today note + schedule (clear Friday)
rep('Thanksgiving &mdash; DW 8:30&ndash;12:30 with Scott Van Camp 10&ndash;11 inside, Reserved 3:30 '
    '&mdash; 5.5h',
    'Friday &mdash; nothing scheduled &mdash; 0h', 1)
i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i)
new_sched = ('<div class="card sched" id="todaysched">\n'
    '        <div class="slot free"><div class="t">7:00&ndash;12:00</div><div class="w">Open morning'
    '<small>Nothing scheduled &mdash; the <b>Caroline</b> and <b>Smart City</b> drafts are one click '
    'from sent; the <b>Smart Oracle update</b> is due before Saturday</small></div></div>\n'
    '        <div class="slot free"><div class="t">12:00&ndash;4:00</div><div class="w">Open afternoon'
    '<small>Clear &mdash; a good slot for the <b>Vapi assistant check</b> before Monday&rsquo;s '
    'retirement</small></div></div>\n'
    '        <div class="slot free"><div class="t">4:00&ndash;8:00</div><div class="w">Open evening'
    '<small>Clear &mdash; yesterday was the ledger&rsquo;s first silent day in sixteen</small></div></div>\n'
    '      </div>\n    ')
s = s[:i] + new_sched + s[j:]

# A6. Chart splice + xaxis + weeknote (Fri 27 - Thu Dec 3)
def bar(tot, pct, segs):
    inner = ''.join(f'<div class="seg {k}" style="height:{v}%"></div>' for k, v in segs)
    return (f'<div class="bar"><div class="tot" style="bottom:calc({pct}% + 6px)">{tot}</div>\n'
            f'            {inner}</div>')
bars = [
    bar('0', '0', []),                                               # Fri 27
    bar('0', '0', []),                                               # Sat 28
    bar('0', '0', []),                                               # Sun 29 (Pilates/red-light removed)
    bar('5.75', '41.07', [('m', '5.36'), ('f', '35.71')]),           # Mon 30
    bar('9.5', '67.86', [('m', '39.29'), ('f', '28.57')]),           # Tue 1
    bar('7.5', '53.57', [('p', '3.57'), ('m', '14.29'), ('f', '35.71')]),  # Wed 2
    bar('6.5', '46.43', [('m', '14.29'), ('f', '32.14')]),           # Thu 3
]
new_plot = ('<div class="plot" id="plot">\n'
            '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
            '          ' + '\n          '.join(bars) + '\n        </div>\n        ')
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"', i)
s = s[:i] + new_plot + s[j:]

rep('<div><b>Thu</b>26</div><div><b>Fri</b>27</div>\n          '
    '<div><b>Sat</b>28</div><div><b>Sun</b>29</div><div><b>Mon</b>30</div><div><b>Tue</b>1</div>'
    '<div><b>Wed</b>2</div>',
    '<div><b>Fri</b>27</div><div><b>Sat</b>28</div>\n          '
    '<div><b>Sun</b>29</div><div><b>Mon</b>30</div><div><b>Tue</b>1</div><div><b>Wed</b>2</div>'
    '<div><b>Thu</b>3</div>', 1)
rep('Thu Nov 26 &ndash; Wed Dec 2', 'Fri Nov 27 &ndash; Thu Dec 3', 1)

# A7. Markers: close Thanksgiving
rep('Wednesday closed <b>5&ndash;0&ndash;2</b> &mdash; seven events: two successes before 7:15 AM, '
    'silence through the workday, then <b>five failures between 6:28 and 8:12 PM</b>, the sixteenth '
    'straight evening with events. The evening cluster is now the dominant shape of the failure run; '
    'Sunday&rsquo;s mid-day flip is still worth a look in the call logs.',
    'Thanksgiving closed <b>0&ndash;0&ndash;0</b> &mdash; the first zero-event day on the ledger, '
    'ending sixteen straight evenings with events (Wednesday before it had closed 5&ndash;0&ndash;2, '
    'five failures between 6:28 and 8:12 PM). Whether the quiet was the holiday or a real shift shows '
    'up tonight; Sunday&rsquo;s mid-day flip is still worth a look in the call logs.', 1)

# A8. Pipeline edits
rep('Mercury flagged the $3,000 to Valera at 4:41 PM Friday and the re-send is on its sixth day;',
    'Mercury flagged the $3,000 to Valera at 4:41 PM Friday and the re-send is on its seventh day;', 1)
rep('Four days out: <b>Vapi retires the Claude model your assistants run on Nov 30</b> and will '
    'auto-migrate them &mdash; worth checking the affected assistants over the long weekend.',
    'Monday: <b>Vapi retires the Claude model your assistants run on Nov 30</b> and will auto-migrate '
    'them &mdash; the weekend is the last window to check the affected assistants.', 1)

# A9. Coming-up card (h4 + p)
rep('Thanksgiving, then the Dec 1 peak', 'A clear long weekend, then the Dec 1 peak', 1)
old_cu = ('Today is Thanksgiving &mdash; 5.5h kept on the calendar: DW 8:30&ndash;12:30 with <b>Scott '
          'Van Camp inside it at 10&ndash;11</b>, Reserved 3:30. Friday Nov 27 and Saturday Nov 28 are '
          'clear. Sunday Nov 29 &mdash; Pilates 9:30, red-light bed 10:30. Monday Nov 30 &mdash; 5.75h: '
          'Sync 8, DW Engineering 10&ndash;2, TTT 2; it is also <b>Vapi&rsquo;s model-retirement '
          'day</b>. Tuesday Dec 1 is the <b>peak of the stretch &mdash; 9.5h, well over the line</b>: '
          'Izzy 10, ATS 10:30, <b>Heart-Led Wellness x GamifyOS 11</b>, GamifyOS noon and <b>Iris '
          'training 1</b> inside DW Client 10&ndash;2, then the <b>Iris onboarding follow-up at 2</b> '
          'and the <b>BFS x GamifyOS demo at 3</b>. Wednesday Dec 2 &mdash; 7.5h: Recover 9, '
          'Sustainable Ambition 9:30, Board Group 10:30, DW 11&ndash;3, TTT 3. Dec 3 holds DW '
          '8:30&ndash;12:30, the 2 PM appointment and <b>Scott Van Camp at 4</b>; Dec 4 brings the '
          '<b>Crexendo EVP intro at 11</b> and the <b>Access Systems follow-up at 11:30</b>. Carried: '
          '<b>the Cathy call</b> (forty-three days), <b>the CCI booking</b>, the drip and performance '
          'reports, the ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io sessions ask</b>, '
          'and the <b>invoice &mdash; twenty-eight days past due</b>.</p>')
new_cu = ('Today and Saturday are completely clear, and the <b>Sunday Pilates and red-light slots came '
          'off the calendar</b> &mdash; the whole long weekend is open. Monday Nov 30 &mdash; 5.75h: '
          'Sync 8, DW Engineering 10&ndash;2, TTT 2; it is also <b>Vapi&rsquo;s model-retirement '
          'day</b>. Tuesday Dec 1 is the <b>peak of the stretch &mdash; 9.5h, well over the line</b>: '
          'Izzy 10, ATS 10:30, <b>Heart-Led Wellness x GamifyOS 11</b>, GamifyOS noon and <b>Iris '
          'training 1</b> inside DW Client 10&ndash;2, then the <b>Iris onboarding follow-up at 2</b> '
          'and the <b>BFS x GamifyOS demo at 3</b>. Wednesday Dec 2 &mdash; 7.5h: Recover 9, '
          'Sustainable Ambition 9:30, Board Group 10:30, DW 11&ndash;3, TTT 3. Thursday Dec 3 &mdash; '
          '6.5h: DW 8:30&ndash;12:30, the 2 PM appointment, Reserved 3:30 and <b>Scott Van Camp at '
          '4</b>; Dec 4 brings the <b>Crexendo EVP intro at 11</b> and the <b>Access Systems follow-up '
          'at 11:30</b>. Carried: <b>the Cathy call</b> (forty-four days), <b>the CCI booking</b>, the '
          'drip and performance reports, the ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io '
          'sessions ask</b>, and the <b>invoice &mdash; twenty-nine days past due</b>.</p>')
rep(old_cu, new_cu, 1)

# ---------- SECTION B: age bumps on what remains ----------
assert s.count('day eighty-two') == 0
rep('day eighty-one', 'day eighty-two', 3)
# bare 'day eighty' (not followed by '-'): regex bump to avoid eighty-two collision
bare = re.findall(r'day eighty(?!-)', s)
assert len(bare) == 3, len(bare)
s = re.sub(r'day eighty(?!-)', 'day eighty-one', s)
rep('night seventy-three', 'night seventy-four', 2)
rep('day seventy-two', 'day seventy-three', 1)
rep('seventy-five days past', 'seventy-six days past', 4)
rep('sixty-five days past', 'sixty-six days past', 1)
rep('forty-sixth day double-approved', 'forty-seventh day double-approved', 1)
rep('Iris, day forty-six', 'Iris, day forty-seven', 1)
rep('Promised Sep 15 &mdash; day forty-six', 'Promised Sep 15 &mdash; day forty-seven', 1)
rep('Forty-three days past', 'Forty-four days past', 2)
rep('forty-three days past', 'forty-four days past', 2)
rep('(forty-three days)', '(forty-four days)', 1)   # second instance consumed by A9 splice
rep('day thirty-eight', 'day thirty-nine', 1)
rep('Day thirty-eight', 'Day thirty-nine', 2)
rep('101 days old', '102 days old', 1)
rep('Ages as of Nov 26', 'Ages as of Nov 27', 1)
rep('twenty-eight days past due', 'twenty-nine days past due', 1)  # the Oct 29 one

# ---------- SECTION C: asserts ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-27T06:11:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('Friday, November 27') == 1
assert s.count('Thursday, November 26') == 0
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('day forty-six of billed Logs') == 1
assert s.count('day forty-six') == 1
assert s.count('sixth day') == 0
assert s.count('twenty-eight days past due') == 0
assert s.count('forty-three days') == 0
assert s.count('day thirty-eight') == 0 and s.count('Day thirty-eight') == 0
for bad in ['ebccf397','atscall','3,082','Jose Luiz','5WY67Sa2','PasswordReset','billcenter.net',
            'hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','mm7me9zr','fK9Bn7og','quoter.com','smartkonnect.app',
            'jY9Li67u','vercel-dns','vee.js','claude-sonnet','claude-haiku','spa-jzeq-dqt',
            '3786223867732','120836304','televolve','209.189.202.13','199.191.62.116',
            'humenetwork.com','275255105845747','bE3ze98A']:
    assert bad not in s, bad

open(p, 'w').write(s)
print('ok', len(s))
