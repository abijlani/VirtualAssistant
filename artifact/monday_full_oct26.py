# Monday Oct 26, 2026 — FULL morning pass (UGM day 1, Austin).
# Sunday closed 17F/0NA/8S (new streak high). Monday opened 1F/1NA/1S by 7:13 AM.
# Calendar now carries the full UGM build-out: Booth Setup 12-4, Sponsor Kick-off 4-5,
# Reception Dinner 6:30-8:30, plus a barbershop run 9:30-11:30 => 9.75h booked today.
# Tue/Wed are 13h booth days. Drafts (tarbour, rtanyag) still unsent => Tim day seven.
# No Granola captures over the weekend. No tarbour/pgaustin/emilio/lmathwig motion.
# New: review requests on PR #886 (VOXAI-813) and #991 (VOXAI-937), bugbot sweeping;
# Whova message from Nunnally Torres. cc-state empty (no republish-wake all weekend).
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    assert s.count(old) == n, f"{old!r}: {s.count(old)} != {n}"
    s = s.replace(old, new)

def rx(pat, new, n, flags=0):
    global s
    s, c = re.subn(pat, new, s, flags=flags)
    assert c == n, f"{pat!r}: {c} != {n}"

# ---------- global age bumps FIRST (post-bump values used in structural rewrites) ----------
rep('day forty-nine', 'day fifty', 3)            # #799
rep('day forty-eight', 'day forty-nine', 3)      # Eric / Izzy trio
rep('day forty;', 'day forty-one;', 1)           # JDs
rep('forty-three days past', 'forty-four days past', 2)
rep('night forty-one', 'night forty-two', 2)
rep('thirty-three days past', 'thirty-four days past', 1)  # Appulse
rep('twenty-three days', 'twenty-four days', 4)  # Emilio
rep('Twenty-three days', 'Twenty-four days', 1)
rep('eleven days past', 'twelve days past', 6)   # ProGraphix
rep('Eleven days past', 'Twelve days past', 1)
rep('day six', 'day seven', 4)                   # Tim ('day sixt*' == 0, safe)
rep('Five days past the promise', 'Six days past the promise', 1)
rep('Iris, day fourteen', 'Iris, day fifteen', 1)
rep('Seventeen days carried', 'Eighteen days carried', 1)
rep('hr-nda is 69 days old', 'hr-nda is 70 days old', 1)
rep('Ages as of Oct 25', 'Ages as of Oct 26', 1)
rep('bugbot swept #992, #996 and #997 Monday', 'bugbot swept #992, #996 and #997 last Monday', 1)

# chip auto-bump (5 total)
def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- date turn: mast, stamps ----------
rep('2026-10-25T22:08:00-05:00', '2026-10-26T07:25:00-05:00', 2)
rep('Sunday, October 25 &middot; 2026', 'Monday, October 26 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)
rep('<b>Brief compiled</b> Sun 8:10 AM &middot; data checked Sun 10:08 PM CT',
    '<b>Brief compiled</b> Mon 7:25 AM &middot; data checked Mon 7:25 AM CT', 1)

# masthead paragraph (full replace)
m0 = s.find('Saturday was the quiet day')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Sunday did the opposite of Saturday: <b>seventeen failures against eight successes</b> &mdash; '
 'the streak&rsquo;s heaviest single day and the third Sunday spike in a row &mdash; before the line '
 'went quiet at 5:33 PM. <b>UGM opens today</b>, and the day is far fuller than the calendar held '
 'yesterday: Product Sync at 8:00 with Jr and Eelco, the barbershop run 9:30&ndash;11:30, '
 '<b>Booth Setup 12&ndash;4</b>, the Sponsor Kick-off 4&ndash;5 and the Reception Dinner '
 '6:30&ndash;8:30 &mdash; 9.75 booked hours, the first day past the 8h line in weeks. The pockets are '
 '11:30&ndash;12 and 5&ndash;6:30; they carry the two sends: <b>the damage-control call to Cathy at '
 'ProGraphix</b> (twelve days past the submit-by) and <b>the Tim record on day seven</b>. If the '
 '<b>Printavo tees</b> (Cedar Park) aren&rsquo;t in hand, pickup is before the floor or not at all. '
 'Overnight the line opened 1&ndash;1&ndash;1 by 7:13 AM. No reactions saved.</p>'
) + s[m1:]

# ledger: Monday opener (restores 'window open' to 2)
rep('Sunday closes 17&ndash;0&ndash;8.',
    'Sunday closes 17&ndash;0&ndash;8. Monday opened before the brief: a needs-attention at 6:45, '
    'a &ldquo;Call handled&rdquo; at 6:50 and a failure at 7:13 &mdash; 1&ndash;1&ndash;1 by 7:25 AM, window open.', 1)

# ---------- today schedule ----------
rep('0h booked &mdash; recovery Sunday; UGM opens tomorrow',
    '9.75h booked &mdash; UGM day one: setup, kick-off, reception', 1)
