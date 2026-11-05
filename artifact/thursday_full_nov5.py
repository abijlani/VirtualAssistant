# Thursday Nov 5, 2026 FULL morning pass (fired 6:13 AM CST).
# Overnight verified (16h trash incl): late NA 11:18 PM -> WEDNESDAY CLOSES 9-3-1
# (thirteen events; nine failures = heaviest weekday failure count on the ledger).
# Thursday opened 0-0-1: lone success 3:42 AM. cc-state EMPTY (no reactions).
# NORTEC: Tyler Wed 9:00 AM "we appreciate the concessions... one remaining sticking
# point" -> Jr Wed 2:25 PM: YES to the structure - $500 platform fee converts to a
# monthly minimum fully credited toward usage, one adjustment flagged transparently.
# Ball with Tyler/Nortec since 2:25 PM. One yes away.
# IRIS: Laura Wed 8:52 AM: "Thank you. I shared with the entire sales team."
# Invoice now SEVEN days past due (Oct 29), still no payment confirmation.
# PR CLEANUP overnight: #1073 MERGED (Pagebakers + cursor[bot] finished it - the
# screenshot ask dissolved), #721 merged (SPE-111), #809 merged, #805 closed,
# #609 closed ("revisit when we build the new vendor portal"). Remaining queue:
# #886, #991, #992, #799 (day sixty) + Illia's six.
# ATS: "doing this tomorrow" was yesterday - no orders visible. Five items stand.
# CALENDAR: TODAY Thu = DW Proj Eng 8:30-12:30 (4f), NEW Kyle/Taylor/Bodhi 2-3
# (wildlysatisfied), Honor/Taylor 3-3:30 (Equistamp), Reserved 3:30-4, Scott 4-5
# -> 7.0h. FRIDAY grew: Mike 11, GigTel 12-12:30, NEW GamifyOS working session
# w/ Taylor 2:30-5:30 at Gevity -> 4.5h. Friendsgiving Nov 12 now ACCEPTED.
# Jr shared "Voxtell AI Brand Kit" Drive folder Wed 12:13 PM (cc Sofia).
# Drafts still empty (Tim record day seventeen). Granola: no Nov 4 captures.
# Chart rolls Thu Nov 5 - Wed Nov 11.
# Substring hazards: ages run fifty-eight/fifty-nine/sixty - bump highest first;
# 'day fifty;' semicolon-anchored; 'day sixteen'/'day seventeen' clean.
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
rep('day fifty-nine', 'day sixty', 3)                          # #799
rep('day fifty-eight', 'day fifty-nine', 3)                    # Eric / Izzy trio
rep('night fifty-one', 'night fifty-two', 2)
rep('day fifty;', 'day fifty-one;', 1)                         # JDs
rep('fifty-three days past', 'fifty-four days past', 2)
rep('forty-three days past', 'forty-four days past', 1)        # Appulse
rep('twenty-one days past', 'twenty-two days past', 3)         # ProGraphix
rep('Twenty-one days past', 'Twenty-two days past', 2)
rep('(twenty-one days)', '(twenty-two days)', 2)
rep('day sixteen', 'day seventeen', 3)                         # Tim
# ('Fifteen days past the promise' was consumed by Wednesday's li2 splice - gone)
rep('Iris, day twenty-four', 'Iris, day twenty-five', 1)
rep('hr-nda is 79 days old', 'hr-nda is 80 days old', 1)
rep('Ages as of Nov 4', 'Ages as of Nov 5', 1)
rep('six days past due', 'seven days past due', 5)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-04T21:08:00-06:00', '2026-11-05T06:55:00-06:00', 2)
rep('<b>Brief compiled</b> Wed 6:55 AM &middot; data checked Wed 9:08 PM CT',
    '<b>Brief compiled</b> Thu 6:55 AM &middot; data checked Thu 6:55 AM CT', 1)
