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

# ---- A. stamps / chrome ----
rep('2026-10-08T22:03:00-05:00','2026-10-09T07:14:00-05:00',2)
rep('<b>Brief compiled</b> Thu 7:14 AM &middot; data checked Thu 10:03 PM CT',
    '<b>Brief compiled</b> Fri 7:14 AM &middot; data checked Fri 7:14 AM CT')
rep('Thursday, October 8 &middot; 2026','Friday, October 9 &middot; 2026')
rep('<h1>Good evening, Bodhi.</h1>','<h1>Good morning, Bodhi.</h1>')

# ---- aging bumps that must precede rewrites (highest first, whole chains) ----
c=s.count('day thirty-two'); print('d32:',c); s=s.replace('day thirty-two','day thirty-three')   # 799
c=s.count('day thirty-one'); print('d31:',c); s=s.replace('day thirty-one','day thirty-two')     # Eric

# ---- B. masthead sub ----
rx(r'<p class="sub">.*?</p>',
'<p class="sub">Friday runs <b>10.5h</b> &mdash; the week&rsquo;s new peak, and you built it yourself overnight: Gym 7&ndash;8, the <b>Voxtell Iris engagement 9&ndash;9:30 with Laura Mathwig and Jason Dow</b>, <b>Work on UGM 9:30&ndash;11:30</b> with the <b>v2 + UGM email blast</b> booked inside it, <b>Emilio&rsquo;s clause 11:30&ndash;12</b>, Grok Bot 201 at noon, <b>Push Level mobile to the App Store 1&ndash;2</b>, and the Quincy dinner 6&ndash;8:30. You also drafted a new email to <b>Jake Leidy and Laura (CC Jr) at 9:58 last night</b> &mdash; ready to send before the 9:00 call, where your Monday draft to Laura still sits too. Thursday&rsquo;s line ledger closed light: <b>two failures (7:25, 8:08 PM) against a day of &ldquo;Call handled&rdquo; successes</b> &mdash; the evening window&rsquo;s fifth weekday but its smallest, and Friday opened clean. <b>The IRS matter is done</b>: Nate confirmed he&rsquo;ll send the response right after 10/15. Still owed: <b>the Emilio recap, seven days</b> (your 11:30 clause block is the natural pairing) and <b>the Affiliated pricing reply, day four</b> &mdash; the open 2&ndash;6 stretch is today&rsquo;s catch. #799 at <b>day thirty-three</b>, Eric at <b>day thirty-two</b>, the job descriptions at <b>day twenty-four</b> with the workshop eight days out, billing/RevIO at twenty-seven days past, Nick on night twenty-five. No reactions saved.</p>')

# ---- C. needs-decision note ----
rep('The Emilio recap (six days) and the Affiliated pricing reply (day three, answer agreed) have aged three days running &mdash; the 7:30&ndash;8:30 pocket is the catch and the noon MSA block is Emilio-adjacent; the 8:30&ndash;12:30 engineering block opens with the identification query',
    'The Emilio recap (seven days) and the Affiliated pricing reply (day four, answer agreed) are the carried sends &mdash; the open 2&ndash;6 stretch is today&rsquo;s catch, and your 11:30 Emilio-clause block pairs with the recap; the 9:58 PM draft to Jake and Laura is ready for the 9:00 call')

# ---- D. today note + schedule ----
rep('Deep Work 8:30&ndash;12:30, the Emilio MSA clause at noon, Taylor at 2, Scott Van Camp at 4',
    'Iris engagement at 9, Work on UGM 9:30&ndash;11:30, Emilio&rsquo;s clause 11:30, Grok Bot at noon, Level mobile 1&ndash;2, Quincy dinner at 6')
rx(r'<div class="card sched" id="todaysched">.*?\n      </div>\n    </section>',
'''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">7:00 &ndash; 8:00</div><div class="w">Gym<small>Doggy Care runs 7&ndash;7:30 alongside</small></div></div>
        <div class="slot"><div class="t">8:00 &ndash; 8:30</div><div class="w">Shower</div></div>
        <div class="slot"><div class="t">9:00 &ndash; 9:30</div><div class="w">Voxtell Iris engagement<small>Laura Mathwig + Jason Dow &middot; your 9:58 PM draft to Jake and Laura is ready to send first</small></div></div>
        <div class="slot"><div class="t">9:30 &ndash; 11:30</div><div class="w">Work on UGM<small>The v2 + UGM email blast is booked inside, 10:30&ndash;11:30</small></div></div>
        <div class="slot"><div class="t">11:30 &ndash; 12:00</div><div class="w">Work on Emilio&rsquo;s clause<small>The seven-day recap belongs beside it</small></div></div>
        <div class="slot"><div class="t">12:00 &ndash; 1:00</div><div class="w">Grok Bot 201</div></div>
        <div class="slot"><div class="t">1:00 &ndash; 2:00</div><div class="w">Push Level mobile to the App Store</div></div>
        <div class="slot free"><div class="t">2:00 &ndash; 6:00</div><div class="w">Open &mdash; the afternoon stretch<small>The Affiliated reply (day four) and anything the morning left behind</small></div></div>
        <div class="slot"><div class="t">6:00 &ndash; 8:30</div><div class="w">Dinner With The Crew (Quincy)<small>91 Red River St</small></div></div>
      </div>
    </section>''')

