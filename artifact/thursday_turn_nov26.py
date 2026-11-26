# Thursday Nov 26 (Thanksgiving) morning full turn.
# Wednesday closed 5-0-2 (verified with trash; overnight clean).
# Order: content splices FIRST (old anchors verbatim from current file),
# then age bumps on what remains, then asserts, then write.
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
rep('2026-11-25T21:07:00-06:00', '2026-11-26T06:11:00-06:00', 2)
rep('Brief compiled</b> Wed 6:11 AM &middot; data checked Wed 9:07 PM CT',
    'Brief compiled</b> Thu 6:11 AM &middot; data checked Thu 6:11 AM CT', 1)
rep('Wednesday, November 25', 'Thursday, November 26', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# A2. Masthead splice
i = s.index('Wednesday is demo day again:')
j = s.index('No reactions saved.</p>')
assert i < j
new_masthead = (
    'Thanksgiving, and the calendar kept its morning: <b>Deep Work 8:30&ndash;12:30</b> with the '
    '<b>Scott Van Camp call inside it at 10</b>, Reserved at 3:30 &mdash; 5.5 hours on a holiday. '
    'Wednesday&rsquo;s demo day ran its full slate and closed <b>5&ndash;0&ndash;2</b>. Two threads moved '
    'while it ran: <b>Chandler&rsquo;s snag is answered</b> &mdash; you replied Wednesday morning and Jr '
    'followed with a config guide, so the ball is back with Threshold &mdash; and <b>your Caroline reply '
    'is written</b>, sitting in Drafts since Wednesday 9:01 AM next to the Smart City draft that never '
    'went out. The <b>Exit Code ACH is on its sixth day</b> with no re-send, the <b>$5,000 invoice is '
    'twenty-eight days past due</b>, and <b>Vapi&rsquo;s model retirement is four days out</b> (Nov 30). '
    'No reactions saved.</p>'
)
s = s[:i] + new_masthead + s[j + len('No reactions saved.</p>'):]

# A3. Ledger: close Wednesday, open Thanksgiving
rep('The evening window then arrived on schedule &mdash; <b>five failures</b> between 6:28 and 8:12 PM, '
    'the sixteenth straight evening with events &mdash; <b>5&ndash;0&ndash;2 by 9:07, window open</b>.',
    'The evening window then arrived on schedule &mdash; <b>five failures</b> between 6:28 and 8:12 PM, '
    'the sixteenth straight evening with events. <b>Wednesday closes 5&ndash;0&ndash;2</b> &mdash; seven '
    'events, verified Thursday morning with trash included. The overnight into Thanksgiving was clean '
    '&mdash; <b>0&ndash;0&ndash;0 by 6:11, window open</b>.', 1)

# A4. Today flag (h3 + p)
old_flag = ('<h3><span class="pill warn">Today</span> The Smart City reply is drafted but unsent &mdash; '
            'the catch-up is at 10</h3>\n           <p>You wrote Emilio a reply <b>yesterday at 9:03 AM and '
            'it is still in Drafts</b>; the catch-up runs at 10 with Jr. Two blockers carried in: '
            '<b>Chandler is stuck</b> &mdash; the config button is not appearing on his internal test '
            'domain and he is troubleshooting while waiting on a look from your side &mdash; and the '
            '<b>Exit Code re-send is on its fifth day</b>, the invoice twenty-seven days past due. '
            '<b>Both SpectrumVoIP asks are answered</b>: you replied to Laura at 9:22 &mdash; promising an '
            '<b>Iris audit</b> on the Lakeland failures &mdash; and to Cole at 9:39 with a routing '
            'approach for his internal use case. Still waiting: <b>Caroline&rsquo;s second nudge</b> on '
            'the Dec 11 workshop.</p>')
new_flag = ('<h3><span class="pill warn">Today</span> Two written replies are sitting in Drafts &mdash; '
            'Caroline and Smart City</h3>\n           <p>The <b>Caroline workshop reply went into Drafts '
            'Wednesday at 9:01 AM</b> (cc Ellie) and has not gone out &mdash; her Dec 11 workshop ask is '
            'now answered on paper only. The <b>Smart City reply to Emilio is still in Drafts too</b>; the '
            'catch-up it was written for already ran Wednesday at 10, so send it as the recap or let the '
            'meeting stand as the answer. <b>Chandler&rsquo;s snag is answered</b>: you replied Wednesday '
            'morning and <b>Jr followed with a config guide at 9:49</b> &mdash; the ball is with '
            'Threshold. Still open: the <b>Exit Code re-send (sixth day)</b> and the <b>Iris audit</b> '
            'you promised Laura ahead of the Dec 1 sessions.</p>')
rep(old_flag, new_flag, 1)

# A5. Today note + schedule (Thanksgiving)
rep('Wednesday &mdash; Future proofing 8, Smart City 10, Sumo Fiber demo 11:30 inside DW 11&ndash;3, '
    'TTT 3&ndash;4 &mdash; 8h',
    'Thanksgiving &mdash; DW 8:30&ndash;12:30 with Scott Van Camp 10&ndash;11 inside, Reserved 3:30 '
    '&mdash; 5.5h', 1)
i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i)
new_sched = ('<div class="card sched" id="todaysched">\n'
    '        <div class="slot free"><div class="t">7:00&ndash;8:30</div><div class="w">Open morning'
    '<small>Holiday morning &mdash; the <b>Caroline</b> and <b>Smart City</b> drafts are both written '
    'and ready to send; the <b>Exit Code re-send</b> enters day six</small></div></div>\n'
    '        <div class="slot"><div class="t">8:30&ndash;12:30</div><div class="w">Deep Work (Project '
    'Engineering)<small>Kept on the holiday &mdash; the <b>Scott Van Camp call runs 10&ndash;11 '
    'inside</b></small></div></div>\n'
    '        <div class="slot free"><div class="t">12:30&ndash;3:30</div><div class="w">Open afternoon'
    '<small>Thanksgiving</small></div></div>\n'
    '        <div class="slot"><div class="t">3:30&ndash;4:00</div><div class="w">Reserved'
    '<small>Protected half-hour</small></div></div>\n'
    '        <div class="slot free"><div class="t">4:00&ndash;8:00</div><div class="w">Open evening'
    '<small>Thanksgiving dinner &mdash; the ledger&rsquo;s evening window has run sixteen straight '
    'days</small></div></div>\n'
    '      </div>\n    ')