rep('<div class="slot free"><div class="t">All day</div><div class="w">Nothing booked<small>recovery Sunday &middot; UGM opens tomorrow &mdash; Product Sync 8:00, then Austin</small></div></div>',
    '<div class="slot"><div class="t">8:00&ndash;8:45</div><div class="w">Weekly Product Sync<small>Jr + Eelco &mdash; last sync before the floor</small></div></div>\n'
    '        <div class="slot"><div class="t">9:30&ndash;11:30</div><div class="w">Beard trim at Olde Soul<small>drives folded in (9:30 out, 11:00 back)</small></div></div>\n'
    '        <div class="slot free"><div class="t">11:30&ndash;12:00</div><div class="w">Open pocket<small>the Cathy call fits here &mdash; twelve days past</small></div></div>\n'
    '        <div class="slot"><div class="t">12:00&ndash;4:00</div><div class="w">Booth Setup<small>UGM, Austin &mdash; brochures hand-carried; tees if picked up</small></div></div>\n'
    '        <div class="slot"><div class="t">4:00&ndash;5:00</div><div class="w">UGM Sponsor Kick-off<small>sponsor briefing on the floor</small></div></div>\n'
    '        <div class="slot free"><div class="t">5:00&ndash;6:30</div><div class="w">Open pocket<small>the Tim record (day seven) &mdash; or the PR queue</small></div></div>\n'
    '        <div class="slot"><div class="t">6:30&ndash;8:30</div><div class="w">UGM Reception Dinner<small>evening event, day one closes</small></div></div>', 1)

# ---------- top 5 ----------
rep('ProGraphix &mdash; twelve days past &mdash; the submit-by came and went Friday with the thread silent',
    'ProGraphix &mdash; twelve days past &mdash; today is the damage-control call to Cathy', 1)
rep('If the table cover and banner still matter, Monday is damage control: call Cathy and ask what&rsquo;s recoverable.',
    'If the table cover and banner still matter, today is damage control: call Cathy and ask what&rsquo;s recoverable &mdash; the 11:30 pocket is the window before the booth takes the day.', 1)
rep('and send it &mdash; <b>Friday&rsquo;s 2:00 Oracle MAKE / ETA review has come and gone</b>, and whatever was agreed live still isn&rsquo;t on paper. UGM week starts Monday.',
    'and send it &mdash; <b>Friday&rsquo;s 2:00 Oracle MAKE / ETA review has come and gone</b>, and whatever was agreed live still isn&rsquo;t on paper. UGM is here: the 5:00 pocket is the realistic slot.', 1)
rep('(Invoice #1186) and UGM opens tomorrow.', '(Invoice #1186) and UGM opens today &mdash; pickup is now or never.', 1)
rep('<span class="pill warn">Tees: pickup this weekend</span>', '<span class="pill warn">Tees: pickup before the floor</span>', 1)
rep('#799 at day fifty &mdash; and PR #992 now waits on your review',
    '#799 at day fifty &mdash; and the review queue grew to four this morning', 1)
rep('The next Deep Work (Engineering) block is Mon Nov 2, 10&ndash;2 &mdash; UGM week has none; the gaps today are the only window',
    'This morning <b>Pagebakers requested your review on #886</b> (VOXAI-813, caller vs dialed number split) <b>and #991</b> (VOXAI-937, insights usage card date filter), with bugbot sweeping both. The next Deep Work (Engineering) block is Mon Nov 2, 10&ndash;2 &mdash; UGM week has none', 1)
rep('<span class="pill warn">Two reviews deep</span>', '<span class="pill warn">Four reviews deep</span>', 1)

# ---------- flags ----------
f0 = s.find('<span class="pill warn">Today</span> Sunday is open &mdash; the recovery day before UGM')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:s.rfind('<h3>', 0, f0)] + (
 '<h3><span class="pill warn">Today</span> UGM day one is the heaviest day in weeks &mdash; 9.75h booked</h3>\n'
 '          <p>Product Sync 8:00, the barbershop run 9:30&ndash;11:30, <b>Booth Setup 12&ndash;4</b>, Sponsor '
 'Kick-off 4&ndash;5, Reception Dinner 6:30&ndash;8:30. The only pockets are <b>11:30&ndash;12</b> and '
 '<b>5&ndash;6:30</b> &mdash; they hold the carried sends: <b>Cathy at ProGraphix</b> (twelve days past) and '
 '<b>the Tim record</b> (day seven). If the <b>Printavo tees</b> (Cedar Park) aren&rsquo;t in hand, the morning '
 'is the last chance before the floor.</p>'
) + s[f1:]

rep('UGM takes this week &mdash; tomorrow through Thursday in Austin',
    'UGM takes this week &mdash; today through Thursday in Austin', 1)