# ---- E. top 5 ----
rx(r'<ol class="prio">.*?</ol>',
'''<ol class="prio">
        <li><div>
          <h4>The 9:00 Iris engagement &mdash; and the draft you wrote for it last night</h4>
          <p class="why">Laura Mathwig and Jason Dow at 9:00&ndash;9:30 on Teams. You drafted an email to <b>Jake Leidy and Laura (CC Jr) at 9:58 PM</b> &mdash; sending it before the call puts it on the table rather than after; your Monday draft to Laura alone is still sitting in the same folder. The engagement-audit proposal went to Jake last Friday &mdash; this call is its follow-through.</p>
          <div class="meta"><span class="pill crit">9:00 AM &middot; SpectrumVoIP</span><span class="pill quiet">Draft ready &middot; send before the call</span></div>
        </div></li>
        <li><div>
          <h4>The Affiliated pricing reply &mdash; day four of a live deal waiting on your answer</h4>
          <p class="why">Michael&rsquo;s volume-discount question has been open since Monday, the proposal already in front of Tom Welsh. The answer is agreed: <b>$0.16 floor, $0.15 at 100,000 minutes as a first-for-any-partner exception</b>, partnership value (ConnectWise-style integrations at no charge) over per-minute price. Pyro sheet, then send &mdash; the 2&ndash;6 stretch is the day&rsquo;s only real pocket.</p>
          <div class="meta"><span class="pill crit">Deal live &middot; day four</span><span class="pill quiet">Reply to Michael (CC Jr) &middot; 2&ndash;6</span></div>
        </div></li>
        <li><div>
          <h4>The Emilio recap &mdash; seven days old; your 11:30 clause block is the pairing</h4>
          <p class="why">A week since Friday&rsquo;s &ldquo;Smart City Partnership Next Steps&rdquo; call and the written recap (CC Jr) is still what keeps the deal moving. You&rsquo;ve now booked Emilio-clause work two days running &mdash; the deal is clearly live on your side; the recap is the half that Emilio can see. One block, both pieces.</p>
          <div class="meta"><span class="pill crit">Seven days</span><span class="pill quiet">11:30&ndash;12 block &middot; or the 2&ndash;6 stretch</span></div>
        </div></li>
        <li><div>
          <h4>The v2 + UGM email blast and the UGM block &mdash; your own 9:30&ndash;11:30 commitment</h4>
          <p class="why">The UGM registration (Silver, $250 off the final invoice) and the v2 announcement blast now have a two-hour home you built for them. Jr chased Jason Byrne for the attendee list yesterday morning &mdash; the blast and the registration landing together makes the booth real. UGM is Oct 26&ndash;28 in Austin.</p>
          <div class="meta"><span class="pill warn">Today 9:30&ndash;11:30</span><span class="pill quiet">Blast booked 10:30&ndash;11:30</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day thirty-three &mdash; no engineering block until Monday</h4>
          <p class="why">Double-approved and a month old, with the TCP switch, the #830/#831/#842/#843/#886 reviews and the #894/#855 pair behind it. Thursday&rsquo;s identification query opportunity has passed; <b>Monday&rsquo;s Deep Work (Engineering) 10&ndash;2 is the next real window</b>. Thursday&rsquo;s evening tally &mdash; two failures against a day of successes &mdash; is the first sign the stream may be easing.</p>
          <div class="meta"><span class="pill warn">Review waiting</span><span class="pill quiet">Monday 10&ndash;2</span></div>
        </div></li>
      </ol>''')

# ---- F. week flags ----
rx(r'<h3><span class="pill warn">Today</span> Thursday is now the week&rsquo;s biggest day.*?</p>',
'''<h3><span class="pill warn">Today</span> Friday is the week&rsquo;s new peak &mdash; 10.5h, built by your own hand overnight</h3>
          <p>Gym 7&ndash;8 with Doggy Care alongside, Shower, the <b>Iris engagement 9&ndash;9:30</b> (Laura Mathwig + Jason Dow), <b>Work on UGM 9:30&ndash;11:30</b> with the email blast inside it, <b>Emilio&rsquo;s clause 11:30&ndash;12</b>, Grok Bot 201 at noon, <b>Level mobile to the App Store 1&ndash;2</b>, and the Quincy dinner 6&ndash;8:30 at 91 Red River St. The 2&ndash;6 afternoon stretch is the only open ground &mdash; the Affiliated reply (day four) belongs there. Second day running over the 8h line.</p>''')
