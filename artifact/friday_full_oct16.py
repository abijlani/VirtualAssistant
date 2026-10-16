import re
src = open('page-template.html').read()

def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, f"count {c} != {n} for: {old[:90]}"
    src = src.replace(old, new)

# ---------- 1. stamps / greeting / eyebrow ----------
rep('2026-10-15T22:03:00-05:00', '2026-10-16T07:21:00-05:00', 2)
rep('<b>Brief compiled</b> Thu 7:14 AM &middot; data checked Thu 10:03 PM CT',
    '<b>Brief compiled</b> Fri 7:21 AM &middot; data checked Fri 7:21 AM CT')
rep('<div class="eyebrow">Thursday, October 15 &middot; 2026</div>',
    '<div class="eyebrow">Friday, October 16 &middot; 2026</div>')
rep('<h1>Good afternoon, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- 2. masthead sub ----------
i = src.find('<p class="sub">Wednesday delivered:')
j = src.find('No reactions saved.</p>') + len('No reactions saved.</p>')
assert 0 < i < j
new_sub = ('<p class="sub">Thursday delivered: <b>Kayla&rsquo;s ATS questionnaire came back submitted</b> (Jr picked up the '
  'next steps), the Iris training ran and <b>Laura&rsquo;s all-time funnel report is in hand</b> &mdash; you turned it into a '
  '<b>10&ndash;11 review block today</b> with five actions (decide the official counts, recap + re-request the per-account '
  'export, log the Waco Family Medicine cancellation, prep Monday&rsquo;s 62-account billing reconciliation, watch the $5,000 '
  'invoice due Oct 29) &mdash; and <b>Smart City said yes-but-binding</b> on the continuity letter, so the redline ask is with '
  'Jake and Matt, Christine added. The miss: <b>ProGraphix &mdash; the reply you drafted was deleted unsent</b>; the submission '
  'is two days past the date Cathy named for 10/23 and her follow-up is still unanswered. Today is the valve: one booked hour, '
  'open otherwise, with <b>the workshop TOMORROW</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30). New: a review '
  'request on <b>PR #992</b>, a <b>$1,086.29 past-due first notice</b>, and Vipin&rsquo;s third Whova message. The line: '
  'Thursday closed at <b>eight failures</b> &mdash; a 6:01&ndash;6:47 burst plus a late 9:25 &mdash; the heaviest day since '
  'Sunday; Friday opened clean. No reactions saved.</p>')
src = src[:i] + new_sub + src[j:]

# ---------- 3. needs-a-decision note ----------
rep('<span class="note">The ProGraphix submission is a day past due and the reply to Cathy is still in drafts; Kayla&rsquo;s ATS form is due back this afternoon; Laura&rsquo;s billing-reconciliation ask still needs its confirming reply &mdash; today&rsquo;s 11:00 training is the natural anchor; the Emilio recap is thirteen days carried</span>',
    '<span class="note">ProGraphix is two days past its submit-by date and the drafted reply was deleted unsent &mdash; submit, call Cathy, or let 10/23 slip; a <b>$1,086.29 past-due first notice</b> wants payment or a dispute; the Emilio recap is fourteen days carried while the binding-agreement redline sits with Jake and Matt; PR #992 waits on your review</span>')

# ---------- 4. schedule card + todaynote ----------
rep('<span class="note" id="todaynote">7.5h &mdash; Deep Work 8:30&ndash;12:30 with training at 11 and the webinar at noon; open after 3</span>',
    '<span class="note" id="todaynote">1h booked &mdash; the Iris audit block 10&ndash;11; the valve day before tomorrow&rsquo;s workshop</span>')
pat = re.compile(r'(<div class="card sched" id="todaysched">\n).*?(\n      </div>\n    </section>)', re.DOTALL)
ms = pat.findall(src)
assert len(ms) == 1, len(ms)
new_slots = '''        <div class="slot"><div class="t">10:00 &ndash; 11:00</div><div class="w">SpectrumVoIP: review Iris audit action items<small>your block &middot; funnel counts (324 vs 350 vs ~180) &middot; recap + export re-request to Laura &middot; Waco churn entry &middot; Monday&rsquo;s 62-account reconciliation &middot; $5,000 invoice watch</small></div></div>
        <div class="slot free"><div class="t">Otherwise open</div><div class="w">The valve<small>ProGraphix decision first &middot; workshop prep &middot; the job descriptions &middot; the Emilio/Smart City chase</small></div></div>'''
src = pat.sub(lambda m: m.group(1) + new_slots + m.group(2), src, count=1)

# ---------- 5. Top 5 ----------
i = src.find('<ol class="prio">'); j = src.find('</ol>', i)
new_prio = '''<ol class="prio">
        <li><div>
          <h4>ProGraphix &mdash; two days past the submit-by date, and the drafted reply was DELETED unsent</h4>
          <p class="why">Cathy needed everything by Wednesday to hold 10/23 for the table cover and banner; her Tuesday follow-up is still unanswered, and the reply drafted Wednesday morning is no longer in drafts &mdash; nothing was sent on the thread. Decide this morning: submit and reply, call her directly, or accept that the conference date slips.</p>
          <div class="meta"><span class="pill crit">Two days past due</span><span class="pill warn">Draft deleted &middot; thread silent</span></div>
        </div></li>
        <li><div>
          <h4>The Iris audit block, 10&ndash;11 &mdash; your own five-point agenda</h4>
          <p class="why">Laura&rsquo;s all-time funnel report (new vs. upsold, per Jake) is in hand. The block&rsquo;s list: decide the official counts (324 vs 350 vs ~180), send Laura the recap re-requesting the per-account export, add the Waco Family Medicine cancellation to the churn findings, prep Monday&rsquo;s reconciliation of the <b>62 accounts with agreements but no live agent</b>, and watch the $5,000 invoice due Oct 29.</p>
          <div class="meta"><span class="pill warn">Today 10&ndash;11</span><span class="pill quiet">Recap to Laura after</span></div>
        </div></li>
        <li><div>
          <h4>The workshop is TOMORROW &mdash; today is the last pocket</h4>
          <p class="why">Prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30 at Gevity, Luma page live. The three job descriptions (day thirty-one) still gate the landing page &mdash; the open afternoon is the last real window to move them before the room fills.</p>
          <div class="meta"><span class="pill crit">Tomorrow 1&ndash;4</span><span class="pill quiet">JDs in the open afternoon</span></div>
        </div></li>
        <li><div>
          <h4>Emilio / Smart City &mdash; recap fourteen days; the deal moved to a binding-agreement redline</h4>
          <p class="why">You told Jake and Matt that Smart City loves the letter but will only move on something binding &mdash; Matt added Christine. Chase the redline so the momentum holds, and the written recap to Emilio (CC Jr) is still the carried send keeping his side warm.</p>
          <div class="meta"><span class="pill crit">Fourteen days</span><span class="pill quiet">Redline with Jake + Matt</span></div>
        </div></li>
        <li><div>
          <h4>#799 at day forty &mdash; and PR #992 now waits on your review</h4>
          <p class="why">#799 is still double-approved and unmerged. Illia requested your review on <b>#992</b> (VOXAI-936: suffix transfer tools with Ring/Voicemail) last evening. The hours after the audit block are the engineering pocket.</p>
          <div class="meta"><span class="pill warn">Two reviews deep</span><span class="pill quiet">After 11</span></div>
        </div></li>
      </ol>'''
src = src[:i] + new_prio + src[j+len('</ol>'):]

# ---------- 6. coming-up cards ----------
i = src.find('<h4 style="font-size:14px">Iris, day four &mdash; training TODAY at 11; Laura&rsquo;s reports are in</h4>')
j = src.find('</p>', src.find('direct tagging.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Iris, day five &mdash; the audit has a work plan; reconciliation preps for Monday</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">The training ran Thursday and Laura followed with her <b>all-time funnel report</b> (top chart new customers, bottom existing upsells &mdash; Jake clarified). Your 10&ndash;11 block today carries the follow-through: official counts, the recap re-requesting the <b>per-account export</b> (go-live, trial dates, cancel date/reason, owner, salesperson, minutes), the Waco cancellation into the churn findings, and prep for <b>Monday&rsquo;s billing reconciliation &mdash; 62 accounts with active agreements but no live agent</b>. The $5,000 invoice is due Oct 29. The Oct 6 update draft is on day ten in drafts. The series recurs Tuesdays 1&ndash;2. lmccree is in the Voxtell Linear workspace for direct tagging.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">Today 8:30&ndash;3 &mdash; one block, three meetings, then open</h4>')
j = src.find('</p>', src.find('the training leaves it open.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">Today 10&ndash;11, otherwise open &mdash; the valve before the workshop</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">One booked hour: the <b>Iris audit review 10&ndash;11</b>. The rest is the week&rsquo;s valve &mdash; the ProGraphix decision first thing, then workshop prep for tomorrow, the job descriptions (day thirty-one), and the sends: the Emilio recap, the Laura recap + export re-request out of the audit block, the redline chase with Jake and Matt.</p>''' + src[j:]

i = src.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
j = src.find('</p>', src.find('artwork deadline</b>.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h4 style="font-size:14px">The week&rsquo;s markers</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px"><b>Saturday is the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), Luma page live; Sunday stays open &mdash; the nature day. Next week: Monday 5.75h, <b>Tuesday 6.5h</b> with Iris Training 1&ndash;2, <b>Wednesday Oct 21 runs 6.5h against the 2F-15 artwork deadline</b> (FedEx&rsquo;s specs are with Jr), and <b>Thursday Oct 22 runs 6.5h</b> with &ldquo;Pay the Netsapiens booth bill&rdquo; scheduled 9&ndash;9:30 inside Deep Work. UGM itself is Oct 26&ndash;30 in Austin.</p>''' + src[j:]

# ---------- 7. chart ----------
i = src.find('<div class="plot" id="plot">'); j = src.find('</div>\n        <div class="xaxis"', i)
new_plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(32.14% + 6px)">4.5</div>
            <div class="seg m" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
        '''
src = src[:i] + new_plot + src[j:]
rep('''<div class="xaxis" id="xaxis">
          <div><b>Thu</b>15</div><div><b>Fri</b>16</div>
          <div><b>Sat</b>17</div><div><b>Sun</b>18</div><div><b>Mon</b>19</div><div><b>Tue</b>20</div><div><b>Wed</b>21</div>
        </div>''',
'''<div class="xaxis" id="xaxis">
          <div><b>Fri</b>16</div><div><b>Sat</b>17</div>
          <div><b>Sun</b>18</div><div><b>Mon</b>19</div><div><b>Tue</b>20</div><div><b>Wed</b>21</div><div><b>Thu</b>22</div>
        </div>''')
rep('Thu Oct 15 &ndash; Wed Oct 21', 'Fri Oct 16 &ndash; Thu Oct 22')

# ---------- 8. week flags ----------
i = src.find('<h3><span class="pill warn">Today</span> Thursday runs 7.5h')
j = src.find('</p>', src.find('settle it live.', i)) + len('</p>')
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">Today</span> Friday has one booked hour &mdash; the audit block 10&ndash;11; everything else is the valve</h3>
          <p>The morning opens with the <b>ProGraphix decision</b> &mdash; two days past the submit-by date, drafted reply deleted unsent: submit and reply, call Cathy, or let 10/23 slip. Then the <b>Iris audit block 10&ndash;11</b> with its five-point agenda, and the open afternoon carries <b>workshop prep for tomorrow</b>, the job descriptions (day thirty-one, still gating the landing page), and the sends &mdash; the Emilio recap (fourteen days), the Laura recap + export re-request, the binding-agreement redline chase.</p>''' + src[j:]

i = src.find('<h3><span class="pill warn">This week</span> Friday stays the valve; the workshop is two days out with 2F-15 artwork behind it</h3>')
j = src.find('Jr&rsquo;s hands.</p>') + len('Jr&rsquo;s hands.</p>')
assert 0 < i < j
src = src[:i] + '''<h3><span class="pill warn">This week</span> The workshop is tomorrow; next week runs steady into the 2F-15 and booth deadlines</h3>
          <p><b>Saturday Oct 17 is the workshop</b> &mdash; prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30 at Gevity, Luma page live. Sunday stays open. Next week opens gentle: Monday 5.75h with the <b>62-account billing reconciliation</b> you&rsquo;re prepping today, Tuesday 6.5h with Iris Training 1&ndash;2, <b>Wednesday Oct 21 runs 6.5h against the 2F-15 artwork deadline</b> (FedEx&rsquo;s specs already in Jr&rsquo;s hands), and Thursday Oct 22 6.5h with the Netsapiens booth bill scheduled 9&ndash;9:30. <b>UGM is the week after, Oct 26&ndash;30.</b></p>''' + src[j:]

# ---------- 9. already-have-a-home table ----------
rep('<tr><td class="tid">Today after 3</td><td><b>The Emilio recap</b> (thirteen days), <b>the Kayla ATS check</b> (form due back this afternoon) and <b>the confirming note to Laura</b> if the 11:00 training doesn&rsquo;t settle it<div class="src">Eric&rsquo;s reply (day thirty-eight) and the send backlog (thirty-three days past on billing/RevIO &middot; Nick night thirty-one) queue behind them</div></td></tr>',
    '<tr><td class="tid">Today after 11</td><td><b>The Emilio recap</b> (fourteen days; the binding-agreement redline is with Jake and Matt), <b>the ProGraphix decision</b> (two days past due) and <b>the Laura recap + per-account export re-request</b> out of the audit block<div class="src">Eric&rsquo;s reply (day thirty-nine) and the send backlog (thirty-four days past on billing/RevIO &middot; Nick night thirty-two) queue behind them &middot; Kayla&rsquo;s ATS form resolved: submitted Thursday, Jr has next steps</div></td></tr>')
rep('<tr><td class="tid">This week</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day thirty; the promo blast is public and the workshop&rsquo;s Luma page is live while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; workshop two days out &mdash; Friday&rsquo;s empty calendar is the last big pocket</div></td></tr>',
    '<tr><td class="tid">Today</td><td><b>The three job descriptions</b> (VA, EA, Content Manager) &mdash; day thirty-one; the promo blast is public and the workshop&rsquo;s Luma page is live while the landing page stays blocked<div class="src">ws-jds &rarr; ws-landing &middot; the workshop is tomorrow &mdash; today&rsquo;s open afternoon is the last pocket</div></td></tr>')
rep('<tr><td class="tid">Today 8:30&ndash;11</td>', '<tr><td class="tid">Today after 11</td>', 1)

# ---------- 10. FYI list ----------
rep('<li><b>Vipin Gupta has two unanswered Whova messages waiting</b> (Monday 3:41 AM, Tuesday 3:19 AM), <b>Carlos Bustamante&rsquo;s booth-staff invite is still open</b> (accepting enables lead capture) &mdash; and <b>Sue Giansiracusa sent UGM sponsor shipping &amp; FedEx deadlines marked action-required</b> yesterday; Jr forwarded it to you.</li>',
    '''<li><b>Vipin Gupta is now at three unanswered Whova messages</b> (Monday, Tuesday, and this morning 6:36 AM) and <b>Carlos Bustamante&rsquo;s booth-staff invite is still open</b> (accepting enables lead capture). The UGM shipping deadlines turned into a scheduled block: <b>&ldquo;Pay the Netsapiens booth bill,&rdquo; Thursday Oct 22, 9&ndash;9:30</b>.</li>
        <li><b>A &ldquo;Voxtell Billing: Past Due 1st Notice&rdquo; landed Thursday</b> &mdash; $1,086.29 on account 11001045 &mdash; and <b>PR #992 (VOXAI-936, Ring/Voicemail transfer labels) requested your review</b> last evening.</li>''')
rep('Today&rsquo;s noon <b>Grok Bot + Cursor webinar</b> sits inside the Deep Work block&rsquo;s last half hour.</li>',
    'You attended Thursday&rsquo;s Grok Bot + Cursor webinar and drafted masterclass prep notes in Granola.</li>')

# ---------- 11. line health ----------
rep('eight failures, one needs-attention and three successes on the day.',
    'eight failures, one needs-attention and three successes on the day. The overnight into Friday stayed quiet &mdash; <b>Friday opened clean</b>, four Daily Digests on schedule at 7:00. (LiveKit logged another Frankfurt incident this morning &mdash; intermittent connection timeouts, opened 5:55, resolved 6:59 AM CT &mdash; after Thursday&rsquo;s burst, not during it.)')

# ---------- 12. aging bumps ----------
rep('#799 is still sitting there, day thirty-nine', '#799 is still sitting there, day forty')
rep('thirty-fifth day double-approved', 'thirty-sixth day double-approved')
rep('#799 (day thirty-nine, double-approved)', '#799 (day forty, double-approved)')
rep('Day thirty-one on Eric Bramini', 'Day thirty-two on Eric Bramini')
rep('thirty-seven full days ago', 'thirty-eight full days ago')
rep('day thirty-six of billed Logs', 'day thirty-seven of billed Logs')
rep('Promised Sep 15 &mdash; day thirty', 'Promised Sep 15 &mdash; day thirty-one')
rep('twenty-four days unsent', 'twenty-five days unsent')
rep('forty-five days past retirement', 'forty-six days past retirement')
rep('Retired Aug 31 &mdash; forty-five days past', 'Retired Aug 31 &mdash; forty-six days past')
rep('em-roadmap at 49 days', 'em-roadmap at 50 days')
rep('now thirty-three days past due', 'now thirty-four days past due')
rep('Behind those: <b>Eric &mdash; day thirty-eight</b>, Nick&rsquo;s program-details reply on night thirty-one',
    'Behind those: <b>Eric &mdash; day thirty-nine</b>, Nick&rsquo;s program-details reply on night thirty-two')
rep('61d &mdash; chronic', '62d &mdash; chronic')
rep('<span class="chip old">61d</span>', '<span class="chip old">62d</span>')
rep('<span class="chip old">58d</span>', '<span class="chip old">59d</span>')
rep('54d &mdash; stalled', '55d &mdash; stalled')
rep('69d &mdash; chronic', '70d &mdash; chronic')

# ---------- sanity ----------
assert src.count('__CC_STATE__') == 1
assert src.count('__CC_TEMPLATE__') == 1
assert src.count('data-react-task="') == 59
assert src.count('class="bar"') == 7
assert src.count('2026-10-16T07:21:00-05:00') == 2
assert src.count('thirteen days') == 0
assert src.count('7.5h') == 0
assert src.count('training TODAY') == 0
assert src.count('due back this afternoon') == 0
assert src.count('two days out') == 0
open('page-template.html', 'w').write(src)
print('OK', len(src))