rep('Wednesday, November 4 &middot; 2026', 'Thursday, November 5 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Nortec answers this morning.')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Nortec is one yes away. Tyler came back yesterday at 9 AM &mdash; &ldquo;we appreciate the '
 'concessions&rdquo; &mdash; with <b>one remaining sticking point</b>, and <b>Jr answered at 2:25 PM: '
 'yes to their structure</b> &mdash; the $500 platform fee converts to a monthly minimum fully '
 'credited toward usage, with one adjustment flagged transparently. <b>The ball has been with Tyler '
 'since; watch the thread and answer fast.</b> Overnight gift: <b>Pagebakers merged #1073 himself</b> '
 '&mdash; the screenshot ask dissolved &mdash; plus <b>#721 and #809</b>, and closed #805 and #609: '
 'both of your changes-requested PRs cleared without you. At Spectrum, <b>Laura shared your Lakeland '
 'case study with the entire sales team</b> (8:52 AM yesterday); the drip campaign and performance '
 'reports are still yours, and the <b>invoice is seven days past due</b>. ATS: &ldquo;doing this '
 'tomorrow&rdquo; was yesterday and <b>no orders are visible yet</b> &mdash; the five items stand, '
 'pricing confirmation first. Today is the engineering day: <b>DW 8:30&ndash;12:30</b>, the window '
 'the review stack waited for, then <b>Kyle / Taylor at 2 (new), Honor at 3, Scott at 4</b>. Friday '
 'grew: <b>GigTel at noon plus a three-hour GamifyOS session with Taylor, 2:30&ndash;5:30</b>. '
 'Wednesday closed <b>9&ndash;3&ndash;1</b> &mdash; nine failures, the heaviest weekday count on the '
 'ledger. No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Wednesday + open Thursday ----------
rep('<b>9&ndash;2&ndash;1 by 9:08, window open</b>, quiet since 8:06; nine failures passes '
    'Monday&rsquo;s eight as the heaviest weekday failure count on the ledger.',
    '<b>9&ndash;2&ndash;1 by 9:08</b>, then a late needs-attention at 11:18 PM &mdash; <b>Wednesday '
    'closes 9&ndash;3&ndash;1</b>, thirteen events, verified Thursday morning with trash included; '
    'nine failures passes Monday&rsquo;s eight as the heaviest weekday failure count on the ledger. '
    'Thursday opened with a lone success at 3:42 AM &mdash; <b>0&ndash;0&ndash;1 by 6:55, window '
    'open</b>.', 1)

# ---------- 5. "Needs a decision" note ----------
rep('Nortec&rsquo;s answer lands this morning and ATS submits its beta orders today &mdash; the HOLD at 10:30 is the reply pocket',
    'Nortec&rsquo;s yes is the watch item &mdash; Jr matched their structure at 2:25 yesterday; answer fast if Tyler replies mid-block', 1)

