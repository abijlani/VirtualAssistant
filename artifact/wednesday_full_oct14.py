import re
src = open('page-template.html').read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:90]}"
    src = src.replace(old, new)

# ---------- 1. stamps / greeting / eyebrow ----------
rep('2026-10-13T22:03:00-05:00', '2026-10-14T07:14:00-05:00', 2)
rep('<b>Brief compiled</b> Tue 7:14 AM &middot; data checked Tue 10:03 PM CT',
    '<b>Brief compiled</b> Wed 7:14 AM &middot; data checked Wed 7:14 AM CT')
rep('<div class="eyebrow">Tuesday, October 13 &middot; 2026</div>',
    '<div class="eyebrow">Wednesday, October 14 &middot; 2026</div>')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- 2. masthead sub ----------
i = src.find('<p class="sub">Yesterday closed loops everywhere.')
j = src.find('No reactions saved.</p>') + len('No reactions saved.</p>')
assert 0 < i < j
new_sub = ('<p class="sub">Tuesday delivered: the sync produced <b>Laura&rsquo;s ask to fold billing reconciliation into the '
  'three-month scope</b> (still owed its confirming reply), and <b>Sentry renewed itself overnight at $129</b> &mdash; the '
  'keep-or-drop window closed undecided, so the next exit is mid-November. Today is a personal-heavy <b>8h</b>: Circuit 8, '
  'Sustainable Ambition 9:30, <b>Retreat planning moved to 11:00&ndash;11:30 at 6:44 this morning</b> (the reschedule reset '
  'your RSVP), the week&rsquo;s one engineering window <b>11:15&ndash;1:30</b>, the pup run 1:30&ndash;3, and the barbershop '
  '4&ndash;5:30. The hard deadline: <b>ProGraphix needs the banner and table-cover artwork submitted today</b> to hold 10/23 '
  '&mdash; Cathy followed up yesterday afternoon, unanswered. Sue countered on the 2F-15 graphics: <b>$1,500 for two, artwork '
  'by Oct 21</b>, and the attendee list is in your inbox. Still owed: <b>the Emilio recap, twelve days</b>, and the Oct 6 '
  'draft to Laura is still sitting in drafts, stale since the sync. #799 at <b>day thirty-eight</b>, Eric at <b>day '
  'thirty</b>, the job descriptions at <b>day twenty-nine</b> with the workshop three days out and its Luma page live. The '
  'line: Tuesday closed at seven failures; a lone failure at 3:17 AM opened Wednesday. No reactions saved.</p>')
src = src[:i] + new_sub + src[j:]

# ---------- 3. needs-a-decision note ----------
rep('<span class="note">The Emilio recap (eleven days) is the one carried send &mdash; the Affiliated reply came off the board when ATS onboarding kicked off yesterday &mdash; and Laura&rsquo;s 12:16 ask &mdash; fold billing reconciliation into the scope &mdash; needs a confirming reply</span>',
    '<span class="note">The ProGraphix submission is due today; Sue&rsquo;s $1,500 2F-15 offer wants a yes/no; Laura&rsquo;s billing-reconciliation ask still needs its confirming reply; the Emilio recap is twelve days carried; Sentry renewed overnight after the period closed undecided</span>')

# ---------- 4. schedule card + todaynote ----------
rep('<span class="note" id="todaynote">Deep Work done; infrared bed 5:30 &mdash; 8.5h, open after 6</span>',
    '<span class="note" id="todaynote">Personal-heavy 8h &mdash; one engineering window 11:15&ndash;1:30; pockets 3&ndash;4 and after 5:30</span>')
