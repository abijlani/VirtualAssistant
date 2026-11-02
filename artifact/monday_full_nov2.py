# Monday Nov 2, 2026 FULL morning pass (weekday trigger, fired 6:20 AM CST).
# Verified overnight (16h, trash included): Sunday closed 6-2-6 retroactively — the
# 10 PM close never fired; nothing landed after the 5:15 PM success. Monday opened
# 1-0-1 (failure 6:02 AM, success 6:11 AM). cc-state EMPTY — no reactions to merge.
# Big movers: the Friday blast CONVERTED (Steve Myhre / Nortec booked today 1-1:30);
# Friday's Iris session notes landed (Ask Iris live demo 1,880 calls / 89.1%, trial
# 7->14 days, Hubler resolved live -> Bodhi owes the Hubler call-performance report,
# the Lakeland case study, and the Jeff mail-server follow-up); Saturday 2:53 PM the
# 10/30 minutes went to the full Spectrum team. Calendar: DW moved to 9-1 (was 10-2),
# Vercel webinar ACCEPTED 10:45-11:30 inside it, weBreathe 3:30-4:30 needsAction
# (schedule only), Tuesday is the new 10h peak, Wednesday eased to 7.25h (engineering
# block moved to Nov 11). Chart rolls Mon Nov 2 - Sun Nov 8.
# SUBSTRING HAZARDS for future bumps: 'weekday thirteen' x2 contains 'day thirteen';
# 'opening-Sunday fourteen' contains 'day fourteen' — Tuesday's Tim bump must use
# rx(r'(?<!Sun)day fourteen', 'day fifteen', n) style anchors.
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

