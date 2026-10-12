import re
src = open('page-template.html').read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:90]}"
    src = src.replace(old, new)

def rx(pat, new, n=1):
    global src
    ms = re.findall(pat, src, re.DOTALL)
    assert len(ms) == n, f"rx count {len(ms)} != {n} for: {pat[:90]}"
    src = re.sub(pat, lambda m: new, src, count=n, flags=re.DOTALL)

# ---------- 1. stamps / greeting / eyebrow ----------
rep('2026-10-11T22:03:00-05:00', '2026-10-12T07:14:00-05:00', 2)
rep('<b>Brief compiled</b> Fri 7:14 AM &middot; data checked Sun 10:03 PM CT',
    '<b>Brief compiled</b> Mon 7:14 AM &middot; data checked Mon 7:14 AM CT')
rep('<div class="eyebrow">Sunday, October 11 &middot; 2026</div>',
    '<div class="eyebrow">Monday, October 12 &middot; 2026</div>')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- 2. masthead sub ----------
old_sub = src[src.find('<p class="sub">Sunday is clear'):src.find('No reactions saved.</p>')+len('No reactions saved.</p>')]
assert old_sub.startswith('<p class="sub">') and old_sub.endswith('</p>')
new_sub = ('<p class="sub">The Iris engagement is <b>live as of today</b> &mdash; Laura signed Friday at 3:03 PM, '
  'effective Monday, October 12, and the agreed first focus is refining the onboarding process. Today runs <b>6.75h</b>: '
  'Product Sync at 8, <b>UGM Planning with Jr 9&ndash;10</b> (Vipin Gupta also messaged you in the Whova event app overnight), '
  '<b>Deep Work (Engineering) 10&ndash;2</b> &mdash; the #799 window at last &mdash; and Transition 2&ndash;3, with the evening open. '
  'Tomorrow is Iris-heavy: <b>Monthly Iris Sync at 9:00</b> &mdash; your Oct 6 draft to Laura (&ldquo;Iris updates ahead of our '
  'October 13 sync&rdquo;) is still unsent &mdash; plus a <b>new Iris Training block 1&ndash;2 PM</b> inside Deep Work and the Izzy '
  'check-in at 10. The weekend line story ran heavy: <b>Sunday set the streak record &mdash; fourteen failures and five '
  'needs-attention</b>, with thirteen &ldquo;Call handled&rdquo; successes keeping pace, after Saturday&rsquo;s five-failure burst; '
  'Monday has already opened with two failures by 7:13. Still owed: <b>the Emilio recap, ten days</b>, and <b>the Affiliated '
  'pricing reply, day seven</b> ($0.16 floor, $0.15 at 100K agreed). #799 at <b>day thirty-six</b>, Eric at <b>day thirty-five</b>, '
  'the job descriptions at <b>day twenty-seven</b> with the workshop five days out, billing/RevIO at thirty days past, Nick on '
  'night twenty-eight. No reactions saved over the weekend.</p>')
src = src.replace(old_sub, new_sub)

# ---------- 3. needs-a-decision note ----------
rep('<span class="note">The Emilio recap (seven days) and the Affiliated pricing reply (day four, answer agreed) are the carried sends &mdash; the open 2&ndash;6 stretch is today&rsquo;s catch, and your 11:30 Emilio-clause block pairs with the recap; the 9:58 PM draft to Jake and Laura is ready for the 9:00 call</span>',
    '<span class="note">The Emilio recap (ten days) and the Affiliated pricing reply (day seven, answer agreed) are the carried sends &mdash; Transition 2&ndash;3 is today&rsquo;s pocket &mdash; and the Oct 6 draft to Laura should go out before tomorrow&rsquo;s 9:00 Iris Sync</span>')

# ---------- 4. schedule card + todaynote ----------
rep('<span class="note" id="todaynote">Nothing on the calendar &mdash; an open Sunday</span>',
    '<span class="note" id="todaynote">Four blocks, 6.75h &mdash; open after 3</span>')
