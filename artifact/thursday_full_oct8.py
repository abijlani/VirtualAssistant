import re
p='page-template.html'
s=open(p).read()

def rep(old,new,n=1):
    global s
    c=s.count(old)
    assert c==n, f"rep expected {n} got {c}: {old[:80]}"
    s=s.replace(old,new)

def rx(pat,new,n=1):
    global s
    s,c=re.subn(pat,new,s,flags=re.DOTALL)
    assert c==n, f"rx expected {n} got {c}: {pat[:80]}"

# ---- A. stamps / masthead chrome ----
rep('2026-10-07T22:03:00-05:00','2026-10-08T07:14:00-05:00',2)
rep('<b>Brief compiled</b> Wed 7:14 AM &middot; data checked Wed 10:03 PM CT',
    '<b>Brief compiled</b> Thu 7:14 AM &middot; data checked Thu 7:14 AM CT')
rep('Wednesday, October 7 &middot; 2026','Thursday, October 8 &middot; 2026')
rep('<h1>Good evening, Bodhi.</h1>','<h1>Good morning, Bodhi.</h1>')

# ---- #799 bump BEFORE rewrites (all five are #799) ----
rep('day thirty-one','day thirty-two',5)

# ---- B. masthead sub ----
rx(r'<p class="sub">.*?</p>',
'<p class="sub">Thursday runs <b>9.0h</b> &mdash; the week&rsquo;s new biggest day and the only one over the 8h line: Deep Work (Project Engineering) 8:30&ndash;12:30, the <b>noon block you created at 4:14 AM for Emilio&rsquo;s MSA clause</b>, Lift (Full) at 1, a <b>workshop session with Taylor 2&ndash;3 at Gevity</b>, and <b>Scott Van Camp 4&ndash;5</b>. The two sends aged again &mdash; <b>the Emilio recap is six days old</b> and <b>the Affiliated pricing reply is on day three</b> (no send on record); the 7:30&ndash;8:30 pocket is the catch, and the noon MSA block pairs naturally with the recap. Wednesday&rsquo;s clean day broke at 6:08 PM: <b>seven failures by 8:09</b> &mdash; the evening window&rsquo;s fourth weekday running and its heaviest burst since Friday&rsquo;s nine &mdash; then a first &ldquo;Call handled&rdquo; success note at 8:50 and a quiet overnight; <b>Thursday opened without a failure</b>. <b>Laura Mathwig (SpectrumVoIP) booked a Voxtell Iris engagement for tomorrow 9&ndash;9:30</b> &mdash; the invite is unanswered and your Monday draft to her is still unsent. The accountants answered: <b>$250 for a written response to the IRS</b> &mdash; a yes/no now. #799 at <b>day thirty-two</b>, Eric at <b>day thirty-one</b>, the job descriptions at <b>day twenty-three</b> with the workshop nine days out and Taylor in the building today, billing/RevIO at twenty-six days past, Nick on night twenty-four. No reactions saved.</p>')

# ---- C. needs-decision note ----
rep('The Emilio recap (five days) and the Affiliated pricing reply (deal live, answer agreed) both missed Tuesday&rsquo;s block &mdash; the twenty minutes before 9:30 is the catch; the 11&ndash;3 engineering block opens with the identification query',
    'The Emilio recap (six days) and the Affiliated pricing reply (day three, answer agreed) have aged three days running &mdash; the 7:30&ndash;8:30 pocket is the catch and the noon MSA block is Emilio-adjacent; the 8:30&ndash;12:30 engineering block opens with the identification query')

# ---- D. today note + schedule ----
rep('Sustainable Ambition 9:30, then Deep Work (Project Engineering) 11&ndash;3 &mdash; identification first, then the review stack',
    'Deep Work 8:30&ndash;12:30, the Emilio MSA clause at noon, Taylor at 2, Scott Van Camp at 4')
