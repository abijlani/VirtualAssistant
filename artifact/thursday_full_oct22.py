#!/usr/bin/env python3
# Thursday Oct 22 2026 full-pass date turn.
# Age bumps FIRST (counts verified against the live template), then structural rewrites
# written with post-bump values. Calendar check: the 1:30-2 Reserved block is gone, so
# Thursday runs 6h (DW 4 + booth 0.5 + Reserved 0.5 + Scott 1), not the carried 6.5h.
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
rep('fifty-one days past', 'fifty-two days past', 2)
rep('55 days', '56 days', 1)
rep('day forty-five', 'day forty-six', 3)               # 799
rep('day forty-four', 'day forty-five', 3)              # Eric x2 + trio note
rep('day forty-two of billed Logs', 'day forty-three of billed Logs', 1)
rep('forty-first day', 'forty-second day', 1)
rep('forty-three full days', 'forty-four full days', 1)
rep('thirty-nine days past', 'forty days past', 2)
rep('Day thirty-seven on Eric', 'Day thirty-eight on Eric', 1)
rep('night thirty-seven', 'night thirty-eight', 2)
rep('day thirty-six', 'day thirty-seven', 2)            # JDs
rep('thirty days unsent', 'thirty-one days unsent', 1)
rep('twenty-nine days past its &ldquo;before Sep 22&rdquo; window', 'thirty days past its &ldquo;before Sep 22&rdquo; window', 1)
rep('the window closed Sep 22 &mdash; twenty-nine days now', 'the window closed Sep 22 &mdash; thirty days now', 1)
rep('Day twenty-six on all three', 'Day twenty-seven on all three', 1)
rep('nineteen days', 'twenty days', 6)
rep('Nineteen days', 'Twenty days', 1)
rep('seven days past', 'eight days past', 5)
rep('Seven days past due', 'Eight days past due', 1)
rep('day two', 'day three', 3)
rep('Iris, day ten', 'Iris, day eleven', 1)
rep('hr-nda is 65 days', 'hr-nda is 66 days', 1)
rep('Ages as of Oct 21', 'Ages as of Oct 22', 1)
# Projects-tab carry note was last rewritten Monday at "Eleven days"; frozen since -> true value is fourteen.
rep('Eleven days carried', 'Fourteen days carried', 1)
rep('Deep Work 10&ndash;5 is today&rsquo;s pocket', 'the 12:30&ndash;3:30 gap is today&rsquo;s pocket', 1)

def chip1(m):
    return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s2, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s3, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s2)
assert c1 + c2 == 5, f"chips: {c1}+{c2}"
s = s3

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-21T22:07:00-05:00', '2026-10-22T07:26:00-05:00', 2)
rep('<b>Brief compiled</b> Wed 7:21 AM &middot; data checked Wed 10:07 PM CT',
    '<b>Brief compiled</b> Thu 7:26 AM &middot; data checked Thu 7:26 AM CT', 1)
