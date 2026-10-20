#!/usr/bin/env python3
# Tuesday Oct 20 2026 full-pass date turn.
# Age bumps FIRST (counts verified against the live template), then structural rewrites.
import re

p = 'page-template.html'
s = open(p, encoding='utf-8').read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f"rep anchor {old[:70]!r}: expected {n}, found {c}"
    s = s.replace(old, new)

def rx(pat, new, n, flags=0):
    global s
    s, c = re.subn(pat, new, s, flags=flags)
    assert c == n, f"rx {pat[:70]!r}: expected {n}, replaced {c}"

# ---------- 1. GLOBAL AGE BUMPS (highest numbers first) ----------
rep('day forty-three', 'day forty-four', 3)            # 799
rep('day forty-two', 'day forty-three', 3)             # Eric x2 + trio note
rx(r'day forty(?!-)', 'day forty-one', 1)              # billed Logs
rep('thirty-ninth day', 'fortieth day', 1)
rep('forty-one full days', 'forty-two full days', 1)
rep('Day thirty-five on Eric', 'Day thirty-six on Eric', 1)
rep('day thirty-four', 'day thirty-five', 2)           # JDs
# Appulse invoice count was frozen at "eighteen days" since written; Sep 22 -> Oct 20 is 28.
rep('eighteen days past its &ldquo;before Sep 22&rdquo; window', 'twenty-eight days past its &ldquo;before Sep 22&rdquo; window', 1)
rep('the window closed Sep 22 &mdash; eighteen days now', 'the window closed Sep 22 &mdash; twenty-eight days now', 1)
rep('seventeen days', 'eighteen days', 5)
rep('Seventeen days', 'Eighteen days', 1)
rep('five days past', 'six days past', 5)
rep('Five days past due', 'Six days past due', 1)
rep('night thirty-five', 'night thirty-six', 2)
rep('thirty-seven days past', 'thirty-eight days past', 2)
rep('twenty-eight days unsent', 'twenty-nine days unsent', 1)
rep('forty-nine days past', 'fifty days past', 2)
rep('53 days', '54 days', 1)
rep('Iris, day eight', 'Iris, day nine', 1)
rep('hr-nda is 63 days', 'hr-nda is 64 days', 1)
rep('Ages as of Oct 19', 'Ages as of Oct 20', 1)

def chip1(m):
    return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s2, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s3, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s2)
assert c1 + c2 == 5, f"chips: {c1}+{c2}"
s = s3

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-19T22:07:00-05:00', '2026-10-20T07:21:00-05:00', 2)
rep('<b>Brief compiled</b> Mon 7:22 AM &middot; data checked Mon 10:07 PM CT',
    '<b>Brief compiled</b> Tue 7:21 AM &middot; data checked Tue 7:21 AM CT', 1)