rx(r'<div class="card sched" id="todaysched">.*?\n      </div>\n    </section>',
'''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">7:00 &ndash; 7:30</div><div class="w">Doggy Care</div></div>
        <div class="slot free"><div class="t">7:30 &ndash; 8:30</div><div class="w">Open &mdash; the send pocket<small>The Affiliated reply (day three) and the Emilio recap (six days)</small></div></div>
        <div class="slot"><div class="t">8:30 &ndash; 12:30</div><div class="w">Deep Work (Project Engineering)<small>Identification query first (Wednesday hit seven), then #799, TCP switch, review stack</small></div></div>
        <div class="slot"><div class="t">12:00 &ndash; 1:00</div><div class="w">Work on Emilio&rsquo;s legal clause for the MSA<small>Your 4:14 AM block &mdash; overlaps the last half-hour of Deep Work</small></div></div>
        <div class="slot"><div class="t">1:00 &ndash; 1:45</div><div class="w">The Lift (Full Body)</div></div>
        <div class="slot"><div class="t">1:45 &ndash; 2:00</div><div class="w">Recover + Shower</div></div>
        <div class="slot"><div class="t">2:00 &ndash; 3:00</div><div class="w">Workshop Session with Taylor<small>Huddle Room 2 at Gevity is booked 2&ndash;4 &mdash; bring the three job descriptions</small></div></div>
        <div class="slot"><div class="t">3:30 &ndash; 4:00</div><div class="w">Reserved</div></div>
        <div class="slot"><div class="t">4:00 &ndash; 5:00</div><div class="w">Call with Scott Van Camp</div></div>
      </div>
    </section>''')

# ---- E. top 5 ----
rx(r'<ol class="prio">.*?</ol>',
'''<ol class="prio">
        <li><div>
          <h4>The Affiliated pricing reply &mdash; day three of a live deal waiting on your answer</h4>
          <p class="why">Michael&rsquo;s volume-discount question has been open since Monday afternoon, the proposal already forwarded to Tom Welsh for their non-vertical AI clients. The answer is agreed: <b>$0.16 floor, $0.15 at 100,000 minutes as a first-for-any-partner exception</b>, led with partnership value (ConnectWise-style integrations at no charge &mdash; Cairo won&rsquo;t) rather than per-minute price. Pyro sheet first, then send. Three days is where a hot internal forward starts to cool.</p>
          <div class="meta"><span class="pill crit">Deal live &middot; day three</span><span class="pill quiet">Reply to Michael (CC Jr) &middot; 7:30&ndash;8:30 pocket</span></div>
        </div></li>
        <li><div>
          <h4>The Emilio recap &mdash; six days old, and you booked an Emilio hour at noon</h4>
          <p class="why">Friday&rsquo;s &ldquo;Smart City Partnership Next Steps&rdquo; call logged no concrete decisions &mdash; the written recap (CC Jr) proposing rollout shape, pricing posture and white-label is still what keeps the deal moving. Your own 4:14 AM move says the deal is on your mind: <b>the noon block for Emilio&rsquo;s MSA clause</b> is the natural place to send the recap too &mdash; one deal, one hour, both pieces.</p>
          <div class="meta"><span class="pill crit">Six days</span><span class="pill quiet">Pocket at 7:30 or the noon block</span></div>
        </div></li>
        <li><div>
          <h4>The identification query opens the 8:30 block &mdash; Wednesday&rsquo;s burst hit seven</h4>
          <p class="why">Wednesday held clean until 6:08 PM, then produced <b>seven failures by 8:09</b> &mdash; the evening window&rsquo;s fourth weekday in a row and its heaviest burst since Friday&rsquo;s nine &mdash; followed by the stream&rsquo;s first &ldquo;Call handled&rdquo; success note at 8:50. <b>#891&rsquo;s ended-reason classification is live</b>; the look is query-sized and answers whose calls these are and why they fail at dinner time.</p>
          <div class="meta"><span class="pill crit">First item, 8:30&ndash;12:30</span><span class="pill quiet">Four evening bursts running</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day thirty-two &mdash; the review stack rides the same block</h4>
          <p class="why">Double-approved and a month old; behind it the TCP switch, the #830/#831/#842/#843/#886 reviews and the #894/#855 pair. #895 merged Tuesday (VOXAI-918 Done) &mdash; the stack moves when it gets a window, and today&rsquo;s 8:30&ndash;12:30 is the longest one this week.</p>
          <div class="meta"><span class="pill warn">Review waiting</span><span class="pill quiet">Today 8:30&ndash;12:30</span></div>
        </div></li>
        <li><div>
          <h4>The three job descriptions &mdash; day twenty-three, and Taylor is in the building at 2</h4>
          <p class="why">Three workshop working sessions this week &mdash; video content, pricing, ad creative with Richard and Tom &mdash; while the landing page stays blocked behind ws-jds. The 2&ndash;3 session with Taylor is the natural handoff: even rough drafts of the VA, EA and Content Manager descriptions turn the meeting into unblocking rather than status.</p>
          <div class="meta"><span class="pill warn">Day twenty-three</span><span class="pill quiet">ws-jds &rarr; ws-landing &middot; Taylor 2&ndash;3</span></div>
        </div></li>
      </ol>''')

