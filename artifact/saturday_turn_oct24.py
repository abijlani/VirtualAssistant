#!/usr/bin/env python3
# Saturday Oct 24 2026 weekend date turn (runs from the hourly pass; the morning trigger is weekdays-only).
# Verified facts: Iris deliverables SHIPPED Friday (scenarios to Alex+LeVarr 3:08 PM, industry one-pagers
# 3:56 PM, team CC'd, LeVarr acknowledged 3:17 on the scenarios thread). No pgaustin send - the ProGraphix
# submit-by (10/23) passed silent. No tarbour send - Tim draft day five; Friday's 2:00 Oracle review came
# and went. Friday closed 4F/0NA/0S (burst 6:25-8:36 PM); overnight quiet; two Sat digests by 7:02.
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

# ---------- 1. GLOBAL AGE BUMPS (highest first) ----------
rep('fifty-three days past', 'fifty-four days past', 2)
rep('57 days', '58 days', 1)
rep('day forty-seven', 'day forty-eight', 3)            # 799
rep('day forty-six', 'day forty-seven', 3)              # Eric x2 + trio
rep('day forty-four of billed Logs', 'day forty-five of billed Logs', 1)
rep('forty-third day', 'forty-fourth day', 1)
rep('forty-five full days', 'forty-six full days', 1)
rep('forty-one days past', 'forty-two days past', 2)
rep('Day thirty-nine on Eric', 'Day forty on Eric', 1)
rep('night thirty-nine', 'night forty', 2)
rep('day thirty-eight', 'day thirty-nine', 2)           # JDs
rep('thirty-two days unsent', 'thirty-three days unsent', 1)
rep('thirty-one days past its &ldquo;before Sep 22&rdquo; window', 'thirty-two days past its &ldquo;before Sep 22&rdquo; window', 1)
rep('the window closed Sep 22 &mdash; thirty-one days now', 'the window closed Sep 22 &mdash; thirty-two days now', 1)
rep('Day twenty-eight on all three', 'Day twenty-nine on all three', 1)
rep('twenty-one days', 'twenty-two days', 5)
rep('Twenty-one days', 'Twenty-two days', 1)
rep('nine days past', 'ten days past', 5)
rep('Nine days past due', 'Ten days past due', 1)
rep('day four', 'day five', 3)
rep('Iris, day twelve', 'Iris, day thirteen', 1)
rep('hr-nda is 67 days', 'hr-nda is 68 days', 1)
rep('Ages as of Oct 23', 'Ages as of Oct 24', 1)
rep('Fifteen days carried', 'Sixteen days carried', 1)

def chip1(m):
    return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s2, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s3, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s2)
assert c1 + c2 == 5, f"chips: {c1}+{c2}"
s = s3

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-23T22:07:00-05:00', '2026-10-24T08:07:00-05:00', 2)
rep('<b>Brief compiled</b> Fri 7:16 AM &middot; data checked Fri 10:07 PM CT',
    '<b>Brief compiled</b> Sat 8:07 AM &middot; data checked Sat 8:07 AM CT', 1)
