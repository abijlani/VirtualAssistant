import re
src = open('page-template.html').read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:90]}"
    src = src.replace(old, new)

# ---------- 1. stamps / greeting / eyebrow ----------
rep('2026-10-12T22:03:00-05:00', '2026-10-13T07:14:00-05:00', 2)
rep('<b>Brief compiled</b> Mon 7:14 AM &middot; data checked Mon 10:03 PM CT',
    '<b>Brief compiled</b> Tue 7:14 AM &middot; data checked Tue 7:14 AM CT')
rep('<div class="eyebrow">Monday, October 12 &middot; 2026</div>',
    '<div class="eyebrow">Tuesday, October 13 &middot; 2026</div>')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- 2. masthead sub ----------
i = src.find('<p class="sub">The Iris engagement is')
j = src.find('No reactions saved over the weekend.</p>') + len('No reactions saved over the weekend.</p>')
assert i > 0 and j > i
new_sub = ('<p class="sub">Yesterday closed loops everywhere. <b>ATS onboarding is live</b> &mdash; you sent Kayla Carroll '
  'the kickoff form at 12:17 PM (Michael Wheelock CC&rsquo;d) and she&rsquo;ll have it back Thursday afternoon &mdash; the stale '
  'CAIRO drafts are cleared, and the UGM hour became a procurement sprint: <b>booth moved to Table 12</b>, the 2F-15 graphic in '
  'negotiation, tees quoted with Austin Print Co, a 4imprint order placed, and <b>ProGraphix needs your banner artwork by '
  'tomorrow</b> to hit the 10/23 deadline. Today runs <b>6.75h</b>: Lift 8:15, <b>Monthly Iris Sync 9:00</b> &mdash; your Oct 6 '
  'update draft to Laura is still unsent &mdash; the Izzy check-in at 10 (the Levitt verdict&rsquo;s window), Deep Work '
  '(Client + Admin + Sales) 10&ndash;2 and Transition 2&ndash;3. <b>Iris Training moved to Thursday 11&ndash;12</b> (Alexander is '
  'out today; your 11-or-noon counter was taken), stacking Thursday to <b>9.75h, the week&rsquo;s peak</b> &mdash; and Wednesday '
  'picked up Retreat planning 10:30&ndash;11:30, nudging it to 8.25h. <b>The Sentry Logs billing period ends today</b> &mdash; '
  'keep-or-drop is now or it rolls another month. Still owed: <b>the Emilio recap, eleven days</b>. #799 at <b>day '
  'thirty-seven</b>, Eric at <b>day thirty-six</b>, the job descriptions at <b>day twenty-eight</b> with the workshop four days '
  'out, billing/RevIO at thirty-one days past, Nick on night twenty-nine. No reactions saved.</p>')
src = src[:i] + new_sub + src[j:]

# ---------- 3. needs-a-decision note ----------
rep('<span class="note">The Emilio recap (ten days) and the Affiliated pricing reply (day seven, answer agreed) are the carried sends &mdash; Transition 2&ndash;3 is today&rsquo;s pocket &mdash; and the Oct 6 draft to Laura should go out before tomorrow&rsquo;s 9:00 Iris Sync</span>',
    '<span class="note">The Emilio recap (eleven days) is the one carried send &mdash; the Affiliated reply came off the board when ATS onboarding kicked off yesterday &mdash; and the Oct 6 draft to Laura should go out before the 9:00 Iris Sync</span>')

# ---------- 4. schedule card + todaynote ----------
rep('<span class="note" id="todaynote">Four blocks, 6.75h &mdash; open after 3</span>',
    '<span class="note" id="todaynote">Iris morning, then the admin block &mdash; 6.75h, open after 3</span>')