# ---- F. week flags ----
rx(r'<h3><span class="pill warn">Today</span> Wednesday is the week&rsquo;s biggest day.*?</p>',
'''<h3><span class="pill warn">Today</span> Thursday is now the week&rsquo;s biggest day &mdash; 9.0h, the only day over the 8h line</h3>
          <p>The schedule reshaped overnight: Deep Work 8:30&ndash;12:30, then the <b>noon Emilio-MSA block you created at 4:14 AM</b> (it overlaps the block&rsquo;s last half-hour &mdash; the backlog gets 8:30&ndash;12, realistically), Lift 1&ndash;1:45, the <b>Taylor workshop session 2&ndash;3</b> (Huddle Room 2 at Gevity, booked to 4), Reserved 3:30&ndash;4, and <b>Scott Van Camp 4&ndash;5</b>. There is no TTT today &mdash; the 7:30&ndash;8:30 pocket is the day&rsquo;s only natural send window.</p>''')
rx(r'<h3><span class="pill warn">This week</span> Thursday 8h, a 4h Friday.*?</p>',
'''<h3><span class="pill warn">This week</span> A 4h Friday with an unanswered 9 AM invite, then the floor &mdash; and next Thursday&rsquo;s collision stands</h3>
          <p><b>Friday 4.0h</b>: Grok Bot 201 at noon and the Quincy dinner 6&ndash;8:30 PM at 91 Red River St &mdash; plus <b>Laura Mathwig&rsquo;s Voxtell Iris engagement 9&ndash;9:30 AM, invite unanswered</b> and not counted; answering it is a ten-second decision that also surfaces your unsent Monday draft to her. The weekend holds the 0.5h floor, <b>Monday restarts at 6.25h</b>, <b>Tuesday Oct 13 runs 7.25h</b> &mdash; Monthly Iris Sync 9:00 and the Izzy check-in 10:00 (the Levitt verdict&rsquo;s next window) inside Deep Work 10&ndash;2 &mdash; and <b>Wednesday Oct 14 runs 7.75h</b>. <b>Saturday Oct 17 carries the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown at Gevity) &mdash; nine days out, prep moving: three working sessions this week and Taylor in the building today. The flag stands: <b>Thursday Oct 15 books Parr PT 8:45&ndash;10 inside Deep Work 8:30&ndash;12:30</b>.</p>''')