rx(r'<h3><span class="pill warn">This week</span> A 4h Friday with an unanswered 9 AM invite.*?</p>',
'''<h3><span class="pill warn">This week</span> The floor, then a climbing back half &mdash; and next Thursday is both over the line and colliding</h3>
          <p>The weekend holds the 0.5h floor, <b>Monday restarts at 6.25h</b> (Product Sync 8:00, Deep Work Engineering 10&ndash;2 &mdash; the #799 window), <b>Tuesday Oct 13 runs 7.25h</b> &mdash; Monthly Iris Sync 9:00 and the Izzy check-in 10:00 (the Levitt verdict&rsquo;s next window) inside Deep Work 10&ndash;2 &mdash; and <b>Wednesday Oct 14 runs 7.75h</b>. <b>Thursday Oct 15 now charts at 9.25h</b> with the standing collision: <b>Parr PT 8:45&ndash;10 sits inside Deep Work 8:30&ndash;12:30</b>, plus Scott Van Camp at 2. <b>Saturday Oct 17 carries the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown at Gevity) &mdash; eight days out, prep moving: four working sessions this week including Thursday&rsquo;s reseller-value session.</p>''')

# ---- G. coming-up cards ----
rx(r'This morning &mdash; the send pocket before the 8:30 block</h4>\s*<p style="font-size:13px;color:var\(--ink-2\);margin-top:7px">.*?</p>',
'''This morning &mdash; the Iris engagement at 9, draft in hand</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Laura Mathwig and Jason Dow, 9:00&ndash;9:30 on Teams. <b>Your 9:58 PM draft to Jake Leidy and Laura (CC Jr) is ready</b> &mdash; sending it before the call makes it the agenda; the Monday draft to Laura alone still sits beside it. The engagement-audit proposal went to Jake last Friday, so this is the follow-through call.</p>''')
rx(r'Today 8:30&ndash;12:30 &mdash; the engineering block, then the Emilio hour</h4>\s*<p style="font-size:13px;color:var\(--ink-2\);margin-top:7px">.*?</p>',
'''Today 9:30&ndash;2 &mdash; the blocks you built, then the open stretch</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Work on UGM 9:30&ndash;11:30</b> (the Silver registration and the v2 + UGM email blast, booked 10:30&ndash;11:30), <b>Emilio&rsquo;s clause 11:30&ndash;12</b> &mdash; send the seven-day recap from the same seat &mdash; Grok Bot 201 at noon, and <b>Level mobile to the App Store 1&ndash;2</b>. Then the day opens: <b>2&ndash;6 is the pocket</b> for the Affiliated reply ($0.16 floor, $0.15 at 100K as the first-time exception, Pyro sheet first) before the Quincy dinner at 6.</p>''')
rx(r'The week&rsquo;s markers</h4>\s*<p style="font-size:13px;color:var\(--ink-2\);margin-top:7px">.*?</p>',
'''The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Monday &mdash; Product Sync returns, Deep Work Engineering 10&ndash;2</b> (the #799 window). <b>Tuesday Oct 13 &mdash; Iris Sync 9:00, Izzy check-in 10:00</b> (the Levitt verdict&rsquo;s next window). <b>Wednesday 7.75h.</b> <b>Thursday Oct 15 &mdash; 9.25h with Parr PT 8:45&ndash;10 inside Deep Work 8:30&ndash;12:30</b>, the collision to settle, and Scott Van Camp at 2. <b>Saturday Oct 17 &mdash; the workshop</b>, eight days out, prep moving on four working sessions this week.</p>''')

# ---- H. chart ----
rep('Thu Oct 8 &ndash; Wed Oct 14','Fri Oct 9 &ndash; Thu Oct 15')
rx(r'<div class="cap8" style="bottom:57\.14%"><span>8h sustainable load</span></div>.*?\n        </div>\n        <div class="xaxis"',
'''<div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(75% + 6px)">10.5</div>
            <div class="seg m" style="height:60.71%"></div><div class="seg p" style="height:14.29%"></div></div>
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
          <div class="bar"><div class="tot" style="bottom:calc(66.07% + 6px)">9.25</div>
            <div class="seg m" style="height:16.07%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:14.29%"></div></div>
        </div>
        <div class="xaxis"''')