g0 = s.find('<p><b>UGM runs tomorrow through Thursday</b>')
g1 = s.find('</p>', g0) + len('</p>')
assert 0 < g0 < g1
s = s[:g0] + (
 '<p><b>The UGM schedule filled in</b>: booth time runs 7:30&ndash;4 Tuesday and Wednesday &mdash; <b>13-hour '
 'days</b> once the evening events are counted (Banger&rsquo;s Tuesday, the Bullock Museum reception Wednesday) '
 '&mdash; and Thursday holds booth till 10:30, Scott at 2 and two Reserved blocks; Friday brings the Gevity '
 'pizza party 12:30 and <b>the Iris session at 2</b> &mdash; the series resumes. Still on the wire: '
 '<b>LiveKit&rsquo;s uncharged-invoices notice</b> and the GPT-Live BAA answer (Jr&rsquo;s call), the booth-bill '
 'payment (BillCenter resets Thursday, unconfirmed), and now <b>two people waiting in Whova</b> &mdash; Vipin '
 'Gupta (Tragofone) and, since last night, Nunnally Torres. Brochures are hand-carried; the one-pager is at the '
 'Marriott.</p>'
) + s[g1:]

# ---------- markers card ----------
k0 = s.find('Monday&rsquo;s weekday record (thirteen failures) stands')
k1 = s.find('</p>', k0) + len('</p>')
assert 0 < k0 < k1
s = s[:k0] + (
 'Sunday closed <b>17&ndash;0&ndash;8 &mdash; the streak&rsquo;s heaviest single day</b>, the third Sunday spike '
 'in a row (fourteen, then nine, now seventeen), pushing Monday&rsquo;s weekday thirteen to second place; '
 'Saturday remains the only failure-free day. <b>UGM runs today through Thursday</b> (Austin): Tuesday and '
 'Wednesday are 13-hour booth days, Thursday holds Scott at 2, Friday the Gevity pizza party and <b>the Iris '
 'session at 2</b>. The next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.</p>'
) + s[k1:]

# ---------- coming-up card: tomorrow -> today ----------
rep('Tomorrow &mdash; UGM opens in Austin', 'Today &mdash; UGM opens in Austin', 1)
h0 = s.find('Product Sync at 8:00 with Jr and Eelco, then the conference floor')
h1 = s.find('</p>', h0) + len('</p>')
assert 0 < h0 < h1
s = s[:h0] + (
 'Product Sync at 8:00 with Jr and Eelco, then <b>Booth Setup 12&ndash;4, Sponsor Kick-off 4&ndash;5 and the '
 'Reception Dinner 6:30&ndash;8:30</b> &mdash; UGM runs through Thursday. The brochures are hand-carried and the '
 'one-pager is at the Marriott; <b>the Printavo tees</b> (Invoice #1186, Cedar Park) are the remaining physical '
 'item if not yet picked up. Carried into the week: <b>the Cathy call</b> (twelve days past), <b>the Tim '
 'record</b> (day seven), the Emilio recap (twenty-four days), Taylor&rsquo;s group-channel exercise, and '
 '<b>two review requests that landed this morning</b> (#886, #991).</p>'
) + s[h1:]

# Iris card: next-session line gains the Nov 3 slot
rep('The next session is Fri Oct 30, 2&ndash;3 (the Tuesday slot falls in UGM week).',
    'The next session is Fri Oct 30, 2&ndash;3 (the Tuesday slot falls in UGM week), then Tue Nov 3, 1&ndash;2.', 1)

# Needs-a-reply note: stale Friday pocket
rep('the 11&ndash;2 gap is today&rsquo;s pocket',
    'the 11:30 and 5:00 pockets are today&rsquo;s only gaps', 1)

# table row tid
rep('<td class="tid">Weekend</td>', '<td class="tid">Today</td>', 1)

# ---------- week chart: roll to Mon Oct 26 - Sun Nov 1 ----------
rep('Sun Oct 25 &ndash; Sat Oct 31', 'Mon Oct 26 &ndash; Sun Nov 1', 1)
c0 = s.find('<div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>')
c1 = s.find('</div>\n        <div class="xaxis"')
assert 0 < c0 < c1
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(69.64% + 6px)">9.75</div>\n'
 '            <div class="seg m" style="height:69.64%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(92.86% + 6px)">13</div>\n'
 '            <div class="seg m" style="height:92.86%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(92.86% + 6px)">13</div>\n'
 '            <div class="seg m" style="height:92.86%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>\n'
 '            <div class="seg m" style="height:39.29%"></div><div class="seg f" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>\n'
 '            <div class="seg m" style="height:14.29%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n        '
) + s[c1:]
rep('<div><b>Sun</b>25</div><div><b>Mon</b>26</div>\n          <div><b>Tue</b>27</div><div><b>Wed</b>28</div><div><b>Thu</b>29</div><div><b>Fri</b>30</div><div><b>Sat</b>31</div>',
    '<div><b>Mon</b>26</div><div><b>Tue</b>27</div>\n          <div><b>Wed</b>28</div><div><b>Thu</b>29</div><div><b>Fri</b>30</div><div><b>Sat</b>31</div><div><b>Sun</b>1</div>', 1)

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-10-26T07:25:00-05:00') == 2
assert s.count('window open') == 2
assert s.count('UGM opens tomorrow') == 0
assert s.count('recovery Sunday') == 0
assert s.count('eleven days past') == 0 and s.count('day forty-eight') == 0
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s

open(p, 'w').write(s)
print('monday turn ok', len(s))
