# Friday Nov 6, 2026 FULL morning pass (fired 6:11 AM CST).
# Overnight verified (16h trash incl): nothing after Thu 7:38 PM -> THURSDAY
# CLOSES 10-5-3 (eighteen events; TEN failures = new weekday record, third
# straight day the record moved: Mon 8 -> Wed 9 -> Thu 10). Friday opens silent.
# NORTEC: AGREED ON TERMS. Tyler 8:46 AM "That work?" -> Jr 10:34 AM: "That
# works" - $250 platform fee + $250 monthly minimum credited toward usage,
# day one, 12-month term, weekly calls off. Awaiting Tyler's confirmation/paperwork.
# TIM RECORD: DRAFTED Thu 9:07 AM, UNSENT - names test orders 102813/102862/
# 103088/101356 (shipped/backorder, inventory, lensless, kit) + wires the sheet.
# LIVEKIT: Ben Cherry replied overnight 12:44 AM to Jr's Oct 14 intro thread -
# "would love to learn more about how I can help" (Bodhi + Eelco cc'd).
# CATHERINE WEIR (365agents, w/ Rick - UGM AI Showcase winners) followed up 4:01 PM.
# GAMIFYOS session desc updated by Taylor: half Ashlyn (dashboard mockup for
# feedback ~1wk), half Gamify (web page + community landing live by Wed Nov 12,
# before Review Crew Fri Nov 13); Discord bot feasibility confirmed by Bodhi
# Nov 5; HOLD EquiStamp proposal until Honor's Discord brain-dump.
# ATS: still no order traffic ("doing this tomorrow" now two days stale).
# CALENDAR today: Mike 11-12 (Gevity), Stratus noon-12:30 (Jr joins; 1,200
# customers), GigTel 1-1:30 (Jr + Carlos; 80,000), GamifyOS 2:30-5:30 = 5h all
# meetings. Thu Nov 12 now 8.5h (DW 4f + Scott VC 1m + Reserved .5f +
# Friendsgiving 3m) - crosses the 8h line. Chart rolls Fri Nov 6 - Thu Nov 12.
# Hazards: bump 'day sixty'->sixty-one BEFORE 'day fifty-nine'->sixty.
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
rep('day sixty', 'day sixty-one', 3)                           # #799
rep('day fifty-nine', 'day sixty', 3)                          # Eric / Izzy trio
rep('night fifty-two', 'night fifty-three', 2)
rep('day fifty-one;', 'day fifty-two;', 1)                     # JDs
rep('fifty-four days past', 'fifty-five days past', 2)
rep('forty-four days past', 'forty-five days past', 1)         # Appulse
rep('twenty-two days past', 'twenty-three days past', 2)       # ProGraphix
rep('Twenty-two days past', 'Twenty-three days past', 2)
rep('(twenty-two days)', '(twenty-three days)', 2)
rep('day seventeen', 'day eighteen', 3)                        # Tim
rep('Iris, day twenty-five', 'Iris, day twenty-six', 1)
rep('hr-nda is 80 days old', 'hr-nda is 81 days old', 1)
rep('Ages as of Nov 5', 'Ages as of Nov 6', 1)
rep('seven days past due', 'eight days past due', 7)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-05T21:07:00-06:00', '2026-11-06T06:55:00-06:00', 2)
rep('<b>Brief compiled</b> Thu 6:55 AM &middot; data checked Thu 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:55 AM &middot; data checked Fri 6:55 AM CT', 1)
rep('Thursday, November 5 &middot; 2026', 'Friday, November 6 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Nortec came back at 8:46 this morning')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Nortec is agreed. Tyler asked &ldquo;That work?&rdquo; at 8:46 yesterday morning, and <b>Jr '
 'answered at 10:34: &ldquo;That works&rdquo;</b> &mdash; $250 platform fee plus a $250 monthly '
 'minimum credited toward usage, starting day one, 12-month term, weekly calls off. The negotiation '
 'that opened with Monday&rsquo;s demo is <b>done on terms; what&rsquo;s left is Tyler&rsquo;s '
 'confirmation and the paperwork</b>. Today is reseller day: <b>Mike at 11, Stratus Networks at '
 'noon</b> (1,200 customers, Jr joins), <b>GigTel at 1</b> (80,000 customers &mdash; Jr and Carlos '
 'join), then <b>three hours of GamifyOS with Taylor from 2:30</b> &mdash; she wrote the agenda into '
 'the invite: half Ashlyn (a dashboard mockup for her feedback), half Gamify (web page and community '
 'landing <b>live by Wednesday Nov 12</b>); EquiStamp holds until Honor&rsquo;s Discord brain-dump. '
 'Overnight, <b>Ben Cherry at LiveKit replied to Jr&rsquo;s October intro</b> &mdash; &ldquo;would '
 'love to learn more about how I can help&rdquo; &mdash; a named human for the TCP/SIP and BAA '
 'questions. And the Tim record finally has words: <b>a reply to Tim has sat in your Drafts since '
 '9:07 yesterday morning</b> &mdash; four test orders named, the sheet wired in &mdash; <b>it just '
 'needs Send</b>. Thursday closed <b>10&ndash;5&ndash;3</b>: ten failures, the weekday record moving '
 'for the third straight day. The Iris <b>invoice is eight days past due</b>. No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Thursday + open Friday ----------
