#!/usr/bin/env python3
# Friday Oct 23 2026 full-pass date turn.
# Age bumps FIRST (counts grep-verified), then structural rewrites with post-bump values.
# Overnight facts: Jr emailed 3 UGM brochure PDFs Thu ~5:13 PM; Bodhi forwarded all three to
# FedEx Print & Go 5:31-5:36 PM; FedEx confirmed all three ready. Bodhi self-scheduled Friday
# at 10:37 PM: Get print outs 8-8:30, Marriott drop 9-9:30, One pager/Scenarios/Release notes
# for Spectrum 10:00/10:15/10:30. Tim booked "Oracle MAKE / ETA Review" 2:00-2:45 (unaccepted).
# Two Crexendo BillCenter password resets Thu evening (booth bill in motion; links NOT surfaced).
# Thursday closed 3F/2NA/3S; Friday opened clean. Both drafts still unsent.
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
rep('fifty-two days past', 'fifty-three days past', 2)
rep('56 days', '57 days', 1)
rep('day forty-six', 'day forty-seven', 5)             # 799 (incl. Thu slot + card copies)
rep('day forty-five', 'day forty-six', 3)              # Eric x2 + trio note
rep('day forty-three of billed Logs', 'day forty-four of billed Logs', 1)
rep('forty-second day', 'forty-third day', 1)
rep('forty-four full days', 'forty-five full days', 1)
rep('forty days past', 'forty-one days past', 2)
rep('Day thirty-eight on Eric', 'Day thirty-nine on Eric', 1)
rep('night thirty-eight', 'night thirty-nine', 2)
rep('day thirty-seven', 'day thirty-eight', 2)         # JDs
rep('thirty-one days unsent', 'thirty-two days unsent', 1)
rep('thirty days past its &ldquo;before Sep 22&rdquo; window', 'thirty-one days past its &ldquo;before Sep 22&rdquo; window', 1)
rep('the window closed Sep 22 &mdash; thirty days now', 'the window closed Sep 22 &mdash; thirty-one days now', 1)
rep('Day twenty-seven on all three', 'Day twenty-eight on all three', 1)
rep('twenty days', 'twenty-one days', 6)
rep('Twenty days', 'Twenty-one days', 1)
rep('eight days past', 'nine days past', 5)
rep('Eight days past due', 'Nine days past due', 1)
rep('day three', 'day four', 4)
rep('Iris, day eleven', 'Iris, day twelve', 1)
rep('hr-nda is 66 days', 'hr-nda is 67 days', 1)
rep('Ages as of Oct 22', 'Ages as of Oct 23', 1)
rep('Fourteen days carried', 'Fifteen days carried', 1)

def chip1(m):
    return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s2, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s3, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s2)
assert c1 + c2 == 5, f"chips: {c1}+{c2}"
s = s3

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-22T22:07:00-05:00', '2026-10-23T07:16:00-05:00', 2)
rep('<b>Brief compiled</b> Thu 7:26 AM &middot; data checked Thu 10:07 PM CT',
    '<b>Brief compiled</b> Fri 7:16 AM &middot; data checked Fri 7:16 AM CT', 1)
