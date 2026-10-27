# Tuesday Oct 28 — no, Oct 27, 2026 — FULL morning pass (UGM day 2, Austin).
# Monday closed 4F/1NA/4S. Tuesday opened 1F/0NA/2S by 7:50 (S 5:18, S 6:23, F 7:18).
# EMILIO RESOLVED: he checked in Mon 2:42 PM, Bodhi replied 4:08 PM (ball with Spectrum
# counsel, pinged again, update post-UGM) — the 24-day recap carry comes off the board.
# Today: booth 7:30-4 (sponsor early lunch 11:45 per rtanyag email), lunch 12-1 nested,
# Banger's 6-9 => 13h. Drafts still unsent => Tim day eight. ProGraphix: Monday passed
# silent => thirteen days. LiveKit TTS/STT quota raises approved 7:38 AM. Whova queue
# now three (Vipin; Nunnally Torres + Hydnrazl Gutierrez of .ppl Solutions; Matthew
# Abraham). No new Granola captures. cc-state empty (no republish-wake).
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
rep('day fifty', 'day fifty-one', 3)              # #799
rep('day forty-nine', 'day fifty', 3)             # Eric / Izzy trio
rep('day forty-one;', 'day forty-two;', 1)        # JDs
rep('forty-four days past', 'forty-five days past', 2)
rep('night forty-two', 'night forty-three', 2)
rep('thirty-four days past', 'thirty-five days past', 1)   # Appulse
rep('twelve days past', 'thirteen days past', 7)  # ProGraphix
rep('Twelve days past', 'Thirteen days past', 1)
rep('day seven', 'day eight', 5)                  # Tim ('day sevent*' == 0 checked)
rep('Six days past the promise', 'Seven days past the promise', 1)
rep('Iris, day fifteen', 'Iris, day sixteen', 1)
rep('hr-nda is 70 days old', 'hr-nda is 71 days old', 1)
rep('Ages as of Oct 26', 'Ages as of Oct 27', 1)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- date turn ----------
rep('2026-10-26T22:08:00-05:00', '2026-10-27T07:50:00-05:00', 2)
rep('Monday, October 26 &middot; 2026', 'Tuesday, October 27 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)
rep('<b>Brief compiled</b> Mon 7:25 AM &middot; data checked Mon 10:08 PM CT',
    '<b>Brief compiled</b> Tue 7:50 AM &middot; data checked Tue 7:50 AM CT', 1)

# masthead (full replace)
m0 = s.find('Sunday did the opposite of Saturday:')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Monday closed gently for a UGM day: <b>4&ndash;1&ndash;4</b> &mdash; quiet from 7:13 AM to the dinner hour, '
 'a short burst, done by 8:39. And the day did one piece of real work: <b>Emilio checked in and you answered at '
 '4:08 PM</b> &mdash; ball with Spectrum&rsquo;s counsel, update promised after UGM; the twenty-four-day recap '
 'carry is off the board. <b>Today is UGM day two, the heaviest on paper: 13 booked hours</b> &mdash; booth '
 '7:30&ndash;4 (sponsors skip the lunch line from 11:45), then Banger&rsquo;s 6&ndash;9. The pocket is '
 '<b>4&ndash;6</b>, and it has two claimants: <b>the Cathy call</b> (thirteen days past &mdash; Monday passed '
 'silent) and <b>the Tim record on day eight</b> (both drafts untouched). The Whova queue is three deep, and '
 'LiveKit approved the TTS/STT quota raises this morning. The line opened 1&ndash;0&ndash;2 by 7:50. '
 'No reactions saved.</p>'
) + s[m1:]

# ledger: Tuesday opener ('window open' 1 -> 2)
rep('Monday closes 4&ndash;1&ndash;4, the lightest UGM-eve Monday of the streak.',
    'Monday closes 4&ndash;1&ndash;4, the lightest UGM-eve Monday of the streak. Tuesday opened early: '
    '&ldquo;Call handled&rdquo; at 5:18 and 6:23 AM, a failure at 7:18 &mdash; 1&ndash;0&ndash;2 by 7:50, window open.', 1)