pat = re.compile(r'(<div class="card sched" id="todaysched">\n).*?(\n      </div>\n    </section>)', re.DOTALL)
ms = pat.findall(src)
assert len(ms) == 1, len(ms)
new_slots = '''        <div class="slot"><div class="t">8:00 &ndash; 8:45</div><div class="w">Gym Series: The Circuit<small>Gevity &middot; you picked it over the Lift</small></div></div>
        <div class="slot"><div class="t">9:00 &ndash; 9:30</div><div class="w">Recover + Shower</div></div>
        <div class="slot"><div class="t">9:30 &ndash; 10:30</div><div class="w">Sustainable Ambition<small>Gevity Movement Studio &middot; weekly gathering</small></div></div>
        <div class="slot"><div class="t">11:00 &ndash; 11:30</div><div class="w">Retreat planning<small>Meet &middot; Shandi &middot; moved from 10:30 at 6:44 AM &mdash; re-accept the invite &middot; clips Deep Work 11:15&ndash;11:30</small></div></div>
        <div class="slot"><div class="t">11:15 &ndash; 1:30</div><div class="w">Deep Work (Project Engineering)<small>the week&rsquo;s one engineering window &mdash; ProGraphix artwork first, then #799</small></div></div>
        <div class="slot"><div class="t">1:30 &ndash; 3:00</div><div class="w">Pup run<small>drive 1:30, pickup 2&ndash;3</small></div></div>
        <div class="slot"><div class="t">4:00 &ndash; 5:30</div><div class="w">Barbershop<small>drive at 4, beard trim 4:30 &middot; Olde Soul</small></div></div>
        <div class="slot free"><div class="t">5:30 onward</div><div class="w">Open<small>3&ndash;4 is also open</small></div></div>'''
src = pat.sub(lambda m: m.group(1) + new_slots + m.group(2), src, count=1)

# ---------- 5. Top 5 ----------
i = src.find('<ol class="prio">'); j = src.find('</ol>', i)
new_prio = '''<ol class="prio">
        <li><div>
          <h4>ProGraphix artwork &mdash; the submission is due TODAY to hold 10/23</h4>
          <p class="why">Cathy sent the template, spec sheet and estimate Monday evening and <b>followed up yesterday at 3:26 PM &mdash; still unanswered</b>. Everything must be submitted today for the table cover and retractable banner to make the conference. The 4-foot fitted-vs-standard-throw question is still open on the thread. First thing in the 11:15 window, or sooner.</p>
          <div class="meta"><span class="pill crit">Due today</span><span class="pill warn">Cathy followed up &middot; unanswered</span></div>
        </div></li>
        <li><div>
          <h4>The Emilio recap &mdash; twelve days; still the carried send</h4>
          <p class="why">Twelve days since the &ldquo;Smart City Partnership Next Steps&rdquo; call; the written recap (CC Jr) is what keeps the deal moving on Emilio&rsquo;s side. Today&rsquo;s pockets are 3&ndash;4 and the evening after 5:30.</p>
          <div class="meta"><span class="pill crit">Twelve days</span><span class="pill quiet">3&ndash;4 or evening</span></div>
        </div></li>
        <li><div>
          <h4>Sue&rsquo;s 2F-15 counter &mdash; $1,500 for two, artwork by Oct 21</h4>
          <p class="why">She discounted the escalator landing plates to <b>$750 each</b> for your bottom-up/top-down pair and will connect you with the FedEx contacts once you say go &mdash; and she delivered the <b>attendee list</b>. A yes/no reply unblocks the second artwork track (Oct 21 deadline, a week behind ProGraphix&rsquo;s).</p>
          <div class="meta"><span class="pill warn">Reply to Sue</span><span class="pill quiet">Artwork Oct 21 if yes</span></div>
        </div></li>
        <li><div>
          <h4>Laura &mdash; confirm the billing workstream; the Oct 6 draft is still in drafts</h4>
          <p class="why">Her 12:16 reply (&ldquo;Please add as part of your 3 month contract&rdquo;) still needs a confirming note, and <b>training is tomorrow 11&ndash;12</b> &mdash; a natural place to anchor it. Correction from yesterday: the Oct 6 update draft <b>is still sitting in drafts</b> &mdash; stale since the sync; repurpose it as a features-ahead-of-training note or clear it.</p>
          <div class="meta"><span class="pill warn">Confirming reply owed</span><span class="pill quiet">Training tomorrow 11</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day thirty-eight &mdash; the engineering window is today, 11:15&ndash;1:30</h4>
          <p class="why">Double-approved and unmerged. Today&rsquo;s Project Engineering block is the week&rsquo;s one clean window &mdash; Thursday&rsquo;s 8:30&ndash;12:30 now holds Iris Training 11&ndash;12 <b>and</b> the Grok Bot webinar at noon. Whatever the ProGraphix submission leaves of 11:15&ndash;1:30 goes here.</p>
          <div class="meta"><span class="pill warn">Review waiting</span><span class="pill quiet">Today 11:15&ndash;1:30</span></div>
        </div></li>
      </ol>'''