# ---------- 6. TODAY SCHEDULE ----------
rep('Taylor&rsquo;s double-header 11&ndash;3 &mdash; the HOLD at 10:30 is the Nortec pocket',
    'Four hours of engineering, then four calls &mdash; the 12:30&ndash;2 gap is the pocket', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot"><div class="t">8:30&ndash;12:30</div><div class="w">DW: Project Engineering<small>The review window: #886, #991, #992, #799 + Illia&rsquo;s six &mdash; and the Oracle tabs + Tim record</small></div></div>\n'
 '        <div class="slot free"><div class="t">12:30&ndash;2:00</div><div class="w">Open pocket<small>The Cathy call (twenty-two days, phone not email) and the ATS pricing confirmation</small></div></div>\n'
 '        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Kyle / Taylor / Bodhi<small>New &mdash; booked yesterday</small></div></div>\n'
 '        <div class="slot"><div class="t">3:00&ndash;3:30</div><div class="w">Honor / Taylor / Bodhi<small>Equistamp</small></div></div>\n'
 '        <div class="slot"><div class="t">3:30&ndash;4:00</div><div class="w">Reserved<small>Buffer between the calls</small></div></div>\n'
 '        <div class="slot"><div class="t">4:00&ndash;5:00</div><div class="w">Scott<small>Weekly 1:1</small></div></div>\n'
 '        <div class="slot free"><div class="t">After 5</div><div class="w">Open evening<small>Friday opens with Mike at 11 and GigTel at noon</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 7. TOP 5 ----------
rep('<span class="note">Nortec and ATS first &mdash; both move today</span>',
    '<span class="note">Watch Nortec &mdash; and spend the block on the review queue</span>', 1)

# li1: Nortec - one yes away
splice('<h4>Nortec answers this morning &mdash; Tyler is reviewing your counter with Steve right now</h4>',
       '</div></li>',
 '<h4>Nortec is one yes away &mdash; Jr matched their structure yesterday; the ball is with Tyler</h4>\n'
 '          <p class="why">Tyler&rsquo;s 9 AM reply was warm &mdash; &ldquo;we appreciate the '
 'concessions&rdquo; &mdash; with <b>one remaining sticking point</b>: the $500 platform fee. <b>Jr '
 'answered at 2:25 PM and gave it to them</b> &mdash; the $500 converts to a <b>monthly minimum '
 'fully credited toward usage</b>, with one adjustment flagged transparently rather than buried. '
 'Nothing has come back since, so the deal sits with Tyler and Steve with every objection answered: '
 'price countered Tuesday, structure matched Wednesday. The Monday context still frames it &mdash; '
 '300 customers, Cairo actively coming out, a halted demo program waiting on a replacement. '
 '<b>Yours: watch the thread and answer fast</b>, even from inside the engineering block. Still '
 'unbooked behind it: <b>Michael at CCI&rsquo;s call</b>.</p>\n'
 '          <div class="meta"><span class="pill crit">Ball with Nortec since 2:25 PM</span><span class="pill good">Structure matched</span></div>\n'
 '        ')

# li2: ATS - orders not visible yet
splice('<h4>ATS went from testing to buying &mdash; three beta accounts are queued, and five items are yours</h4>',
       '</div></li>',
 '<h4>ATS: &ldquo;doing this tomorrow&rdquo; was yesterday &mdash; and no orders are visible yet</h4>\n'
 '          <p class="why">Tuesday&rsquo;s onboarding queued <b>three beta accounts</b> (Integrity '
 'Property Management, LaParkin, Environmental Pest Solutions &mdash; two months free), and Jamie '
 'said &ldquo;we&rsquo;re doing this tomorrow.&rdquo; That was yesterday, and <b>no order traffic '
 'has shown up</b> &mdash; either they slipped a day or the orders are coming through a channel you '
 'haven&rsquo;t seen. The five items are still yours and the <b>bundle-pricing confirmation</b> '
 '($450 for 1,000 minutes, $295 for 500; overage TBD) is the one that blocks them: after it, the '
 '<b>SIP-trace 404 to engineering</b>, <b>Bandwidth app instructions</b> for Jamie, the '
 '<b>anonymized one-pagers</b>, and tag-teaming the first deployments with Jr. The 12:30&ndash;2 '
 'gap fits the pricing note.</p>\n'
 '          <div class="meta"><span class="pill warn">Orders due, none visible</span><span class="pill warn">Pricing confirm blocks the rest</span></div>\n'
 '        ')

# li3: Iris - case study with the whole sales team
splice('<h4>The Lakeland revision shipped last night &mdash; and the Iris session restocked your list</h4>',
       '</div></li>',
 '<h4>Laura shared the case study with the entire sales team &mdash; and the invoice hits seven days past due</h4>\n'
 '          <p class="why"><b>Laura&rsquo;s reply landed yesterday at 8:52 AM: &ldquo;Thank you. I '
 'shared with the entire sales team.&rdquo;</b> Your revised Lakeland case study (15% of 40,129 '
 'calls handled end to end) is now in front of every Spectrum seller &mdash; which raises the '
 'stakes on what you still owe: the <b>five-email drip campaign</b> (riding Jeff&rsquo;s SendGrid '
 'integration, in progress) and the <b>performance reports for the high-volume accounts</b> '
 '(McCallum, McNeil Chevrolet, Diamond Hawk&hellip;); <b>notification-per-agent is promised for '
 'next week</b>. Laura and Jason take the Hubler reports to John Gerhardt; Grayson chases '
 'Lakeland&rsquo;s name approval. The <b>$5,000 invoice is seven days past due (Oct 29)</b> &mdash; '
 'still no payment confirmation, and the sales-team share is a natural hook to ask on.</p>\n'
 '          <div class="meta"><span class="pill good">Case study with full sales team</span><span class="pill crit">Invoice seven days past due</span></div>\n'
 '        ')

# li4 Cathy: slot update (ages bumped globally)
rep('today&rsquo;s TTT hour at 3 is the slot',
    'today&rsquo;s 12:30&ndash;2 gap after the engineering block is the slot', 1)
rep('Call, not email &middot; TTT at 3', 'Call, not email &middot; 12:30 gap', 1)

# li5: reviews - the queue shrank overnight
splice('<h4>#799 at day sixty &mdash; the Tim thread revived, and the review stack waits on tomorrow&rsquo;s block</h4>',
       '</div></li>',
 '<h4>The queue shrank overnight &mdash; Pagebakers merged #1073, #721 and #809; today&rsquo;s block takes the rest</h4>\n'
 '          <p class="why">While you slept, <b>Pagebakers finished and merged #1073</b> (he and '
 'cursor[bot] pushed the fixes &mdash; the screenshot ask dissolved), merged <b>#721</b> (your old '
 'SPE-111 insights-dates PR) and <b>#809</b>, and closed <b>#805</b> and <b>#609</b> (&ldquo;revisit '
 'when we build the new vendor portal&rdquo;). Both of your changes-requested PRs are cleared '
 'without a line from you. What&rsquo;s left for <b>today&rsquo;s 8:30&ndash;12:30 block</b>: '
 '<b>#886, #991, #992, Illia&rsquo;s six</b>, and <b>#799 at day sixty</b>. The Izzy side rides '
 'along: <b>confirm which Oracle tabs Izzy reads</b> for Tim (his record is at day seventeen and '
 'the written record is still unsent), and the Levitt verdict is still unrecorded &mdash; iz-10dlc '
 'stays open.</p>\n'
 '          <div class="meta"><span class="pill good">#1073 + #721 + #809 merged</span><span class="pill warn">Block today 8:30&ndash;12:30</span></div>\n'
 '        ')

# ---------- 8. FLAG 1 (Today) ----------
f0 = s.find('<h3><span class="pill warn">Today</span> Taylor&rsquo;s double-header &mdash; with Nortec and ATS landing in the gaps</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> The engineering day &mdash; four hours of block, then four calls back to back</h3>\n'
 '          <p><b>DW: Project Engineering 8:30&ndash;12:30</b> is the window the review stack has '
 'waited on all week &mdash; #886, #991, #992, #799 and Illia&rsquo;s six, plus the Oracle-tabs '
 'confirmation and the Tim record if the queue moves fast. <b>The 12:30&ndash;2 gap is the working '
 'pocket</b>: the Cathy call (twenty-two days, phone not email) and the ATS pricing confirmation. '
 'Then the afternoon stacks: <b>Kyle / Taylor at 2</b> (new &mdash; booked yesterday), <b>Honor / '
 'Taylor at 3</b> (Equistamp), Reserved at 3:30, <b>Scott at 4</b>. If Nortec answers mid-block, '
 '<b>answer anyway</b> &mdash; the deal is one yes away. Evening open.</p>'
) + s[f1:]

# ---------- 9. FLAG 2 (On the wire) ----------
rep('<h3><span class="pill warn">On the wire</span> The Jeff threads, the Sahiti intro, and the UGM tail</h3>',
    '<h3><span class="pill warn">On the wire</span> The Jeff threads, the Sahiti intro, and a Brand Kit in the Drive</h3>', 1)
w0 = s.find('<p><b>Jeff at Spectrum now holds three threads</b>:')
w1 = s.find('</p>', w0) + len('</p>')
assert 0 < w0 < w1
s = s[:w0] + (
 '<p><b>Jeff at Spectrum holds three threads</b>: the SendGrid integration is <b>in progress</b> '
 '(your drip campaign rides on it), the mail-server question folds into it, and <b>ConnectWise '
 'credentials still block Illia&rsquo;s integration</b>. Two warm loops are still yours: <b>the '
 'Sahiti intro</b> (promised Tuesday &ldquo;in a separate email&rdquo;, still not visible) and '
 '<b>Jeff Pulver&rsquo;s note</b> &mdash; the vCon briefing and VON Policy Summit seat. New in the '
 'Drive: <b>Jr shared the &ldquo;Voxtell AI Brand Kit&rdquo; folder</b> yesterday (Sofia cc&rsquo;d) '
 '&mdash; worth a look before the one-pagers. Sentry flagged the <b>replay quota at 80%</b> for the '
 'new billing period &mdash; same pattern as last month. UGM tail: the <b>booth bill is still '
 'unconfirmed</b> and the <b>Whova three</b> still wait; the GPT-Live BAA call stays Jr&rsquo;s. '
 '(RingLogix &mdash; the competitor Tim named &mdash; is running a CodeFest victory lap in its '
 'marketing mail; noted, skipped.)</p>'
) + s[w1:]

# ---------- 10. MARKERS ----------
k0 = s.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
assert k0 > 0
k1 = s.find('<p', k0)
k2 = s.find('</p>', k1) + len('</p>')
assert 0 < k1 < k2
s = s[:k1] + (
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Wednesday closed <b>9&ndash;3&ndash;1</b> '
 '&mdash; thirteen events, a late needs-attention at 11:18 PM, and <b>nine failures: the heaviest '
 'weekday failure count on the ledger</b> (the six-failure evening burst was the twenty-fourth '
 'straight weekday evening). Thursday opened with a 3:42 AM success. The pipeline: <b>Nortec is one '
 'yes away</b>, ATS orders are due but not visible, and <b>GigTel &mdash; 80,000 customers &mdash; '
 'books tomorrow at noon</b>. The review queue <b>shrank overnight</b> (#1073, #721, #809 merged) '
 'and today&rsquo;s 8:30&ndash;12:30 block takes the rest.</p>'
) + s[k2:]

# ---------- 11. COMING-UP week card ----------
c0 = s.find('<h4 style="font-size:14px">This week &mdash; the pipeline stacks onto Friday noon</h4>')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 '<h4 style="font-size:14px">This week &mdash; Friday grew a three-hour Taylor session</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today (7h): <b>DW '
 'Engineering 8:30&ndash;12:30</b>, then Kyle / Taylor 2 (new), Honor / Taylor 3, Reserved 3:30, '
 'Scott 4. Friday (4.5h, all meetings): <b>Mike at 11</b>, <b>GigTel at noon</b> &mdash; 80,000 '
 'customers, white-label resellers, NetSapiens + FreeSwitch asks; Jr and Carlos join &mdash; and the '
 'new <b>GamifyOS working session with Taylor, 2:30&ndash;5:30 at Gevity</b>. The weekend is clear. '
 'Next week: sync Mon 8, DW Engineering Mon 10&ndash;2, Hand and Stone Mon 8 PM; <b>Monthly Iris '
 'Sync Tue Nov 10, 9</b>, Izzy 10, DW Client 10&ndash;2; <b>Ellie &times; Caroline &times; Taylor '
 'Wed Nov 11, 10:30</b> ahead of the engineering block (11&ndash;3); Thu Nov 12: DW 8:30, Scott 2, '
 '<b>Friendsgiving 6&ndash;9 PM &mdash; now accepted</b>; Fri Nov 13: Review Crew happy hour 5:30. '
 'Carried: <b>the Cathy call</b> (twenty-two days), <b>the Tim record</b> (day seventeen), <b>the '
 'CCI booking</b>, the drip campaign and performance reports, the ATS five, the review queue (#886, '
 '#991, #992, #799 + Illia&rsquo;s six), the Whova trio, and the <b>invoice &mdash; seven days past '
 'due</b>.</p>'
) + s[c1:]