rep('Wednesday, October 21 &middot; 2026', 'Thursday, October 22 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD SUB ----------
new_sub = ('<p class="sub">Wednesday&rsquo;s 8h day is behind you &mdash; Taylor&rsquo;s Sustainable Ambition session ran '
 '(satisfaction spectrum, energy leaks; <b>you owe the group channel your three biggest leaks and three '
 'highest-leverage tasks</b>, Taylor follows up), and the Debrief + Kyle calls went uncaptured in Granola. What '
 'didn&rsquo;t move: <b>the Tim draft is still in drafts &mdash; day three</b>, the Emilio recap hits <b>twenty '
 'days</b>, and <b>ProGraphix is eight days past the submit-by &mdash; which is tomorrow</b>: today is the last '
 'full day to submit, reply, or call Cathy. New on the wire: <b>LiveKit named the GPT-Live 503 cause &mdash; the '
 'BAA</b> (GPT-Live isn&rsquo;t HIPAA-eligible on LiveKit Inference yet; quota and region were never it) and <b>Jr '
 'forwarded LiveKit&rsquo;s &ldquo;action needed&rdquo; notice on uncharged usage invoices</b> &mdash; a '
 'payment-method fix to make before UGM week. Also due tomorrow: <b>the Iris one-pagers</b>. Today runs 6h: the '
 'booth bill 9&ndash;9:30 inside Deep Work 8:30&ndash;12:30, Scott at 4 &mdash; and Vipin Gupta messaged you in '
 'the Whova app. The line: Wednesday closed at nine failures, nine needs-attention; Thursday opened clean. '
 'No reactions saved.</p>')
rx(r'<p class="sub">.*?No reactions saved\.</p>', lambda m: new_sub, 1, re.DOTALL)

# ---------- 4. LEDGER: Thursday opener (restores 'window open' to 2) ----------
rep('nothing after 7:54</b> &mdash; verified at 10:07 PM, trash included.',
    'nothing after 7:54</b> &mdash; verified at 10:07 PM, trash included. The overnight into Thursday stayed '
    'quiet &mdash; <b>Thursday opened clean</b>: the four Daily Digests on schedule at 7:00&ndash;7:01 and a '
    'quiet line by 7:26 &mdash; window open.', 1)

# ---------- 5. TODAY SCHEDULE (post-bump anchors: 'twenty days') ----------
old_sched = '''        <div class="slot past"><div class="t">8:00 &ndash; 8:45</div><div class="w">Gym Series: The Circuit<small>Gevity &middot; registered last night &middot; invite unaccepted, so it stays out of the chart</small></div></div>
        <div class="slot past"><div class="t">9:00 &ndash; 9:30</div><div class="w">Recover + Shower<small>after the circuit</small></div></div>
        <div class="slot past"><div class="t">9:30 &ndash; 10:30</div><div class="w">Sustainable Ambition<small>Gevity &middot; Taylor&rsquo;s session: satisfaction spectrum, energy leaks, a sample week</small></div></div>
        <div class="slot past"><div class="t">11:00 &ndash; 3:00</div><div class="w">Deep Work (Project Engineering)<small>2F-15 artwork due today &middot; the #992 / #996 / #997 reviews + #799 &middot; send the Tim draft</small></div></div>
        <div class="slot past"><div class="t">11:30 &ndash; 12:30</div><div class="w">Debrief AI &mdash; Bodhi &amp; Taylor<small>Meet &middot; Taylor&rsquo;s agenda: website name, workshop review, partners &mdash; ends on the Ashlyn ask</small></div></div>
        <div class="slot past"><div class="t">12:30 &ndash; 1:00</div><div class="w">Kyle + Bodhi/Taylor<small>Meet &middot; the $7,500 backend build &mdash; Taylor runs it, you join on Zoom</small></div></div>
        <div class="slot past"><div class="t">3:00 &ndash; 4:00</div><div class="w">Transition, Talking, Triage<small>the Emilio recap (twenty days) &middot; the ProGraphix reply &middot; the Printavo pickup</small></div></div>'''
new_sched = '''        <div class="slot"><div class="t">8:30 &ndash; 12:30</div><div class="w">Deep Work (Project Engineering)<small>#799 (day forty-six) + the #992 / #996 / #997 reviews &middot; send the Tim draft &middot; the one-pagers due tomorrow</small></div></div>
        <div class="slot"><div class="t">9:00 &ndash; 9:30</div><div class="w">Pay the Netsapiens booth bill<small>scheduled inside Deep Work &middot; UGM starts Monday</small></div></div>
        <div class="slot"><div class="t">3:30 &ndash; 4:00</div><div class="w">Reserved<small>the sends: ProGraphix (submit-by tomorrow) &middot; Emilio (twenty days) &middot; the Printavo pickup</small></div></div>
        <div class="slot"><div class="t">4:00 &ndash; 5:00</div><div class="w">Call with Scott Van Camp<small>recurring Thursday slot</small></div></div>'''
rep(old_sched, new_sched, 1)
rep('todaynote">8h &mdash; Sustainable Ambition 9:30, Deep Work 11&ndash;3 with the Debrief 11:30 + Kyle 12:30 inside, Transition 3&ndash;4',
    'todaynote">6h &mdash; Deep Work 8:30&ndash;12:30 with the booth bill 9&ndash;9:30 inside, Reserved 3:30&ndash;4, Scott 4&ndash;5', 1)

# ---------- 6. CHART (Thu 6 / Fri 1 / Sat 1.25 / Sun 0 / Mon 0.75 / Tue 0 / Wed 0) ----------
rep('Wed Oct 21 &ndash; Tue Oct 27', 'Thu Oct 22 &ndash; Wed Oct 28', 1)
old_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(57.14% + 6px)">8</div>
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
new_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>
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
rep(old_bars, new_bars, 1)
rep('''<div><b>Wed</b>21</div><div><b>Thu</b>22</div>
          <div><b>Fri</b>23</div><div><b>Sat</b>24</div><div><b>Sun</b>25</div><div><b>Mon</b>26</div><div><b>Tue</b>27</div>''',
    '''<div><b>Thu</b>22</div><div><b>Fri</b>23</div>
          <div><b>Sat</b>24</div><div><b>Sun</b>25</div><div><b>Mon</b>26</div><div><b>Tue</b>27</div><div><b>Wed</b>28</div>''', 1)

# ---------- 7. TOP 5 ----------
rep('or let 10/23 go', 'or let 10/23 go &mdash; that&rsquo;s tomorrow', 1)
rep('Nothing moved Tuesday either. Today is the decision',
    'Nothing moved Wednesday either. Today is the decision', 1)
rep('the submit-by is Friday &mdash; two days out.', 'the submit-by is Friday &mdash; tomorrow.', 1)
rep('<h4>Two days past the promise: the Tim draft is still unsent &mdash; though the Izzy call moved the work</h4>',
    '<h4>Three days past the promise: the Tim draft is still unsent &mdash; UGM week starts Monday</h4>', 1)
rep('<h4>New Friday commitment: vertical one-pagers for the Iris onboarding &mdash; promised at Tuesday&rsquo;s training</h4>',
    '<h4>Due tomorrow: the vertical one-pagers for the Iris onboarding &mdash; promised at Tuesday&rsquo;s training</h4>', 1)
rep('vertical-specific one-pagers built from live customers by Friday</b>',
    'vertical-specific one-pagers built from live customers by Friday &mdash; tomorrow</b>', 1)
rep('<span class="pill warn">Due Friday</span>', '<span class="pill warn">Due tomorrow</span>', 1)
rep('Today&rsquo;s Deep Work (Engineering) 11&ndash;3 is the window',
    'Today&rsquo;s Deep Work (Engineering) 8:30&ndash;12:30 is the window', 1)
rep('<span class="pill quiet">DW today 11&ndash;3</span>', '<span class="pill quiet">DW today 8:30&ndash;12:30</span>', 1)

# ---------- 8. NEW FLAG: LiveKit billing + GPT-Live root cause ----------
rep('''<div class="flag crit">
          <h3><span class="pill crit">Customer</span> Day thirty-eight on Eric''',
'''<div class="flag warn">
          <h3><span class="pill warn">Billing</span> LiveKit flagged uncharged usage invoices &mdash; and named the GPT-Live 503 cause: the BAA</h3>
          <p><b>Jr forwarded LiveKit AR&rsquo;s &ldquo;action needed&rdquo; notice Wednesday midday</b>: usage invoices on the production project are accruing without a successful charge &mdash; a payment-method fix in the LiveKit billing console closes it, best done before UGM week starts Monday. Separately, <b>the GPT-Live 503 ticket broke open Wednesday at 11:00</b>: support says the production project is covered by the BAA and <b>GPT-Live isn&rsquo;t HIPAA-eligible on LiveKit Inference yet</b> &mdash; quota and region were never the issue. The call is Jr&rsquo;s to make: wait for HIPAA eligibility or run GPT-Live outside the BAA project.</p>
        </div>

        <div class="flag crit">
          <h3><span class="pill crit">Customer</span> Day thirty-eight on Eric''', 1)

# ---------- 9. COMING-UP CARDS ----------
rep(' &mdash; crawl-walk-run agreed; the one-pagers are due Friday</h4>',
    ' &mdash; crawl-walk-run agreed; the one-pagers are due tomorrow</h4>', 1)
rep('The next session is Friday (the Tuesday slot falls in UGM week; the series resumes Fri Oct 30, 2&ndash;3).',
    'The next session is Fri Oct 30, 2&ndash;3 (the Tuesday slot falls in UGM week).', 1)
rep('<h4 style="font-size:14px">Today &mdash; a full 8h: the Debrief and Kyle back-to-back inside Deep Work</h4>',
    '<h4 style="font-size:14px">Today &mdash; 6h: the booth bill inside Deep Work, then Scott at 4</h4>', 1)
rep('Sustainable Ambition 9:30&ndash;10:30 is Taylor&rsquo;s session. Deep Work (Project Engineering) 11&ndash;3 carries the <b>2F-15 artwork (due today)</b>, the #992/#996/#997 reviews and the Tim draft &mdash; with the <b>Debrief 11:30&ndash;12:30</b> (Taylor&rsquo;s agenda ends on the Ashlyn ask: what you built, when, what you charged) and <b>Kyle at 12:30</b> stacked inside, the block effectively runs 11&ndash;11:30 and 1&ndash;3. Transition 3&ndash;4 takes the sends: the Emilio recap (twenty days), the ProGraphix reply, and the Printavo pickup.',
    'Deep Work (Project Engineering) 8:30&ndash;12:30 carries the engineering backlog (#799 at day forty-six, the #992/#996/#997 reviews) with <b>&ldquo;Pay the Netsapiens booth bill&rdquo; scheduled 9&ndash;9:30 inside it</b>. The 12:30&ndash;3:30 gap and Reserved 3:30&ndash;4 take the sends: the ProGraphix decision (submit-by is tomorrow), the Emilio recap (twenty days), the Tim draft (day three), the Printavo pickup &mdash; and the <b>one-pagers due tomorrow</b>. Scott Van Camp closes the day 4&ndash;5. From Taylor&rsquo;s session you owe the group channel <b>three energy leaks and three highest-leverage tasks</b> &mdash; Taylor follows up. (Wednesday&rsquo;s Debrief and Kyle calls weren&rsquo;t captured in Granola; only Sustainable Ambition was.)', 1)
# markers card
rep('Monday&rsquo;s record (thirteen failures) stood; Tuesday eased to eight.',
    'Monday&rsquo;s record (thirteen failures) stands; Wednesday ran second-heaviest at nine failures and nine needs-attention.', 1)
rep('This week: <b>today runs a full 8h</b> &mdash; the 2F-15 artwork deadline (scope confirmed: just the two escalator signs) with the Debrief 11:30 and Kyle 12:30 inside Deep Work; <b>Thursday 6.5h</b> with the Netsapiens booth bill 9&ndash;9:30 and Scott at 4; Friday one hour (AI-Powered Marketing 9:30&ndash;10:30) plus the <b>one-pagers owed to SpectrumVoIP</b>; Saturday holds a self-booked Acquisition.com session 12&ndash;1:15.',
    'This week: <b>today runs 6h</b> &mdash; the booth bill 9&ndash;9:30 inside Deep Work 8:30&ndash;12:30, then Scott at 4 (the 1:30 Reserved block came off the calendar); <b>tomorrow is the double deadline</b> &mdash; the ProGraphix submit-by and the <b>one-pagers owed to SpectrumVoIP</b> &mdash; around one scheduled hour (AI-Powered Marketing 9:30&ndash;10:30); Saturday holds a self-booked Acquisition.com session 12&ndash;1:15.', 1)

# ---------- 10. WEEK FLAGS ----------
rep('<span class="pill warn">Today</span> Wednesday runs exactly 8h &mdash; the Kyle call pushed it to the line',
    '<span class="pill warn">Today</span> Thursday runs 6h &mdash; one long engineering block, then Scott at 4', 1)
rep('Three meetings stack into the middle: Sustainable Ambition 9:30, then the <b>Debrief 11:30 and Kyle 12:30 back-to-back inside Deep Work 11&ndash;3</b> &mdash; the engineering block effectively runs 11&ndash;11:30 and 1&ndash;3 against the <b>2F-15 artwork due today</b>. Still open: the <b>ProGraphix decision</b> (eight days past the submit-by &mdash; Friday is two days out), the Emilio recap (twenty days), and the Tim draft on day three.',
    'One block carries the day: <b>Deep Work (Project Engineering) 8:30&ndash;12:30</b> with the booth bill scheduled 9&ndash;9:30 inside it, then Reserved 3:30&ndash;4 and <b>Scott Van Camp 4&ndash;5</b>. The 12:30&ndash;3:30 gap is the send window: the <b>ProGraphix decision</b> (eight days past the submit-by &mdash; Friday is tomorrow), the Emilio recap (twenty days), the Tim draft on day three, and the <b>one-pagers due tomorrow</b>.', 1)
rep('<span class="pill warn">This week</span> A steady week into the 2F-15 and booth deadlines &mdash; Wednesday&rsquo;s debrief now has an agenda',
    '<span class="pill warn">This week</span> Two deadlines land tomorrow &mdash; then UGM takes the week', 1)
rep('Today runs <b>a full 8h</b> &mdash; the 2F-15 artwork deadline (scope confirmed: two escalator signs) plus the <b>&ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30 and the new Kyle call 12:30&ndash;1</b>, whose posted agenda includes the website, the workshop review, preferred partners, and a direct ask: what you built for Ashlyn, when, and what you charged; Thursday Oct 22 6.5h with the Netsapiens booth bill 9&ndash;9:30 and Scott at 4; Friday Oct 23 holds one hour &mdash; AI-Powered Marketing with Claude 9:30&ndash;10:30.',
    'Today runs 6h with the booth bill 9&ndash;9:30 and Scott at 4. <b>Friday stacks the deadlines</b>: the ProGraphix submit-by, the Iris one-pagers, and the attendee-bag one-pager to the hotel &mdash; around AI-Powered Marketing with Claude 9:30&ndash;10:30. New on the wire: <b>LiveKit named the GPT-Live 503 cause (the BAA &mdash; not HIPAA-eligible on Inference yet)</b> and flagged <b>uncharged usage invoices</b> (&ldquo;action needed,&rdquo; forwarded by Jr) &mdash; and Vipin Gupta messaged you in the Whova app.', 1)

# ---------- 11. TASKS TABLE ----------
rep('<tr><td class="tid">Today 3&ndash;4</td>', '<tr><td class="tid">Today 3:30&ndash;4</td>', 1)
rep('<tr><td class="tid">Today 11&ndash;3</td><td><b>The identification query first</b>',
    '<tr><td class="tid">Today 8:30&ndash;12:30</td><td><b>The identification query first</b>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('window open') == 2
assert s.count('2026-10-22T07:26:00-05:00') == 2
assert s.count('Wed Oct 21') == 0
assert s.count('nineteen days') == 0
assert s.count('seven days past') == 0
assert 'Thursday 6.5h' not in s and 'Thursday Oct 22 6.5h' not in s
assert '">6.5<' not in s
assert 'Good evening' not in s
assert s.count('Transition 3&ndash;4') == 0, s.count('Transition 3&ndash;4')

open(p, 'w', encoding='utf-8').write(s)
print('thursday turn applied:', len(s), 'chars')