rep('<b>10&ndash;5&ndash;3 by 8:07, window open</b>, eighteen events, and ten failures passes '
    'Wednesday&rsquo;s nine as the heaviest weekday failure count on the ledger.',
    '<b>10&ndash;5&ndash;3 by 8:07</b>, and nothing followed &mdash; <b>Thursday closes '
    '10&ndash;5&ndash;3</b>, eighteen events, verified Friday morning with trash included; ten '
    'failures passes Wednesday&rsquo;s nine as the heaviest weekday failure count, the third '
    'straight day the record moved (eight, nine, ten). Friday opened silent &mdash; nothing by '
    '6:55, window open.', 1)

# ---------- 5. "Needs a decision" note ----------
rep('Tyler countered at 8:46 &mdash; $250 fee + $250 usage, no weekly calls, &ldquo;That work?&rdquo; &mdash; a one-line answer closes it',
    'Nortec is agreed on terms &mdash; Jr&rsquo;s &ldquo;that works&rdquo; went out at 10:34 yesterday; watch for Tyler&rsquo;s confirmation and the paperwork', 1)

# ---------- 6. TODAY SCHEDULE ----------
rep('Four hours of engineering, then four calls &mdash; the 12:30&ndash;2 gap is the pocket',
    'Reseller day &mdash; three calls 11&ndash;1:30, then three hours with Taylor', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">Until 11:00</div><div class="w">Open morning<small>Send the Tim draft, the Cathy call (twenty-three days), the ATS nudge, Catherine Weir&rsquo;s reply, the Pipedrive review</small></div></div>\n'
 '        <div class="slot"><div class="t">11:00&ndash;12:00</div><div class="w">Mike and Bodhi<small>In person at Gevity</small></div></div>\n'
 '        <div class="slot"><div class="t">12:00&ndash;12:30</div><div class="w">Alex Penichet / Stratus Networks<small>White-label reseller pitch &mdash; 1,200 customers; Jr joins</small></div></div>\n'
 '        <div class="slot"><div class="t">1:00&ndash;1:30</div><div class="w">Tanner Robinson / GigTel<small>80,000 customers &mdash; NetSapiens integration, FreeSwitch, reseller structure; Jr + Carlos</small></div></div>\n'
 '        <div class="slot"><div class="t">2:30&ndash;5:30</div><div class="w">GamifyOS: Working Session &mdash; Taylor<small>Half Ashlyn (dashboard mockup), half Gamify (web page + landing by Wed Nov 12) &mdash; at Gevity</small></div></div>\n'
 '        <div class="slot free"><div class="t">After 5:30</div><div class="w">Open evening<small>The weekend is clear; Monday opens with the 8 AM sync and the 10&ndash;2 engineering block</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 7. TOP 5 ----------
rep('<span class="note">Watch Nortec &mdash; and spend the block on the review queue</span>',
    '<span class="note">The Nortec paperwork, the reseller double-header, and the Send button on the Tim draft</span>', 1)

# li1: Nortec agreed
splice('<h4>Nortec countered at 8:46 this morning &mdash; $250 fee + $250 usage, no weekly calls: &ldquo;That work?&rdquo;</h4>',
       '</div></li>',
 '<h4>Nortec is agreed &mdash; Jr&rsquo;s &ldquo;that works&rdquo; closed the terms at 10:34 yesterday</h4>\n'
 '          <p class="why">The final shape: <b>$250 platform fee plus a $250 monthly minimum fully '
 'credited toward usage, starting day one, on a 12-month term; weekly calls off, everything else as '
 'outlined</b>. Five days, demo to agreement: Monday&rsquo;s demo, Tuesday&rsquo;s proposal and '
 'price pushback, your Tuesday-night counter, Wednesday&rsquo;s structure trade, and '
 'Thursday&rsquo;s split-the-difference close. Nothing has come back from Tyler since Jr&rsquo;s '
 'acceptance, so what remains is <b>his confirmation and the paperwork</b> &mdash; contract and '
 'onboarding &mdash; and the 300-customer rollout behind it. Still unbooked behind the deal: '
 '<b>Michael at CCI&rsquo;s call</b>.</p>\n'
 '          <div class="meta"><span class="pill good">Terms agreed Thu 10:34 AM</span><span class="pill warn">Watch for the paperwork</span></div>\n'
 '        ')

# li2: reseller double-header
splice('<h4>ATS: &ldquo;doing this tomorrow&rdquo; was yesterday &mdash; and no orders are visible yet</h4>',
       '</div></li>',
 '<h4>Two white-label resellers today &mdash; Stratus at noon (1,200 customers), GigTel at 1 (80,000)</h4>\n'
 '          <p class="why">Both booked through Apollo on the same reseller pitch. <b>GigTel wrote '
 'their asks into the booking</b>: the NetSapiens integration, whether you can integrate with '
 'FreeSwitch, and what reseller relationships are built into the system &mdash; they run &ldquo;a '
 'very high amount of white-label resellers.&rdquo; <b>Jr and Carlos join GigTel; Jr joins '
 'Stratus.</b> Worth having ready: the NetSapiens story, the white-label/reseller structure, and a '
 'point of difference from RingLogix, who are running a CodeFest victory lap in the same '
 'ecosystem this week. Nortec&rsquo;s five-day close is the fresh proof point.</p>\n'
 '          <div class="meta"><span class="pill crit">Noon + 1 PM today</span><span class="pill good">Jr + Carlos join</span></div>\n'
 '        ')

# li3: Tim draft - send it
splice('<h4>Laura shared the case study with the entire sales team &mdash; and the invoice hits eight days past due</h4>',
       '</div></li>',
 '<h4>The Tim record is drafted &mdash; it has sat in Drafts since 9:07 yesterday morning. Send it.</h4>\n'
 '          <p class="why">Yesterday&rsquo;s engineering block finally produced the written Oracle '
 'record: a reply to Tim naming the <b>four test orders &mdash; 102813, 102862, 103088, 101356</b> '
 '&mdash; validating Izzy against shipped/backorder, inventory, lensless and kit cases, and wiring '
 'his Google sheet into the flow. It answers the Oracle-tabs question and closes the record promise '
 '<b>at day eighteen</b> &mdash; but it is still sitting unsent. One Send this morning and '
 'Tuesday&rsquo;s Izzy check-in arrives with it done. The <b>Levitt verdict</b> is the thread&rsquo;s '
 'other open item &mdash; iz-10dlc stays open until someone records it.</p>\n'
 '          <div class="meta"><span class="pill crit">Drafted, unsent</span><span class="pill warn">Day eighteen &mdash; one click closes it</span></div>\n'
 '        ')

# li4 Cathy: slot update (ages bumped globally)
rep('today&rsquo;s 12:30&ndash;2 gap after the engineering block is the slot',
    'this morning before Mike at 11 is the slot', 1)
rep('Call, not email &middot; 12:30 gap', 'Call, not email &middot; before 11', 1)

# li5: ATS quiet + review queue parked to Monday
splice('<h4>The queue shrank overnight &mdash; Pagebakers merged #1073, #721 and #809; today&rsquo;s block takes the rest</h4>',
       '</div></li>',
 '<h4>ATS went quiet &mdash; &ldquo;doing this tomorrow&rdquo; is two days old and no orders have landed</h4>\n'
 '          <p class="why">Tuesday&rsquo;s onboarding queued <b>three beta accounts</b> (Integrity '
 'Property Management, LaParkin, Environmental Pest Solutions) and Jamie said the orders were coming '
 'the next day &mdash; that was Wednesday, and the channel has been silent since. <b>A short nudge '
 'to Jamie and Wheelock fits the open morning</b>, and the <b>bundle-pricing confirmation</b> ($450 '
 'for 1,000 minutes, $295 for 500) still rides with it, then the SIP-trace 404, the Bandwidth '
 'instructions, and the one-pagers (Jr&rsquo;s new <b>Brand Kit folder</b> is live for those). The '
 'review queue waits on <b>Monday&rsquo;s 10&ndash;2 engineering block</b>: #886, #991, #992, '
 '<b>#799 at day sixty-one</b>, Illia&rsquo;s six, and the new <b>Pipedrive CRM review</b> '
 '(voxai-851, requested yesterday 1:15 PM).</p>\n'
 '          <div class="meta"><span class="pill warn">Nudge Jamie + Wheelock</span><span class="pill quiet">Reviews: Mon 10&ndash;2</span></div>\n'
 '        ')

# ---------- 8. FLAG 1 (Today) ----------
f0 = s.find('<h3><span class="pill warn">Today</span> The engineering day &mdash; four hours of block, then four calls back to back</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Reseller Friday &mdash; Mike, Stratus and GigTel back to back, then three hours of GamifyOS</h3>\n'
 '          <p>The morning is open until 11 &mdash; the working pocket for <b>Send on the Tim '
 'draft</b>, the <b>Cathy call</b> (twenty-three days), the <b>ATS nudge</b>, a reply to '
 '<b>Catherine Weir&rsquo;s UGM follow-up</b>, and the <b>Pipedrive review</b> if it fits. Then the '
 'run: <b>Mike at 11</b> in person at Gevity, <b>Stratus Networks at noon</b> (1,200 customers, Jr '
 'joins), <b>GigTel at 1</b> (80,000 customers; NetSapiens, FreeSwitch and reseller-structure asks; '
 'Jr and Carlos join), and <b>GamifyOS with Taylor 2:30&ndash;5:30</b> &mdash; her agenda: half '
 'Ashlyn (dashboard mockup for feedback), half Gamify (web page + community landing live by Wed Nov '
 '12, ahead of Friday&rsquo;s Review Crew hour); EquiStamp holds until Honor&rsquo;s Discord '
 'brain-dump. Evening open, weekend clear.</p>'
) + s[f1:]

# ---------- 9. FLAG 2 (On the wire) ----------
rep('<h3><span class="pill warn">On the wire</span> The Jeff threads, the Sahiti intro, and a Brand Kit in the Drive</h3>',
    '<h3><span class="pill warn">On the wire</span> Ben Cherry surfaced at LiveKit &mdash; plus Catherine Weir, the Sahiti intro, and the Jeff threads</h3>', 1)
w0 = s.find('<p><b>Jeff at Spectrum holds three threads</b>:')
w1 = s.find('</p>', w0) + len('</p>')
assert 0 < w0 < w1
s = s[:w0] + (
 '<p><b>Ben Cherry at LiveKit replied overnight</b> (12:44 AM) to Jr&rsquo;s October intro &mdash; '
 '&ldquo;would love to learn more about how I can help&rdquo; &mdash; a named human at LiveKit for '
 'the TCP/SIP-leg question and the GPT-Live BAA eligibility call; the thread is Jr&rsquo;s, with '
 'you and Eelco cc&rsquo;d. <b>Catherine Weir (365agents, with Rick &mdash; the UGM AI Showcase '
 'winners) followed up yesterday afternoon</b>: a warm note from a fellow NetSapiens-ecosystem AI '
 'builder &mdash; a reply is owed, and worth it. Still yours: <b>the Sahiti intro</b> (promised '
 'Tuesday &ldquo;in a separate email&rdquo;), <b>the CCI booking</b>, the <b>Whova three</b>, and '
 'the <b>booth bill</b>. <b>Jeff at Spectrum holds three threads</b>: SendGrid in progress (your '
 'drip campaign rides on it), the mail-server question folded in, and <b>ConnectWise credentials '
 'still block Illia</b>. Sentry&rsquo;s replay quota sits at 80% for the new period &mdash; same '
 'pattern as last month. The GPT-Live BAA call stays Jr&rsquo;s, now with a LiveKit human to put '
 'it to.</p>'
) + s[w1:]

# ---------- 10. MARKERS ----------
k0 = s.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
assert k0 > 0
k1 = s.find('<p', k0)
k2 = s.find('</p>', k1) + len('</p>')
assert 0 < k1 < k2
s = s[:k1] + (
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Thursday closed <b>10&ndash;5&ndash;3</b> '
 '&mdash; eighteen events, and <b>ten failures: the weekday record moved for the third straight day</b> '
 '(Monday eight, Wednesday nine, Thursday ten), with the evening burst arriving on script for the '
 'twenty-fifth weekday running. The pipeline: <b>Nortec agreed on terms Thursday 10:34 AM</b> &mdash; '
 'paperwork next; <b>two more resellers pitch today</b> (Stratus 1,200, GigTel 80,000); ATS&rsquo;s '
 'promised orders are two days overdue. <b>The Tim record is drafted and unsent</b> &mdash; one '
 'click closes day eighteen. The next engineering block is <b>Monday, 10&ndash;2</b>.</p>'
) + s[k2:]

# ---------- 11. COMING-UP week card ----------
c0 = s.find('<h4 style="font-size:14px">This week &mdash; Friday grew a three-hour Taylor session</h4>')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 '<h4 style="font-size:14px">This week &mdash; reseller Friday, a clear weekend, and an 8.5-hour Thursday ahead</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today (5h, all meetings): '
 '<b>Mike at 11</b>, <b>Stratus Networks at noon</b>, <b>GigTel at 1</b>, <b>GamifyOS with Taylor '
 '2:30&ndash;5:30</b>. The weekend is clear. Monday: sync 8, <b>DW Engineering 10&ndash;2</b> &mdash; '
 'the review queue&rsquo;s window (#886, #991, #992, #799, Illia&rsquo;s six, Pipedrive voxai-851) '
 '&mdash; TTT 2, Hand and Stone 8 PM. Tuesday: <b>Monthly Iris Sync 9</b> (the eight-days-past-due '
 'invoice and the drip/report commitments belong on its agenda), <b>Izzy 10</b> (the Levitt '
 'verdict&rsquo;s fifth chance &mdash; and the Tim record arrives done if the draft goes out today), '
 'DW Client 10&ndash;2, TTT 2. Wednesday: Ellie &times; Caroline &times; Taylor 10:30, DW '
 '11&ndash;3, TTT 3 &mdash; and <b>the GamifyOS web page + landing are due live</b>. Thursday Nov 12 '
 'is <b>the week&rsquo;s heaviest at 8.5h, over the 8h line</b>: DW 8:30&ndash;12:30, Scott Van Camp '
 'at 2, Reserved 3:30, <b>Friendsgiving 6&ndash;9 PM</b>. Friday Nov 13: Review Crew happy hour '
 '5:30. Carried: <b>the Cathy call</b> (twenty-three days), <b>the CCI booking</b>, the drip '
 'campaign and performance reports, the ATS five, the Whova trio, the Sahiti intro, and the '
 '<b>invoice &mdash; eight days past due</b>.</p>'
) + s[c1:]