# ---- G. coming-up cards ----
rx(r'This morning &mdash; the send pocket, then Sustainable Ambition</h4>\s*<p style="font-size:13px;color:var\(--ink-2\);margin-top:7px">.*?</p>',
'''This morning &mdash; the send pocket before the 8:30 block</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Both sends aged again: <b>the Emilio recap (six days)</b> and <b>the Affiliated pricing reply (day three)</b> &mdash; $0.16 floor, $0.15 at 100K as the first-time exception, partnership value over price, Pyro sheet first. The 7:30&ndash;8:30 pocket is today&rsquo;s best window; the noon MSA block is the natural second stop for the Emilio side.</p>''')
rx(r'Today 11&ndash;3 &mdash; the engineering block the backlog waited for</h4>\s*<p style="font-size:13px;color:var\(--ink-2\);margin-top:7px">.*?</p>',
'''Today 8:30&ndash;12:30 &mdash; the engineering block, then the Emilio hour</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Open with <b>the identification query on #891&rsquo;s ended-reason data</b> &mdash; Wednesday&rsquo;s evening burst hit <b>seven failures by 8:09</b>, the heaviest since Friday&rsquo;s nine, before a first &ldquo;Call handled&rdquo; note at 8:50 and a clean overnight. Then <b>#799</b> (day thirty-two, double-approved), the TCP switch, the #830/#831/#842/#843/#886 reviews and the #894/#855 pair. At noon the calendar turns to <b>Emilio&rsquo;s MSA clause</b> &mdash; your own block; the six-day recap belongs beside it.</p>''')
rx(r'The week&rsquo;s markers</h4>\s*<p style="font-size:13px;color:var\(--ink-2\);margin-top:7px">.*?</p>',
'''The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Tomorrow &mdash; Laura Mathwig&rsquo;s Iris engagement 9&ndash;9:30 AM (invite unanswered)</b>, Grok Bot 201 at noon, Quincy dinner 6&ndash;8:30 PM (91 Red River St). <b>Monday &mdash; Product Sync returns.</b> <b>Tuesday Oct 13 &mdash; Iris Sync 9:00, Izzy check-in 10:00</b> (the Levitt verdict&rsquo;s next window). <b>Thursday Oct 15: Parr PT 8:45&ndash;10 inside Deep Work 8:30&ndash;12:30</b> &mdash; the collision to settle. <b>Saturday Oct 17 &mdash; the workshop</b>, nine days out, Taylor in the building today 2&ndash;3.</p>''')

# ---- H. chart ----
rep('Wed Oct 7 &ndash; Tue Oct 13','Thu Oct 8 &ndash; Wed Oct 14')
rx(r'<div class="cap8" style="bottom:57\.14%"><span>8h sustainable load</span></div>.*?\n        </div>\n        <div class="xaxis"',
'''<div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(64.29% + 6px)">9.0</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:32.14%"></div><div class="seg p" style="height:10.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(28.57% + 6px)">4.0</div>
            <div class="seg m" style="height:25%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(3.57% + 6px)">0.5</div>
            <div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(3.57% + 6px)">0.5</div>
            <div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(44.64% + 6px)">6.25</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(51.79% + 6px)">7.25</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:12.5%"></div></div>
        </div>
        <div class="xaxis"''')
rep('<div><b>Wed</b>7</div><div><b>Thu</b>8</div>\n          <div><b>Fri</b>9</div><div><b>Sat</b>10</div><div><b>Sun</b>11</div><div><b>Mon</b>12</div><div><b>Tue</b>13</div>',
    '<div><b>Thu</b>8</div><div><b>Fri</b>9</div>\n          <div><b>Sat</b>10</div><div><b>Sun</b>11</div><div><b>Mon</b>12</div><div><b>Tue</b>13</div><div><b>Wed</b>14</div>')

# ---- I. already-home rows ----
rep('<td class="tid">This morning</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing) and <b>the Emilio recap</b> (five days old) &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread) and the <b>UGM registration</b><div class="src">Eric&rsquo;s reply (day thirty) and the send backlog (twenty-five days past on billing/RevIO &middot; Nick night twenty-three) fit the pre-9:30 pocket or TTT 3&ndash;4</div></td>',
    '<td class="tid">This morning</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing) and <b>the Emilio recap</b> (six days old) &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread), the <b>UGM registration</b> and <b>the accountants&rsquo; $250 quote</b> (a yes/no on them answering the IRS)<div class="src">Eric&rsquo;s reply (day thirty-one) and the send backlog (twenty-six days past on billing/RevIO &middot; Nick night twenty-four) fit the 7:30&ndash;8:30 pocket &mdash; today has no TTT</div></td>')