# ---------- 12. INBOX LEAD ----------
splice('The Nortec thread ran all Tuesday:',
       'the HOLD at 10:30 and the post-4:15 evening are today&rsquo;s ground.',
 'The Nortec thread turned yesterday: Tyler at 9 AM (&ldquo;we appreciate the concessions&rdquo;, '
 'one sticking point) and <b>Jr&rsquo;s 2:25 PM answer matching their structure</b> &mdash; the '
 'ball is with Tyler now. <b>Laura at 8:52 AM: the Lakeland case study went to the entire Spectrum '
 'sales team.</b> Overnight, <b>Pagebakers merged #1073, #721 and #809</b> and closed #805 and #609 '
 '&mdash; both of your changes-requested PRs cleared without you. <b>Jr shared the Voxtell AI Brand '
 'Kit folder</b>. Still not visible: <b>the Sahiti intro</b> (promised Tuesday &ldquo;in a separate '
 'email&rdquo;) and any ATS order. The Drafts folder is still empty &mdash; the Tim record stays '
 'unwritten at day seventeen. Still needing words: <b>Cathy at ProGraphix</b> (twenty-two days), '
 '<b>the CCI booking</b>, and the <b>Whova three</b> &mdash; the 12:30&ndash;2 gap and the open '
 'evening are today&rsquo;s ground.', incl_b=True)

