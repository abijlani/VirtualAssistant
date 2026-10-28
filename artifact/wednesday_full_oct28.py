# Wednesday Oct 28, 2026 — FULL morning pass (UGM day 3, Austin).
# Tuesday closed 5F/0NA/3S. Wednesday opened with a failure pair 7:18/7:19 AM.
# NEW from the floor (Granola Tue): Michael/CCI (AppDirect-acquired, RingCentral seats
# in play, Telzino 25c/min pain, wants a call next week) and David/Dynalink (call
# intelligence, david@dynalink.com). NEW ask from Laura (Tue 11:54 AM): reach out to
# the Hubler channel partner — Iris feature refresh + current-state evaluation for the
# two active Hubler agents (call error flagged). Emilio closed the loop Tue 8:46 AM
# ("Sounds good, thanks!"). Drafts still unsent => Tim day nine. Calendar: UGM
# recurrences trimmed off Nov 3-5; Hand and Stone added Thu 8-9 PM. Iris $5,000
# invoice due TOMORROW (Oct 29). Chart rolls Wed 28 - Tue Nov 3. cc-state empty.
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    assert s.count(old) == n, f"{old!r}: {s.count(old)} != {n}"
    s = s.replace(old, new)

def rx(pat, new, n, flags=0):
    global s
    s, c = re.subn(pat, new, s, flags=flags)
    assert c == n, f"{pat!r}: {c} != {n}"