rep('day twenty-two; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; date settled: Oct 17, Taylor accepting</div>',
    'day twenty-three; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; Taylor is in the building today 2&ndash;3 &mdash; the natural handoff</div>')
rep('<td class="tid">Today 11&ndash;3</td><td><b>The identification query first</b> (#891&rsquo;s ended-reason data), then the engineering backlog &mdash; #799 (day thirty-two, double-approved), the TCP switch',
    '<td class="tid">Today 8:30&ndash;12:30</td><td><b>The identification query first</b> (#891&rsquo;s ended-reason data &mdash; Wednesday&rsquo;s burst hit seven, the heaviest since Friday&rsquo;s nine), then the engineering backlog &mdash; #799 (day thirty-two, double-approved), the TCP switch')

# ---- J. line-health + needs-reply + fyi ----
rep('and the window closed with nothing after 8:09 &mdash; verified at 10:03, trash included.',
    'and the window closed with nothing after 8:09 &mdash; verified at 10:03, trash included. The overnight into Thursday stayed quiet, and <b>Thursday opened without a failure</b> &mdash; Wednesday&rsquo;s ledger closes at seven failures, all evening, beside Tuesday&rsquo;s eleven-alert record.')
rep('Five days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply beside it &mdash; the twenty minutes before 9:30 is the catch',
    'Six days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply (day three) beside it &mdash; the 7:30&ndash;8:30 pocket is the catch')
rep('Behind those: <b>Eric &mdash; day thirty</b>, Nick&rsquo;s program-details reply on night twenty-three, and',
    'Behind those: <b>Eric &mdash; day thirty-one</b>, Nick&rsquo;s program-details reply on night twenty-four, and')
rep('<ul class="fyi">\n        <li>',
    '<ul class="fyi">\n        <li><b>The accountants quoted $250</b> for a written response to the IRS letter (Nate Richards, Thu 6:40 AM) &mdash; your &ldquo;how much would it cost?&rdquo; answered; a yes/no unblocks it.</li>\n        <li>')
rep('Inbox <span class="cnt">16</span>','Inbox <span class="cnt">17</span>')

# ---- L. remaining daily bumps ----
rep('Day twenty-four on all three','Day twenty-five on all three')
rep('Day twenty-three on Eric','Day twenty-four on Eric')
rep('twenty-nine full days','thirty full days')
rep('sixteen days','seventeen days',3)
rep('day twenty-eight','day twenty-nine',2)
rep('twenty-four days in','twenty-five days in',2)
rep('ten days left','nine days left')
rep('thirty-seven days','thirty-eight days',2)
rep('41 days','42 days')
rep('61 days','62 days')
c=s.count('twenty-five days past'); print('twenty-five days past remaining:',c)
s=s.replace('twenty-five days past','twenty-six days past')
c=s.count('day twenty-two'); print('day twenty-two remaining:',c)
s=s.replace('day twenty-two','day twenty-three')
c=s.count('ten days out'); print('ten days out remaining:',c)
s=s.replace('ten days out','nine days out')

# chips +1
def chip(m): return m.group(1)+str(int(m.group(2))+1)+m.group(3)
s,n=re.subn(r'(class="chip old">)(\d+)(d)', chip, s)
print('chips bumped:',n); assert n==5

# ---- N. sanity ----
assert s.count('__CC_STATE__')==1 and s.count('__CC_TEMPLATE__')==1
assert s.count('data-react-task="')==59, s.count('data-react-task="')
assert s.count('class="bar"')==7
assert s.count('2026-10-08T07:14:00-05:00')==2
assert s.count('class="slot past"')==0
assert s.count('night twenty-three')==0
assert s.count('day thirty-one')>=3   # Eric x3 (masthead, row1, needs-reply)
assert s.count('Wed Oct 7')==0
for leftover in ['five days old','day two of a live deal','11&ndash;3 &mdash;','Sustainable Ambition 9:30']:
    print('leftover',repr(leftover),s.count(leftover))
print('before 9:30 remaining:', s.count('before 9:30'))
open(p,'w').write(s)
print('THURSDAY FULL OK', len(s))