rep('<div class="slot free"><div class="t">All day</div><div class="w">Open &mdash; nothing scheduled<small>nothing booked; Monday opens with Product Sync at 8 and UGM Planning with Jr at 9</small></div></div>',
    '''<div class="slot"><div class="t">8:00 &ndash; 8:45</div><div class="w">Weekly Product Sync<small>Google Meet &middot; Jr accepted, Eelco pending</small></div></div>
        <div class="slot"><div class="t">9:00 &ndash; 10:00</div><div class="w">UGM Planning: Bodhi + Junior<small>the hour you asked for Friday &middot; registration, booth, blast &mdash; and Vipin Gupta&rsquo;s Whova message</small></div></div>
        <div class="slot"><div class="t">10:00 &ndash; 2:00</div><div class="w">Deep Work (Engineering)<small>the #799 window &mdash; day thirty-six, double-approved</small></div></div>
        <div class="slot"><div class="t">2:00 &ndash; 3:00</div><div class="w">Transition, Talking, Triage<small>the pocket for the Emilio recap and the Affiliated reply</small></div></div>
        <div class="slot free"><div class="t">3:00 onward</div><div class="w">Open<small>evening clear &mdash; first open evening after the weekend&rsquo;s alert storm</small></div></div>''')

# ---------- 5. Top 5 ----------
i = src.find('<ol class="prio">'); j = src.find('</ol>', i)
new_prio = '''<ol class="prio">
        <li><div>
          <h4>The Iris engagement starts today &mdash; and tomorrow is its first full morning</h4>
          <p class="why">Laura&rsquo;s signed copy came back Friday at 3:03 PM &mdash; effective today, 15-day notice, net-15 &mdash; with onboarding refinement the agreed first focus. Tomorrow carries the <b>Monthly Iris Sync at 9:00</b> and a <b>new Iris Training block 1&ndash;2 PM</b> Laura organized. Your <b>Oct 6 draft &ldquo;Iris updates ahead of our October 13 sync&rdquo; is still unsent</b> &mdash; sending it today walks into tomorrow prepared.</p>
          <div class="meta"><span class="pill good">Live &middot; effective today</span><span class="pill warn">Draft to Laura before tomorrow 9:00</span></div>
        </div></li>
        <li><div>
          <h4>The Emilio recap &mdash; ten days; the deal&rsquo;s visible half is still unsent</h4>
          <p class="why">Ten days since the &ldquo;Smart City Partnership Next Steps&rdquo; call and the written recap (CC Jr) is still what keeps the deal moving on Emilio&rsquo;s side. You worked the clause twice last week &mdash; the work exists; the send doesn&rsquo;t. Transition 2&ndash;3 is today&rsquo;s pocket.</p>
          <div class="meta"><span class="pill crit">Ten days</span><span class="pill quiet">Transition 2&ndash;3</span></div>
        </div></li>
        <li><div>
          <h4>The Affiliated pricing reply &mdash; day seven of a live deal waiting on your answer</h4>
          <p class="why">Michael&rsquo;s volume-discount question is a week old, the proposal already in front of Tom Welsh. The answer is agreed: <b>$0.16 floor, $0.15 at 100,000 minutes as a first-for-any-partner exception</b>, partnership value over per-minute price. Pyro sheet, then send &mdash; and clear the two stale CAIRO drafts on the Wheelock thread while you&rsquo;re there.</p>
          <div class="meta"><span class="pill crit">Deal live &middot; day seven</span><span class="pill quiet">Reply to Michael (CC Jr) &middot; 2&ndash;3</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day thirty-six &mdash; the engineering window is today, 10&ndash;2</h4>
          <p class="why">Double-approved for over a month, with the TCP switch, the #830/#831/#842/#843/#886 reviews and the #894/#855 pair behind it. <b>Deep Work (Engineering) 10&ndash;2 is the first real engineering block since the backlog formed</b> &mdash; ship #799 first and the SpectrumVoIP SIP-cancel failures end regardless of transport.</p>
          <div class="meta"><span class="pill warn">Today 10&ndash;2</span><span class="pill quiet">#799 first, then reviews</span></div>
        </div></li>
        <li><div>
          <h4>UGM Planning at 9 &mdash; registration, booth and blast in one hour with Jr</h4>
          <p class="why">The hour you asked for Friday evening. On the table: the Silver registration ($250 off the final invoice), Jr&rsquo;s booth pricing thread with Crexendo (Silver committed, registration owed), the v2 + UGM email blast, and the attendee-list chase with Jason Byrne. <b>Vipin Gupta messaged you in the Whova event app overnight</b> &mdash; worth opening before the hour. UGM is Oct 26&ndash;28 in Austin.</p>
          <div class="meta"><span class="pill warn">Today 9&ndash;10</span><span class="pill quiet">Whova message waiting</span></div>
        </div></li>
      </ol>'''
src = src[:i] + new_prio + src[j+len('</ol>'):]