# ---------- 1. GLOBAL AGE BUMPS (highest first) ----------
rep('day fifty-six', 'day fifty-seven', 3)                    # #799
rep('day fifty-five', 'day fifty-six', 3)                     # Eric / Izzy trio
rep('night forty-eight', 'night forty-nine', 2)               # before JD bump creates forty-eight
rep('day forty-seven;', 'day forty-eight;', 1)                # JDs
rep('fifty days past', 'fifty-one days past', 2)
rep('forty days past', 'forty-one days past', 1)              # Appulse
rep('eighteen days past', 'nineteen days past', 5)            # ProGraphix / Cathy
rep('Eighteen days past', 'Nineteen days past', 1)
rep('(eighteen days)', '(nineteen days)', 3)
rx(r'(?<!week)day thirteen', 'day fourteen', 4)               # Tim ('weekday thirteen' x2 stays)
rep('Twelve days past the promise', 'Thirteen days past the promise', 1)
rep('Iris, day twenty-one', 'Iris, day twenty-two', 1)
rep('hr-nda is 76 days old', 'hr-nda is 77 days old', 1)
rep('Ages as of Nov 1', 'Ages as of Nov 2', 1)
rep('is three days past due (Oct 29)', 'is four days past due (Oct 29)', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-01T21:08:00-06:00', '2026-11-02T06:55:00-06:00', 2)
rep('<b>Brief compiled</b> Sun 7:13 AM &middot; data checked Sun 9:08 PM CT',
    '<b>Brief compiled</b> Mon 6:55 AM &middot; data checked Mon 6:55 AM CT', 1)
rep('Sunday, November 1 &middot; 2026', 'Monday, November 2 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Halloween closed <b>3&ndash;0&ndash;0</b>')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'The Friday blast is converting: <b>Steve Myhre at Nortec booked a 30-minute demo for today, '
 '1&ndash;1:30</b>, and a <b>Voxtell AI Onboarding call landed on Tuesday at 11</b>. Friday&rsquo;s '
 'Iris session turned out to be a working one &mdash; <b>Ask Iris demoed live</b> (1,880 calls, 89.1% '
 'success), the trial moved to 14 days &mdash; and it left <b>three deliverables with your name on '
 'them</b>: the <b>Hubler call-performance report</b> (Alex&rsquo;s voicemail to the channel partner '
 'went unanswered; the report is the new opening move), the <b>Lakeland case study with visuals</b>, '
 'and the <b>Jeff follow-up on mail-server config</b> &mdash; agent emails must send from a '
 'SpectrumVoIP address. Saturday&rsquo;s minutes went to the whole team. Sunday spiked again &mdash; '
 'closed <b>6&ndash;2&ndash;6</b>, fourteen events, the fourth Sunday running &mdash; and Monday '
 'opened split (a failure at 6:02, a success at 6:11). Today: sync at 8, <b>engineering 9&ndash;1</b> '
 'with the accepted Vercel webinar at 10:45 sitting inside it &mdash; one of the two gives way &mdash; '
 'then <b>Nortec at 1</b>. You also cleared Wednesday: the engineering block moved to Nov 11, so '
 'Taylor&rsquo;s double-header stands alone. Still carried: <b>the Cathy call</b> (nineteen days '
 'past), <b>the Tim record on day fourteen</b>, <b>the CCI call booking</b>, and the Iris <b>invoice '
 '&mdash; four days past due</b>. No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Sunday retroactively + open Monday ----------
rep('tying the opening-Sunday spike &mdash; window open.',
    'tying the opening-Sunday spike. Nothing landed after the 5:15 success &mdash; verified Monday '
    'morning with trash included (the 10 PM close never ran). <b>Sunday closes 6&ndash;2&ndash;6</b> '
    '&mdash; fourteen events, the fourth consecutive Sunday spike, and the two needs-attention were '
    'the first in a week. Monday opened split: a failure at 6:02, a success at 6:11 &mdash; '
    '<b>1&ndash;0&ndash;1 by 6:55, window open</b>.', 1)

# ---------- 5. TODAY SCHEDULE ----------
rep('Open Sunday &mdash; one unaccepted invite at 1; the week starts Monday at 8',
    '6h booked &mdash; sync at 8, engineering 9&ndash;1, Nortec at 1; one unaccepted invite at 3:30', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot"><div class="t">8:00&ndash;8:45</div><div class="w">Weekly Product Sync<small>The week opener &mdash; Jr and Eelco</small></div></div>\n'
 '        <div class="slot"><div class="t">9:00&ndash;1:00</div><div class="w">DW (Engineering)<small>Moved up from 10&ndash;2 &mdash; four clear hours, except for the webinar below</small></div></div>\n'
 '        <div class="slot"><div class="t">10:45&ndash;11:30</div><div class="w">Leading with AI webinar (Vercel)<small>Accepted &mdash; sits inside the engineering block; keep one, concede the other</small></div></div>\n'
 '        <div class="slot"><div class="t">1:00&ndash;1:30</div><div class="w">Steve Myhre &mdash; Nortec<small>The first booking off Friday&rsquo;s blast &mdash; a demo ask from the booth list</small></div></div>\n'
 '        <div class="slot free"><div class="t">1:30&ndash;3:30</div><div class="w">Open<small>The queue&rsquo;s first pocket: the Cathy call, the Tim record, the CCI booking, the Hubler report pull</small></div></div>\n'
 '        <div class="slot"><div class="t">3:30&ndash;4:30</div><div class="w">weBreathe<small>Invite still unaccepted &mdash; on the schedule, out of the chart</small></div></div>\n'
 '        <div class="slot free"><div class="t">After 4:30</div><div class="w">Open evening<small>Tuesday runs ten hours &mdash; tonight is the recovery slot</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 6. CHART: roll to Mon Nov 2 - Sun Nov 8 ----------
rep('Sun Nov 1 &ndash; Sat Nov 7', 'Mon Nov 2 &ndash; Sun Nov 8', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:28.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(71.43% + 6px)">10</div>\n'
 '            <div class="seg m" style="height:35.71%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(51.79% + 6px)">7.25</div>\n'
 '            <div class="seg m" style="height:41.07%"></div><div class="seg f" style="height:7.14%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(39.29% + 6px)">5.5</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Sun</b>1</div><div><b>Mon</b>2</div>\n          <div><b>Tue</b>3</div><div><b>Wed</b>4</div><div><b>Thu</b>5</div><div><b>Fri</b>6</div><div><b>Sat</b>7</div>',
    '<div><b>Mon</b>2</div><div><b>Tue</b>3</div>\n          <div><b>Wed</b>4</div><div><b>Thu</b>5</div><div><b>Fri</b>6</div><div><b>Sat</b>7</div><div><b>Sun</b>8</div>', 1)

# ---------- 7. FLAG 1 (Today) ----------
f0 = s.find('<h3><span class="pill warn">Today</span> Recovery Sunday &mdash; one decision: the 1 PM build session</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Monday &mdash; the follow-through week opens, and the blast already converted</h3>\n'
 '          <p>Sync at 8, then <b>engineering 9&ndash;1</b> with a decision inside it: the <b>Vercel '
 '&ldquo;Leading with AI&rdquo; webinar (10:45&ndash;11:30) is accepted</b> and sits in the middle of '
 'the block &mdash; keep one, concede the other. At <b>1, Steve Myhre of Nortec</b>: the first '
 'conversion off Friday&rsquo;s blast, a demo ask off the booth list. The <b>1:30&ndash;3:30 '
 'pocket</b> is the queue&rsquo;s first slot of the week &mdash; <b>the Cathy call</b> (nineteen '
 'days), <b>the Tim record</b> (day fourteen), <b>the CCI booking</b>, and the Hubler report pull. '
 'weBreathe at 3:30 is still unaccepted &mdash; schedule only. Tonight stays open; Tuesday runs ten '
 'hours.</p>'
) + s[f1:]

# ---------- 8. FLAG 2 (On the wire) ----------
rep('<h3><span class="pill warn">On the wire</span> UGM wrapped &mdash; and Wednesday&rsquo;s calendar moved underneath you</h3>',
    '<h3><span class="pill warn">On the wire</span> UGM loose ends &mdash; plus two new wires from Friday&rsquo;s session</h3>', 1)
rep('And the calendar moved under Wednesday: <b>Taylor&rsquo;s GamifyOS working session (Nov 4, 1&ndash;3) landed on top of the kickoff (11&ndash;1)</b>, burying the 11&ndash;3 engineering block &mdash; Nov 4 now reads 10.5h; if the engineering block matters that week, it has to move.',
    'The Wednesday collision resolved your way: <b>the engineering block moved off Nov 4</b> (it '
    'reappears Wed Nov 11, 11&ndash;3), so Taylor&rsquo;s double-header &mdash; kickoff 11&ndash;1, '
    'GamifyOS 1&ndash;3 &mdash; stands alone with a HOLD at 10:30, and the day eases to 7.25h. Two new '
    'wires from Friday&rsquo;s session: <b>agent emails must send from a SpectrumVoIP address</b> (the '
    'Jeff follow-up is yours) and <b>notification splitting by agent</b> is now on the Voxtell to-do '
    'list &mdash; Alex has absorbed some thirty thousand notification emails.', 1)

# ---------- 9. MARKERS ----------
rep('Halloween closed 3&ndash;0&ndash;0 (three evening failures, no successes) and Sunday opened with successes only. <b>The follow-up blast shipped Friday evening</b>; Monday starts the follow-through week. The next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.',
    'Sunday closed 6&ndash;2&ndash;6 &mdash; fourteen events, the fourth Sunday spike in a row &mdash; '
    'and Monday opened split (failure 6:02, success 6:11). <b>The blast converted: Nortec demos today '
    'at 1.</b> The next engineering block is <b>today, 9&ndash;1</b>.', 1)

# ---------- 10. COMING-UP ----------
c0 = s.find('<h4 style="font-size:14px">Sunday &mdash; one invite; then a loaded week</h4>')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 '<h4 style="font-size:14px">This week &mdash; the conversions stack onto a ten-hour Tuesday</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: sync 8, <b>DW '
 'Engineering 9&ndash;1</b> (Vercel webinar 10:45 inside it), <b>Nortec 1&ndash;1:30</b>, weBreathe '
 '3:30 unaccepted. Tuesday is the new wall at <b>10 hours</b>: Izzy 10, <b>Voxtell AI Onboarding '
 '11&ndash;12</b> (new, inside the client block), <b>Iris session 1&ndash;2</b>, TTT 2&ndash;3, Parr '
 'PT 3:30 with the drive blocks around it. Wednesday eased to 7.25h: SA 9:30, HOLD 10:30, <b>Taylor '
 'kickoff 11&ndash;1 + GamifyOS 1&ndash;3</b> &mdash; the engineering block moved to Nov 11. Thursday: '
 'DW 8:30&ndash;12:30, Scott at 4. The weekend is clear; <b>Monthly Iris Sync lands Nov 10</b>. '
 'Carried: <b>the Cathy call</b> (nineteen days), <b>the Tim record</b> (day fourteen), <b>the CCI '
 'booking</b>, the Hubler report and Lakeland case study, the review queue (#886, #991, #992, #799), '
 'the Whova trio, and the <b>invoice &mdash; four days past due</b>.</p>'
) + s[c1:]

# ---------- 11. INBOX LEAD ----------
rep('Friday evening delivered: <b>the UGM follow-up blast went out 6:13&ndash;6:27 PM</b> &mdash; fifteen-plus personalized sends off the 55-lead list, <b>Dynalink included</b>. Still queued: <b>the CCI call booking</b> (Michael asked for a call; no CCI send is visible in the blast), <b>the Hubler confirm</b> (the draft left drafts with no email sent), and the <b>Tim record</b>. Still needing words: <b>Cathy at ProGraphix</b> (nineteen days) and the <b>Whova three</b> &mdash; Monday morning is the next pocket &mdash; the first free one of UGM week.',
    'The blast is converting: <b>Steve Myhre at Nortec booked a demo &mdash; today, 1&ndash;1:30</b> '
    '&mdash; the first booking off the fifteen-plus Friday sends, and a <b>Voxtell AI Onboarding call '
    'landed on Tuesday at 11</b>. Saturday 2:53 PM you sent the <b>10/30 minutes to the whole Spectrum '
    'team</b>. Still queued: <b>the CCI call booking</b> (Michael asked for a call; no CCI send went '
    'out), <b>the Tim record</b>, and the three Friday-session deliverables &mdash; the Jeff '
    'mail-server follow-up, the Hubler performance report, the Lakeland case study. Still needing '
    'words: <b>Cathy at ProGraphix</b> (nineteen days) and the <b>Whova three</b> &mdash; the '
    '1:30&ndash;3:30 gap after Nortec is today&rsquo;s pocket.', 1)

# ---------- 12. TOP5 #3 HUBLER -> deliverables ----------
h0 = s.find('<h4>Laura&rsquo;s new ask: reach out to the Hubler channel partner &mdash; an Iris refresh for their two active agents</h4>')
h1 = s.find('</p>', h0) + len('</p>')
assert 0 < h0 < h1
s = s[:h0] + (
 '<h4>Hubler moved from an email to deliverables: the performance report and the Lakeland case study are yours</h4>\n'
 '          <p class="why">Friday&rsquo;s session settled it live: <b>Alex owns the channel-partner '
 'outreach</b> &mdash; he voicemailed the partner and got no response &mdash; and the opening move is '
 'now data. <b>You owe the Hubler call-performance report</b> for the one live location (&ldquo;'
 'here&rsquo;s what you&rsquo;re not leveraging&rdquo; across the other thirteen &mdash; Hubler runs '
 'fourteen dealerships on one Iris agent) and <b>the Lakeland case study with visuals</b> Laura wants '
 'beside it. Saturday&rsquo;s minutes to the team confirmed the split. Today&rsquo;s 1:30&ndash;3:30 '
 'pocket or tomorrow&rsquo;s client block fits the report pull; the next session is <b>Tuesday '
 '1&ndash;2</b>. The <b>$5,000 invoice is four days past due (Oct 29) &mdash; no payment confirmation '
 'has landed</b>.</p>'
) + s[h1:]
rep('<span class="pill warn">Draft gone, no send &mdash; confirm Monday</span>',
    '<span class="pill warn">Two reports owed &middot; set Friday</span>', 1)

# ---------- 13. TOP5 #4 blast/CCI ----------
rep('Mostly DONE: <b>the follow-up blast went out Friday evening</b> &mdash; David at Dynalink got his at 6:17 PM, alongside fifteen-plus sends off the 55-lead list. Still open: <b>Michael at CCI asked for a call, not an email</b>, and no CCI send is visible in the blast &mdash; Monday is the booking window for that call.',
    'The blast is CONVERTING: <b>Steve Myhre at Nortec booked a 30-minute demo &mdash; today, '
    '1&ndash;1:30</b> &mdash; the first booking off the fifteen-plus Friday sends; David at Dynalink '
    'has his (6:17 PM) and hasn&rsquo;t replied yet. Still open: <b>Michael at CCI asked for a call, '
    'not an email</b>, and no CCI send is visible in the blast &mdash; this week is the booking '
    'window, and today&rsquo;s open afternoon is the first slot.', 1)
rep('<span class="pill good">Dynalink: sent Fri 6:17 PM</span>',
    '<span class="pill good">Nortec booked &mdash; today 1 PM</span>', 1)

# ---------- 14. TOP5 #2 tail ----------
rep('Monday: fill the brackets and send.', 'Today: fill the brackets and send.', 1)

# ---------- 15. IRIS CARD ----------
rep('Laura&rsquo;s Tuesday ask adds a deliverable: the <b>Hubler channel-partner outreach</b> (feature refresh + current-state evaluation for the two active Hubler agents; she flagged a call error). The Oct 6 update draft is gone from drafts &mdash; superseded by the sent recap. Friday&rsquo;s session has come and gone; the next is <b>Tue Nov 3, 1&ndash;2</b>. The items Friday should have covered &mdash; the invoice (two days past due) and the Hubler outreach &mdash; need a Monday confirmation either way.',
    'Friday&rsquo;s session delivered: <b>Ask Iris demoed live</b> (1,880 calls, 89.1% success), the '
    '<b>trial moved from 7 to 14 days</b> (Laura validating the Revio billing trigger), Alex&rsquo;s '
    'onboarding gets a two-call cadence, and <b>the Hubler ask resolved live</b> &mdash; Alex '
    'voicemailed the channel partner, no response, so the opening move is now <b>your '
    'call-performance report plus the Lakeland case study</b>. LeVarr takes pre-install domain builds '
    'to Donna; <b>notification splitting by agent is on the Voxtell to-do list</b> (Alex absorbed '
    'some 30,000 notification emails). You sent the <b>minutes to the full team Saturday 2:53 PM</b>. '
    'The next session is <b>Tue Nov 3, 1&ndash;2</b> &mdash; raise the invoice there if it '
    'hasn&rsquo;t cleared &mdash; and the <b>Monthly Iris Sync lands Nov 10, 9&ndash;9:30</b>.', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-02T06:55:00-06:00') == 2
assert s.count('window open') == 2
assert len(re.findall(r'(?<!week)day thirteen', s)) == 0
assert 'eighteen days' not in s and 'three days past due' not in s and 'two days past due' not in s
assert 'Good evening' not in s and 'Sunday, November 1' not in s
assert 'Hubler confirm' not in s and 'DW Engineering 10&ndash;2' not in s
assert 'Sun Nov 1 &ndash; Sat Nov 7' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s
assert 'doxy.me/scottvlmft' not in s

open(p, 'w', encoding='utf-8').write(s)
print('monday full ok', len(s))
