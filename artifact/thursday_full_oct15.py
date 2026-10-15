import re
src = open('page-template.html').read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:90]}"
    src = src.replace(old, new)

# ---------- 1. stamps / greeting / eyebrow ----------
rep('2026-10-14T22:03:00-05:00', '2026-10-15T07:14:00-05:00', 2)
rep('<b>Brief compiled</b> Wed 7:14 AM &middot; data checked Wed 10:03 PM CT',
    '<b>Brief compiled</b> Thu 7:14 AM &middot; data checked Thu 7:14 AM CT')
rep('<div class="eyebrow">Wednesday, October 14 &middot; 2026</div>',
    '<div class="eyebrow">Thursday, October 15 &middot; 2026</div>')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- 2. masthead sub ----------
i = src.find('<p class="sub">Tuesday delivered:')
j = src.find('No reactions saved.</p>') + len('No reactions saved.</p>')
assert 0 < i < j
new_sub = ('<p class="sub">Wednesday delivered: <b>the 2F-15 plates are confirmed</b> &mdash; you told Sue yes on both '
  '($1,500 for the pair), FedEx sent the file specs (final PDF, no crop or bleed), and Jr has them for production, artwork '
  'by Oct 21. <b>Laura answered the export ask</b> &mdash; LeVarr&rsquo;s reports are in your inbox and she pulled one '
  '&ldquo;we can digest&rdquo; at <b>today&rsquo;s 11:00 training</b>. Eelco approved the transcript-storage opt-out hotfix '
  'in Linear yesterday morning. The miss: <b>ProGraphix &mdash; the submission was due yesterday</b> to hold 10/23, Cathy&rsquo;s '
  'follow-up is still unanswered, and your reply to her has sat in drafts since 9:08 yesterday morning &mdash; first thing in '
  'the 8:30 block. Today runs <b>7.5h</b>: Deep Work 8:30&ndash;12:30 holding <b>Iris Training 11&ndash;12</b> and the noon '
  'Grok Bot webinar, Reserved 1:30, Scott Van Camp at 2; open after 3. <b>Kayla&rsquo;s ATS form is due back this '
  'afternoon</b>. Still owed: <b>the Emilio recap, thirteen days</b>. The line: Wednesday closed at four failures, two '
  'needs-attention and one success &mdash; all after 6 PM &mdash; and Thursday opened clean, no overnight entries. '
  'No reactions saved.</p>')
src = src[:i] + new_sub + src[j:]

# ---------- 3. needs-a-decision note ----------
rep('<span class="note">The ProGraphix submission is due today; Sue&rsquo;s $1,500 2F-15 offer wants a yes/no; Laura&rsquo;s billing-reconciliation ask still needs its confirming reply; the Emilio recap is twelve days carried; Sentry renewed overnight after the period closed undecided</span>',
    '<span class="note">The ProGraphix submission is a day past due and the reply to Cathy is still in drafts; Kayla&rsquo;s ATS form is due back this afternoon; Laura&rsquo;s billing-reconciliation ask still needs its confirming reply &mdash; today&rsquo;s 11:00 training is the natural anchor; the Emilio recap is thirteen days carried</span>')

# ---------- 4. schedule card + todaynote ----------
rep('<span class="note" id="todaynote">Personal-heavy 8h &mdash; one engineering window 11:15&ndash;1:30; pockets 3&ndash;4 and after 5:30</span>',
    '<span class="note" id="todaynote">7.5h &mdash; Deep Work 8:30&ndash;12:30 with training at 11 and the webinar at noon; open after 3</span>')