# ---------- 6. coming-up cards ----------
rep('''<h4 style="font-size:14px">The Iris arc, start to signature &mdash; held at 9, signed by 3:03</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Call at 9 with Laura Mathwig and Jason Dow, proposal forwarded at 9:05, your kickoff note at 11:17 &mdash; and <b>Laura&rsquo;s signed copy came back at 3:03 PM</b>, effective Monday, October 12, with her two edits (15-day notice, net-15 payment) accepted at 3:32. First focus, as discussed: refining the onboarding process and team follow-ups.</p>''',
'''<h4 style="font-size:14px">Iris, week one &mdash; signed Friday, live today, three touchpoints tomorrow</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Laura&rsquo;s signed copy came back Friday 3:03 PM (15-day notice, net-15, accepted at 3:32) &mdash; <b>effective today</b>. First focus: refining the onboarding process and team follow-ups. Tomorrow: <b>Monthly Iris Sync 9:00</b> (your Oct 6 update draft to Laura still unsent) and a <b>new Iris Training session 1&ndash;2 PM</b> Laura put on the calendar Friday &mdash; and lmccree joined the Voxtell Linear workspace, so SpectrumVoIP can now be tagged on work directly.</p>''')

rep('''<h4 style="font-size:14px">Today 9:30&ndash;2 &mdash; the blocks you built, then the open stretch</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Work on UGM 9:30&ndash;11:30</b> (the Silver registration and the v2 + UGM email blast, booked 10:30&ndash;11:30), <b>Emilio&rsquo;s clause 11:30&ndash;12</b> &mdash; send the seven-day recap from the same seat &mdash; Grok Bot 201 at noon, and <b>Level mobile to the App Store 1&ndash;2</b>. Then the day opens: <b>2&ndash;6 is the pocket</b> for the Affiliated reply ($0.16 floor, $0.15 at 100K as the first-time exception, Pyro sheet first) before the Quincy dinner at 6.</p>''',
'''<h4 style="font-size:14px">Today 8&ndash;3 &mdash; sync, UGM hour, the engineering window, then the sends</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Product Sync 8:00</b> (Jr in, Eelco pending &mdash; bring the Sentry weekly: errors down 77%), <b>UGM Planning 9&ndash;10</b> with Jr (registration, booth, blast, Vipin&rsquo;s Whova message), <b>Deep Work (Engineering) 10&ndash;2</b> &mdash; #799 first &mdash; and <b>Transition 2&ndash;3 carries the sends</b>: the Emilio recap (ten days), the Affiliated reply (day seven, answer agreed), and the pre-sync Iris draft to Laura. The evening is open.</p>''')

rep('''<h4 style="font-size:14px">The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Monday &mdash; Product Sync returns, Deep Work Engineering 10&ndash;2</b> (the #799 window). <b>Tuesday Oct 13 &mdash; Iris Sync 9:00, Izzy check-in 10:00</b> (the Levitt verdict&rsquo;s next window). <b>Wednesday 7.75h.</b> <b>Thursday Oct 15 &mdash; 9.25h with Parr PT 8:45&ndash;10 inside Deep Work 8:30&ndash;12:30</b>, the collision to settle, and Scott Van Camp at 2. <b>Saturday Oct 17 &mdash; the workshop</b>, eight days out, prep moving on four working sessions this week.</p>''',
'''<h4 style="font-size:14px">The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Tuesday Oct 13 &mdash; Iris Sync 9:00, Izzy check-in 10:00</b> (the Levitt verdict&rsquo;s next window) <b>and the new Iris Training 1&ndash;2</b>, both inside Deep Work 10&ndash;2. <b>Wednesday 7.25h</b> &mdash; and the Gym Series Circuit you registered for Sunday night (8&ndash;8:45) overlaps your own Lift at 8:15. <b>Thursday Oct 15 &mdash; 8.75h, over the line, with Parr PT 8:45&ndash;10 inside Deep Work 8:30&ndash;12:30</b> and Scott Van Camp at 2. <b>Friday is empty</b> &mdash; the week&rsquo;s recovery valve or its catch-up day. <b>Saturday Oct 17 &mdash; the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), five days out.</p>''')