src = src[:i] + new_prio + src[j+len('</ol>'):]

# ---------- 6. coming-up cards ----------
i = src.find('<h4 style="font-size:14px">Iris, day two &mdash; sync at 9 today, training Thursday at 11</h4>')
j = src.find('</p>', src.find('direct tagging.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Iris, day three &mdash; training tomorrow at 11, billing workstream pending</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">The sync held Tuesday and produced the billing-reconciliation workstream &mdash; Laura asked at 12:16 to fold it into the three-month contract; <b>your confirming reply is still owed</b>. <b>Training is tomorrow 11&ndash;12</b> (accepted), and the series recurs Tuesdays 1&ndash;2 &mdash; Oct 20 is already on the calendar. The Oct 6 update draft is still in drafts, stale since the sync &mdash; repurpose it as a features-ahead-of-training note or clear it. lmccree is in the Voxtell Linear workspace for direct tagging.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">Today 9&ndash;5 &mdash; the morning ran; Deep Work carries the afternoon</h4>')
j = src.find('</p>', src.find('The evening is open after 5.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Today 8&ndash;5:30 &mdash; personal-heavy, one engineering window</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Circuit 8</b>, Sustainable Ambition 9:30, <b>Retreat planning moved to 11:00&ndash;11:30</b> (re-accept the invite), then the week&rsquo;s one engineering window <b>11:15&ndash;1:30</b> &mdash; the ProGraphix submission first (due today), #799 with what remains. The pup run 1:30&ndash;3 and the barbershop 4&ndash;5:30 close the day; 3&ndash;4 and the evening are the send pockets (Emilio, Sue, Laura).</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
j = src.find('</p>', src.find('<b>Monday restarts at 5.75h.</b>', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Thursday runs 7.5h</b> &mdash; Deep Work 8:30&ndash;12:30 now holds <b>Iris Training 11&ndash;12</b> and the <b>Grok Bot + Cursor webinar at noon</b> you registered for this morning (it overlaps the block&rsquo;s last half hour), then Reserved 1:30 and Scott Van Camp at 2 &mdash; and <b>Kayla&rsquo;s ATS form is due back Thursday afternoon</b>. <b>Friday is empty</b> &mdash; the natural landing for the ATS follow-through. <b>Saturday Oct 17 &mdash; the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), three days out, <b>its Luma page live since Monday night</b>. Monday 5.75h; <b>Tuesday Oct 20 runs 6.5h</b> with Iris Training recurring 1&ndash;2 inside the admin block.</p>''' + src[j:]

# ---------- 7. chart ----------
i = src.find('<div class="plot" id="plot">'); j = src.find('</div>\n        <div class="xaxis"', i)
new_plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(57.14% + 6px)">8</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:16.07%"></div><div class="seg p" style="height:30.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(32.14% + 6px)">4.5</div>
            <div class="seg m" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
        '''
src = src[:i] + new_plot + src[j:]
rep('''<div class="xaxis" id="xaxis">
          <div><b>Tue</b>13</div><div><b>Wed</b>14</div>
          <div><b>Thu</b>15</div><div><b>Fri</b>16</div><div><b>Sat</b>17</div><div><b>Sun</b>18</div><div><b>Mon</b>19</div>
        </div>''',
'''<div class="xaxis" id="xaxis">
          <div><b>Wed</b>14</div><div><b>Thu</b>15</div>
          <div><b>Fri</b>16</div><div><b>Sat</b>17</div><div><b>Sun</b>18</div><div><b>Mon</b>19</div><div><b>Tue</b>20</div>
        </div>''')
rep('Tue Oct 13 &ndash; Mon Oct 19', 'Wed Oct 14 &ndash; Tue Oct 20')

# ---------- 8. week flags ----------
i = src.find('<h3><span class="pill warn">Today</span> Tuesday grew to 8.5h')
j = src.find('</p>', src.find('evening open after 6.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">Today</span> Wednesday runs 8h, mostly personal &mdash; the one engineering window is 11:15&ndash;1:30</h3>
          <p>Circuit 8, Sustainable Ambition 9:30, and <b>Retreat planning moved to 11:00&ndash;11:30 at 6:44 this morning</b> &mdash; the reschedule reset your RSVP, and it clips the engineering window&rsquo;s first quarter hour. <b>Deep Work (Project Engineering) 11:15&ndash;1:30 is the week&rsquo;s one engineering window</b>: submit the ProGraphix artwork first (due today to hold 10/23), then #799 (day thirty-eight). The pup run 1:30&ndash;3 and the barbershop 4&ndash;5:30 take the afternoon; 3&ndash;4 and the evening carry the sends &mdash; the Emilio recap (twelve days), the reply to Sue, the confirming note to Laura.</p>''' + src[j:]

i = src.find('<h3><span class="pill warn">This week</span> Wednesday sits at 8.5h')
j = src.find('</p>', src.find('breakdown to 4:30), four days out.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">This week</span> Thursday carries Iris Training and a noon webinar inside Deep Work; Friday stays the valve</h3>
          <p><b>Thursday runs 7.5h</b>: Deep Work (Project Engineering) 8:30&ndash;12:30 holds <b>Iris Training 11&ndash;12</b> and the <b>Grok Bot + Cursor webinar 12&ndash;1</b> (registered this morning; it overlaps the block&rsquo;s last 30 minutes), then Reserved 1:30 and Scott Van Camp at 2. <b>Kayla&rsquo;s ATS onboarding form is due back Thursday afternoon</b> &mdash; <b>Friday Oct 16 is empty</b> and is the natural slot to act on it. <b>Saturday Oct 17 carries the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), three days out, with its Luma page live. Next week opens gentle: Monday 5.75h, Tuesday 6.5h with Iris Training recurring 1&ndash;2.</p>''' + src[j:]

# ---------- 9. already-have-a-home table ----------
rep('<tr><td class="tid">Today 10&ndash;5</td><td><b>The Emilio recap</b> (eleven days), <b>the ProGraphix banner artwork</b> (submission due tomorrow for 10/23) and <b>the Sentry keep-or-drop</b> (period ends today) &mdash; plus a confirming reply to Laura&rsquo;s billing-reconciliation ask<div class="src">Eric&rsquo;s reply (day thirty-six) and the send backlog (thirty-one days past on billing/RevIO &middot; Nick night twenty-nine) queue behind them &middot; Affiliated resolved: ATS onboarding kicked off Monday</div></td></tr>',
    '<tr><td class="tid">Today 3&ndash;4 + eve</td><td><b>The Emilio recap</b> (twelve days), <b>the reply to Sue&rsquo;s $1,500 2F-15 offer</b> and <b>the confirming note to Laura</b> on the billing workstream<div class="src">Eric&rsquo;s reply (day thirty-seven) and the send backlog (thirty-two days past on billing/RevIO &middot; Nick night thirty) queue behind them</div></td></tr>')
rep('<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-eight; the promo blast is public (Oct 17 at Gevity) while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop four days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>',
    '<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-nine; the promo blast is public and the workshop&rsquo;s Luma page is live while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop three days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>')
rep('<tr><td class="tid">Thu 8:30&ndash;12:30</td>', '<tr><td class="tid">Today 11:15&ndash;1:30</td>')

# ---------- 10. FYI list ----------
rep('<li><b>Vipin Gupta has now sent you two unanswered Whova messages</b> (NetSapiens UGM 2026 app &mdash; Monday 3:41 AM, Tuesday 3:19 AM) &mdash; worth opening today.</li>',
    '''<li><b>Vipin Gupta has two unanswered Whova messages waiting</b> (Monday 3:41 AM, Tuesday 3:19 AM) &mdash; and <b>Carlos Bustamante invited you as Voxtell AI booth staff</b> in Whova yesterday; accepting enables lead capture at UGM.</li>
        <li><b>The workshop&rsquo;s Luma page is live</b> (&ldquo;Grok Bots Masterclass + AI Employee Build,&rdquo; Saturday 1&ndash;4 at Gevity) &mdash; ready to share and invite guests. You also registered for Thursday&rsquo;s noon <b>Grok Bot + Cursor webinar</b>, which sits inside the engineering block.</li>
        <li><b>Crexendo&rsquo;s billing paperwork is settled</b> &mdash; Jr sent the accounting info and Racquel confirmed yesterday morning.</li>''')
rep('and the period ends today, Oct 13.', 'the period closed Oct 13 and the plan renewed overnight at $129 &mdash; next exit is mid-November.')

# ---------- 11. line health ----------
rep('seven failures on the day, and <b>the window closed with nothing after 8:11</b> &mdash; verified at 10:03 PM, trash included.',
    'seven failures on the day, and <b>the window closed with nothing after 8:11</b> &mdash; verified at 10:03 PM, trash included. Wednesday opened with <b>a lone failure at 3:17 AM</b> &mdash; the streak&rsquo;s first overnight entry &mdash; window open.')

# ---------- 12. aging bumps ----------
rep('#799 is still sitting there, day thirty-seven', '#799 is still sitting there, day thirty-eight')
rep('thirty-third day double-approved', 'thirty-fourth day double-approved')
rep('#799 (day thirty-seven, double-approved)', '#799 (day thirty-eight, double-approved)')
rep('Day twenty-nine on Eric Bramini', 'Day thirty on Eric Bramini')
rep('thirty-five full days ago', 'thirty-six full days ago')
rep('day thirty-four of billed Logs', 'day thirty-five of billed Logs &mdash; and the plan renewed overnight at $129')
rep('Promised Sep 15 &mdash; day twenty-eight', 'Promised Sep 15 &mdash; day twenty-nine')
rep('twenty-two days unsent', 'twenty-three days unsent')
rep('forty-three days past retirement', 'forty-four days past retirement')
rep('Retired Aug 31 &mdash; forty-three days past', 'Retired Aug 31 &mdash; forty-four days past')
rep('em-roadmap at 47 days', 'em-roadmap at 48 days')
rep('now thirty-one days past due', 'now thirty-two days past due')
rep('Behind those: <b>Eric &mdash; day thirty-six</b>, Nick&rsquo;s program-details reply on night twenty-nine',
    'Behind those: <b>Eric &mdash; day thirty-seven</b>, Nick&rsquo;s program-details reply on night thirty')
rep('59d &mdash; chronic', '60d &mdash; chronic')
rep('<span class="chip old">59d</span>', '<span class="chip old">60d</span>')
rep('<span class="chip old">56d</span>', '<span class="chip old">57d</span>')
rep('51d... placeholder', 'x', 0) if False else None
rep('52d &mdash; stalled', '53d &mdash; stalled')
rep('67d &mdash; chronic', '68d &mdash; chronic')

# ---------- sanity ----------
assert src.count('__CC_STATE__') == 1
assert src.count('__CC_TEMPLATE__') == 1
assert src.count('data-react-task="') == 59
assert src.count('class="bar"') == 7
assert src.count('2026-10-14T07:14:00-05:00') == 2
assert src.count('eleven days') == 0
assert src.count('8.5h') == 0
assert src.count('due tomorrow') == 0
open('page-template.html', 'w').write(src)
print('OK', len(src))