s = s[:i] + new_sched + s[j:]

# A6. Chart splice + xaxis + weeknote
def bar(tot, pct, segs):
    inner = ''.join(f'<div class="seg {k}" style="height:{v}%"></div>' for k, v in segs)
    return (f'<div class="bar"><div class="tot" style="bottom:calc({pct}% + 6px)">{tot}</div>\n'
            f'            {inner}</div>')
bars = [
    bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')]),            # Thu 26
    bar('0', '0', []),                                               # Fri 27
    bar('0', '0', []),                                               # Sat 28
    bar('2', '14.29', [('p', '14.29')]),                             # Sun 29
    bar('5.75', '41.07', [('m', '5.36'), ('f', '35.71')]),           # Mon 30
    bar('9.5', '67.86', [('m', '39.29'), ('f', '28.57')]),           # Tue 1
    bar('7.5', '53.57', [('p', '3.57'), ('m', '14.29'), ('f', '35.71')]),  # Wed 2
]
new_plot = ('<div class="plot" id="plot">\n'
            '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
            '          ' + '\n          '.join(bars) + '\n        </div>\n        ')
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"', i)
s = s[:i] + new_plot + s[j:]

rep('<div><b>Wed</b>25</div><div><b>Thu</b>26</div>\n          '
    '<div><b>Fri</b>27</div><div><b>Sat</b>28</div><div><b>Sun</b>29</div><div><b>Mon</b>30</div>'
    '<div><b>Tue</b>1</div>',
    '<div><b>Thu</b>26</div><div><b>Fri</b>27</div>\n          '
    '<div><b>Sat</b>28</div><div><b>Sun</b>29</div><div><b>Mon</b>30</div><div><b>Tue</b>1</div>'
    '<div><b>Wed</b>2</div>', 1)
rep('Wed Nov 25 &ndash; Tue Dec 1', 'Thu Nov 26 &ndash; Wed Dec 2', 1)

# A7. Markers: close Wednesday
rep('Tuesday closed <b>4&ndash;1&ndash;1</b> &mdash; six events, the lightest weekday of the stretch: a '
    'success and a needs-attention before 7:15 AM, silence all day, then <b>four failures between 6:19 '
    'and 10:33 PM</b>, the fifteenth straight evening with events.',
    'Wednesday closed <b>5&ndash;0&ndash;2</b> &mdash; seven events: two successes before 7:15 AM, '
    'silence through the workday, then <b>five failures between 6:28 and 8:12 PM</b>, the sixteenth '
    'straight evening with events.', 1)

# A8. Pipeline edits
rep('<b>Threshold &mdash; Chandler is implementing and hit a snag</b>: the PHP and Dial Translation are '
    'in, but the config button is not appearing on his internal test domain and he is troubleshooting '
    'while waiting on a look from your side; countersignature still the last step, Inteliquent confirmed;',
    '<b>Threshold &mdash; Chandler&rsquo;s snag is answered</b>: the PHP and Dial Translation are in, '
    'the config button was not appearing on his test setup, and <b>Jr sent a config guide Wednesday '
    'morning</b> after your reply &mdash; the ball is back with Threshold; countersignature still the '
    'last step, Inteliquent confirmed;', 1)
rep('<b>Caroline&rsquo;s workshop reply</b> sits with you and Taylor, and she circled back Tuesday;',
    '<b>Caroline&rsquo;s workshop reply is written</b> &mdash; drafted Wednesday morning, cc Ellie, '
    'still in Drafts;', 1)