# ---------- 7. chart ----------
i = src.find('<div class="plot" id="plot">'); j = src.find('</div>\n        <div class="xaxis"', i)
new_plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(51.79% + 6px)">7.25</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(62.5% + 6px)">8.75</div>
            <div class="seg m" style="height:16.07%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:10.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(32.14% + 6px)">4.5</div>
            <div class="seg m" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
        '''
src = src[:i] + new_plot + src[j:]
rep('''<div class="xaxis" id="xaxis">
          <div><b>Fri</b>9</div><div><b>Sat</b>10</div>
          <div><b>Sun</b>11</div><div><b>Mon</b>12</div><div><b>Tue</b>13</div><div><b>Wed</b>14</div><div><b>Thu</b>15</div>
        </div>''',
'''<div class="xaxis" id="xaxis">
          <div><b>Mon</b>12</div><div><b>Tue</b>13</div>
          <div><b>Wed</b>14</div><div><b>Thu</b>15</div><div><b>Fri</b>16</div><div><b>Sat</b>17</div><div><b>Sun</b>18</div>
        </div>''')
rep('Fri Oct 9 &ndash; Thu Oct 15', 'Mon Oct 12 &ndash; Sun Oct 18')

# ---------- 8. week flags ----------
i = src.find('<h3><span class="pill warn">Today</span> Friday is the week&rsquo;s new peak')
j = src.find('</p>', src.find('Second day running over the 8h line.'))
assert i > 0 and j > i
new_flag1 = '''<h3><span class="pill warn">Today</span> Monday restarts at 6.75h &mdash; the Iris engagement is live and the engineering window finally lands</h3>
          <p>Product Sync 8:00, <b>UGM Planning with Jr 9&ndash;10</b>, <b>Deep Work (Engineering) 10&ndash;2</b> &mdash; the first real engineering block since the backlog formed; #799 (day thirty-six, double-approved) goes first &mdash; and Transition 2&ndash;3 carries the sends: the Emilio recap (ten days), the Affiliated reply (day seven) and the pre-sync Iris draft to Laura. The evening is open. No Doggy Care on the calendar today.'''
src = src[:i] + new_flag1 + src[j:]

i = src.find('<h3><span class="pill warn">This week</span> The floor, then a climbing back half')
j = src.find('</p>', src.find('including Thursday&rsquo;s reseller-value session.'))
assert i > 0 and j > i
new_flag2 = '''<h3><span class="pill warn">This week</span> Tuesday stacks three meetings around Deep Work; Thursday is over the line; Friday is empty</h3>
          <p><b>Tuesday Oct 13 runs 7.75h</b> &mdash; Monthly Iris Sync 9:00, the Izzy check-in 10:00 (the Levitt verdict&rsquo;s next window) <b>and the new Iris Training 1&ndash;2</b>, the last two both sitting inside Deep Work (Client + Admin + Sales) 10&ndash;2: barely two clear hours of that block survive. <b>Wednesday runs 7.25h</b> with the morning double-booked (Gym Circuit 8&ndash;8:45 against your Lift 8:15 &mdash; pick one). <b>Thursday Oct 15 charts at 8.75h, over the 8h line</b>, with the standing collision: <b>Parr PT 8:45&ndash;10 inside Deep Work 8:30&ndash;12:30</b>, plus Scott Van Camp at 2. <b>Friday Oct 16 is completely empty</b> &mdash; hold it as recovery or let it absorb what Thursday&rsquo;s collision displaces. <b>Saturday Oct 17 carries the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), five days out.'''
src = src[:i] + new_flag2 + src[j:]

# ---------- 9. already-have-a-home table ----------
rep('<tr><td class="tid">Today 2&ndash;6</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing) and <b>the Emilio recap</b> (seven days old) &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread); the <b>UGM registration</b> finally has its own block, today 9:30&ndash;11:30<div class="src">Eric&rsquo;s reply (day thirty-two) and the send backlog (twenty-seven days past on billing/RevIO &middot; Nick night twenty-five) fit the open 2&ndash;6 stretch</div></td></tr>',
    '<tr><td class="tid">Today 2&ndash;3</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing), <b>the Emilio recap</b> (ten days old) and <b>the pre-sync Iris draft to Laura</b> &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread); the <b>UGM registration</b> belongs in the 9&ndash;10 planning hour<div class="src">Eric&rsquo;s reply (day thirty-five) and the send backlog (thirty days past on billing/RevIO &middot; Nick night twenty-eight) queue behind them</div></td></tr>')
rep('<tr><td class="tid">Today (open)</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-four; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; the Taylor session came and went Thursday &mdash; workshop eight days out</div></td></tr>',
    '<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-seven; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop five days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>')
rep('<tr><td class="tid">Monday 10&ndash;2</td>', '<tr><td class="tid">Today 10&ndash;2</td>')