# ---------- 12. INBOX LEAD ----------
splice('The Nortec thread turned yesterday:',
       'the 12:30&ndash;2 gap and the open evening are today&rsquo;s ground.',
 'The Nortec thread closed its loop yesterday: Tyler&rsquo;s 8:46 &ldquo;That work?&rdquo; and '
 '<b>Jr&rsquo;s 10:34 &ldquo;That works&rdquo;</b> &mdash; terms agreed, paperwork next. Overnight, '
 '<b>Ben Cherry at LiveKit replied</b> to Jr&rsquo;s October intro, offering help &mdash; a channel '
 'for the TCP/SIP and BAA questions. <b>Catherine Weir (365agents) followed up from UGM</b> &mdash; '
 'the AI Showcase winners, a warm reply owed. <b>Illia requested your review on the Pipedrive CRM '
 'PR</b> (voxai-851). And the one that matters most costs one click: <b>the Tim reply has sat in '
 'Drafts since 9:07 yesterday morning</b> &mdash; four test orders, the sheet wired in &mdash; send '
 'it and day eighteen closes. Still needing words: <b>Cathy at ProGraphix</b> (twenty-three days), '
 '<b>the CCI booking</b>, the <b>Whova three</b>, and the <b>Sahiti intro</b> &mdash; the open '
 'morning before 11 is today&rsquo;s ground.', incl_b=True)