pat = re.compile(r'(<div class="card sched" id="todaysched">\n).*?(\n      </div>\n    </section>)', re.DOTALL)
ms = pat.findall(src)
assert len(ms) == 1, len(ms)
new_slots = '''        <div class="slot"><div class="t">8:30 &ndash; 12:30</div><div class="w">Deep Work (Project Engineering)<small>8:30&ndash;11 is the clean stretch &mdash; ProGraphix submission first (a day past due), then #799</small></div></div>
        <div class="slot"><div class="t">11:00 &ndash; 12:00</div><div class="w">Iris Training<small>Teams &middot; Laura organizing &middot; her reports are in your inbox &mdash; inside Deep Work</small></div></div>
        <div class="slot"><div class="t">12:00 &ndash; 1:00</div><div class="w">Grok Bot + Cursor webinar<small>Luma &middot; overlaps Deep Work&rsquo;s last 30 minutes</small></div></div>
        <div class="slot"><div class="t">1:30 &ndash; 2:00</div><div class="w">Reserved</div></div>
        <div class="slot"><div class="t">2:00 &ndash; 3:00</div><div class="w">Call with Scott Van Camp</div></div>
        <div class="slot free"><div class="t">3:00 onward</div><div class="w">Open<small>the Emilio recap &middot; the Kayla ATS check &middot; Laura&rsquo;s confirming note if the training doesn&rsquo;t settle it</small></div></div>'''
src = pat.sub(lambda m: m.group(1) + new_slots + m.group(2), src, count=1)

# ---------- 5. Top 5 ----------
i = src.find('<ol class="prio">'); j = src.find('</ol>', i)
new_prio = '''<ol class="prio">
        <li><div>
          <h4>ProGraphix &mdash; the submission is now a day PAST DUE; your reply to Cathy is still in drafts</h4>
          <p class="why">Everything had to be submitted <b>by yesterday</b> to hold the 10/23 conference date for the table cover and banner. Cathy followed up Tuesday at 3:26 PM &mdash; still unanswered &mdash; and the reply you drafted yesterday at 9:08 AM never went out. Send it and submit first thing in the 8:30 block; if the date is at risk, her thread has the direct line.</p>
          <div class="meta"><span class="pill crit">A day past due</span><span class="pill warn">Draft unsent since yesterday</span></div>
        </div></li>
        <li><div>
          <h4>Iris Training 11&ndash;12 &mdash; Laura&rsquo;s reports arrived; land the billing confirmation live</h4>
          <p class="why">She answered your export ask at 4:54 yesterday: LeVarr&rsquo;s reports are attached and she pulled &ldquo;a great report that we can digest&rdquo; at today&rsquo;s session. Walk in with the onboarding-audit angle ready &mdash; and close the loop on her billing-reconciliation ask in the room, which retires the owed confirming reply.</p>
          <div class="meta"><span class="pill warn">Today 11&ndash;12</span><span class="pill quiet">Reports in inbox</span></div>
        </div></li>
        <li><div>
          <h4>The Emilio recap &mdash; thirteen days; still the carried send</h4>
          <p class="why">Thirteen days since the &ldquo;Smart City Partnership Next Steps&rdquo; call; the written recap (CC Jr) is what keeps the deal moving on Emilio&rsquo;s side. Today&rsquo;s pocket is after 3.</p>
          <div class="meta"><span class="pill crit">Thirteen days</span><span class="pill quiet">After 3</span></div>
        </div></li>
        <li><div>
          <h4>2F-15 artwork &mdash; confirmed yesterday; FedEx specs in hand, due Oct 21</h4>
          <p class="why">You told Sue yes on both plates ($1,500 for the pair &mdash; bottom landing going up 2&rarr;3, top landing coming down), Michael at FedEx sent the file instructions (final PDF, no crop or bleed), and you forwarded them to Jr last night. Six days to produce against the Oct 21 deadline &mdash; agree with Jr today on who builds the files.</p>
          <div class="meta"><span class="pill warn">Artwork due Oct 21</span><span class="pill quiet">Jr has the specs</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day thirty-nine &mdash; the clean stretch is 8:30&ndash;11, after ProGraphix</h4>
          <p class="why">Double-approved and unmerged. Today&rsquo;s Deep Work block loses its back half to Iris Training and the noon webinar, so <b>8:30&ndash;11 is the week&rsquo;s remaining clean engineering stretch</b> &mdash; whatever the ProGraphix submission leaves of it goes here.</p>
          <div class="meta"><span class="pill warn">Review waiting</span><span class="pill quiet">Today 8:30&ndash;11</span></div>
        </div></li>
      </ol>'''
