# Wednesday Nov 4, 2026 FULL morning pass (fired 6:14 AM CST).
# Overnight verified (16h trash incl): nothing after Tue 6:52 PM -> TUESDAY CLOSES
# 7-2-1 (ten events). Wednesday opens silent. cc-state EMPTY.
# NORTEC: live negotiation - Tyler pushed on price Tue 10:42 AM ("top of the list
# on product"), Bodhi countered 7:38 PM (where I can move / can't), Tyler 8:05 PM:
# reviews with Steve THIS MORNING, "put a pin in this and move forward".
# ATS: Tue 11 AM onboarding = Affiliated Tech going live. 3 beta accounts queued
# (Integrity Property Mgmt, LaParkin, Environmental Pest Solutions; "doing this
# tomorrow"). Bodhi owes: bundle-pricing confirm ($450/1000min, $295/500), SIP 404
# trace to eng, Bandwidth app instructions, anonymized one-pagers, tag-team deploys.
# IRIS (Tue 1 PM): revised Lakeland case study SENT 7:24 PM + recap 7:45 PM. New
# owed: 5-email drip campaign + performance reports for 5-10 high-volume accounts.
# Hubler outreach -> Laura + Jason (John Gerhardt). Notification-per-agent promised
# "next week". SendGrid via Jeff in progress. Invoice six days past due, no payment.
# IZZY: Levitt verdict STILL unrecorded. Tim forwarded Oracle sheet + 4 test orders
# (10:14 AM) - Bodhi owes tab confirmation; refresh feature built, cost model Junior.
# GIGTEL: 80,000-customer white-label prospect booked Fri Nov 6, 12-12:30 (Apollo).
# Thu gains Honor/Taylor/Bodhi 3-3:30. #1080 MERGED by Pagebakers; #1073 still open.
# Sahiti intro promised Tue 9:02 AM "in a separate email". Drafts still empty.
# Chart rolls Wed Nov 4 - Tue Nov 10.
import re

p = 'page-template.html'
s = open(p, encoding='utf-8').read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f"rep {old[:70]!r}: expected {n}, found {c}"
    s = s.replace(old, new)

def rx(pat, new, n, flags=0):
    global s
    s, c = re.subn(pat, new, s, flags=flags)
    assert c == n, f"rx {pat[:70]!r}: expected {n}, replaced {c}"

def splice(a, b, new, incl_b=False):
    global s
    i0 = s.find(a)
    assert i0 >= 0, f"splice start missing: {a[:60]!r}"
    i1 = s.find(b, i0)
    assert i1 > i0, f"splice end missing: {b[:60]!r}"
    if incl_b: i1 += len(b)
    s = s[:i0] + new + s[i1:]