rep('Monday, October 19 &middot; 2026', 'Tuesday, October 20 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD SUB ----------
new_sub = ('<p class="sub">Monday finally moved the sends: <b>the Laura recap went out at 11:35</b> and drew '
 'replies within the hour (Grayson now owes the trial-date ETA), the <b>billing answer followed at 5:06</b> '
 'after you confirmed the Rev.io sync with Jeff, and ATS onboarding ran all day &mdash; Jamie takes the '
 'vendor-portal owner seat, a shared Slack channel is proposed. The line answered with its heaviest day of '
 'the streak: <b>thirteen failures, ten needs-attention, nine successes</b>, closed at 10:07 PM. Still '
 'carried: <b>the Oracle instructions to Tim are drafted (last night, 7:17 PM) but unsent</b> &mdash; one day '
 'past the promise, with Tim on the 10:00 Izzy call this morning; <b>ProGraphix is six days past the '
 'submit-by date</b> (Friday is three days out); the Emilio recap is at <b>eighteen days</b>. New this '
 'morning: Jr forwarded the <b>UGM shipping notice</b> &mdash; tracking numbers were due to Crexendo '
 'yesterday and <b>FedEx payment info is due Thursday</b> or the giveaways miss the attendee bags &mdash; '
 'and Jr opened a GPT-Live 503 ticket with LiveKit on production. Today runs 6.5h: Izzy 10:00, Deep Work '
 '10&ndash;2 with Iris Training 1&ndash;2 inside, Transition 2&ndash;3. No reactions saved.</p>')
rx(r'<p class="sub">.*?No reactions saved\.</p>', lambda m: new_sub, 1, re.DOTALL)

# ---------- 4. LEDGER: Tuesday opener ----------
rep('nothing after 9:23</b> &mdash; verified at 10:07 PM, trash included.',
    'nothing after 9:23</b> &mdash; verified at 10:07 PM, trash included. Overnight into Tuesday was quiet; '
    'the Daily Digests landed on schedule at 7:00&ndash;7:02 and <b>a first failure followed at 7:03 AM</b> '
    '&mdash; one failure by 7:21, window open.', 1)

# ---------- 5. TODAY SCHEDULE ----------
old_sched = '''        <div class="slot past"><div class="t">8:00 &ndash; 8:45</div><div class="w">Weekly Product Sync<small>with Jr &middot; Google Meet</small></div></div>
        <div class="slot past"><div class="t">10:00 &ndash; 2:00</div><div class="w">Deep Work (Engineering)<small>the 62-account reconciliation &middot; the Oracle Make-scenario instructions for Tim (due today) &middot; then the #992 / #996 / #997 reviews</small></div></div>
        <div class="slot past"><div class="t">2:00 &ndash; 3:00</div><div class="w">Transition, Talking, Triage<small>the sends: Laura recap + export re-request &middot; Emilio recap &middot; the ProGraphix reply</small></div></div>'''
new_sched = '''        <div class="slot"><div class="t">10:00 &ndash; 10:30</div><div class="w">Izzy Weekly Checkin<small>Teams &middot; Tim, Adam, Jr &middot; the backorder-ETA lookup &mdash; your instructions are drafted, unsent</small></div></div>
        <div class="slot"><div class="t">10:00 &ndash; 2:00</div><div class="w">Deep Work (Client + Admin + Sales)<small>send the Tim instructions &middot; the ProGraphix decision (submit-by is Friday) &middot; the UGM FedEx payment call</small></div></div>
        <div class="slot"><div class="t">1:00 &ndash; 2:00</div><div class="w">Iris Training with Bodhi<small>Laura&rsquo;s team &middot; agreed topic: onboarding new + existing clients, review the onboarding call</small></div></div>
        <div class="slot"><div class="t">2:00 &ndash; 3:00</div><div class="w">Transition, Talking, Triage<small>the Emilio recap (eighteen days) &middot; the ProGraphix reply &middot; 2F-15 artwork check with Jr (due tomorrow)</small></div></div>'''
rep(old_sched, new_sched, 1)
rep('todaynote">5.75h &mdash; Product Sync 8:00, Deep Work (Engineering) 10&ndash;2, Transition 2&ndash;3',
    'todaynote">6.5h &mdash; Izzy 10:00, Deep Work 10&ndash;2 with Iris Training 1&ndash;2 inside, Transition 2&ndash;3', 1)

# ---------- 6. CHART ----------
rep('Mon Oct 19 &ndash; Sun Oct 25', 'Tue Oct 20 &ndash; Mon Oct 26', 1)
old_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>'''
new_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(5.36% + 6px)">0.75</div>
            <div class="seg m" style="height:5.36%"></div></div>'''
rep(old_bars, new_bars, 1)
rep('''<div><b>Mon</b>19</div><div><b>Tue</b>20</div>
          <div><b>Wed</b>21</div><div><b>Thu</b>22</div><div><b>Fri</b>23</div><div><b>Sat</b>24</div><div><b>Sun</b>25</div>''',
    '''<div><b>Tue</b>20</div><div><b>Wed</b>21</div>
          <div><b>Thu</b>22</div><div><b>Fri</b>23</div><div><b>Sat</b>24</div><div><b>Sun</b>25</div><div><b>Mon</b>26</div>''', 1)

# ---------- 7. TOP 5 ----------
# #1 ProGraphix tail
rep('Nothing moved all weekend. This morning is the decision: submit and reply, call Cathy, or accept that the conference date slips &mdash; 10/23 is Friday.',
    'Nothing moved through Monday either. Today is the decision: submit and reply, call Cathy, or accept that the conference date slips &mdash; the submit-by is Friday, three days out.', 1)
# #2 full rewrite
rep('''<h4>Monday opens the week: Product Sync 8:00, then the 62-account reconciliation</h4>
          <p class="why">The reconciliation of the <b>62 accounts with active agreements but no live agent</b> is Monday&rsquo;s anchor, inside Deep Work (Engineering) 10&ndash;2 &mdash; and it leans on the Laura recap + per-account export re-request that still hasn&rsquo;t gone out. The Laura send never left, so open the block with the recap + re-request, then run the reconciliation from the funnel report already in hand.</p>
          <div class="meta"><span class="pill warn">Today 10&ndash;2</span><span class="pill quiet">Deep Work 10&ndash;2</span></div>''',
'''<h4>One day past the promise: the Oracle instructions to Tim are drafted &mdash; send before the 10:00 Izzy call</h4>
          <p class="why">The working instructions for the backorder-ETA Make scenario were promised for Monday; the draft to Tim went in at 7:17 last night and is still sitting unsent. The Izzy Weekly Checkin is at 10:00 with Tim on the call &mdash; verify the scenario end-to-end (/export CSV URL, the renamed aggregator columns), finish the draft, and send it before or during the call.</p>
          <div class="meta"><span class="pill crit">Promised Monday</span><span class="pill warn">Draft unsent &middot; Izzy call 10:00</span></div>''', 1)
# #3 full rewrite
rep('''<h4>Due today: the Oracle Lighting Make-scenario instructions to Tim</h4>
          <p class="why">Friday&rsquo;s troubleshooting session ended with the backorder-ETA lookup rebuilt but unverified &mdash; the aggregator&rsquo;s renamed columns were blanking the output, and the sheet URL must be the /export CSV, not /edit. You promised Tim working instructions by today: export the blueprint, rebuild with correct column mappings, verify end-to-end, and queue the YouTube link sheet for his team to maintain.</p>
          <div class="meta"><span class="pill crit">Promised Monday</span><span class="pill quiet">Deep Work 10&ndash;2</span></div>''',
'''<h4>Laura&rsquo;s thread moved &mdash; today&rsquo;s Iris Training 1&ndash;2 has an agreed agenda</h4>
          <p class="why">The recap finally went out Monday at 11:35 and the thread lit up: Laura added Grayson and Jeff, Grayson owes an ETA on trial-date flexibility, and you set today&rsquo;s focus &mdash; onboarding new and existing clients, with the onboarding-call review. The billing answer went at 5:06 (minutes usage lives in their database; Shannon syncs it to Rev.io with Jeff&rsquo;s script). Bring the funnel report and the per-account export ask.</p>
          <div class="meta"><span class="pill good">Recap sent Monday</span><span class="pill quiet">Training 1&ndash;2</span></div>''', 1)
# #5 window + bugbot tense
rep('Deep Work (Engineering) 10&ndash;2 is the window &mdash; bugbot swept #992, #996 and #997 this morning; the reviews still wait on you.',
    'Wednesday&rsquo;s Deep Work (Engineering) 11&ndash;3 is the window &mdash; bugbot swept #992, #996 and #997 Monday; the reviews still wait on you.', 1)
rep('<span class="pill warn">Two reviews deep</span><span class="pill quiet">Deep Work 10&ndash;2</span>',
    '<span class="pill warn">Two reviews deep</span><span class="pill quiet">DW Wed 11&ndash;3</span>', 1)

# ---------- 8. COMING-UP CARDS ----------
rep('Iris, day nine &mdash; the audit has a work plan; reconciliation preps for Monday',
    'Iris, day nine &mdash; the recap landed, the thread moved; training today 1&ndash;2', 1)
rep('Friday&rsquo;s 10&ndash;11 block set the follow-through &mdash; the recap + export re-request hasn&rsquo;t gone out yet: official counts, the recap re-requesting the <b>per-account export</b>',
    'Monday&rsquo;s recap went out at 11:35 and drew replies within the hour &mdash; Laura added Grayson and Jeff, Grayson owes the trial-date ETA, and the billing answer followed at 5:06 (usage lives in their database; Shannon syncs Rev.io with Jeff&rsquo;s script). Still to re-request: the <b>per-account export</b>', 1)
rep('The Oct 6 update draft is on day thirteen in drafts. ',
    'The Oct 6 update draft is gone from drafts &mdash; superseded by the sent recap. ', 1)
rep('Today &mdash; re-entry: sync at 8, two deliverables inside Deep Work',
    'Today &mdash; Izzy at 10, training at 1: the Oracle send is the one deliverable', 1)
rep('Product Sync 8&ndash;8:45 (Jr confirmed). Deep Work (Engineering) 10&ndash;2 carries the <b>62-account reconciliation</b>, the <b>Oracle Make-scenario instructions promised to Tim today</b>, and the PR reviews (#992, #996, #997 &mdash; bugbot swept all three this morning). Transition 2&ndash;3 is the send window: the Laura recap + export re-request, the Emilio recap (eighteen days), the ProGraphix reply.',
    'Izzy Weekly Checkin 10&ndash;10:30 with Tim on the call &mdash; the drafted instructions should be sent by then. Deep Work (Client + Admin + Sales) 10&ndash;2 wraps around Iris Training 1&ndash;2 (agreed topic: onboarding new and existing clients, with the onboarding-call review). Transition 2&ndash;3 is the send window: the Emilio recap (eighteen days), the ProGraphix reply, and the UGM FedEx payment call &mdash; due Thursday.', 1)
rep('The workshop ran Saturday clean; Sunday brought the line&rsquo;s weekly spike (nine failures, seven needs-attention). This week: today 5.75h, <b>Tuesday 6.5h</b> with Iris Training 1&ndash;2, ',
    'Sunday&rsquo;s spike (nine failures) stood one day &mdash; <b>Monday beat it: thirteen failures, ten needs-attention, nine successes</b>, closed at 10:07 PM. This week: today 6.5h with Izzy at 10 and Iris Training 1&ndash;2, ', 1)
rep('UGM itself is Oct 26&ndash;30 in Austin.</p>',
    'UGM itself is Oct 26&ndash;30 in Austin &mdash; <b>tracking numbers were due to Crexendo Oct 19; FedEx payment is due Thursday Oct 22</b> or the giveaways miss the attendee bags.</p>', 1)

# ---------- 9. FLAGS ----------
rep('<span class="pill warn">Today</span> Monday runs 5.75h &mdash; sync at 8, Deep Work 10&ndash;2 with two deliverables inside',
    '<span class="pill warn">Today</span> Tuesday runs 6.5h &mdash; Izzy at 10, Iris Training 1&ndash;2 inside Deep Work', 1)
rep('The <b>62-account reconciliation</b> and the <b>Oracle Make-scenario instructions promised to Tim today</b> both live in Deep Work (Engineering) 10&ndash;2. Before the block: the <b>ProGraphix decision</b> (six days past the submit-by date &mdash; 10/23 is Friday). Transition 2&ndash;3 takes the sends: the Laura recap + per-account export re-request feeding the reconciliation, and the Emilio recap (eighteen days).',
    'The <b>Oracle instructions to Tim</b> are drafted and unsent &mdash; send before the 10:00 Izzy call with Tim on it. Iris Training 1&ndash;2 sits inside Deep Work (Client + Admin + Sales) 10&ndash;2 with the agreed onboarding topic. Still open: the <b>ProGraphix decision</b> (six days past the submit-by &mdash; Friday is three days out), the Emilio recap (eighteen days), and the <b>UGM FedEx payment due Thursday</b>.', 1)
rep('Today 5.75h opens with Product Sync at 8:00 and carries the <b>62-account billing reconciliation</b> plus the Oracle instructions; Tuesday 6.5h has the Izzy check-in at 10:00 and Iris Training 1&ndash;2; ',
    'Today 6.5h has the Izzy check-in at 10:00 and Iris Training 1&ndash;2 inside Deep Work; ', 1)
rep('<b>UGM starts Monday Oct 26 in Austin.</b>',
    '<b>UGM starts Monday Oct 26 in Austin &mdash; FedEx payment info is due by phone Thursday, or the giveaways miss the attendee bags.</b>', 1)

# ---------- 10. TASKS TABLE ----------
rep(' and <b>the Laura recap + per-account export re-request</b> &mdash; none of the three moved all weekend',
    ' &mdash; the two carried sends; <b>the Laura recap went out Monday 11:35</b> and is off this list', 1)
rep('Kayla&rsquo;s ATS form resolved: submitted Thursday, Jr has next steps',
    'ATS onboarding is live: Jamie takes the vendor-portal owner seat; Eelco owes next steps + the test domain', 1)
rep('<tr><td class="tid">Today 10&ndash;2</td><td><b>The identification query first</b>',
    '<tr><td class="tid">Wed 11&ndash;3</td><td><b>The identification query first</b>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('window open') == 2
assert s.count('2026-10-20T07:21:00-05:00') == 2
assert s.count('5.75h') == 0, s.count('5.75h')
assert s.count('Mon Oct 19') == 0
assert 'day thirteen in drafts' not in s
assert s.count('eighteen days') == 6, s.count('eighteen days')

open(p, 'w', encoding='utf-8').write(s)
print('tuesday turn applied:', len(s), 'chars')