rep('Thursday, October 22 &middot; 2026', 'Friday, October 23 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD SUB ----------
new_sub = ('<p class="sub">Thursday closed light &mdash; <b>three failures, two needs-attention, three successes</b>, '
 'the week&rsquo;s gentlest close &mdash; and the evening turned into UGM prep: <b>Jr sent three brochure PDFs, you '
 'forwarded them to FedEx Print &amp; Go, and all three came back &ldquo;ready for retrieval&rdquo;</b> &mdash; '
 'your 8:00 block picks them up and the <b>9:00 block drops them at the Marriott</b>. Two Crexendo BillCenter '
 'password resets landed Thursday evening, so the booth-bill payment looks in motion &mdash; no confirmation '
 'either way yet. Today is deadline day: <b>ProGraphix is nine days past and the submit-by is TODAY</b> (Cathy '
 'unanswered, draft deleted), the <b>Iris one-pagers are due</b> &mdash; you blocked 10:00&ndash;10:45 for the '
 'one-pager, scenarios and release notes &mdash; and new this morning: <b>Tim booked an Oracle MAKE / ETA review '
 'for 2:00</b> (Adam and Jr cc&rsquo;d; invite unaccepted) while your drafted instructions sit unsent on day four '
 '&mdash; send them before 2:00 or walk them through live. Carried: the Emilio recap at <b>twenty-one days</b>. '
 'The line: Friday opened clean. No reactions saved.</p>')
rx(r'<p class="sub">.*?No reactions saved\.</p>', lambda m: new_sub, 1, re.DOTALL)

# ---------- 4. LEDGER: Friday opener (restores 'window open' to 2) ----------
rep('nothing after 7:49</b> &mdash; verified at 10:07 PM, trash included.',
    'nothing after 7:49</b> &mdash; verified at 10:07 PM, trash included. The overnight into Friday stayed quiet '
    '&mdash; <b>Friday opened clean</b>: the Daily Digests on schedule at 7:00&ndash;7:01 and no alerts by 7:16 '
    '&mdash; window open.', 1)

# ---------- 5. TODAY SCHEDULE (post-bump anchors) ----------
old_sched = '''        <div class="slot past"><div class="t">8:30 &ndash; 12:30</div><div class="w">Deep Work (Project Engineering)<small>#799 (day forty-seven) + the #992 / #996 / #997 reviews &middot; send the Tim draft &middot; the one-pagers due tomorrow</small></div></div>
        <div class="slot past"><div class="t">9:00 &ndash; 9:30</div><div class="w">Pay the Netsapiens booth bill<small>scheduled inside Deep Work &middot; UGM starts Monday</small></div></div>
        <div class="slot past"><div class="t">3:30 &ndash; 4:00</div><div class="w">Reserved<small>the sends: ProGraphix (submit-by tomorrow) &middot; Emilio (twenty-one days) &middot; the Printavo pickup</small></div></div>
        <div class="slot past"><div class="t">4:00 &ndash; 5:00</div><div class="w">Call with Scott Van Camp<small>recurring Thursday slot</small></div></div>'''
new_sched = '''        <div class="slot"><div class="t">8:00 &ndash; 8:30</div><div class="w">Get print outs<small>FedEx Office &middot; all three brochures confirmed ready last night</small></div></div>
        <div class="slot"><div class="t">9:00 &ndash; 9:30</div><div class="w">Drop off print outs at Marriott<small>the attendee-bag drop for UGM &middot; text Sue on arrival</small></div></div>
        <div class="slot"><div class="t">9:30 &ndash; 10:30</div><div class="w">AI-Powered Marketing with Claude<small>Gevity &middot; hands-on workshop</small></div></div>
        <div class="slot"><div class="t">10:00 &ndash; 10:15</div><div class="w">One pager for Spectrum<small>the Iris deliverable &mdash; due today</small></div></div>
        <div class="slot"><div class="t">10:15 &ndash; 10:30</div><div class="w">Scenarios for Spectrum<small>second Spectrum block</small></div></div>
        <div class="slot"><div class="t">10:30 &ndash; 10:45</div><div class="w">Share release notes with Spectrum<small>third Spectrum block</small></div></div>
        <div class="slot"><div class="t">2:00 &ndash; 2:45</div><div class="w">Oracle MAKE / ETA Review<small>Teams &middot; Tim, Adam + Jr cc&rsquo;d &middot; invite unaccepted, so it stays out of the chart</small></div></div>'''
rep(old_sched, new_sched, 1)
rep('todaynote">6h &mdash; Deep Work 8:30&ndash;12:30 with the booth bill 9&ndash;9:30 inside, Reserved 3:30&ndash;4, Scott 4&ndash;5',
    'todaynote">2.75h &mdash; print run 8&ndash;9:30, Spectrum blocks 10&ndash;10:45 inside the workshop, Oracle review at 2 unaccepted', 1)

# ---------- 6. CHART (Fri 2.75 / Sat 1.25 / Sun 0 / Mon 0.75 / Tue 0 / Wed 0 / Thu 2) ----------
rep('Thu Oct 22 &ndash; Wed Oct 28', 'Fri Oct 23 &ndash; Thu Oct 29', 1)
old_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(8.93% + 6px)">1.25</div>
            <div class="seg m" style="height:8.93%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(5.36% + 6px)">0.75</div>
            <div class="seg m" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>'''
new_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(19.64% + 6px)">2.75</div>
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
rep(old_bars, new_bars, 1)
rep('''<div><b>Thu</b>22</div><div><b>Fri</b>23</div>
          <div><b>Sat</b>24</div><div><b>Sun</b>25</div><div><b>Mon</b>26</div><div><b>Tue</b>27</div><div><b>Wed</b>28</div>''',
    '''<div><b>Fri</b>23</div><div><b>Sat</b>24</div>
          <div><b>Sun</b>25</div><div><b>Mon</b>26</div><div><b>Tue</b>27</div><div><b>Wed</b>28</div><div><b>Thu</b>29</div>''', 1)

# ---------- 7. TOP 5 ----------
rep('or let 10/23 go &mdash; that&rsquo;s tomorrow', 'or let 10/23 go &mdash; that&rsquo;s today', 1)
rep('Nothing moved Wednesday either. Today is the decision',
    'Nothing moved Thursday either. Today IS the submit-by day', 1)
rep('the submit-by is Friday &mdash; tomorrow.', 'the submit-by is today.', 1)
rep('<h4>Three days past the promise: the Tim draft is still unsent &mdash; UGM week starts Monday</h4>',
    '<h4>Four days past the promise &mdash; and Tim booked an Oracle review for 2:00 today</h4>', 1)
rep('finish it as the written record of the v2 scenario (/export CSV, three return fields) and send it so the handoff survives UGM week.',
    'finish it as the written record of the v2 scenario (/export CSV, three return fields) and send it before 2:00 &mdash; <b>Tim put &ldquo;Oracle MAKE / ETA Review&rdquo; on the calendar this morning</b> (Teams, Adam and Jr cc&rsquo;d), so the draft is the agenda.', 1)
rep('<h4>Due tomorrow: the vertical one-pagers for the Iris onboarding &mdash; promised at Tuesday&rsquo;s training</h4>',
    '<h4>Due today &mdash; and on the calendar: the Spectrum blocks at 10:00, 10:15 and 10:30</h4>', 1)
rep('vertical-specific one-pagers built from live customers by Friday &mdash; tomorrow</b>, and your action-items recap went out at 4:43.',
    'vertical-specific one-pagers built from live customers by Friday &mdash; today</b>, and you blocked the morning for them: <b>One pager 10:00, Scenarios 10:15, Release notes 10:30</b>.', 1)
rep('<span class="pill warn">Due tomorrow</span>', '<span class="pill warn">Due today &middot; blocked 10:00</span>', 1)
rep('Today&rsquo;s Deep Work (Engineering) 8:30&ndash;12:30 is the window',
    'The next Deep Work (Engineering) block is Mon Nov 2, 10&ndash;2 &mdash; UGM week has none; the gaps today are the only window', 1)
rep('<span class="pill quiet">DW today 8:30&ndash;12:30</span>', '<span class="pill quiet">Next DW: Nov 2</span>', 1)

# ---------- 8. COMING-UP CARDS ----------
rep(' &mdash; crawl-walk-run agreed; the one-pagers are due tomorrow</h4>',
    ' &mdash; crawl-walk-run agreed; the one-pagers are due today</h4>', 1)
rep('<h4 style="font-size:14px">Today &mdash; 6h: the booth bill inside Deep Work, then Scott at 4</h4>',
    '<h4 style="font-size:14px">Today &mdash; the print run, the Spectrum blocks, then Tim at 2</h4>', 1)
rep('Deep Work (Project Engineering) 8:30&ndash;12:30 carries the engineering backlog (#799 at day forty-seven, the #992/#996/#997 reviews) with <b>&ldquo;Pay the Netsapiens booth bill&rdquo; scheduled 9&ndash;9:30 inside it</b>. The 12:30&ndash;3:30 gap and Reserved 3:30&ndash;4 take the sends: the ProGraphix decision (submit-by is tomorrow), the Emilio recap (twenty-one days), the Tim draft (day four), the Printavo pickup &mdash; and the <b>one-pagers due tomorrow</b>. Scott Van Camp closes the day 4&ndash;5. From Taylor&rsquo;s session you owe the group channel <b>three energy leaks and three highest-leverage tasks</b> &mdash; Taylor follows up. (Wednesday&rsquo;s Debrief and Kyle calls weren&rsquo;t captured in Granola; only Sustainable Ambition was.)',
    'The brochures are <b>confirmed ready at FedEx Office</b> (all three uploads bounced back &ldquo;ready for retrieval&rdquo; Thursday evening) &mdash; pickup is blocked 8:00&ndash;8:30, the <b>Marriott drop 9:00&ndash;9:30</b>. AI-Powered Marketing runs 9:30&ndash;10:30 with your <b>Spectrum blocks at 10:00, 10:15 and 10:30</b> (one-pager, scenarios, release notes &mdash; the Iris deliverables, due today). <b>Tim&rsquo;s Oracle MAKE / ETA review is at 2:00</b> (Teams; Adam and Jr cc&rsquo;d; invite unaccepted) &mdash; send the drafted instructions before it or walk them through live. Still open in the gaps: ProGraphix (submit-by today), the Emilio recap (twenty-one days), the Printavo pickup, and the group-channel exercise from Taylor&rsquo;s session.', 1)
# markers card
rep('Monday&rsquo;s record (thirteen failures) stands; Wednesday ran second-heaviest at nine failures and nine needs-attention.',
    'Monday&rsquo;s record (thirteen failures) stands; Thursday was the week&rsquo;s lightest close &mdash; three failures, two needs-attention, three successes.', 1)
rep('This week: <b>today runs 6h</b> &mdash; the booth bill 9&ndash;9:30 inside Deep Work 8:30&ndash;12:30, then Scott at 4 (the 1:30 Reserved block came off the calendar); <b>tomorrow is the double deadline</b> &mdash; the ProGraphix submit-by and the <b>one-pagers owed to SpectrumVoIP</b> &mdash; around one scheduled hour (AI-Powered Marketing 9:30&ndash;10:30); Saturday holds a self-booked Acquisition.com session 12&ndash;1:15. UGM is Oct 26&ndash;30 in Austin &mdash; <b>shipping resolved: you hand-carry</b>, the attendee-bag one-pager drops at the hotel Friday, and the tees are ready at Printavo.',
    'Today: <b>the double deadline</b> &mdash; the ProGraphix submit-by and the SpectrumVoIP one-pagers &mdash; plus the print run (FedEx pickup 8:00, Marriott drop 9:00) and <b>Tim&rsquo;s Oracle review at 2:00</b>; Saturday holds the Acquisition.com session 12&ndash;1:15. UGM is Oct 26&ndash;30 in Austin &mdash; <b>the brochures print this morning for hand-carry</b>, the tees are ready at Printavo, and the next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.', 1)

# ---------- 9. WEEK FLAGS ----------
rep('<span class="pill warn">Today</span> Thursday runs 6h &mdash; one long engineering block, then Scott at 4',
    '<span class="pill warn">Today</span> Deadline day: 2.75h scheduled around three sends and the print run', 1)
rep('One block carries the day: <b>Deep Work (Project Engineering) 8:30&ndash;12:30</b> with the booth bill scheduled 9&ndash;9:30 inside it, then Reserved 3:30&ndash;4 and <b>Scott Van Camp 4&ndash;5</b>. The 12:30&ndash;3:30 gap is the send window: the <b>ProGraphix decision</b> (nine days past the submit-by &mdash; Friday is tomorrow), the Emilio recap (twenty-one days), the Tim draft on day four, and the <b>one-pagers due tomorrow</b>.',
    'The morning is the UGM print run &mdash; <b>FedEx Office pickup 8:00, Marriott drop 9:00</b> &mdash; then AI-Powered Marketing 9:30&ndash;10:30 with the <b>Spectrum blocks 10:00&ndash;10:45</b> (one-pager, scenarios, release notes) stacked inside. The afternoon holds <b>Tim&rsquo;s Oracle MAKE / ETA review at 2:00</b> (invite unaccepted). In the gaps: the <b>ProGraphix decision</b> (nine days past &mdash; the submit-by is today), the Emilio recap (twenty-one days), and the Tim draft on day four &mdash; the 2:00 review is its natural deadline.', 1)
rep('<span class="pill warn">This week</span> Two deadlines land tomorrow &mdash; then UGM takes the week',
    '<span class="pill warn">This week</span> Deadline day today &mdash; then UGM takes the week', 1)
rep('Today runs 6h with the booth bill 9&ndash;9:30 and Scott at 4. <b>Friday stacks the deadlines</b>: the ProGraphix submit-by, the Iris one-pagers, and the attendee-bag one-pager to the hotel &mdash; around AI-Powered Marketing with Claude 9:30&ndash;10:30. New on the wire: <b>LiveKit named the GPT-Live 503 cause (the BAA &mdash; not HIPAA-eligible on Inference yet)</b> and flagged <b>uncharged usage invoices</b> (&ldquo;action needed,&rdquo; forwarded by Jr) &mdash; and Vipin Gupta messaged you in the Whova app.',
    'Today is the last working day before UGM: the ProGraphix submit-by, the Iris one-pagers and the Marriott brochure drop all land today, and <b>Tim&rsquo;s Oracle review sits at 2:00</b>. Saturday holds the Acquisition.com session 12&ndash;1:15; <b>UGM runs Monday through Thursday in Austin</b> with only the Product Sync (Mon 8:00) and the declined Izzy slot on the calendar. Still on the wire: <b>LiveKit&rsquo;s uncharged-invoices notice</b> and the GPT-Live BAA answer (Jr&rsquo;s call), two <b>Crexendo BillCenter password resets Thursday evening</b> (the booth-bill payment in motion, unconfirmed), and <b>Vipin Gupta (Tragofone) still waiting in the Whova app</b>.', 1)

# ---------- 10. TASKS TABLE ----------
rep('<tr><td class="tid">Today 3:30&ndash;4</td>', '<tr><td class="tid">Today, in gaps</td>', 1)
rep('<tr><td class="tid">Today 8:30&ndash;12:30</td><td><b>The identification query first</b>',
    '<tr><td class="tid">Mon Nov 2</td><td><b>The identification query first</b>', 1)
rep('the 12:30&ndash;3:30 gap is today&rsquo;s pocket', 'the 11&ndash;2 gap is today&rsquo;s pocket', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('window open') == 2
assert s.count('2026-10-23T07:16:00-05:00') == 2
assert s.count('Thu Oct 22') == 0
assert s.count('due tomorrow') == 0 and s.count('Due tomorrow') == 0
assert s.count('eight days past') == 0 and s.count('twenty days') == 0
assert 'Good evening' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s
assert s.count('Thursday runs 6h') == 0

open(p, 'w', encoding='utf-8').write(s)
print('friday turn applied:', len(s), 'chars')