# ---------- 13. CHART: roll to Fri Nov 6 - Thu Nov 12 ----------
rep('Thu Nov 5 &ndash; Wed Nov 11', 'Fri Nov 6 &ndash; Thu Nov 12', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(35.71% + 6px)">5</div>\n'
 '            <div class="seg m" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(50% + 6px)">7</div>\n'
 '            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>\n'
 '            <div class="seg m" style="height:28.57%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Thu</b>5</div><div><b>Fri</b>6</div>\n          <div><b>Sat</b>7</div><div><b>Sun</b>8</div><div><b>Mon</b>9</div><div><b>Tue</b>10</div><div><b>Wed</b>11</div>',
    '<div><b>Fri</b>6</div><div><b>Sat</b>7</div>\n          <div><b>Sun</b>8</div><div><b>Mon</b>9</div><div><b>Tue</b>10</div><div><b>Wed</b>11</div><div><b>Thu</b>12</div>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-06T06:55:00-06:00') == 2
assert s.count('window open') == 2
assert 'day seventeen' not in s and 'seven days past due' not in s
assert 'twenty-two days' not in s and 'Twenty-two days' not in s
assert 'Good evening' not in s and 'Thursday, November 5' not in s
assert 'Thu Nov 5 &ndash; Wed Nov 11' not in s
assert 'Drafts folder is still empty' not in s
assert 'That work?&rdquo; &mdash; a one-line answer closes it' not in s
assert 'quoter' not in s and 'hw7Mh6cK' not in s and 'pY3DM73R' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'bT5uDhjRSBk3' not in s and 'doxy.me/scottvlmft' not in s
assert 'atscall-frontline' not in s and 'sfw-mvnn-nfd' not in s and 'cjk-wubx-vna' not in s

open(p, 'w', encoding='utf-8').write(s)
print('friday full ok', len(s))