# ---------- today schedule (full splice) ----------
rep('9.75h booked &mdash; UGM day one: setup, kick-off, reception',
    '13h booked &mdash; UGM day two: booth till 4, Banger&rsquo;s at 6', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot past"><div class="t">7:00&ndash;7:30</div><div class="w">UGM Breakfast<small>day two opens</small></div></div>\n'
 '        <div class="slot"><div class="t">7:30&ndash;4:00</div><div class="w">UGM Booth Time<small>Moontower &mdash; sponsors get early lunch access from 11:45</small></div></div>\n'
 '        <div class="slot"><div class="t">12:00&ndash;1:00</div><div class="w">UGM Lunch<small>inside the booth block &mdash; the 11:45 side door skips the line</small></div></div>\n'
 '        <div class="slot free"><div class="t">4:00&ndash;6:00</div><div class="w">Open pocket<small>the Cathy call (thirteen days) and the Tim record (day eight) both fit here</small></div></div>\n'
 '        <div class="slot"><div class="t">6:00&ndash;9:00</div><div class="w">UGM: Banger&rsquo;s Sausage House &amp; Beer Garden<small>evening event &mdash; day two closes</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- top 5 ----------
rep('ProGraphix &mdash; thirteen days past &mdash; today is the damage-control call to Cathy',
    'ProGraphix &mdash; thirteen days past &mdash; Monday passed with the thread still silent', 1)
rep('today is damage control: call Cathy and ask what&rsquo;s recoverable &mdash; the 11:30 pocket is the window before the booth takes the day.',
    'the damage-control call to Cathy still hasn&rsquo;t visibly happened &mdash; Monday&rsquo;s window came and went. It is now a from-the-floor call: the 4&ndash;6 gap before Banger&rsquo;s is today&rsquo;s opening.', 1)
rep('UGM is here: the 5:00 pocket is the realistic slot.',
    'UGM is here: the 4&ndash;6 gap before Banger&rsquo;s is the realistic slot.', 1)
rep('(Invoice #1186) and UGM opens today &mdash; pickup is now or never.',
    '(Invoice #1186); UGM is underway &mdash; if they didn&rsquo;t make it to the booth Monday, they wait for the weekend.', 1)
rep('<span class="pill warn">Tees: pickup before the floor</span>',
    '<span class="pill warn">Tees: with the booth or not at all</span>', 1)
rep('Emilio / Smart City &mdash; recap twenty-four days; the deal moved to a binding-agreement redline',
    'Emilio / Smart City &mdash; he checked in Monday and you answered; the ball is with Spectrum&rsquo;s counsel', 1)
rep('You told Jake and Matt that Smart City loves the letter but will only move on something binding &mdash; Matt added Christine. Chase the redline so the momentum holds, and the written recap to Emilio (CC Jr) is still the carried send keeping his side warm.',
    'Emilio checked in Monday afternoon (&ldquo;just checking in on the process&rdquo;) and <b>you replied at 4:08 PM</b>: still waiting on Spectrum&rsquo;s counsel, pinged them again, update after UGM. The twenty-four-day recap carry is off the board &mdash; what remains is <b>chasing the counsel redline</b> (Jake + Matt, Christine added) so the promised post-UGM update has substance.', 1)
rep('<span class="pill crit">Twenty-four days</span>', '<span class="pill good">Replied Mon 4:08 PM</span>', 1)
rep('This morning <b>Pagebakers requested your review on #886</b>', 'Monday morning <b>Pagebakers requested your review on #886</b>', 1)

# ---------- flags ----------
f0 = s.find('<span class="pill warn">Today</span> UGM day one is the heaviest day in weeks &mdash; 9.75h booked')
fh = s.rfind('<h3>', 0, f0)
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < fh < f0 < f1
s = s[:fh] + (
 '<h3><span class="pill warn">Today</span> UGM day two is a 13-hour day &mdash; booth till 4, Banger&rsquo;s till 9</h3>\n'
 '          <p>Booth time runs <b>7:30&ndash;4</b> at Moontower (sponsors skip the lunch line from 11:45 &mdash; '
 'Crexendo&rsquo;s note), then <b>Banger&rsquo;s 6&ndash;9</b>. The one pocket is <b>4&ndash;6</b>, and both '
 'carried sends want it: <b>Cathy at ProGraphix</b> (thirteen days past) and <b>the Tim record</b> (day eight). '
 'The Whova queue is three deep &mdash; floor time can clear it between conversations.</p>'
) + s[f1:]

rep('The UGM schedule filled in</b>: booth time runs 7:30&ndash;4 Tuesday and Wednesday',
    'The UGM schedule filled in</b>: booth time runs 7:30&ndash;4 today and Wednesday', 1)
rep('and now <b>two people waiting in Whova</b> &mdash; Vipin Gupta (Tragofone) and, since last night, Nunnally Torres.',
    'and now <b>three waiting in Whova</b> &mdash; Vipin Gupta (Tragofone), Nunnally Torres with Hydnrazl Gutierrez (.ppl Solutions), and Matthew Abraham since Monday evening. One LiveKit wire cleared: <b>the TTS/STT gateway quota raises were approved Tuesday morning</b>.', 1)

# ---------- markers card ----------
rep('Saturday remains the only failure-free day.',
    'Saturday remains the only failure-free day, and Monday closed 4&ndash;1&ndash;4 &mdash; quiet all day, a dinner-hour burst, done by 8:39.', 1)
rep('<b>UGM runs today through Thursday</b> (Austin): Tuesday and Wednesday are 13-hour booth days',
    '<b>UGM runs through Thursday</b> (Austin): today and Wednesday are 13-hour booth days', 1)

# ---------- coming-up card ----------
rep('Today &mdash; UGM opens in Austin', 'Today &mdash; UGM day two: the long booth day', 1)
h0 = s.find('Product Sync at 8:00 with Jr and Eelco, then <b>Booth Setup 12&ndash;4')
h1 = s.find('</p>', h0) + len('</p>')
assert 0 < h0 < h1
s = s[:h0] + (
 'Booth 7:30&ndash;4, lunch 12&ndash;1 (early sponsor access from 11:45), <b>Banger&rsquo;s Sausage House '
 '6&ndash;9</b> &mdash; UGM runs through Thursday. Carried into the floor day: <b>the Cathy call</b> (thirteen '
 'days past), <b>the Tim record</b> (day eight), the review queue (#886, #991, #992, #799), and the '
 '<b>Whova trio</b>. The Emilio carry closed Monday &mdash; replied at 4:08 PM, ball with Spectrum&rsquo;s '
 'counsel.</p>'
) + s[h1:]

# ---------- inbox panel ----------
n0 = s.find('Eighteen days carried: <b>the Emilio recap (CC Jr)</b>')
n1 = s.find('Apollo logged no concrete decisions, so the email defines them.', n0)
assert 0 < n0 < n1
s = s[:n0] + (
 'The Emilio carry closed Monday: he checked in and <b>the reply went out at 4:08 PM</b> (ball with '
 'Spectrum&rsquo;s counsel, update promised after UGM). Still needing words: <b>Cathy at ProGraphix</b> '
 '(thirteen days) and the <b>Whova queue of three</b> &mdash; the 4&ndash;6 gap before Banger&rsquo;s is '
 'today&rsquo;s pocket. '
) + s[n1:]

rep('<span class="pill warn">Ran &mdash; recap owed</span>', '<span class="pill good">Replied Mon 4:08 PM</span>', 1)

# table Today row
rep('<b>The Emilio recap</b> (twenty-four days; the binding-agreement redline is with Jake and Matt), <b>the ProGraphix decision</b> (thirteen days past due) &mdash; the two carried sends;',
    '<b>The ProGraphix decision</b> (thirteen days past due) is the carried send; <b>the Emilio carry closed Monday</b> (replied 4:08 PM &mdash; redline with Jake + Matt, ball with Spectrum&rsquo;s counsel);', 1)

# ---------- week chart: roll to Tue Oct 27 - Mon Nov 2 ----------
rep('Mon Oct 26 &ndash; Sun Nov 1', 'Tue Oct 27 &ndash; Mon Nov 2', 1)
c0 = s.find('<div class="bar"><div class="tot" style="bottom:calc(69.64% + 6px)">9.75</div>')
c1 = s.find('<div class="xaxis"')
c1 = s.rfind('</div>', c0, c1)  # closing of plot div sits right before xaxis
assert 0 < c0 < c1
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(92.86% + 6px)">13</div>\n'
 '            <div class="seg m" style="height:92.86%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(92.86% + 6px)">13</div>\n'
 '            <div class="seg m" style="height:92.86%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>\n'
 '            <div class="seg m" style="height:39.29%"></div><div class="seg f" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>\n'
 '            <div class="seg m" style="height:14.29%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Mon</b>26</div><div><b>Tue</b>27</div>\n          <div><b>Wed</b>28</div><div><b>Thu</b>29</div><div><b>Fri</b>30</div><div><b>Sat</b>31</div><div><b>Sun</b>1</div>',
    '<div><b>Tue</b>27</div><div><b>Wed</b>28</div>\n          <div><b>Thu</b>29</div><div><b>Fri</b>30</div><div><b>Sat</b>31</div><div><b>Sun</b>1</div><div><b>Mon</b>2</div>', 1)

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-10-27T07:50:00-05:00') == 2
assert s.count('window open') == 2
assert s.count('UGM day one') == 0
assert s.count('twenty-four days') == 0  # all rewritten; new text uses "twenty-four-day"
assert s.count('Eighteen days carried') == 0
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s

open(p, 'w').write(s)
print('tuesday turn ok', len(s))