# ---------- 13. IRIS CARD ----------
splice('Tuesday&rsquo;s session was a working one: LeVarr runs customer PDFs',
       'Monthly Iris Sync lands Tue Nov 10, 9&ndash;9:30</b>.',
 '<b>Laura shared your Lakeland case study with the entire sales team</b> &mdash; her reply landed '
 'yesterday at 8:52 AM. The numbers it carries: <b>Lakeland 40,129 calls, 15% handled end to '
 'end</b>; Hubler&rsquo;s reports (15,331 calls, 3,883 bookings) go to John Gerhardt via <b>Laura '
 'and Jason</b>; Grayson chases Lakeland&rsquo;s name approval. Still yours: the <b>five-email drip '
 'campaign</b> (on Jeff&rsquo;s SendGrid rails, in progress) and the <b>performance reports for '
 '5&ndash;10 high-volume accounts</b> (McCallum, McNeil Chevrolet, Diamond Hawk&hellip;); '
 '<b>notification-per-agent ships next week</b> per your own commitment. The <b>invoice is seven '
 'days past due (Oct 29), no payment confirmation</b> &mdash; the sales-team share is the natural '
 'hook to ask on. The <b>Monthly Iris Sync lands Tue Nov 10, 9&ndash;9:30</b>.', incl_b=True)