pat = re.compile(r'(<div class="card sched" id="todaysched">\n).*?(\n      </div>\n    </section>)', re.DOTALL)
ms = pat.findall(src)
assert len(ms) == 1, len(ms)
new_slots = '''        <div class="slot"><div class="t">8:15 &ndash; 9:00</div><div class="w">The Lift Class (Lower Body)<small>Gevity</small></div></div>
        <div class="slot"><div class="t">9:00 &ndash; 9:30</div><div class="w">Monthly Iris Sync with Voxtell<small>Teams &middot; Laura + the SpectrumVoIP team &middot; day two of the engagement &mdash; send the update draft first</small></div></div>
        <div class="slot"><div class="t">10:00 &ndash; 10:30</div><div class="w">Izzy Weekly Checkin<small>Teams &middot; Tim, Adam &middot; the Levitt verdict&rsquo;s window &mdash; sits inside Deep Work</small></div></div>
        <div class="slot"><div class="t">10:00 &ndash; 2:00</div><div class="w">Deep Work (Client + Admin + Sales)<small>Emilio recap, ProGraphix artwork, the Sentry call &mdash; all fit here</small></div></div>
        <div class="slot"><div class="t">2:00 &ndash; 3:00</div><div class="w">Transition, Talking, Triage<small>overflow pocket</small></div></div>
        <div class="slot free"><div class="t">3:00 onward</div><div class="w">Open<small>evening clear</small></div></div>'''
src = pat.sub(lambda m: m.group(1) + new_slots + m.group(2), src, count=1)

# ---------- 5. Top 5 ----------
i = src.find('<ol class="prio">'); j = src.find('</ol>', i)
new_prio = '''<ol class="prio">
        <li><div>
          <h4>Iris Sync at 9:00 &mdash; day two of the engagement, and the update draft is still unsent</h4>
          <p class="why">Laura&rsquo;s team joins on Teams at 9. Your <b>Oct 6 draft &ldquo;Iris updates ahead of our October 13 sync&rdquo; has sat unsent for a week</b> &mdash; sending it before the call (or walking its contents in) sets the agenda. Training moved to <b>Thursday 11&ndash;12</b> at your suggestion; onboarding refinement remains the agreed first focus.</p>
          <div class="meta"><span class="pill warn">Today 9:00</span><span class="pill crit">Draft unsent &middot; day seven</span></div>
        </div></li>
        <li><div>
          <h4>The Emilio recap &mdash; eleven days; the only carried send left</h4>
          <p class="why">With the Affiliated reply resolved by yesterday&rsquo;s ATS kickoff, this is the one send still owed. Eleven days since the &ldquo;Smart City Partnership Next Steps&rdquo; call &mdash; the written recap (CC Jr) is what keeps the deal moving on Emilio&rsquo;s side. Deep Work 10&ndash;2 or Transition 2&ndash;3.</p>
          <div class="meta"><span class="pill crit">Eleven days</span><span class="pill quiet">10&ndash;2 or 2&ndash;3</span></div>
        </div></li>
        <li><div>
          <h4>ProGraphix banner artwork &mdash; due tomorrow to hold the 10/23 conference deadline</h4>
          <p class="why">Cathy sent the template, spec sheet and estimate at 5:32 PM yesterday: <b>everything must be submitted by Wednesday</b>. The table cover question (4-foot fitted vs standard throw) is still open on the thread too. This is the hardest deadline on the board.</p>
          <div class="meta"><span class="pill crit">Due tomorrow</span><span class="pill quiet">Template + spec sheet in the Cathy thread</span></div>
        </div></li>
        <li><div>
          <h4>Sentry Logs keep-or-drop &mdash; the billing period ends today</h4>
          <p class="why">The Sep 14&ndash;Oct 13 period closes today with reserved volume already at 100% and data being dropped. Deciding now &mdash; keep and right-size, or switch Logs off &mdash; beats rolling into another month by default. Last week&rsquo;s report (errors down 77%) is the context on the page.</p>
          <div class="meta"><span class="pill crit">Period ends today</span><span class="pill quiet">Two-minute call &middot; any pocket</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day thirty-seven &mdash; next engineering windows are Wednesday 11&ndash;3 and Thursday morning</h4>
          <p class="why">Double-approved and unmerged, with the TCP switch and the review stack behind it. Today&rsquo;s Deep Work is Client + Admin + Sales; <b>Wednesday&rsquo;s Project Engineering 11&ndash;3 is the next clean shot</b> &mdash; Thursday&rsquo;s 8:30&ndash;12:30 block is already carved up by Parr PT and Iris Training.</p>
          <div class="meta"><span class="pill warn">Review waiting</span><span class="pill quiet">Wed 11&ndash;3</span></div>
        </div></li>
      </ol>'''