rep('Friday, October 23 &middot; 2026', 'Saturday, October 24 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
new_sub = ('<p class="sub">Friday delivered on deadline: <b>the five Iris scenarios went to Alex and LeVarr at 3:08 PM '
 'and the industry one-pagers followed at 3:56</b> (Laura, Jason, Jake, Grayson and Jr CC&rsquo;d; LeVarr thanked you '
 'minutes later) &mdash; both Tuesday commitments landed. The UGM print run was set up end to end: all three brochures '
 'confirmed ready at FedEx, pickup and the Marriott drop blocked for the morning. What slipped: <b>the ProGraphix '
 'submit-by passed with the thread silent</b> &mdash; ten days past now, and Monday is a damage-control call to Cathy '
 '&mdash; and <b>the Tim draft hits day five</b>: Friday&rsquo;s 2:00 Oracle review came and went, but the written '
 'record is still unsent with UGM week starting Monday. The line: Friday ran spotless for eleven hours, then the '
 'evening window burst &mdash; <b>four failures, 6:25 to 8:36 PM</b>, the sixteenth straight weekday evening; the '
 'overnight was quiet. Today: Acquisition.com 12&ndash;1:15 &mdash; and <b>the Printavo tees</b> (Cedar Park) before '
 'UGM opens Monday. No reactions saved.</p>')
rx(r'<p class="sub">.*?No reactions saved\.</p>', lambda m: new_sub, 1, re.DOTALL)

# ---------- 4. LEDGER: Saturday opener ----------
rep('nothing after 8:36</b> &mdash; verified at 10:07 PM, trash included.',
    'nothing after 8:36</b> &mdash; verified at 10:07 PM, trash included. The overnight into Saturday stayed quiet '
    '&mdash; <b>Saturday opened clean</b>: Daily Digests on schedule at 7:00&ndash;7:02 and no alerts by 8:07 '
    '&mdash; window open.', 1)

# ---------- 5. TODAY SCHEDULE ----------
old_sched = '''        <div class="slot past"><div class="t">8:00 &ndash; 8:30</div><div class="w">Get print outs<small>FedEx Office &middot; all three brochures confirmed ready last night</small></div></div>
        <div class="slot past"><div class="t">9:00 &ndash; 9:30</div><div class="w">Drop off print outs at Marriott<small>the attendee-bag drop for UGM &middot; text Sue on arrival</small></div></div>
        <div class="slot past"><div class="t">9:30 &ndash; 10:30</div><div class="w">AI-Powered Marketing with Claude<small>Gevity &middot; hands-on workshop</small></div></div>
        <div class="slot past"><div class="t">10:00 &ndash; 10:15</div><div class="w">One pager for Spectrum<small>the Iris deliverable &mdash; due today</small></div></div>
        <div class="slot past"><div class="t">10:15 &ndash; 10:30</div><div class="w">Scenarios for Spectrum<small>second Spectrum block</small></div></div>
        <div class="slot past"><div class="t">10:30 &ndash; 10:45</div><div class="w">Share release notes with Spectrum<small>third Spectrum block</small></div></div>
        <div class="slot past"><div class="t">2:00 &ndash; 2:45</div><div class="w">Oracle MAKE / ETA Review<small>Teams &middot; Tim, Adam + Jr cc&rsquo;d &middot; invite unaccepted, so it stays out of the chart</small></div></div>'''
new_sched = '''        <div class="slot"><div class="t">12:00 &ndash; 1:15</div><div class="w">Acquisition.com LIVE &mdash; Think Like a Great CEO<small>self-booked session &middot; the one booking of the day</small></div></div>'''
rep(old_sched, new_sched, 1)
rep('todaynote">2.75h &mdash; print run 8&ndash;9:30, Spectrum blocks 10&ndash;10:45 inside the workshop, Oracle review at 2 unaccepted',
    'todaynote">1.25h &mdash; Acquisition.com LIVE 12&ndash;1:15; the rest of Saturday is open', 1)

# ---------- 6. CHART (Sat 1.25 / Sun 0 / Mon 0.75 / Tue 0 / Wed 0 / Thu 2 / Fri 2) ----------
rep('Fri Oct 23 &ndash; Thu Oct 29', 'Sat Oct 24 &ndash; Fri Oct 30', 1)
old_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(19.64% + 6px)">2.75</div>
            <div class="seg m" style="height:19.64%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(8.93% + 6px)">1.25</div>
            <div class="seg m" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(5.36% + 6px)">0.75</div>
            <div class="seg m" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:7.14%"></div></div>'''
new_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(8.93% + 6px)">1.25</div>
            <div class="seg m" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(5.36% + 6px)">0.75</div>
            <div class="seg m" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg m" style="height:14.29%"></div></div>'''
rep(old_bars, new_bars, 1)
rep('''<div><b>Fri</b>23</div><div><b>Sat</b>24</div>
          <div><b>Sun</b>25</div><div><b>Mon</b>26</div><div><b>Tue</b>27</div><div><b>Wed</b>28</div><div><b>Thu</b>29</div>''',
    '''<div><b>Sat</b>24</div><div><b>Sun</b>25</div>
          <div><b>Mon</b>26</div><div><b>Tue</b>27</div><div><b>Wed</b>28</div><div><b>Thu</b>29</div><div><b>Fri</b>30</div>''', 1)

# ---------- 7. TOP 5 ----------
rep('the decision point is this morning: submit and reply, call Cathy, or let 10/23 go &mdash; that&rsquo;s today',
    '10/23 passed silent &mdash; Monday is a damage-control call to Cathy', 1)
rep('ten days past the submit-by date, and the drafted reply was DELETED unsent</h4>',
    'ten days past &mdash; the submit-by came and went Friday with the thread silent</h4>', 1)
rep('Nothing moved Thursday either. Today IS the submit-by day: submit and reply, call Cathy, or accept that the conference date slips &mdash; the submit-by is today.',
    'Friday &mdash; the submit-by day &mdash; passed with no reply and no submission on the thread. If the table cover and banner still matter, Monday is damage control: call Cathy and ask what&rsquo;s recoverable.', 1)
rep('<h4>Four days past the promise &mdash; and Tim booked an Oracle review for 2:00 today</h4>',
    '<h4>Five days past the promise: the written Oracle record is still unsent &mdash; Friday&rsquo;s review came and went</h4>', 1)
rep('finish it as the written record of the v2 scenario (/export CSV, three return fields) and send it before 2:00 &mdash; <b>Tim put &ldquo;Oracle MAKE / ETA Review&rdquo; on the calendar this morning</b> (Teams, Adam and Jr cc&rsquo;d), so the draft is the agenda.',
    'finish it as the written record of the v2 scenario (/export CSV, three return fields) and send it &mdash; <b>Friday&rsquo;s 2:00 Oracle MAKE / ETA review has come and gone</b>, and whatever was agreed live still isn&rsquo;t on paper. UGM week starts Monday.', 1)
rep('<h4>Due today &mdash; and on the calendar: the Spectrum blocks at 10:00, 10:15 and 10:30</h4>',
    '<h4>Shipped on deadline: the Iris scenarios and one-pagers went out Friday afternoon</h4>', 1)
rep('The crawl-walk-run onboarding landed: pre-built frontline + after-hours agents by default &mdash; interact first, customize second, integrate third. You owe <b>vertical-specific one-pagers built from live customers by Friday &mdash; today</b>, and you blocked the morning for them: <b>One pager 10:00, Scenarios 10:15, Release notes 10:30</b>. Also moving: <b>the Revio API key arrived</b> (Junior schedules the in-person billing kickoff), Laura is chasing Shannon on the usage sync, and you flagged Lakeland as charged since July.',
    'The <b>five scenarios went to Alex and LeVarr at 3:08 PM</b> and the <b>industry one-pagers followed at 3:56</b> (Laura, Jason, Jake, Grayson and Jr CC&rsquo;d) &mdash; LeVarr thanked you minutes later. Both Friday commitments landed. The physical one remains: <b>the Printavo tees are ready at Cedar Park</b> (Invoice #1186) and UGM opens Monday &mdash; this weekend is the pickup window.', 1)
rep('<span class="pill warn">Due today &middot; blocked 10:00</span><span class="pill good">Recap sent Tue 4:43</span>',
    '<span class="pill good">Sent Fri 3:08 + 3:56</span><span class="pill warn">Tees: pickup this weekend</span>', 1)

# ---------- 8. COMING-UP CARDS ----------
rep(' &mdash; crawl-walk-run agreed; the one-pagers are due today</h4>',
    ' &mdash; crawl-walk-run agreed; the scenarios and one-pagers shipped Friday</h4>', 1)
rep('Tuesday&rsquo;s training set crawl-walk-run onboarding and the <b>Friday one-pagers</b>;',
    'Tuesday&rsquo;s training set crawl-walk-run onboarding and the Friday deliverables &mdash; <b>both shipped Friday afternoon</b> (scenarios 3:08, one-pagers 3:56; LeVarr acknowledged);', 1)
rep('<h4 style="font-size:14px">Today &mdash; the print run, the Spectrum blocks, then Tim at 2</h4>',
    '<h4 style="font-size:14px">The weekend &mdash; one session today, then UGM takes the week</h4>', 1)
rep('The brochures are <b>confirmed ready at FedEx Office</b> (all three uploads bounced back &ldquo;ready for retrieval&rdquo; Thursday evening) &mdash; pickup is blocked 8:00&ndash;8:30, the <b>Marriott drop 9:00&ndash;9:30</b>. AI-Powered Marketing runs 9:30&ndash;10:30 with your <b>Spectrum blocks at 10:00, 10:15 and 10:30</b> (one-pager, scenarios, release notes &mdash; the Iris deliverables, due today). <b>Tim&rsquo;s Oracle MAKE / ETA review is at 2:00</b> (Teams; Adam and Jr cc&rsquo;d; invite unaccepted) &mdash; send the drafted instructions before it or walk them through live. Still open in the gaps: ProGraphix (submit-by today), the Emilio recap (twenty-two days), the Printavo pickup, and the group-channel exercise from Taylor&rsquo;s session.',
    'Acquisition.com LIVE runs 12&ndash;1:15, the only booking. The weekend&rsquo;s one errand: <b>the Printavo tees</b> (Invoice #1186, Cedar Park) before UGM opens Monday. Sunday is open &mdash; the usual recovery day. Monday: Product Sync at 8, then <b>UGM in Austin through Thursday</b>; the brochures went to FedEx Thursday night and the Marriott drop was blocked Friday morning. Carried into UGM week: the Tim record (day five), the Emilio recap (twenty-two days), and the group-channel exercise from Taylor&rsquo;s session.', 1)
# markers card
rep('Monday&rsquo;s record (thirteen failures) stands; Thursday was the week&rsquo;s lightest close &mdash; three failures, two needs-attention, three successes.',
    'Monday&rsquo;s record (thirteen failures) stands; Friday ran spotless for eleven hours, then closed at four evening failures &mdash; the sixteenth straight weekday-evening burst.', 1)
rep('Today: <b>the double deadline</b> &mdash; the ProGraphix submit-by and the SpectrumVoIP one-pagers &mdash; plus the print run (FedEx pickup 8:00, Marriott drop 9:00) and <b>Tim&rsquo;s Oracle review at 2:00</b>; Saturday holds the Acquisition.com session 12&ndash;1:15. UGM is Oct 26&ndash;30 in Austin &mdash; <b>the brochures print this morning for hand-carry</b>, the tees are ready at Printavo, and the next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.',
    'This weekend: Acquisition.com 12&ndash;1:15 today, <b>the Printavo pickup</b>, and an open Sunday. UGM is Oct 26&ndash;30 in Austin &mdash; brochures printed for hand-carry, Product Sync Monday 8:00 &mdash; then Thursday holds Scott at 2 with two Reserved blocks, Friday the Gevity pizza party and <b>the Iris session at 2</b>. The next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.', 1)

# ---------- 9. WEEK FLAGS ----------
rep('<span class="pill warn">Today</span> Deadline day: 2.75h scheduled around three sends and the print run',
    '<span class="pill warn">Today</span> Saturday holds one session &mdash; and the weekend&rsquo;s one errand', 1)
rep('The morning is the UGM print run &mdash; <b>FedEx Office pickup 8:00, Marriott drop 9:00</b> &mdash; then AI-Powered Marketing 9:30&ndash;10:30 with the <b>Spectrum blocks 10:00&ndash;10:45</b> (one-pager, scenarios, release notes) stacked inside. The afternoon holds <b>Tim&rsquo;s Oracle MAKE / ETA review at 2:00</b> (invite unaccepted). In the gaps: the <b>ProGraphix decision</b> (ten days past &mdash; the submit-by is today), the Emilio recap (twenty-two days), and the Tim draft on day five &mdash; the 2:00 review is its natural deadline.',
    'Acquisition.com LIVE 12&ndash;1:15 is the only booking. The <b>Printavo tees</b> (Cedar Park) need picking up before UGM opens Monday. Friday&rsquo;s scorecard: <b>the Iris scenarios and one-pagers shipped on deadline</b>; the <b>ProGraphix submit-by passed silent</b> (ten days past &mdash; Monday is a call to Cathy); and the Tim draft sits on day five with the written record still owed.', 1)
rep('<span class="pill warn">This week</span> Deadline day today &mdash; then UGM takes the week',
    '<span class="pill warn">This week</span> UGM takes next week &mdash; Monday through Thursday in Austin', 1)
rep('Today is the last working day before UGM: the ProGraphix submit-by, the Iris one-pagers and the Marriott brochure drop all land today, and <b>Tim&rsquo;s Oracle review sits at 2:00</b>. Saturday holds the Acquisition.com session 12&ndash;1:15; <b>UGM runs Monday through Thursday in Austin</b> with only the Product Sync (Mon 8:00) and the declined Izzy slot on the calendar. Still on the wire: <b>LiveKit&rsquo;s uncharged-invoices notice</b> and the GPT-Live BAA answer (Jr&rsquo;s call), two <b>Crexendo BillCenter password resets Thursday evening</b> (the booth-bill payment in motion, unconfirmed), and <b>Vipin Gupta (Tragofone) still waiting in the Whova app</b>.',
    'Sunday is open. <b>UGM runs Monday through Thursday</b> with only the Product Sync (Mon 8:00) and the declined Izzy slot on the calendar; Thursday holds Scott at 2 and two Reserved blocks, and Friday brings the Gevity pizza party 12:30 and <b>the Iris session at 2</b> &mdash; the series resumes. Still on the wire: <b>LiveKit&rsquo;s uncharged-invoices notice</b> and the GPT-Live BAA answer (Jr&rsquo;s call), the booth-bill payment (BillCenter resets Thursday, unconfirmed), and <b>Vipin Gupta (Tragofone) still waiting in the Whova app</b>.', 1)

# ---------- 10. TASKS TABLE ----------
rep('<tr><td class="tid">Today, in gaps</td>', '<tr><td class="tid">Weekend</td>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('window open') == 2
assert s.count('2026-10-24T08:07:00-05:00') == 2
assert s.count('Fri Oct 23') == 0
assert s.count('due today') == 0 and s.count('Due today') == 0
assert s.count('nine days past') == 0 and s.count('twenty-one days') == 0
assert 'Good evening' not in s
assert 'submit-by is today' not in s

open(p, 'w', encoding='utf-8').write(s)
print('saturday turn applied:', len(s), 'chars')