# ---------- 14. CHART: roll to Thu Nov 5 - Wed Nov 11 ----------
rep('Wed Nov 4 &ndash; Tue Nov 10', 'Thu Nov 5 &ndash; Wed Nov 11', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(50% + 6px)">7</div>\n'
 '            <div class="seg m" style="height:17.86%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(32.14% + 6px)">4.5</div>\n'
 '            <div class="seg m" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(50% + 6px)">7</div>\n'
 '            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Wed</b>4</div><div><b>Thu</b>5</div>\n          <div><b>Fri</b>6</div><div><b>Sat</b>7</div><div><b>Sun</b>8</div><div><b>Mon</b>9</div><div><b>Tue</b>10</div>',
    '<div><b>Thu</b>5</div><div><b>Fri</b>6</div>\n          <div><b>Sat</b>7</div><div><b>Sun</b>8</div><div><b>Mon</b>9</div><div><b>Tue</b>10</div><div><b>Wed</b>11</div>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-05T06:55:00-06:00') == 2
assert s.count('window open') == 2
assert 'day sixteen' not in s and 'six days past due' not in s
assert 'twenty-one days' not in s and 'Twenty-one days' not in s
assert 'Good evening' not in s and 'Wednesday, November 4' not in s
assert 'Wed Nov 4 &ndash; Tue Nov 10' not in s
assert 'HOLD at 10:30' not in s and 'double-header' not in s
assert 'answers this morning' not in s
assert 'quoter' not in s and 'hw7Mh6cK' not in s and 'pY3DM73R' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'bT5uDhjRSBk3' not in s and 'doxy.me/scottvlmft' not in s
assert 'atscall-frontline' not in s and 'wildlysatisfied' not in s

open(p, 'w', encoding='utf-8').write(s)
print('thursday full ok', len(s))
