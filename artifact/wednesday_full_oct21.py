#!/usr/bin/env python3
# Wednesday Oct 21 2026 full-pass date turn.
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
rep('day forty-four', 'day forty-five', 3)              # 799
rep('day forty-three', 'day forty-four', 3)             # Eric x2 + trio note
rep('day forty-one of billed Logs', 'day forty-two of billed Logs', 1)
rep('fortieth day', 'forty-first day', 1)
rep('forty-two full days', 'forty-three full days', 1)
rep('Day thirty-six on Eric', 'Day thirty-seven on Eric', 1)
rep('day thirty-five', 'day thirty-six', 2)             # JDs
rep('twenty-eight days past its &ldquo;before Sep 22&rdquo; window', 'twenty-nine days past its &ldquo;before Sep 22&rdquo; window', 1)
rep('the window closed Sep 22 &mdash; twenty-eight days now', 'the window closed Sep 22 &mdash; twenty-nine days now', 1)
rep('eighteen days', 'nineteen days', 6)
rep('Eighteen days', 'Nineteen days', 1)
rep('six days past', 'seven days past', 5)
rep('Six days past due', 'Seven days past due', 1)
rep('night thirty-six', 'night thirty-seven', 2)
rep('thirty-eight days past', 'thirty-nine days past', 2)
rep('twenty-nine days unsent', 'thirty days unsent', 1)
rep('fifty days past', 'fifty-one days past', 2)
rep('54 days', '55 days', 1)
rep('Iris, day nine', 'Iris, day ten', 1)
rep('hr-nda is 64 days', 'hr-nda is 65 days', 1)
rep('Ages as of Oct 20', 'Ages as of Oct 21', 1)

def chip1(m):
    return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s2, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s3, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s2)
assert c1 + c2 == 5, f"chips: {c1}+{c2}"
s = s3

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-20T22:07:00-05:00', '2026-10-21T07:21:00-05:00', 2)
rep('<b>Brief compiled</b> Tue 7:21 AM &middot; data checked Tue 10:07 PM CT',
    '<b>Brief compiled</b> Wed 7:21 AM &middot; data checked Wed 7:21 AM CT', 1)