src = src[:i] + new_prio + src[j+len('</ol>'):]

# ---------- 6. coming-up cards ----------
i = src.find('<h4 style="font-size:14px">Iris, week one')
j = src.find('</p>', src.find('tagged on work directly.')) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Iris, day two &mdash; sync at 9 today, training Thursday at 11</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">The engagement went live yesterday; today is its first customer-facing touchpoint. <b>Monthly Iris Sync 9:00</b> (Laura, Alexander, LeVarr, Steven, Josh on the invite) &mdash; your Oct 6 update draft is still unsent. <b>Training moved to Thursday 11&ndash;12</b>: Laura asked for Thursday since Alexander is out today, you countered 11 or noon at 7:10 PM, and she rebooked it at 11 &mdash; accept the updated invite when you see it. lmccree is in the Voxtell Linear workspace for direct tagging.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">Today 8&ndash;3')
j = src.find('</p>', src.find('The evening is open.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Today 8:15&ndash;3 &mdash; Iris morning, then the admin block carries the backlog</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Lift 8:15</b>, <b>Iris Sync 9:00</b> (send the draft first), <b>Izzy check-in 10:00</b> &mdash; ask for the Levitt verdict plainly &mdash; then <b>Deep Work (Client + Admin + Sales) 10&ndash;2</b>: the Emilio recap (eleven days), the ProGraphix artwork (due tomorrow) and the Sentry keep-or-drop (period ends today) all belong in it. Transition 2&ndash;3 is overflow; the evening is open.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
j = src.find('</p>', src.find('five days out.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Wednesday 8.25h</b> &mdash; Retreat planning 10:30&ndash;11:30 (new, with Shandi) overlaps Deep Work&rsquo;s first half hour, and the Gym Circuit you registered for (8&ndash;8:45) overlaps your own Lift at 8:15. <b>Thursday 9.75h is the week&rsquo;s peak</b>: Parr PT 8:45&ndash;10 and the rebooked <b>Iris Training 11&ndash;12</b> both sit inside Deep Work 8:30&ndash;12:30, then Lift, Scott Van Camp at 2 and two Reserved blocks. <b>Friday is empty</b> &mdash; recovery valve or catch-up. <b>Saturday Oct 17 &mdash; the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), four days out. <b>Monday restarts at 5.75h.</b></p>''' + src[j:]

# ---------- 7. chart ----------
i = src.find('<div class="plot" id="plot">'); j = src.find('</div>\n        <div class="xaxis"', i)
new_plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(58.93% + 6px)">8.25</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(69.64% + 6px)">9.75</div>
            <div class="seg m" style="height:23.21%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:10.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(32.14% + 6px)">4.5</div>
            <div class="seg m" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
        '''
src = src[:i] + new_plot + src[j:]
rep('''<div class="xaxis" id="xaxis">
          <div><b>Mon</b>12</div><div><b>Tue</b>13</div>
          <div><b>Wed</b>14</div><div><b>Thu</b>15</div><div><b>Fri</b>16</div><div><b>Sat</b>17</div><div><b>Sun</b>18</div>
        </div>''',
'''<div class="xaxis" id="xaxis">
          <div><b>Tue</b>13</div><div><b>Wed</b>14</div>
          <div><b>Thu</b>15</div><div><b>Fri</b>16</div><div><b>Sat</b>17</div><div><b>Sun</b>18</div><div><b>Mon</b>19</div>
        </div>''')
rep('Mon Oct 12 &ndash; Sun Oct 18', 'Tue Oct 13 &ndash; Mon Oct 19')

# ---------- 8. week flags ----------
i = src.find('<h3><span class="pill warn">Today</span> Monday restarts at 6.75h')
j = src.find('</p>', src.find('No Doggy Care on the calendar today.'))
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">Today</span> Tuesday runs 6.75h &mdash; Iris faces the customer at 9, and three decisions share the admin block</h3>
          <p>Lift 8:15, <b>Monthly Iris Sync 9:00</b> (the unsent Oct 6 draft is the prep), <b>Izzy check-in 10:00</b> inside Deep Work &mdash; the Levitt verdict&rsquo;s window &mdash; then <b>Deep Work (Client + Admin + Sales) 10&ndash;2</b> carrying the Emilio recap (eleven days), the ProGraphix artwork (due tomorrow) and the Sentry keep-or-drop (period ends today). Transition 2&ndash;3, evening open.''' + src[j:]

i = src.find('<h3><span class="pill warn">This week</span> Tuesday stacks three meetings')
j = src.find('</p>', src.find('breakdown to 4:30), five days out.'))
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">This week</span> Wednesday crossed the line overnight, and Thursday is now the 9.75h peak</h3>
          <p><b>Wednesday runs 8.25h</b> &mdash; the new <b>Retreat planning 10:30&ndash;11:30</b> with Shandi overlaps Deep Work (Project Engineering) 11&ndash;3 by half an hour, and the Gym Circuit (8&ndash;8:45, registered Sunday) overlaps your own Lift at 8:15: pick one of each pair. <b>Thursday Oct 15 charts at 9.75h, the week&rsquo;s peak and well over the line</b>: Parr PT 8:45&ndash;10 and the rebooked <b>Iris Training 11&ndash;12</b> both sit inside Deep Work 8:30&ndash;12:30 &mdash; barely 90 clear minutes of that block survive &mdash; then Lift 1:00, Scott Van Camp 2:00 and two Reserved blocks to 4. <b>Friday Oct 16 is empty</b> &mdash; hold it as recovery or let it absorb what Thursday displaces; the ATS form lands Thursday afternoon and Friday is the natural slot to act on it. <b>Saturday Oct 17 carries the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), four days out.''' + src[j:]

# ---------- 9. already-have-a-home table ----------
rep('<tr><td class="tid">Today 2&ndash;3</td><td><b>The Affiliated pricing reply</b> ($0.15 at 100K minutes, the exception framing), <b>the Emilio recap</b> (ten days old) and <b>the pre-sync Iris draft to Laura</b> &mdash; alongside the <b>CAIRO cleanup</b> (two drafts on the Wheelock thread); the <b>UGM registration</b> belongs in the 9&ndash;10 planning hour<div class="src">Eric&rsquo;s reply (day thirty-five) and the send backlog (thirty days past on billing/RevIO &middot; Nick night twenty-eight) queue behind them</div></td></tr>',
    '<tr><td class="tid">Today 10&ndash;2</td><td><b>The Emilio recap</b> (eleven days), <b>the ProGraphix banner artwork</b> (submission due tomorrow for 10/23) and <b>the Sentry keep-or-drop</b> (period ends today) &mdash; the pre-sync Iris draft goes before 9<div class="src">Eric&rsquo;s reply (day thirty-six) and the send backlog (thirty-one days past on billing/RevIO &middot; Nick night twenty-nine) queue behind them &middot; Affiliated resolved: ATS onboarding kicked off Monday</div></td></tr>')
rep('<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-seven; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop five days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>',
    '<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-eight; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop four days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>')
rep('<tr><td class="tid">Today 10&ndash;2</td><td><b>The identification query first</b>',
    '<tr><td class="tid">Wed 11&ndash;3</td><td><b>The identification query first</b>')

# ---------- 10. FYI list ----------
rep('<li><b>Vipin Gupta messaged you in the Whova app overnight</b> (NetSapiens UGM 2026, 3:41 AM) &mdash; worth opening before the 9 AM UGM Planning hour.</li>',
    '''<li><b>Vipin Gupta has now sent you two unanswered Whova messages</b> (NetSapiens UGM 2026 app &mdash; Monday 3:41 AM, Tuesday 3:19 AM) &mdash; worth opening today.</li>
        <li><b>Gevity reported a vehicle hit the front of their building Monday evening</b> &mdash; no injuries, everyone safe per their note. Saturday&rsquo;s workshop is at Gevity; worth confirming the space is unaffected.</li>
        <li><b>Monday&rsquo;s UGM hour became a procurement sprint</b>: booth moved to Table 12 (Sue at Crexendo), the 2F-15 escalator graphic in negotiation ($800), tees quoted with Austin Print Co (Bella Canvas 3001, no powerbanks &mdash; budget), a 4imprint order placed (#32393405, art format settled), and ProGraphix&rsquo;s table cover + banner estimate in hand.</li>''')
rep('<li><b>Today 9&ndash;10 AM is UGM Planning with Jr</b> &mdash; you asked Friday evening, the assistants coordinated it, Jr confirmed. It sits between Product Sync and the Deep Work engineering block.</li>',
    '')
rep('before the period ends tomorrow, Oct 13.', 'and the period ends today, Oct 13.')

# ---------- 11. line health ----------
rep('eight failures on the day, and <b>the window closed with nothing after 6:57</b> &mdash; verified at 10:03 PM, trash included.',
    'eight failures on the day, and <b>the window closed with nothing after 6:57</b> &mdash; verified at 10:03 PM, trash included. Tuesday opened with a single failure at 7:01 AM &mdash; window open at 7:14.')

# ---------- 12. aging bumps ----------
rep('Ten days carried: <b>the Emilio recap (CC Jr)</b>, with the Affiliated pricing reply (day seven) beside it &mdash; Transition 2&ndash;3 is today&rsquo;s pocket',
    'Eleven days carried: <b>the Emilio recap (CC Jr)</b> &mdash; the Affiliated reply came off the board with Monday&rsquo;s ATS onboarding kickoff; Deep Work 10&ndash;2 is today&rsquo;s pocket')
rep('Day twenty-eight on Eric Bramini', 'Day twenty-nine on Eric Bramini')
rep('thirty-four full days ago', 'thirty-five full days ago')
rep('day thirty-three of billed Logs', 'day thirty-four of billed Logs')
rep('#799 is still sitting there, day thirty-six', '#799 is still sitting there, day thirty-seven')
rep('thirty-second day double-approved', 'thirty-third day double-approved')
rep('forty-two days past retirement', 'forty-three days past retirement')
rep('Retired Aug 31 &mdash; forty-two days past', 'Retired Aug 31 &mdash; forty-three days past')
rep('em-roadmap at 46 days', 'em-roadmap at 47 days')
rep('Promised Sep 15 &mdash; day twenty-seven', 'Promised Sep 15 &mdash; day twenty-eight')
rep('twenty-one days unsent', 'twenty-two days unsent')
rep('#799 (day thirty-six, double-approved)', '#799 (day thirty-seven, double-approved)')
rep('Behind those: <b>Eric &mdash; day thirty-five</b>, Nick&rsquo;s program-details reply on night twenty-eight',
    'Behind those: <b>Eric &mdash; day thirty-six</b>, Nick&rsquo;s program-details reply on night twenty-nine')
rep('now thirty days past due', 'now thirty-one days past due')
rep('58d &mdash; chronic', '59d &mdash; chronic')
rep('<span class="chip old">58d</span>', '<span class="chip old">59d</span>')
rep('<span class="chip old">55d</span>', '<span class="chip old">56d</span>')
rep('51d &mdash; stalled', '52d &mdash; stalled')
rep('66d &mdash; chronic', '67d &mdash; chronic')

# ---------- sanity ----------
assert src.count('__CC_STATE__') == 1
assert src.count('__CC_TEMPLATE__') == 1
assert src.count('data-react-task="') == 59
assert src.count('class="bar"') == 7
assert src.count('2026-10-13T07:14:00-05:00') == 2
assert src.count('day seven, answer agreed') == 0
assert src.count('five days out') == 0
assert src.count('slot past') == 0
open('page-template.html', 'w').write(src)
print('OK', len(src))
