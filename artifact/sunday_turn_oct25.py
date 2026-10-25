#!/usr/bin/env python3
# Sunday Oct 25 2026 weekend date turn. Saturday closed failure-free (0F/1NA/4S).
# Overnight clean (Lakeland digest 7:01 only). Sunday is empty; UGM opens Monday.
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
rep('fifty-four days past', 'fifty-five days past', 2)
rep('58 days', '59 days', 1)
rep('day forty-eight', 'day forty-nine', 3)             # 799
rep('day forty-seven', 'day forty-eight', 3)            # Eric x2 + trio
rep('day forty-five of billed Logs', 'day forty-six of billed Logs', 1)
rep('forty-fourth day', 'forty-fifth day', 1)
rep('forty-six full days', 'forty-seven full days', 1)
rep('forty-two days past', 'forty-three days past', 2)
rep('Day forty on Eric', 'Day forty-one on Eric', 1)
rep('night forty', 'night forty-one', 2)
rep('day thirty-nine', 'day forty', 2)                  # JDs
rep('thirty-three days unsent', 'thirty-four days unsent', 1)
rep('thirty-two days past its &ldquo;before Sep 22&rdquo; window', 'thirty-three days past its &ldquo;before Sep 22&rdquo; window', 1)
rep('the window closed Sep 22 &mdash; thirty-two days now', 'the window closed Sep 22 &mdash; thirty-three days now', 1)
rep('Day twenty-nine on all three', 'Day thirty on all three', 1)
rep('twenty-two days', 'twenty-three days', 3)
rep('Twenty-two days', 'Twenty-three days', 1)
rep('ten days past', 'eleven days past', 5)
rep('Ten days past due', 'Eleven days past due', 1)
rep('day five', 'day six', 4)
rep('Iris, day thirteen', 'Iris, day fourteen', 1)
rep('hr-nda is 68 days', 'hr-nda is 69 days', 1)
rep('Ages as of Oct 24', 'Ages as of Oct 25', 1)
rep('Sixteen days carried', 'Seventeen days carried', 1)

def chip1(m):
    return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s2, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s3, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s2)
assert c1 + c2 == 5, f"chips: {c1}+{c2}"
s = s3

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-24T22:07:00-05:00', '2026-10-25T08:10:00-05:00', 2)
rep('<b>Brief compiled</b> Sat 8:07 AM &middot; data checked Sat 10:07 PM CT',
    '<b>Brief compiled</b> Sun 8:10 AM &middot; data checked Sun 8:10 AM CT', 1)