rep('<b>Exit Code&rsquo;s ACH bounced</b> &mdash; Mercury flagged the $3,000 to Valera at 4:41 PM Friday '
    'and it needs a re-send;',
    '<b>Exit Code&rsquo;s ACH bounced</b> &mdash; Mercury flagged the $3,000 to Valera at 4:41 PM Friday '
    'and the re-send is on its sixth day;', 1)
rep('right after today&rsquo;s catch-up', 'right after Tuesday&rsquo;s catch-up', 1)
rep('New this morning: <b>Vapi retires the Claude model your assistants run on Nov 30</b> and will '
    'auto-migrate them &mdash; worth checking the affected assistants before the holiday.',
    'Four days out: <b>Vapi retires the Claude model your assistants run on Nov 30</b> and will '
    'auto-migrate them &mdash; worth checking the affected assistants over the long weekend.', 1)

# A9. Coming-up card (h4 + p)
rep('Demo day again, then Thanksgiving', 'Thanksgiving, then the Dec 1 peak', 1)
old_cu = ('Today &mdash; 8h, touching the line: <b>Future proofing 8</b>, <b>Smart City 10</b>, the '
          '<b>Sumo Fiber demo 11:30</b> inside DW 11&ndash;3, TTT 3. Tomorrow is Thanksgiving &mdash; '
          '5.5h still on the calendar: DW 8:30&ndash;12:30 with <b>Scott Van Camp inside it at '
          '10&ndash;11</b>, Reserved 3:30 &mdash; the keep-or-drop call is now hours away. Friday Nov 27 '
          'and Saturday Nov 28 are clear. Sunday Nov 29 &mdash; Pilates 9:30, red-light bed 10:30. '
          'Monday Nov 30 &mdash; 5.75h: Sync 8, DW Engineering 10&ndash;2, TTT 2. Tuesday Dec 1 is the '
          '<b>peak of the next stretch &mdash; 9.5h, well over the line</b>: Izzy 10, ATS 10:30, '
          '<b>Heart-Led Wellness x GamifyOS 11</b>, GamifyOS noon and <b>Iris training 1</b> inside DW '
          'Client 10&ndash;2, then the <b>Iris onboarding follow-up at 2</b> and the <b>BFS x GamifyOS '
          'demo at 3</b>. Wednesday Dec 2 brings Sustainable Ambition back, and Dec 3 holds DW '
          '8:30&ndash;12:30 plus a 2 PM appointment. Carried: <b>the Cathy call</b> (forty-two days), '
          '<b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the '
          'Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-seven days '
          'past due</b>.</p>')
new_cu = ('Today is Thanksgiving &mdash; 5.5h kept on the calendar: DW 8:30&ndash;12:30 with <b>Scott '
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
rep(old_cu, new_cu, 1)

# ---------- SECTION B: age bumps on what remains ----------
assert s.count('day eighty-one') == 0
rep('day eighty', 'day eighty-one', 3)
rep('day seventy-nine', 'day eighty', 3)
rep('night seventy-two', 'night seventy-three', 2)
rep('day seventy-one', 'day seventy-two', 1)
rep('seventy-four days past', 'seventy-five days past', 4)
rep('sixty-four days past', 'sixty-five days past', 1)
rep('forty-fifth day double-approved', 'forty-sixth day double-approved', 1)
rep('day forty-five', 'day forty-six', 2)
rep('Forty-two days past', 'Forty-three days past', 2)
rep('forty-two days past', 'forty-three days past', 2)
rep('(forty-two days)', '(forty-three days)', 1)   # second instance consumed by A9 splice
rep('at day thirty-seven</b> with nothing staged, and the <b>Izzy check-in is tomorrow at 10</b>',
    'at day thirty-eight</b> with nothing staged, and the <b>Izzy check-in is Dec 1 at 10</b>', 1)
rep('Day thirty-seven', 'Day thirty-eight', 2)
rep('100 days old', '101 days old', 1)
rep('Ages as of Nov 25', 'Ages as of Nov 26', 1)
rep('twenty-seven days past due', 'twenty-eight days past due', 1)  # the Oct 29 one; others spliced

# ---------- SECTION C: asserts ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-26T06:11:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('Thursday, November 26') == 1
assert s.count('Wednesday, November 25') == 0
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('day forty-six of billed Logs') == 1
assert s.count('day forty-six') == 3
assert s.count('fifth day') == 0
assert s.count('twenty-seven days past due') == 0
assert s.count('day thirty-seven') == 0 and s.count('Day thirty-seven') == 0
assert s.count('forty-two days') == 0
for bad in ['ebccf397','atscall','3,082','Jose Luiz','5WY67Sa2','PasswordReset','billcenter.net',
            'hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','mm7me9zr','fK9Bn7og','quoter.com','smartkonnect.app',
            'jY9Li67u','vercel-dns','vee.js','claude-sonnet','claude-haiku','spa-jzeq-dqt',
            '3786223867732','120836304','televolve','209.189.202.13','199.191.62.116',
            'humenetwork.com','275255105845747','bE3ze98A']:
    assert bad not in s, bad

open(p, 'w').write(s)
print('ok', len(s))