rep('<div><b>Thu</b>8</div><div><b>Fri</b>9</div>\n          <div><b>Sat</b>10</div><div><b>Sun</b>11</div><div><b>Mon</b>12</div><div><b>Tue</b>13</div><div><b>Wed</b>14</div>',
    '<div><b>Fri</b>9</div><div><b>Sat</b>10</div>\n          <div><b>Sun</b>11</div><div><b>Mon</b>12</div><div><b>Tue</b>13</div><div><b>Wed</b>14</div><div><b>Thu</b>15</div>')

# ---- I. already-home rows ----
rep('<td class="tid">This morning</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing) and <b>the Emilio recap</b> (six days old) &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread) and the <b>UGM registration</b>',
    '<td class="tid">Today 2&ndash;6</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing) and <b>the Emilio recap</b> (seven days old) &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread); the <b>UGM registration</b> finally has its own block, today 9:30&ndash;11:30')
rep('fit the 7:30&ndash;8:30 pocket &mdash; today has no TTT',
    'fit the open 2&ndash;6 stretch')
rep('day twenty-three; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; Taylor is in the building today 2&ndash;3 &mdash; the natural handoff</div>',
    'day twenty-four; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; the Taylor session came and went Thursday &mdash; workshop eight days out</div>')
rep('<td class="tid">Today 8:30&ndash;12:30</td><td><b>The identification query first</b> (#891&rsquo;s ended-reason data &mdash; Wednesday&rsquo;s burst hit seven, the heaviest since Friday&rsquo;s nine), then the engineering backlog',
    '<td class="tid">Monday 10&ndash;2</td><td><b>The identification query first</b> (#891&rsquo;s ended-reason data &mdash; Wednesday hit seven, Thursday only two), then the engineering backlog')

# ---- J. line-health + needs-reply + fyi ----
rep('and the window closed with nothing after 8:08 &mdash; verified at 10:03, trash included.',
    'and the window closed with nothing after 8:08 &mdash; verified at 10:03, trash included. The &ldquo;Call handled&rdquo; notes kept coming (10:47 PM, 6:38 AM), and <b>Friday opened without a failure</b>.')
rep('Six days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply (day three) beside it &mdash; the 7:30&ndash;8:30 pocket is the catch',
    'Seven days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply (day four) beside it &mdash; the open 2&ndash;6 stretch is the catch')
rep('<li><b>The accountants&rsquo; IRS response is go</b> &mdash; Nate quoted $250 at 6:40 AM and you told him to handle it at 10:26. Closed; nothing left to do.</li>',
    '<li><b>The IRS matter is closed end-to-end</b> &mdash; Nate confirmed Thursday afternoon he&rsquo;ll send the response right after 10/15. Nothing left to do.</li>')

# ---- L. remaining bumps ----
rep('Day twenty-four on Eric','Day twenty-five on Eric')
rep('thirty full days','thirty-one full days')
rep('Day twenty-five on all three','Day twenty-six on all three')
rep('seventeen days','eighteen days',3)
rep('day twenty-nine','day thirty',3)  # Sentry x2 + Sep 8 promises header, all +1 chains
rep('twenty-five days in','twenty-six days in',2)
rep('nine days left','eight days left')
rep('thirty-eight days','thirty-nine days',2)
rep('42 days','43 days')
rep('62 days','63 days')
c=s.count('twenty-six days past'); print('26 past remaining:',c)
s=s.replace('twenty-six days past','twenty-seven days past')
c=s.count('day twenty-three'); print('d23 remaining:',c)
s=s.replace('day twenty-three','day twenty-four')
c=s.count('nine days out'); print('9out remaining:',c)
s=s.replace('nine days out','eight days out')
c=s.count('six days'); print('six days remaining:',c)
c=s.count('day three'); print('day three remaining:',c)
c=s.count('night twenty-four'); print('n24 remaining:',c)
s=s.replace('night twenty-four','night twenty-five')

def chip(m): return m.group(1)+str(int(m.group(2))+1)+m.group(3)
s,n=re.subn(r'(class="chip old">)(\d+)(d)', chip, s)
print('chips bumped:',n); assert n==5

# ---- N. sanity ----
assert s.count('__CC_STATE__')==1 and s.count('__CC_TEMPLATE__')==1
assert s.count('data-react-task="')==59, s.count('data-react-task="')
assert s.count('class="bar"')==7
assert s.count('2026-10-09T07:14:00-05:00')==2
assert s.count('class="slot past"')==0
assert s.count('Thu Oct 8')==0
for leftover in ['8:30&ndash;12:30 &mdash;','day three of a live deal','Taylor at 2','invite unanswered']:
    print('leftover',repr(leftover),s.count(leftover))
open(p,'w').write(s)
print('FRIDAY FULL OK', len(s))