# ---------- 10. FYI list ----------
rep('<li><b>Sentry&rsquo;s weekly report landed Saturday afternoon</b>: 776 errors, down 77% week-over-week, across 23 issues (down 63%) &mdash; fresh context for the keep-or-drop call on billed Logs before the period ends Tuesday.</li>',
    '''<li><b>Vipin Gupta messaged you in the Whova app overnight</b> (NetSapiens UGM 2026, 3:41 AM) &mdash; worth opening before the 9 AM UGM Planning hour.</li>
        <li><b>You registered for Gym Series: The Circuit</b> Sunday night &mdash; Wednesday 8&ndash;8:45 at Gevity; it overlaps your standing Lift (Upper Body) at 8:15, so one of them gives way.</li>
        <li><b>Sentry&rsquo;s weekly report landed Saturday afternoon</b>: 776 errors, down 77% week-over-week, across 23 issues (down 63%) &mdash; fresh context for the keep-or-drop call on billed Logs before the period ends tomorrow, Oct 13.</li>''')
rep('<li><b>Monday 9&ndash;10 AM is now UGM Planning with Jr</b> &mdash; you asked Friday evening, the assistants coordinated it, Jr confirmed, and the event is on the calendar. It sits between Product Sync and the Deep Work engineering block.</li>',
    '<li><b>Today 9&ndash;10 AM is UGM Planning with Jr</b> &mdash; you asked Friday evening, the assistants coordinated it, Jr confirmed. It sits between Product Sync and the Deep Work engineering block.</li>')
rep('you archived it with the rest of today&rsquo;s inbox this afternoon.',
    'you archived it with the rest of Friday&rsquo;s inbox.')

# ---------- 11. line health: Monday opener ----------
rep('The successes kept pace: thirteen &ldquo;Call handled&rdquo;, the latest at 3:28 and 3:30 PM.',
    'The successes kept pace: thirteen &ldquo;Call handled&rdquo;, the latest at 3:28 and 3:30 PM. Monday opened on the same rhythm: <b>failures at 7:01 and 7:13 AM</b> against a &ldquo;Call handled&rdquo; at 7:01 &mdash; window open at 7:14.')

# ---------- 12. aging bumps (remaining occurrences) ----------
rep('now twenty-seven days past due', 'now thirty days past due')
rep('Seven days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply (day four) beside it &mdash; the open 2&ndash;6 stretch is the catch',
    'Ten days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply (day seven) beside it &mdash; Transition 2&ndash;3 is today&rsquo;s pocket')
rep('Day twenty-five on Eric Bramini', 'Day twenty-eight on Eric Bramini')
rep('thirty-one full days ago', 'thirty-four full days ago')
rep('day thirty of billed Logs', 'day thirty-three of billed Logs')
rep('#799 is still sitting there, day thirty-three', '#799 is still sitting there, day thirty-six')
rep('twenty-ninth day double-approved', 'thirty-second day double-approved')
rep('thirty-nine days past retirement', 'forty-two days past retirement')
rep('Retired Aug 31 &mdash; thirty-nine days past', 'Retired Aug 31 &mdash; forty-two days past')
rep('em-roadmap at 43 days', 'em-roadmap at 46 days')
rep('Promised Sep 15 &mdash; day twenty-four', 'Promised Sep 15 &mdash; day twenty-seven')
rep('eighteen days unsent', 'twenty-one days unsent')
rep('#799 (day thirty-three, double-approved)', '#799 (day thirty-six, double-approved)')
rep('Behind those: <b>Eric &mdash; day thirty-two</b>, Nick&rsquo;s program-details reply on night twenty-five',
    'Behind those: <b>Eric &mdash; day thirty-five</b>, Nick&rsquo;s program-details reply on night twenty-eight')
rep('55d &mdash; chronic', '58d &mdash; chronic')
rep('<span class="chip old">55d</span>', '<span class="chip old">58d</span>')
rep('<span class="chip old">52d</span>', '<span class="chip old">55d</span>')
rep('48d &mdash; stalled', '51d &mdash; stalled')
rep('63d &mdash; chronic', '66d &mdash; chronic')

# ---------- sanity ----------
assert src.count('__CC_STATE__') == 1
assert src.count('__CC_TEMPLATE__') == 1
assert src.count('data-react-task="') == 59
assert src.count('class="bar"') == 7
assert src.count('2026-10-12T07:14:00-05:00') == 2
assert src.count('day four') == 0, src.count('day four')
assert src.count('day thirty-three') == 1  # the new "day thirty-three of billed Logs"
assert src.count('day twenty-four') == 0
assert src.count('night twenty-five') == 0
assert src.count('eight days out') == 0
assert src.count('9.25h') == 0
open('page-template.html', 'w').write(src)
print('OK', len(src))