rep('Saturday, October 24 &middot; 2026', 'Sunday, October 25 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
new_sub = ('<p class="sub">Saturday was the quiet day the streak has been waiting for: <b>no failures at all</b> '
 '&mdash; one soft &ldquo;needs attention&rdquo; at 6:51 PM against four healthy handled calls &mdash; the first '
 'failure-free day since the evening bursts began. Today is the open recovery Sunday; nothing is booked. <b>UGM '
 'opens tomorrow</b>: Product Sync at 8:00 with Jr and Eelco, then Austin through Thursday &mdash; the brochures '
 'were printed Friday for hand-carry, the attendee-bag one-pager went to the Marriott, and if the <b>Printavo '
 'tees</b> (Cedar Park) aren&rsquo;t in hand yet, that&rsquo;s the errand left. Monday also carries the two sends: '
 '<b>the damage-control call to Cathy at ProGraphix</b> (eleven days past the submit-by) and <b>the Tim record on '
 'day six</b>, with the Emilio recap at <b>twenty-three days</b> behind them. No reactions saved.</p>')
rx(r'<p class="sub">.*?No reactions saved\.</p>', lambda m: new_sub, 1, re.DOTALL)

# ---------- 4. LEDGER: Sunday opener ----------
rep('nothing after 7:18</b> &mdash; verified at 10:07 PM, trash included.',
    'nothing after 7:18</b> &mdash; verified at 10:07 PM, trash included. The overnight into Sunday stayed quiet '
    '&mdash; <b>Sunday opened clean</b>: the Lakeland digest on schedule at 7:01 and no alerts by 8:10 &mdash; '
    'window open.', 1)

# ---------- 5. TODAY SCHEDULE ----------
rep('''        <div class="slot past"><div class="t">12:00 &ndash; 1:15</div><div class="w">Acquisition.com LIVE &mdash; Think Like a Great CEO<small>self-booked session &middot; the one booking of the day</small></div></div>''',
    '''        <div class="slot free"><div class="t">All day</div><div class="w">Nothing booked<small>recovery Sunday &middot; UGM opens tomorrow &mdash; Product Sync 8:00, then Austin</small></div></div>''', 1)
rep('todaynote">1.25h &mdash; Acquisition.com LIVE 12&ndash;1:15; the rest of Saturday is open',
    'todaynote">0h booked &mdash; recovery Sunday; UGM opens tomorrow', 1)

# ---------- 6. CHART (Sun 0 / Mon 0.75 / Tue 0 / Wed 0 / Thu 2 / Fri 2 / Sat 0) ----------
rep('Sat Oct 24 &ndash; Fri Oct 30', 'Sun Oct 25 &ndash; Sat Oct 31', 1)
old_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(8.93% + 6px)">1.25</div>
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
new_bars = '''          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(5.36% + 6px)">0.75</div>
            <div class="seg m" style="height:5.36%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg m" style="height:14.29%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>'''
rep(old_bars, new_bars, 1)
rep('''<div><b>Sat</b>24</div><div><b>Sun</b>25</div>
          <div><b>Mon</b>26</div><div><b>Tue</b>27</div><div><b>Wed</b>28</div><div><b>Thu</b>29</div><div><b>Fri</b>30</div>''',
    '''<div><b>Sun</b>25</div><div><b>Mon</b>26</div>
          <div><b>Tue</b>27</div><div><b>Wed</b>28</div><div><b>Thu</b>29</div><div><b>Fri</b>30</div><div><b>Sat</b>31</div>''', 1)

# ---------- 7. TOP 5 ----------
rep('and UGM opens Monday &mdash; this weekend is the pickup window.', 'and UGM opens tomorrow.', 1)

# ---------- 8. COMING-UP CARDS ----------
rep('<h4 style="font-size:14px">The weekend &mdash; one session today, then UGM takes the week</h4>',
    '<h4 style="font-size:14px">Tomorrow &mdash; UGM opens in Austin</h4>', 1)
rep('Acquisition.com LIVE runs 12&ndash;1:15, the only booking. The weekend&rsquo;s one errand: <b>the Printavo tees</b> (Invoice #1186, Cedar Park) before UGM opens Monday. Sunday is open &mdash; the usual recovery day. Monday: Product Sync at 8, then <b>UGM in Austin through Thursday</b>; the brochures went to FedEx Thursday night and the Marriott drop was blocked Friday morning. Carried into UGM week: the Tim record (day six), the Emilio recap (twenty-three days), and the group-channel exercise from Taylor&rsquo;s session.',
    'Product Sync at 8:00 with Jr and Eelco, then the conference floor &mdash; <b>UGM runs through Thursday</b>. The brochures were printed Friday for hand-carry and the one-pager went to the Marriott; <b>the Printavo tees</b> (Invoice #1186, Cedar Park) are the remaining physical item if not yet picked up. Carried into the week: <b>the Cathy call</b> (eleven days past), <b>the Tim record</b> (day six), the Emilio recap (twenty-three days), and Taylor&rsquo;s group-channel exercise.', 1)
# markers card
rep('Monday&rsquo;s record (thirteen failures) stands; Friday ran spotless for eleven hours, then closed at four evening failures &mdash; the sixteenth straight weekday-evening burst.',
    'Monday&rsquo;s record (thirteen failures) stands &mdash; and Saturday broke the pattern entirely: <b>the streak&rsquo;s first failure-free day</b>, one needs-attention against four healthy calls.', 1)
rep('This weekend: Acquisition.com 12&ndash;1:15 today, <b>the Printavo pickup</b>, and an open Sunday. UGM is Oct 26&ndash;30 in Austin &mdash; brochures printed for hand-carry, Product Sync Monday 8:00 &mdash; then Thursday holds Scott at 2 with two Reserved blocks, Friday the Gevity pizza party and <b>the Iris session at 2</b>. The next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.',
    'Today is the open recovery Sunday. <b>UGM opens tomorrow</b> (Oct 26&ndash;30, Austin) with the Product Sync at 8:00; Thursday holds Scott at 2 with two Reserved blocks, Friday the Gevity pizza party and <b>the Iris session at 2</b>. The next engineering block is <b>Mon Nov 2, 10&ndash;2</b>.', 1)

# ---------- 9. WEEK FLAGS ----------
rep('<span class="pill warn">Today</span> Saturday holds one session &mdash; and the weekend&rsquo;s one errand',
    '<span class="pill warn">Today</span> Sunday is open &mdash; the recovery day before UGM', 1)
rep('Acquisition.com LIVE 12&ndash;1:15 is the only booking. The <b>Printavo tees</b> (Cedar Park) need picking up before UGM opens Monday. Friday&rsquo;s scorecard: <b>the Iris scenarios and one-pagers shipped on deadline</b>; the <b>ProGraphix submit-by passed silent</b> (eleven days past &mdash; Monday is a call to Cathy); and the Tim draft sits on day six with the written record still owed.',
    'Nothing is booked &mdash; the usual recovery Sunday. <b>UGM opens tomorrow</b>: Product Sync at 8:00, then Austin through Thursday. If the <b>Printavo tees</b> (Cedar Park) aren&rsquo;t in hand, that&rsquo;s the one errand left. Tomorrow&rsquo;s carried calls: <b>Cathy at ProGraphix</b> (eleven days past) and <b>the Tim record</b> (day six).', 1)
rep('<span class="pill warn">This week</span> UGM takes next week &mdash; Monday through Thursday in Austin',
    '<span class="pill warn">This week</span> UGM takes this week &mdash; tomorrow through Thursday in Austin', 1)
rep('Sunday is open. <b>UGM runs Monday through Thursday</b> with only the Product Sync (Mon 8:00) and the declined Izzy slot on the calendar;',
    '<b>UGM runs tomorrow through Thursday</b> with only the Product Sync (Mon 8:00) and the declined Izzy slot on the calendar;', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('window open') == 2
assert s.count('2026-10-25T08:10:00-05:00') == 2
assert s.count('Sat Oct 24') == 0
assert s.count('ten days past') == 0 and s.count('twenty-two days') == 0
assert 'Good evening' not in s

open(p, 'w', encoding='utf-8').write(s)
print('sunday turn applied:', len(s), 'chars')