# ---------- global age bumps FIRST ----------
rep('day fifty-one', 'day fifty-two', 3)                     # #799
rx(r'day fifty(?!-)', 'day fifty-one', 3)                    # Eric / Izzy trio
rep('day forty-two;', 'day forty-three;', 1)                 # JDs
rep('forty-five days past', 'forty-six days past', 2)
rep('night forty-three', 'night forty-four', 2)
rep('thirty-five days past', 'thirty-six days past', 1)      # Appulse
rep('thirteen days past', 'fourteen days past', 6)           # ProGraphix
rep('Thirteen days past', 'Fourteen days past', 1)
rep('day eight', 'day nine', 5)                              # Tim ('day eighteen' == 0)
rep('Seven days past the promise', 'Eight days past the promise', 1)
rep('Iris, day sixteen', 'Iris, day seventeen', 1)
rep('hr-nda is 71 days old', 'hr-nda is 72 days old', 1)
rep('Ages as of Oct 27', 'Ages as of Oct 28', 1)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- date turn ----------
rep('2026-10-27T22:07:00-05:00', '2026-10-28T07:40:00-05:00', 2)
rep('Tuesday, October 27 &middot; 2026', 'Wednesday, October 28 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)
rep('<b>Brief compiled</b> Tue 7:50 AM &middot; data checked Tue 10:07 PM CT',
    '<b>Brief compiled</b> Wed 7:40 AM &middot; data checked Wed 7:40 AM CT', 1)

# masthead (full replace)
m0 = s.find('Monday closed gently for a UGM day:')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Tuesday closed <b>5&ndash;0&ndash;3</b> &mdash; a quiet booth day, a burst as Banger&rsquo;s began (failures '
 '6:01&ndash;6:31), done by 6:44. The floor produced: <b>Michael from CCI</b> (AppDirect-acquired, thousands of '
 'RingCentral seats potentially migrating, on Telzino at 25&cent;/min and unhappy &mdash; <b>he wants a call next '
 'week</b>) and <b>David from Dynalink</b> (call intelligence) are both in Granola. And <b>Laura sent a new '
 'ask</b>: reach out to the Hubler channel partner with an Iris feature refresh and a current-state evaluation '
 'for their two active agents. <b>Today is UGM day three, the second 13-hour day</b> &mdash; booth 7:30&ndash;4, '
 'then the Bullock Museum reception 6&ndash;9. The 4&ndash;6 pocket now has a queue: the Hubler reply, <b>the '
 'Cathy call</b> (fourteen days past), <b>the Tim record on day nine</b>. Emilio closed the loop Tuesday '
 '(&ldquo;Sounds good, thanks!&rdquo;), and the Iris <b>$5,000 invoice is due tomorrow</b>. The line opened with '
 'a failure pair at 7:18. No reactions saved.</p>'
) + s[m1:]

# ledger: Wednesday opener ('window open' 1 -> 2)
rep('Tuesday closes 5&ndash;0&ndash;3.',
    'Tuesday closes 5&ndash;0&ndash;3. Wednesday opened with a failure pair at 7:18 and 7:19 AM &mdash; '
    '2&ndash;0&ndash;0 by 7:40, window open.', 1)

# ---------- today schedule ----------
rep('13h booked &mdash; UGM day two: booth till 4, Banger&rsquo;s at 6',
    '13h booked &mdash; UGM day three: booth till 4, Bullock reception at 6', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot past"><div class="t">7:00&ndash;7:30</div><div class="w">UGM Breakfast<small>day three opens</small></div></div>\n'
 '        <div class="slot"><div class="t">7:30&ndash;4:00</div><div class="w">UGM Booth Time<small>Moontower &mdash; sponsor early lunch access runs again today at 11:45</small></div></div>\n'
 '        <div class="slot"><div class="t">12:00&ndash;1:00</div><div class="w">UGM Lunch<small>inside the booth block</small></div></div>\n'
 '        <div class="slot free"><div class="t">4:00&ndash;6:00</div><div class="w">Open pocket<small>queue: the Hubler reply to Laura, the Cathy call (fourteen days), the Tim record (day nine)</small></div></div>\n'
 '        <div class="slot"><div class="t">6:00&ndash;9:00</div><div class="w">UGM: Bullock Museum Reception<small>evening event &mdash; day three closes</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- top 5 ----------
rep('ProGraphix &mdash; fourteen days past &mdash; Monday passed with the thread still silent',
    'ProGraphix &mdash; fourteen days past &mdash; two UGM days have gone by with the thread silent', 1)
rep('It is now a from-the-floor call: the 4&ndash;6 gap before Banger&rsquo;s is today&rsquo;s opening.',
    'It is a from-the-floor call now: the 4&ndash;6 gap before the Bullock reception is today&rsquo;s opening, and after Thursday the week is gone.', 1)
rep('UGM is here: the 4&ndash;6 gap before Banger&rsquo;s is the realistic slot.',
    'UGM is here: the 4&ndash;6 gap today or Thursday&rsquo;s Reserved blocks are the realistic slots.', 1)

# #3: replace the shipped-Iris-deliverables item with Laura's Hubler ask
h0 = s.find('<h4>Shipped on deadline: the Iris scenarios and one-pagers went out Friday afternoon</h4>')
h1 = s.find('</div></li>', h0) + len('</div></li>')
assert 0 < h0 < h1
s = s[:s.rfind('<li><div>', 0, h0)] + (
 '<li><div>\n'
 '          <h4>Laura&rsquo;s new ask: reach out to the Hubler channel partner &mdash; an Iris refresh for their two active agents</h4>\n'
 '          <p class="why">Laura emailed Tuesday at 11:54 AM (&ldquo;Follow up meeting&rdquo;): reach out to the '
 'channel partner with Hubler and give them <b>a refresh of the features and an evaluation of the current state '
 'of Iris for the two active Hubler agents</b> &mdash; she flagged a call error in the same note. This is the '
 'Iris customer asking directly, in week three of the engagement; a reply with a proposed time beats a perfect '
 'plan. The 4&ndash;6 pocket today or Thursday&rsquo;s Reserved blocks fit. The scenarios and one-pagers shipped '
 'on deadline a week ago; the <b>$5,000 invoice is due tomorrow, Oct 29</b>.</p>\n'
 '          <div class="meta"><span class="pill crit">New ask &middot; Tue 11:54 AM</span><span class="pill quiet">Iris &middot; SpectrumVoIP</span></div>\n'
 '        </div></li>'
) + s[h1:]

# #4: replace the resolved Emilio item with the UGM leads
e0 = s.find('<h4>Emilio / Smart City &mdash; he checked in Monday and you answered; the ball is with Spectrum&rsquo;s counsel</h4>')
e1 = s.find('</div></li>', e0) + len('</div></li>')
assert 0 < e0 < e1
s = s[:s.rfind('<li><div>', 0, e0)] + (
 '<li><div>\n'
 '          <h4>Two live leads walked up to the booth &mdash; CCI (AppDirect) and Dynalink</h4>\n'
 '          <p class="why"><b>Michael from CCI</b>, a NOC engineer with platform-decision pull: CCI was acquired '
 'by AppDirect and thousands of RingCentral users could migrate onto them; they run Telzino&rsquo;s teammate '
 'product at 25&cent;/min (billing $1/min) and find it expensive and hard to use &mdash; <b>he asked for a call '
 'next week</b>. <b>David from Dynalink</b> leaned toward call intelligence (david@dynalink.com). Both are '
 'captured in Granola; the follow-up emails are post-UGM sends &mdash; Friday or Monday. Emilio closed his loop '
 'Tuesday (&ldquo;Sounds good, thanks!&rdquo;); the Smart City chase is now Spectrum&rsquo;s counsel.</p>\n'
 '          <div class="meta"><span class="pill good">CCI: call next week</span><span class="pill quiet">Dynalink: call intelligence</span></div>\n'
 '        </div></li>'
) + s[e1:]

# ---------- flags ----------
f0 = s.find('<span class="pill warn">Today</span> UGM day two is a 13-hour day &mdash; booth till 4, Banger&rsquo;s till 9')
fh = s.rfind('<h3>', 0, f0)
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < fh < f0 < f1
s = s[:fh] + (
 '<h3><span class="pill warn">Today</span> UGM day three &mdash; the second 13-hour day, and the pocket has a queue</h3>\n'
 '          <p>Booth <b>7:30&ndash;4</b> at Moontower (early sponsor lunch access again at 11:45), then <b>the '
 'Bullock Museum reception 6&ndash;9</b>. The one pocket is <b>4&ndash;6</b> and three things want it: <b>the '
 'Hubler reply to Laura</b> (her direct ask, Tuesday), <b>the Cathy call</b> (fourteen days past), and <b>the Tim '
 'record</b> (day nine). The Whova three are floor-time work. Tomorrow the booth ends at 10:30 and the Reserved '
 'blocks return &mdash; with <b>Hand and Stone at 8 PM</b> booked Tuesday night to close the conference.</p>'
) + s[f1:]

rep('The UGM schedule filled in</b>: booth time runs 7:30&ndash;4 today and Wednesday',
    'The UGM schedule filled in</b>: booth time ran 7:30&ndash;4 Tuesday and runs again today', 1)
rep('and Thursday holds booth till 10:30, Scott at 2 and two Reserved blocks;',
    'and Thursday holds booth till 10:30, Scott at 2, two Reserved blocks and <b>Hand and Stone at 8</b>;', 1)

# ---------- markers card ----------
rep('Monday closed 4&ndash;1&ndash;4 &mdash; quiet all day, a dinner-hour burst, done by 8:39.',
    'Monday closed 4&ndash;1&ndash;4 and Tuesday repeated the shape at 5&ndash;0&ndash;3 (a Banger&rsquo;s-hour burst, quiet by 6:44).', 1)

# ---------- coming-up card ----------
rep('Today &mdash; UGM day two: the long booth day', 'Today &mdash; UGM day three: booth, then the Bullock', 1)
c0 = s.find('Booth 7:30&ndash;4, lunch 12&ndash;1 (early sponsor access from 11:45)')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 'Booth 7:30&ndash;4, lunch 12&ndash;1 (sponsor early access 11:45), <b>Bullock Museum reception 6&ndash;9</b> '
 '&mdash; the last full UGM day; tomorrow ends at 10:30 with Scott at 2. Carried into the day: <b>the Hubler '
 'reply to Laura</b>, <b>the Cathy call</b> (fourteen days past), <b>the Tim record</b> (day nine), the review '
 'queue (#886, #991, #992, #799), the <b>Whova trio</b>, and two fresh leads to follow up post-UGM (CCI, '
 'Dynalink). The Iris <b>$5,000 invoice is due tomorrow</b>.</p>'
) + s[c1:]

# Iris card: Hubler ask + invoice due tomorrow
rep('The $5,000 invoice is due Oct 29.',
    'The <b>$5,000 invoice is due tomorrow, Oct 29</b>. Laura&rsquo;s Tuesday ask adds a deliverable: the <b>Hubler channel-partner outreach</b> (feature refresh + current-state evaluation for the two active Hubler agents; she flagged a call error).', 1)

# ---------- inbox panel ----------
rep('The Emilio carry closed Monday: he checked in and <b>the reply went out at 4:08 PM</b> (ball with Spectrum&rsquo;s counsel, update promised after UGM).',
    'Emilio closed the loop Tuesday morning &mdash; &ldquo;Sounds good, thanks!&rdquo; &mdash; so the Smart City chase is Spectrum&rsquo;s counsel now. New in the queue: <b>Laura&rsquo;s Hubler ask</b> (Tue 11:54 AM, needs a reply with a proposed time) and the <b>CCI follow-up</b> (Michael wants a call next week).', 1)
rep('Still needing words: <b>Cathy at ProGraphix</b> (thirteen days) and the <b>Whova queue of three</b> &mdash; the 4&ndash;6 gap before Banger&rsquo;s is today&rsquo;s pocket. ',
    'Still needing words: <b>Cathy at ProGraphix</b> (fourteen days) and the <b>Whova three</b> &mdash; the 4&ndash;6 gap before the Bullock reception is today&rsquo;s pocket. ', 1)

# ---------- week chart: roll to Wed Oct 28 - Tue Nov 3 ----------
rep('Tue Oct 27 &ndash; Mon Nov 2', 'Wed Oct 28 &ndash; Tue Nov 3', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(92.86% + 6px)">13</div>\n'
 '            <div class="seg m" style="height:92.86%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>\n'
 '            <div class="seg m" style="height:46.43%"></div><div class="seg f" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>\n'
 '            <div class="seg m" style="height:14.29%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>\n'
 '            <div class="seg m" style="height:19.64%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Tue</b>27</div><div><b>Wed</b>28</div>\n          <div><b>Thu</b>29</div><div><b>Fri</b>30</div><div><b>Sat</b>31</div><div><b>Sun</b>1</div><div><b>Mon</b>2</div>',
    '<div><b>Wed</b>28</div><div><b>Thu</b>29</div>\n          <div><b>Fri</b>30</div><div><b>Sat</b>31</div><div><b>Sun</b>1</div><div><b>Mon</b>2</div><div><b>Tue</b>3</div>', 1)

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-10-28T07:40:00-05:00') == 2
assert s.count('window open') == 2
assert s.count('UGM day two') == 0
assert s.count('thirteen days past') == 0 and s.count('day eight') == 0
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s

open(p, 'w').write(s)
print('wednesday turn ok', len(s))