src = src[:i] + new_prio + src[j+len('</ol>'):]

# ---------- 6. coming-up cards ----------
i = src.find('<h4 style="font-size:14px">Iris, day three &mdash; training tomorrow at 11, billing workstream pending</h4>')
j = src.find('</p>', src.find('direct tagging.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Iris, day four &mdash; training TODAY at 11; Laura&rsquo;s reports are in</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Laura replied at 4:54 yesterday with <b>LeVarr&rsquo;s reports attached</b> (your export ask, answered) and &ldquo;a great report that we can digest&rdquo; at today&rsquo;s 11&ndash;12 session. The billing-reconciliation workstream she asked to fold into the three-month contract <b>still needs your confirming word &mdash; land it live at the training</b>. The series recurs Tuesdays 1&ndash;2 (Oct 20 is on the calendar). The Oct 6 update draft is on day nine in drafts &mdash; repurpose or clear it. lmccree is in the Voxtell Linear workspace for direct tagging.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">Today 8&ndash;5:30 &mdash; personal-heavy, one engineering window</h4>')
j = src.find('</p>', src.find('(Emilio, Sue, Laura).', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Today 8:30&ndash;3 &mdash; one block, three meetings, then open</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Deep Work 8:30&ndash;12:30 is the frame, but its back half belongs to <b>Iris Training 11&ndash;12</b> and the <b>noon webinar</b> &mdash; so <b>8:30&ndash;11 is the real engineering stretch</b>: the ProGraphix submission first (a day past due), #799 with what remains. Reserved 1:30 and Scott Van Camp 2&ndash;3 close the booked day; after 3 carries the sends &mdash; the Emilio recap, the Kayla ATS check, Laura&rsquo;s note if the training leaves it open.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
j = src.find('</p>', src.find('recurring 1&ndash;2 inside the admin block.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Friday Oct 16 is empty</b> &mdash; the last big pocket before the weekend: the three job descriptions (day thirty) that gate the landing page, and the ATS follow-through once Kayla&rsquo;s form lands. <b>Saturday Oct 17 is the workshop, two days out</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), Luma page live. Next week: Monday 5.75h, Tuesday 6.5h with Iris Training 1&ndash;2, and <b>Wednesday Oct 21 runs 6.5h against the 2F-15 artwork deadline</b>.</p>''' + src[j:]

# ---------- 7. chart ----------
i = src.find('<div class="plot" id="plot">'); j = src.find('</div>\n        <div class="xaxis"', i)
new_plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
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
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
        '''
src = src[:i] + new_plot + src[j:]
rep('''<div class="xaxis" id="xaxis">
          <div><b>Wed</b>14</div><div><b>Thu</b>15</div>
          <div><b>Fri</b>16</div><div><b>Sat</b>17</div><div><b>Sun</b>18</div><div><b>Mon</b>19</div><div><b>Tue</b>20</div>
        </div>''',
'''<div class="xaxis" id="xaxis">
          <div><b>Thu</b>15</div><div><b>Fri</b>16</div>
          <div><b>Sat</b>17</div><div><b>Sun</b>18</div><div><b>Mon</b>19</div><div><b>Tue</b>20</div><div><b>Wed</b>21</div>
        </div>''')
rep('Wed Oct 14 &ndash; Tue Oct 20', 'Thu Oct 15 &ndash; Wed Oct 21')

# ---------- 8. week flags ----------
i = src.find('<h3><span class="pill warn">Today</span> Wednesday runs 8h, mostly personal')
j = src.find('</p>', src.find('the confirming note to Laura.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">Today</span> Thursday runs 7.5h &mdash; 8:30&ndash;11 is the day&rsquo;s one clean stretch</h3>
          <p>Deep Work (Project Engineering) 8:30&ndash;12:30 holds <b>Iris Training 11&ndash;12</b> and the <b>Grok Bot + Cursor webinar 12&ndash;1</b> in its back half, so <b>8:30&ndash;11 is the only clean engineering window</b>: the ProGraphix submission first &mdash; <b>it was due yesterday</b>, Cathy&rsquo;s follow-up is unanswered and your reply has sat in drafts since 9:08 yesterday morning &mdash; then #799. Reserved 1:30 and Scott Van Camp 2&ndash;3 take the early afternoon; after 3 is open for the sends &mdash; the Emilio recap (thirteen days), the <b>Kayla ATS check (her form is due back this afternoon)</b>, and Laura&rsquo;s confirming note if the training doesn&rsquo;t settle it live.</p>''' + src[j:]

i = src.find('<h3><span class="pill warn">This week</span> Thursday carries Iris Training')
j = src.find('Iris Training recurring 1&ndash;2.</p>') + len('Iris Training recurring 1&ndash;2.</p>')
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">This week</span> Friday stays the valve; the workshop is two days out with 2F-15 artwork behind it</h3>
          <p><b>Friday Oct 16 is empty</b> &mdash; the last big pocket before the weekend: the three job descriptions (day thirty) that gate the landing page, and the ATS follow-through once Kayla&rsquo;s form lands. <b>Saturday Oct 17 carries the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), two days out, its Luma page live. Next week opens gentle: Monday 5.75h, Tuesday 6.5h with Iris Training 1&ndash;2 &mdash; and <b>Wednesday Oct 21 runs 6.5h against the 2F-15 artwork deadline</b>, FedEx&rsquo;s specs already in Jr&rsquo;s hands.</p>''' + src[j:]

# ---------- 9. already-have-a-home table ----------
rep('<tr><td class="tid">Today 3&ndash;4 + eve</td><td><b>The Emilio recap</b> (twelve days), <b>the reply to Sue&rsquo;s $1,500 2F-15 offer</b> and <b>the confirming note to Laura</b> on the billing workstream<div class="src">Eric&rsquo;s reply (day thirty-seven) and the send backlog (thirty-two days past on billing/RevIO &middot; Nick night thirty) queue behind them</div></td></tr>',
    '<tr><td class="tid">Today after 3</td><td><b>The Emilio recap</b> (thirteen days), <b>the Kayla ATS check</b> (form due back this afternoon) and <b>the confirming note to Laura</b> if the 11:00 training doesn&rsquo;t settle it<div class="src">Eric&rsquo;s reply (day thirty-eight) and the send backlog (thirty-three days past on billing/RevIO &middot; Nick night thirty-one) queue behind them</div></td></tr>')
rep('<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day twenty-nine; the promo blast is public and the workshop&rsquo;s Luma page is live while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop three days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>',
    '<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day thirty; the promo blast is public and the workshop&rsquo;s Luma page is live while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop two days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>')
rep('<tr><td class="tid">Today 11:15&ndash;1:30</td>', '<tr><td class="tid">Today 8:30&ndash;11</td>')

# ---------- 10. FYI list ----------
rep('<li><b>Vipin Gupta has two unanswered Whova messages waiting</b> (Monday 3:41 AM, Tuesday 3:19 AM) &mdash; and <b>Carlos Bustamante invited you as Voxtell AI booth staff</b> in Whova yesterday; accepting enables lead capture at UGM.</li>',
    '<li><b>Vipin Gupta has two unanswered Whova messages waiting</b> (Monday 3:41 AM, Tuesday 3:19 AM), <b>Carlos Bustamante&rsquo;s booth-staff invite is still open</b> (accepting enables lead capture) &mdash; and <b>Sue Giansiracusa sent UGM sponsor shipping &amp; FedEx deadlines marked action-required</b> yesterday; Jr forwarded it to you.</li>')
rep('You also registered for Thursday&rsquo;s noon <b>Grok Bot + Cursor webinar</b>, which sits inside the engineering block.</li>',
    'Today&rsquo;s noon <b>Grok Bot + Cursor webinar</b> sits inside the Deep Work block&rsquo;s last half hour.</li>')
rep('<li><b>Crexendo&rsquo;s billing paperwork is settled</b> &mdash; Jr sent the accounting info and Racquel confirmed yesterday morning.</li>',
    '''<li><b>Crexendo&rsquo;s billing is fully live</b> &mdash; the Bill Center activated yesterday and the first invoice (21543) landed; Jr forwarded both. And <b>LiveKit&rsquo;s Ben Cherry reached out directly</b> &mdash; Jr replied copying you and Eelco; the stalled Sep 21 support draft finally has a human channel.</li>
        <li><b>Retreat planning advanced</b> &mdash; Ember Oak (Wimberley) walked the venue and three packages yesterday; Shandi is confirming funding with Connor, and the workshop breakdown and proposal deck are coming to you for review.</li>''')

# ---------- 11. line health ----------
rep('four failures, two needs-attention and one success on the day, and <b>the window closed with nothing after 8:52</b> &mdash; verified at 10:03 PM, trash included.',
    'four failures, two needs-attention and one success on the day, and <b>the window closed with nothing after 8:52</b> &mdash; verified at 10:03 PM, trash included. The overnight into Thursday stayed quiet &mdash; <b>Thursday opened clean</b>, no overnight entries, the morning Daily Digests on schedule at 7:00.')

# ---------- 12. aging bumps ----------
rep('#799 is still sitting there, day thirty-eight', '#799 is still sitting there, day thirty-nine')
rep('thirty-fourth day double-approved', 'thirty-fifth day double-approved')
rep('#799 (day thirty-eight, double-approved)', '#799 (day thirty-nine, double-approved)')
rep('Day thirty on Eric Bramini', 'Day thirty-one on Eric Bramini')
rep('thirty-six full days ago', 'thirty-seven full days ago')
rep('day thirty-five of billed Logs &mdash; and the plan renewed overnight at $129', 'day thirty-six of billed Logs &mdash; the plan renewed Tuesday night at $129')
rep('Promised Sep 15 &mdash; day twenty-nine', 'Promised Sep 15 &mdash; day thirty')
rep('twenty-three days unsent', 'twenty-four days unsent')
rep('forty-four days past retirement', 'forty-five days past retirement')
rep('Retired Aug 31 &mdash; forty-four days past', 'Retired Aug 31 &mdash; forty-five days past')
rep('em-roadmap at 48 days', 'em-roadmap at 49 days')
rep('now thirty-two days past due', 'now thirty-three days past due')
rep('Behind those: <b>Eric &mdash; day thirty-seven</b>, Nick&rsquo;s program-details reply on night thirty',
    'Behind those: <b>Eric &mdash; day thirty-eight</b>, Nick&rsquo;s program-details reply on night thirty-one')
rep('60d &mdash; chronic', '61d &mdash; chronic')
rep('<span class="chip old">60d</span>', '<span class="chip old">61d</span>')
rep('<span class="chip old">57d</span>', '<span class="chip old">58d</span>')
rep('53d &mdash; stalled', '54d &mdash; stalled')
rep('68d &mdash; chronic', '69d &mdash; chronic')

# ---------- sanity ----------
assert src.count('__CC_STATE__') == 1
assert src.count('__CC_TEMPLATE__') == 1
assert src.count('data-react-task="') == 59
assert src.count('class="bar"') == 7
assert src.count('2026-10-15T07:14:00-05:00') == 2
assert src.count('twelve days') == 0
assert src.count('11:15') == 0
assert src.count('training tomorrow') == 0
assert src.count('three days out') == 0
assert src.count('Sustainable Ambition 9:30') == 0
open('page-template.html', 'w').write(src)
print('OK', len(src))