# ---------- 1. GLOBAL AGE BUMPS (highest first) ----------
rep('day fifty-eight', 'day fifty-nine', 4)                   # #799
rep('day fifty-seven', 'day fifty-eight', 3)                  # Eric / Izzy trio
rep('night fifty', 'night fifty-one', 2)
rep('day forty-nine;', 'day fifty;', 1)                       # JDs
rep('fifty-two days past', 'fifty-three days past', 2)
rep('forty-two days past', 'forty-three days past', 1)        # Appulse
rep('twenty days past', 'twenty-one days past', 3)            # ProGraphix
rep('Twenty days past', 'Twenty-one days past', 2)
rep('(twenty days)', '(twenty-one days)', 2)
rep('day fifteen', 'day sixteen', 4)                          # Tim
rep('Fourteen days past the promise', 'Fifteen days past the promise', 1)
rep('Iris, day twenty-three', 'Iris, day twenty-four', 1)
rep('hr-nda is 78 days old', 'hr-nda is 79 days old', 1)
rep('Ages as of Nov 3', 'Ages as of Nov 4', 1)
rep('is five days past due (Oct 29)', 'is six days past due (Oct 29)', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-03T21:09:00-06:00', '2026-11-04T06:55:00-06:00', 2)
rep('<b>Brief compiled</b> Tue 6:50 AM &middot; data checked Tue 9:09 PM CT',
    '<b>Brief compiled</b> Wed 6:55 AM &middot; data checked Wed 6:55 AM CT', 1)
rep('Tuesday, November 3 &middot; 2026', 'Wednesday, November 4 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Monday delivered.')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Nortec answers this morning. Tyler pushed back on price Tuesday (&ldquo;top of the list on '
 'product&rdquo;), <b>your counter went out at 7:38 PM</b> &mdash; where you can move and where you '
 'can&rsquo;t &mdash; and Tyler closed the night at 8:05: he reviews with Steve this morning and wants '
 'to &ldquo;put a pin in this and move forward.&rdquo; <b>Watch the thread; the HOLD at 10:30 is the '
 'reply pocket.</b> Bigger still: Tuesday&rsquo;s onboarding call was <b>ATS going live</b> &mdash; '
 'seven Affiliated Tech people walked the platform and <b>three beta accounts are queued</b> '
 '(Integrity Property Management, LaParkin, Environmental Pest Solutions &mdash; &ldquo;we&rsquo;re '
 'doing this tomorrow&rdquo;, which is today). Five items are yours: the <b>bundle-pricing '
 'confirmation</b> Wheelock sent to sanity-check ($450 for 1,000 minutes, $295 for 500) before the '
 'orders submit, the <b>SIP-trace 404 to engineering</b>, <b>Bandwidth app instructions</b> for '
 'Jamie, the <b>anonymized one-pagers</b>, and tag-teaming the first deployments with Jr. The Iris '
 'session restocked the list too: the <b>revised Lakeland case study went out last night</b> (15% of '
 'calls handled end to end), and you now owe the <b>five-email drip campaign</b> and <b>performance '
 'reports for the high-volume accounts</b>; the Hubler outreach moved to Laura and Jason. <b>GigTel '
 '&mdash; 80,000 customers, white-label &mdash; booked Friday at noon.</b> Today is Taylor&rsquo;s '
 'double-header: kickoff 11&ndash;1, GamifyOS 1&ndash;3, TTT at 3 (<b>the Cathy call</b>, twenty-one '
 'days past). Tuesday closed <b>7&ndash;2&ndash;1</b>. The Iris <b>invoice is six days past due</b>. '
 'No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Tuesday + open Wednesday ----------
rep('<b>7&ndash;2&ndash;1 by 9:09, window open</b>, quiet since 6:52.',
    '<b>7&ndash;2&ndash;1 by 9:09</b>, and nothing followed &mdash; <b>Tuesday closes '
    '7&ndash;2&ndash;1</b>, ten events, verified Wednesday morning with trash included. Wednesday '
    'opened silent &mdash; nothing by 6:55, window open.', 1)

# ---------- 5. "Needs a decision" note ----------
rep('Nortec decides within 48 hours &mdash; the live number and onboarding doc go out before the 10 AM wall',
    'Nortec&rsquo;s answer lands this morning and ATS submits its beta orders today &mdash; the HOLD at 10:30 is the reply pocket', 1)

# ---------- 6. TODAY SCHEDULE ----------
rep('Ten hours booked from 10 &mdash; the pre-10 morning is the only pocket',
    'Taylor&rsquo;s double-header 11&ndash;3 &mdash; the HOLD at 10:30 is the Nortec pocket', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot"><div class="t">9:00&ndash;9:30</div><div class="w">Recover + Shower<small>The slow start is on the calendar on purpose</small></div></div>\n'
 '        <div class="slot"><div class="t">9:30&ndash;10:30</div><div class="w">Sustainable Ambition<small>Weekly gathering &mdash; Gevity Movement Studio</small></div></div>\n'
 '        <div class="slot"><div class="t">10:30&ndash;11:00</div><div class="w">HOLD<small>The pocket: the Nortec reply and the ATS pricing confirmation</small></div></div>\n'
 '        <div class="slot"><div class="t">11:00&ndash;1:00</div><div class="w">Ashlyn / Taylor / Bodhi Kick Off<small>The Taylor double-header opens</small></div></div>\n'
 '        <div class="slot"><div class="t">1:00&ndash;3:00</div><div class="w">GamifyOS: Working Session<small>Taylor &mdash; Lock-In prep lives in Notion</small></div></div>\n'
 '        <div class="slot"><div class="t">3:00&ndash;4:00</div><div class="w">Transition, Talking, Triage<small>The Cathy call &mdash; twenty-one days; phone, not email</small></div></div>\n'
 '        <div class="slot"><div class="t">4:00&ndash;4:15</div><div class="w">Pickup lady</div></div>\n'
 '        <div class="slot free"><div class="t">After 4:15</div><div class="w">Open evening<small>Thursday opens with the 8:30&ndash;12:30 engineering block</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 7. TOP 5 ----------
rep('<span class="note">The Nortec clock first &mdash; then Cathy and the Spectrum chases</span>',
    '<span class="note">Nortec and ATS first &mdash; both move today</span>', 1)

# li1: Nortec negotiation
splice('<h4>Nortec decides within 48 hours &mdash; the proposal is out; the live number and onboarding doc are still owed</h4>',
       '</div></li>',
 '<h4>Nortec answers this morning &mdash; Tyler is reviewing your counter with Steve right now</h4>\n'
 '          <p class="why">The thread ran all Tuesday: <b>Tyler came back on price in the morning</b> '
 '&mdash; they like the product (&ldquo;top of the list&rdquo;) but are comparing against cheaper '
 'competitors &mdash; and <b>your counter went out at 7:38 PM</b>, laying out where you can move and '
 'where you can&rsquo;t (setup is engineering time). Tyler&rsquo;s 8:05 PM reply: he reviews with '
 'Steve this morning and wants to &ldquo;put a pin in this and move forward.&rdquo; The deal context '
 'from Monday&rsquo;s demo stands: 300 customers, Cairo actively coming out, a halted demo program '
 'waiting on a replacement. <b>The HOLD at 10:30 is the reply pocket</b> &mdash; answer fast, '
 'whichever way it lands. Still unbooked behind it: <b>Michael at CCI&rsquo;s call</b>.</p>\n'
 '          <div class="meta"><span class="pill crit">Answer due this morning</span><span class="pill good">Counter sent Tue 7:38 PM</span></div>\n'
 '        ')

# li2: Tim/Oracle -> ATS beta
splice('<h4>Fifteen days past the promise: the written Oracle record is still unsent &mdash; Friday&rsquo;s review came and went</h4>',
       '</div></li>',
 '<h4>ATS went from testing to buying &mdash; three beta accounts are queued, and five items are yours</h4>\n'
 '          <p class="why">Tuesday&rsquo;s 11 AM &ldquo;onboarding&rdquo; was <b>seven Affiliated '
 'Tech people walking the platform with you and Jr</b> &mdash; an assistant (&ldquo;Marlin&rdquo;) '
 'built live on their provisioned domain. <b>Three beta accounts are queued</b>: Integrity Property '
 'Management, LaParkin, and Environmental Pest Solutions (two months free; Jamie: &ldquo;we&rsquo;re '
 'doing this tomorrow&rdquo; &mdash; which is today). Yours before and as the orders land: <b>confirm '
 'the bundle pricing Wheelock sanity-checked</b> ($450 for 1,000 minutes, $295 for 500; overage TBD), '
 '<b>send the SIP-trace 404 to engineering</b> (David&rsquo;s ladder is in the chat), <b>Bandwidth '
 'app instructions for Jamie</b>, the <b>anonymized industry one-pagers</b> (co-brandable), and '
 'tag-teaming the first one or two deployments with Antonelli and Jordan.</p>\n'
 '          <div class="meta"><span class="pill crit">Orders queued today</span><span class="pill warn">Five items yours</span></div>\n'
 '        ')

# li3: Iris follow-through
splice('<h4>Two of Friday&rsquo;s three deliverables shipped Monday night &mdash; what&rsquo;s left is the Jeff chase and the invoice</h4>',
       '</div></li>',
 '<h4>The Lakeland revision shipped last night &mdash; and the Iris session restocked your list</h4>\n'
 '          <p class="why"><b>The revised Lakeland case study went out Tuesday 7:24 PM</b> (generic '
 'for dealerships; 15% of 40,129 calls handled end to end) with the <b>meeting recap at 7:45</b>. New '
 'from the session: <b>you owe the five-email drip campaign</b> (insights, Ask Iris, notifications, '
 'use cases, results &mdash; it rides on Jeff&rsquo;s SendGrid integration) and <b>performance '
 'reports for 5&ndash;10 high-volume accounts</b> (McCallum, McNeil Chevrolet, Diamond Hawk&hellip;) '
 'as the expansion play; <b>notification-per-agent is promised for next week</b>. The Hubler opening '
 'moved off your desk &mdash; <b>Laura and Jason take both reports to John Gerhardt</b>. Grayson '
 'chases Lakeland&rsquo;s name approval. The <b>$5,000 invoice is six days past due (Oct 29) &mdash; '
 'no payment confirmation has landed</b>, and Tuesday&rsquo;s session came and went without one.</p>\n'
 '          <div class="meta"><span class="pill good">Lakeland revision sent Tue 7:24 PM</span><span class="pill warn">Drip campaign + reports owed</span></div>\n'
 '        ')

# li4 Cathy: slot update
rep('today&rsquo;s TTT hour at 2 is the slot', 'today&rsquo;s TTT hour at 3 is the slot', 1)
rep('Call, not email &middot; TTT at 2', 'Call, not email &middot; TTT at 3', 1)

# li5: reviews + Oracle
splice('<h4>#799 at day fifty-nine &mdash; and you took over Illia&rsquo;s six open PRs</h4>',
       '</div></li>',
 '<h4>#799 at day fifty-nine &mdash; the Tim thread revived, and the review stack waits on tomorrow&rsquo;s block</h4>\n'
 '          <p class="why">Tuesday&rsquo;s Izzy check-in moved Oracle: the <b>spreadsheet refresh '
 'feature is built and tested</b> (cost model is Junior&rsquo;s to settle), and <b>Tim forwarded the '
 'Oracle sheet with four Shopify test orders</b> at 10:14 AM &mdash; yours: <b>confirm which tabs '
 'Izzy reads</b> or have the sheet consolidated to one. The promised written record is still unsent '
 'at day sixteen, but the thread is alive again. On the PR side: <b>Pagebakers finished and merged '
 '#1080 himself</b> Tuesday morning; <b>#1073 still carries its changes-request</b> (a recording or '
 'screenshot of the UI behavior), and #886, #991, #992 plus <b>Illia&rsquo;s six</b> wait on '
 '<b>tomorrow&rsquo;s 8:30&ndash;12:30 engineering block</b>. The Levitt verdict survived another '
 'check-in unrecorded &mdash; iz-10dlc stays open.</p>\n'
 '          <div class="meta"><span class="pill warn">Oracle tabs + #1073 rework</span><span class="pill quiet">Next DW: Thu 8:30</span></div>\n'
 '        ')

# ---------- 8. FLAG 1 (Today) ----------
f0 = s.find('<h3><span class="pill warn">Today</span> Ten-hour Tuesday &mdash; and the Nortec clock runs while you&rsquo;re in calls</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Taylor&rsquo;s double-header &mdash; with Nortec and ATS landing in the gaps</h3>\n'
 '          <p>The morning is gentle (Recover + Shower at 9, Sustainable Ambition at 9:30), and the '
 '<b>HOLD at 10:30 is the working pocket</b>: the Nortec reply when Tyler and Steve answer, and the '
 '<b>ATS bundle-pricing confirmation before their orders submit</b>. Then Taylor owns the middle: '
 '<b>kickoff 11&ndash;1, GamifyOS 1&ndash;3</b> (Lock-In prep is in Notion). <b>TTT at 3 is the '
 'Cathy call</b> &mdash; twenty-one days, phone not email &mdash; and the pickup at 4 closes the '
 'booked day. Evening open; tomorrow opens with the 8:30&ndash;12:30 engineering block the review '
 'stack has been waiting for.</p>'
) + s[f1:]

# ---------- 9. FLAG 2 (On the wire) ----------
rep('<h3><span class="pill warn">On the wire</span> The Jeff chases, Pipedrive, and the UGM loose ends</h3>',
    '<h3><span class="pill warn">On the wire</span> The Jeff threads, the Sahiti intro, and the UGM tail</h3>', 1)
w0 = s.find('<p>Everything open at Spectrum now routes through')
w1 = s.find('</p>', w0) + len('</p>')
assert 0 < w0 < w1
s = s[:w0] + (
 '<p><b>Jeff at Spectrum now holds three threads</b>: the SendGrid integration is <b>in progress</b> '
 '(Tuesday&rsquo;s session confirmed it &mdash; your drip campaign rides on it), the mail-server '
 'question folds into it, and <b>ConnectWise credentials still block Illia&rsquo;s integration</b> '
 '(Junior asked; Illia chased twice). <b>Pipedrive</b> should land any day &mdash; OAuth tested on a '
 'real account, no marketplace approval needed. Two warm loops are yours: <b>the Sahiti intro</b> '
 '(you told her Tuesday morning it would come &ldquo;in a separate email&rdquo; &mdash; the Ora '
 'founder is waiting on it), and <b>Jeff Pulver&rsquo;s note</b> &mdash; a vCon strategy briefing and '
 'a guest seat at the VON Policy Summit in Washington. UGM tail: Whova refreshed the attendee-list '
 'link Tuesday, the <b>booth bill is still unconfirmed</b>, the <b>Whova three</b> are still '
 'waiting, and the GPT-Live BAA call stays Jr&rsquo;s.</p>'
) + s[w1:]

# ---------- 10. MARKERS ----------
k0 = s.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
assert k0 > 0
k1 = s.find('<p', k0)
k2 = s.find('</p>', k1) + len('</p>')
assert 0 < k1 < k2
s = s[:k1] + (
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Tuesday closed <b>7&ndash;2&ndash;1</b> '
 '&mdash; ten events, with the evening burst arriving on script (six failures 6:02&ndash;6:52, the '
 'twenty-third straight weekday evening). The pipeline is the story now: <b>Nortec answers this '
 'morning, ATS submits beta orders today, and GigTel &mdash; 80,000 customers &mdash; books Friday at '
 'noon</b>. The next engineering block is <b>tomorrow, 8:30&ndash;12:30</b>.</p>'
) + s[k2:]

# ---------- 11. COMING-UP week card ----------
c0 = s.find('<h4 style="font-size:14px">This week &mdash; today is the wall; Friday gained a call</h4>')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 '<h4 style="font-size:14px">This week &mdash; the pipeline stacks onto Friday noon</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today (7.25h): SA 9:30, HOLD '
 '10:30, <b>Taylor kickoff 11&ndash;1 + GamifyOS 1&ndash;3</b>, TTT 3, pickup 4. Thursday (6h): '
 '<b>DW Engineering 8:30&ndash;12:30</b> &mdash; the review stack&rsquo;s window &mdash; then '
 '<b>Honor / Taylor at 3</b> (new, Equistamp), Scott at 4. Friday (1.5h): <b>Mike at 11</b>, '
 '<b>GigTel at noon</b> &mdash; 80,000 customers, white-label resellers, NetSapiens + FreeSwitch '
 'asks; Jr and Carlos join. The weekend is clear. Next week: sync Mon 8, DW Engineering Mon '
 '10&ndash;2, Hand and Stone Mon 8 PM; <b>Monthly Iris Sync Tue Nov 10, 9</b>, Izzy 10, DW Client '
 '10&ndash;2; <b>Ellie &times; Caroline &times; Taylor Wed Nov 11, 10:30</b> ahead of the engineering '
 'block (11&ndash;3); Thu Nov 12: DW 8:30, Scott 2, Friendsgiving 6&ndash;9 PM (unaccepted); Fri Nov '
 '13: Review Crew happy hour 5:30. Carried: <b>the Cathy call</b> (twenty-one days), <b>the Tim '
 'record</b> (day sixteen), <b>the CCI booking</b>, the drip campaign and performance reports, the '
 'ATS five, the review queue (#1073, #886, #991, #992, #799 + Illia&rsquo;s six), the Whova trio, and '
 'the <b>invoice &mdash; six days past due</b>.</p>'
) + s[c1:]

# ---------- 12. INBOX LEAD ----------
splice('Monday evening was a shipping night:',
       'the pre-10 pocket is today&rsquo;s only open ground.',
 'The Nortec thread ran all Tuesday: Tyler&rsquo;s price pushback in the morning, <b>your counter at '
 '7:38 PM</b>, and his 8:05 close &mdash; <b>he reviews with Steve this morning</b>. Last night you '
 'also shipped the <b>revised Lakeland case study (7:24) and the session recap (7:45)</b> to the '
 'Spectrum team. <b>Pagebakers merged #1080 himself</b>; #1073 still wants its UI recording. Promised '
 'and not yet visible: <b>the Sahiti intro</b> (&ldquo;in a separate email&rdquo;, Tuesday 9:02 AM). '
 'Worth a read: <b>Jeff Pulver&rsquo;s note</b> &mdash; a vCon briefing and a VON Policy Summit guest '
 'seat. The Drafts folder is still empty &mdash; the Tim record stays unwritten at day sixteen. Still '
 'needing words: <b>Cathy at ProGraphix</b> (twenty-one days), <b>the CCI booking</b>, and the '
 '<b>Whova three</b> &mdash; the HOLD at 10:30 and the post-4:15 evening are today&rsquo;s ground.', incl_b=True)

# ---------- 13. IRIS CARD ----------
splice('Friday&rsquo;s session delivered (Ask Iris live on 1,880 calls',
       ' for direct tagging.',
 'Tuesday&rsquo;s session was a working one: LeVarr runs customer PDFs through Claude into Ask Iris '
 '(deployments down to ~15 minutes) and asked for a <b>direct attach-to-Ask-Iris feature</b>; the '
 '<b>Lakeland report covers 40,129 calls</b> (5,954 &mdash; 15% &mdash; handled end to end) and '
 '<b>Hubler 15,331</b> (3,883 bookings); the churn post-mortem named overage surprise and underselling '
 'as the loss drivers, with five silent accounts flagged and five high-volume accounts marked for '
 'expansion. <b>Your revised Lakeland case study went out Tuesday 7:24 PM</b>; Grayson chases '
 'Lakeland&rsquo;s name approval; <b>Laura and Jason take the Hubler reports to John Gerhardt</b>. '
 'You owe the <b>five-email drip campaign</b> (on Jeff&rsquo;s SendGrid rails) and the <b>account '
 'performance reports</b>; <b>notification-per-agent ships next week</b> per your own commitment. The '
 '<b>invoice is six days past due</b>; the <b>Monthly Iris Sync lands Tue Nov 10, 9&ndash;9:30</b>.', incl_b=True)

# ---------- 14. CHART: roll to Wed Nov 4 - Tue Nov 10 ----------
rep('Tue Nov 3 &ndash; Mon Nov 9', 'Wed Nov 4 &ndash; Tue Nov 10', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(51.79% + 6px)">7.25</div>\n'
 '            <div class="seg m" style="height:41.07%"></div><div class="seg f" style="height:7.14%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(10.71% + 6px)">1.5</div>\n'
 '            <div class="seg m" style="height:10.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Tue</b>3</div><div><b>Wed</b>4</div>\n          <div><b>Thu</b>5</div><div><b>Fri</b>6</div><div><b>Sat</b>7</div><div><b>Sun</b>8</div><div><b>Mon</b>9</div>',
    '<div><b>Wed</b>4</div><div><b>Thu</b>5</div>\n          <div><b>Fri</b>6</div><div><b>Sat</b>7</div><div><b>Sun</b>8</div><div><b>Mon</b>9</div><div><b>Tue</b>10</div>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-04T06:55:00-06:00') == 2
assert s.count('window open') == 2
assert 'day fifteen' not in s and 'five days past due' not in s
assert 'Good evening' not in s and 'Tuesday, November 3' not in s
assert 'Tue Nov 3 &ndash; Mon Nov 9' not in s and ' for direct tagging.' not in s
assert 'quoter' not in s and 'hw7Mh6cK' not in s and 'pY3DM73R' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'bT5uDhjRSBk3' not in s and 'doxy.me/scottvlmft' not in s
assert 'atscall-frontline' not in s

open(p, 'w', encoding='utf-8').write(s)
print('wednesday full ok', len(s))