rep('Tuesday, October 20 &middot; 2026', 'Wednesday, October 21 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD SUB ----------
new_sub = ('<p class="sub">Tuesday delivered: the Iris training set the <b>crawl-walk-run onboarding</b> and your '
 'action-items recap went out at 4:43 (new commitment: <b>vertical one-pagers by Friday</b>); the Izzy call moved '
 'the Oracle lookup &mdash; Tim hit Google-auth errors importing the blueprint, so <b>Tim now owes a Gmail account '
 'for Make, the Bandwidth-application check, and a freeze on the sheet edits</b> &mdash; though your drafted '
 'instructions email is <b>still unsent, day two</b>; and the UGM shipping question dissolved: <b>you hand-carry '
 'from Austin</b>, no FedEx payment needed, the attendee-bag one-pager drops at the hotel Friday, and Crexendo '
 'invoices the two escalator signs. <b>Printavo says the tees are ready for pickup</b> (Invoice #1186, Cedar Park). '
 'New: Taylor brought in Kyle &mdash; a <b>$7,500 backend-systems build split 50/50</b>, target Nov 4&ndash;5 &mdash; '
 'and a <b>Kyle call landed today at 12:30</b>, right behind the Debrief, pushing Wednesday to exactly 8h. Still '
 'carried: <b>ProGraphix at seven days past</b> (submit-by is Friday &mdash; two days out) and the Emilio recap at '
 '<b>nineteen days</b>. The line: Tuesday closed at eight failures; Wednesday opened with one at 5:51 AM. '
 'No reactions saved.</p>')
rx(r'<p class="sub">.*?No reactions saved\.</p>', lambda m: new_sub, 1, re.DOTALL)

# ---------- 4. LEDGER: Wednesday opener ----------
rep('nothing after 9:20</b> &mdash; verified at 10:07 PM, trash included.',
    'nothing after 9:20</b> &mdash; verified at 10:07 PM, trash included. Overnight into Wednesday held <b>one '
    'early failure at 5:51 AM</b>, then the Daily Digests on schedule at 7:00&ndash;7:02 &mdash; one failure by '
    '7:21, window open.', 1)

# ---------- 5. TODAY SCHEDULE ----------
old_sched = '''        <div class="slot past"><div class="t">10:00 &ndash; 10:30</div><div class="w">Izzy Weekly Checkin<small>Teams &middot; Tim, Adam, Jr &middot; the backorder-ETA lookup &mdash; your instructions are drafted, unsent</small></div></div>
        <div class="slot past"><div class="t">10:00 &ndash; 2:00</div><div class="w">Deep Work (Client + Admin + Sales)<small>send the Tim instructions &middot; the ProGraphix decision (submit-by is Friday) &middot; the UGM FedEx payment call</small></div></div>
        <div class="slot past"><div class="t">1:00 &ndash; 2:00</div><div class="w">Iris Training with Bodhi<small>Laura&rsquo;s team &middot; agreed topic: onboarding new + existing clients, review the onboarding call</small></div></div>
        <div class="slot past"><div class="t">2:00 &ndash; 3:00</div><div class="w">Transition, Talking, Triage<small>the Emilio recap (nineteen days) &middot; the ProGraphix reply &middot; 2F-15 artwork check with Jr (due tomorrow)</small></div></div>'''
new_sched = '''        <div class="slot"><div class="t">8:00 &ndash; 8:45</div><div class="w">Gym Series: The Circuit<small>Gevity &middot; registered last night &middot; invite unaccepted, so it stays out of the chart</small></div></div>
        <div class="slot"><div class="t">9:00 &ndash; 9:30</div><div class="w">Recover + Shower<small>after the circuit</small></div></div>
        <div class="slot"><div class="t">9:30 &ndash; 10:30</div><div class="w">Sustainable Ambition<small>Gevity &middot; Taylor&rsquo;s session: satisfaction spectrum, energy leaks, a sample week</small></div></div>
        <div class="slot"><div class="t">11:00 &ndash; 3:00</div><div class="w">Deep Work (Project Engineering)<small>2F-15 artwork due today &middot; the #992 / #996 / #997 reviews + #799 &middot; send the Tim draft</small></div></div>
        <div class="slot"><div class="t">11:30 &ndash; 12:30</div><div class="w">Debrief AI &mdash; Bodhi &amp; Taylor<small>Meet &middot; Taylor&rsquo;s agenda: website name, workshop review, partners &mdash; ends on the Ashlyn ask</small></div></div>
        <div class="slot"><div class="t">12:30 &ndash; 1:00</div><div class="w">Kyle + Bodhi/Taylor<small>Meet &middot; the $7,500 backend build &mdash; Taylor runs it, you join on Zoom</small></div></div>
        <div class="slot"><div class="t">3:00 &ndash; 4:00</div><div class="w">Transition, Talking, Triage<small>the Emilio recap (nineteen days) &middot; the ProGraphix reply &middot; the Printavo pickup</small></div></div>'''
rep(old_sched, new_sched, 1)
rep('todaynote">6.5h &mdash; Izzy 10:00, Deep Work 10&ndash;2 with Iris Training 1&ndash;2 inside, Transition 2&ndash;3',
    'todaynote">8h &mdash; Sustainable Ambition 9:30, Deep Work 11&ndash;3 with the Debrief 11:30 + Kyle 12:30 inside, Transition 3&ndash;4', 1)

# ---------- 6. CHART ----------
rep('Tue Oct 20 &ndash; Mon Oct 26', 'Wed Oct 21 &ndash; Tue Oct 27', 1)
old_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
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
new_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(57.14% + 6px)">8</div>
            <div class="seg m" style="height:17.86%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(8.93% + 6px)">1.25</div>
            <div class="seg m" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(5.36% + 6px)">0.75</div>
            <div class="seg m" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>'''
rep(old_bars, new_bars, 1)
rep('''<div><b>Tue</b>20</div><div><b>Wed</b>21</div>
          <div><b>Thu</b>22</div><div><b>Fri</b>23</div><div><b>Sat</b>24</div><div><b>Sun</b>25</div><div><b>Mon</b>26</div>''',
    '''<div><b>Wed</b>21</div><div><b>Thu</b>22</div>
          <div><b>Fri</b>23</div><div><b>Sat</b>24</div><div><b>Sun</b>25</div><div><b>Mon</b>26</div><div><b>Tue</b>27</div>''', 1)

# ---------- 7. TOP 5 ----------
rep('Nothing moved through Monday either. Today is the decision',
    'Nothing moved Tuesday either. Today is the decision', 1)
rep('the submit-by is Friday, three days out.', 'the submit-by is Friday &mdash; two days out.', 1)
# #2 Oracle rewrite
rep('''<h4>One day past the promise: the Oracle instructions to Tim are drafted &mdash; send before the 10:00 Izzy call</h4>
          <p class="why">The working instructions for the backorder-ETA Make scenario were promised for Monday; the draft to Tim went in at 7:17 last night and is still sitting unsent. The Izzy Weekly Checkin is at 10:00 with Tim on the call &mdash; verify the scenario end-to-end (/export CSV URL, the renamed aggregator columns), finish the draft, and send it before or during the call.</p>
          <div class="meta"><span class="pill crit">Promised Monday</span><span class="pill warn">Draft unsent &middot; Izzy call 10:00</span></div>''',
'''<h4>Two days past the promise: the Tim draft is still unsent &mdash; though the Izzy call moved the work</h4>
          <p class="why">Tuesday&rsquo;s call walked Tim through the import live: the blueprint hit Google-auth errors, so <b>Tim now owes a Gmail account for Make, the Bandwidth-application check with James or Adam, and a freeze on the sheet edits</b>. Your Monday-night draft is still in drafts &mdash; finish it as the written record of the v2 scenario (/export CSV, three return fields) and send it so the handoff survives UGM week.</p>
          <div class="meta"><span class="pill crit">Promised Monday</span><span class="pill warn">Draft unsent &middot; day two</span></div>''', 1)
# #3 rewrite to one-pagers
rep('''<h4>Laura&rsquo;s thread moved &mdash; today&rsquo;s Iris Training 1&ndash;2 has an agreed agenda</h4>
          <p class="why">The recap finally went out Monday at 11:35 and the thread lit up: Laura added Grayson and Jeff, Grayson owes an ETA on trial-date flexibility, and you set today&rsquo;s focus &mdash; onboarding new and existing clients, with the onboarding-call review. The billing answer went at 5:06 (minutes usage lives in their database; Shannon syncs it to Rev.io with Jeff&rsquo;s script). Bring the funnel report and the per-account export ask.</p>
          <div class="meta"><span class="pill good">Recap sent Monday</span><span class="pill quiet">Training 1&ndash;2</span></div>''',
'''<h4>New Friday commitment: vertical one-pagers for the Iris onboarding &mdash; promised at Tuesday&rsquo;s training</h4>
          <p class="why">The crawl-walk-run onboarding landed: pre-built frontline + after-hours agents by default &mdash; interact first, customize second, integrate third. You owe <b>vertical-specific one-pagers built from live customers by Friday</b>, and your action-items recap went out at 4:43. Also moving: <b>the Revio API key arrived</b> (Junior schedules the in-person billing kickoff), Laura is chasing Shannon on the usage sync, and you flagged Lakeland as charged since July.</p>
          <div class="meta"><span class="pill warn">Due Friday</span><span class="pill good">Recap sent Tue 4:43</span></div>''', 1)
# #5 window update
rep('Wednesday&rsquo;s Deep Work (Engineering) 11&ndash;3 is the window &mdash; bugbot swept #992, #996 and #997 Monday; the reviews still wait on you.',
    'Today&rsquo;s Deep Work (Engineering) 11&ndash;3 is the window &mdash; bugbot swept #992, #996 and #997 Monday; the reviews still wait on you.', 1)
rep('<span class="pill warn">Two reviews deep</span><span class="pill quiet">DW Wed 11&ndash;3</span>',
    '<span class="pill warn">Two reviews deep</span><span class="pill quiet">DW today 11&ndash;3</span>', 1)

# ---------- 8. COMING-UP CARDS ----------
rep('Iris, day ten &mdash; the recap landed, the thread moved; training today 1&ndash;2',
    'Iris, day ten &mdash; crawl-walk-run agreed; the one-pagers are due Friday', 1)
rep('and the billing answer followed at 5:06 (usage lives in their database; Shannon syncs Rev.io with Jeff&rsquo;s script).',
    'the billing answer followed at 5:06, and Laura is chasing Shannon on the Rev.io sync. Tuesday&rsquo;s training set crawl-walk-run onboarding and the <b>Friday one-pagers</b>; <b>the Revio API key arrived</b>, so the billing build can start.', 1)
rep('The series recurs Tuesdays 1&ndash;2.', 'The next session is Friday (the Tuesday slot falls in UGM week; the series resumes Fri Oct 30, 2&ndash;3).', 1)
rep('Today &mdash; Izzy at 10, training at 1: the Oracle send is the one deliverable',
    'Today &mdash; a full 8h: the Debrief and Kyle back-to-back inside Deep Work', 1)
rep('Izzy Weekly Checkin 10&ndash;10:30 with Tim on the call &mdash; the drafted instructions should be sent by then. Deep Work (Client + Admin + Sales) 10&ndash;2 wraps around Iris Training 1&ndash;2 (agreed topic: onboarding new and existing clients, with the onboarding-call review). Transition 2&ndash;3 is the send window: the Emilio recap (nineteen days), the ProGraphix reply, and the UGM FedEx payment call &mdash; due Thursday.',
    'Sustainable Ambition 9:30&ndash;10:30 is Taylor&rsquo;s session. Deep Work (Project Engineering) 11&ndash;3 carries the <b>2F-15 artwork (due today)</b>, the #992/#996/#997 reviews and the Tim draft &mdash; with the <b>Debrief 11:30&ndash;12:30</b> (Taylor&rsquo;s agenda ends on the Ashlyn ask: what you built, when, what you charged) and <b>Kyle at 12:30</b> stacked inside, the block effectively runs 11&ndash;11:30 and 1&ndash;3. Transition 3&ndash;4 takes the sends: the Emilio recap (nineteen days), the ProGraphix reply, and the Printavo pickup.', 1)
# markers card
rep('Sunday&rsquo;s spike (nine failures) stood one day &mdash; <b>Monday beat it: thirteen failures, ten needs-attention, nine successes</b>, closed at 10:07 PM. This week: today 6.5h with Izzy at 10 and Iris Training 1&ndash;2, <b>Wednesday Oct 21 runs 7.5h against the 2F-15 artwork deadline</b> (FedEx&rsquo;s specs are with Jr) plus the new &ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30, and <b>Thursday Oct 22 runs 6.5h</b> with &ldquo;Pay the Netsapiens booth bill&rdquo; scheduled 9&ndash;9:30 inside Deep Work. Friday Oct 23 holds one hour &mdash; AI-Powered Marketing with Claude, 9:30&ndash;10:30. UGM itself is Oct 26&ndash;30 in Austin &mdash; <b>tracking numbers were due to Crexendo Oct 19; FedEx payment is due Thursday Oct 22</b> or the giveaways miss the attendee bags.',
    'Monday&rsquo;s record (thirteen failures) stood; Tuesday eased to eight. This week: <b>today runs a full 8h</b> &mdash; the 2F-15 artwork deadline (scope confirmed: just the two escalator signs) with the Debrief 11:30 and Kyle 12:30 inside Deep Work; <b>Thursday 6.5h</b> with the Netsapiens booth bill 9&ndash;9:30 and Scott at 4; Friday one hour (AI-Powered Marketing 9:30&ndash;10:30) plus the <b>one-pagers owed to SpectrumVoIP</b>; Saturday holds a self-booked Acquisition.com session 12&ndash;1:15. UGM is Oct 26&ndash;30 in Austin &mdash; <b>shipping resolved: you hand-carry</b>, the attendee-bag one-pager drops at the hotel Friday, and the tees are ready at Printavo.', 1)

# ---------- 9. FLAGS ----------
rep('<span class="pill warn">Today</span> Tuesday runs 6.5h &mdash; Izzy at 10, Iris Training 1&ndash;2 inside Deep Work',
    '<span class="pill warn">Today</span> Wednesday runs exactly 8h &mdash; the Kyle call pushed it to the line', 1)
rep('The <b>Oracle instructions to Tim</b> are drafted and unsent &mdash; send before the 10:00 Izzy call with Tim on it. Iris Training 1&ndash;2 sits inside Deep Work (Client + Admin + Sales) 10&ndash;2 with the agreed onboarding topic. Still open: the <b>ProGraphix decision</b> (seven days past the submit-by &mdash; Friday is three days out), the Emilio recap (nineteen days), and the <b>UGM FedEx payment due Thursday</b>.',
    'Three meetings stack into the middle: Sustainable Ambition 9:30, then the <b>Debrief 11:30 and Kyle 12:30 back-to-back inside Deep Work 11&ndash;3</b> &mdash; the engineering block effectively runs 11&ndash;11:30 and 1&ndash;3 against the <b>2F-15 artwork due today</b>. Still open: the <b>ProGraphix decision</b> (seven days past the submit-by &mdash; Friday is two days out), the Emilio recap (nineteen days), and the Tim draft on day two.', 1)
rep('Today 6.5h has the Izzy check-in at 10:00 and Iris Training 1&ndash;2 inside Deep Work; <b>Wednesday Oct 21 runs 7.5h</b> &mdash; the 2F-15 artwork deadline (FedEx&rsquo;s specs with Jr) plus the <b>&ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30</b>',
    'Today runs <b>a full 8h</b> &mdash; the 2F-15 artwork deadline (scope confirmed: two escalator signs) plus the <b>&ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30 and the new Kyle call 12:30&ndash;1</b>', 1)
rep('<b>UGM starts Monday Oct 26 in Austin &mdash; FedEx payment info is due by phone Thursday, or the giveaways miss the attendee bags.</b>',
    '<b>UGM starts Monday Oct 26 in Austin &mdash; shipping resolved by hand-carry; the one-pager drops at the hotel Friday.</b>', 1)

# ---------- 10. TASKS TABLE ----------
rep('<tr><td class="tid">Today 2&ndash;3</td>', '<tr><td class="tid">Today 3&ndash;4</td>', 1)
rep('<b>the Laura recap went out Monday 11:35</b> and is off this list',
    '<b>Tuesday&rsquo;s action-items recap went out at 4:43</b> &mdash; the Iris side is current', 1)
rep('<tr><td class="tid">Wed 11&ndash;3</td><td><b>The identification query first</b>',
    '<tr><td class="tid">Today 11&ndash;3</td><td><b>The identification query first</b>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('window open') == 2
assert s.count('2026-10-21T07:21:00-05:00') == 2
assert s.count('Tue Oct 20') == 0
assert 'Izzy call 10:00' not in s
assert s.count('FedEx') == 1, s.count('FedEx')   # only the masthead's "no FedEx payment needed"

open(p, 'w', encoding='utf-8').write(s)
print('wednesday turn applied:', len(s), 'chars')
