import { Link, useParams, useSearchParams } from 'react-router-dom'
import { useEffect, useMemo, useRef, useState } from 'react'
import { useLang } from '../i18n.jsx'
import { useAuth } from '../auth.jsx'
import { CONFIG } from '../config.js'
import { Icon, SaveButton, useTitle, NAV_ALL, LangSwitch, SalaryNote } from '../components/ui.jsx'
import { SCHOOL_EXAMS, SCHOOL_TIMELINE } from '../content/schools.js'
import { DIRECTORY, COL_LABEL } from '../content/directory.js'
import { SOFTWARE, FREE_LEARNING, CREATIVE, CREATIVE_INSTITUTES, MODELLING_RED_FLAGS } from '../content/courses.js'
import { NotFound } from './Browse.jsx'

function Crumb({ to, label, here }) {
  return (
    <nav className="route" aria-label="Your path">
      <Link to={to}><span className="dot" />{label}</Link>
      <span className="seg" aria-hidden="true" />
      <span className="stop here" aria-current="page"><span className="dot" />{here}</span>
    </nav>
  )
}

// ---------------- Class 1–10 ----------------
export function Schools() {
  const { t, L, lang } = useLang()
  useTitle(t('schools'))
  return (
    <div className="page">
      <div className="pagehead">
        <h1>{lang === 'te' ? '1 నుండి 10వ తరగతి – ప్రవేశ పరీక్షలు & పాఠశాలలు' : 'Class 1 to 10 – entrance exams & schools'}</h1>
        <p>{lang === 'te' ? 'గురుకుల, నవోదయ, మోడల్, సైనిక్ పాఠశాలలు, స్కాలర్‌షిప్‌లు – ఏ తరగతిలో ఏ పరీక్ష రాయాలో ఒకే చోట.' : 'Gurukul, Navodaya, Model and Sainik schools and scholarships – which exam to write in which class, all in one place.'}</p>
      </div>
      <h2 className="section-title" style={{ marginTop: 6 }}>{lang === 'te' ? 'ఏ తరగతిలో ఏమిటి' : 'What happens in which class'}</h2>
      <div className="journey">
        {SCHOOL_TIMELINE.map((s, i) => (
          <div className={'stop' + (i === 0 ? ' big' : '')} key={i}>
            <h3>{L(s.cls)}</h3>
            <p style={{ margin: '4px 0 8px' }}>{L(s.what)}</p>
            <div className="branches">{s.ids.map((id) => { const e = SCHOOL_EXAMS.find((x) => x.id === id); return <Link key={id} className="chip" to={`/schools/${id}`}>{L(e.name).split(' – ')[0]}</Link> })}</div>
          </div>
        ))}
      </div>
      <h2 className="section-title">{lang === 'te' ? 'అన్ని పరీక్షలు & పాఠశాలలు' : 'All exams & schools'}</h2>
      <div className="grid2">
        {SCHOOL_EXAMS.map((e) => (
          <Link key={e.id} to={`/schools/${e.id}`} className={'tile ' + e.tone}><span className="t">{L(e.name)}</span><span className="s">{L(e.short)}</span></Link>
        ))}
      </div>
      <div className="callout" style={{ marginTop: 22 }}>
        {lang === 'te' ? 'మీ జిల్లాలోని నవోదయ, గురుకుల పాఠశాలల జాబితా కోసం ' : 'For Navodaya and Gurukul schools in your district, open '}
        <Link to="/colleges?tab=navodaya">{t('colleges')}</Link>.
      </div>
    </div>
  )
}

export function SchoolExam() {
  const { id } = useParams()
  const { t, L } = useLang()
  const e = SCHOOL_EXAMS.find((x) => x.id === id)
  useTitle(e ? L(e.name) : '')
  if (!e) return <NotFound />
  return (
    <div className="page">
      <Crumb to="/schools" label={t('schools')} here={L(e.name).split(' – ')[0]} />
      <div className="headrow"><h1>{L(e.name)}</h1><SaveButton item={{ url: `/schools/${id}`, title: L(e.name) }} /></div>
      <p className="muted" style={{ marginTop: 8 }}>{L(e.about)}</p>
      <div className="factrow">
        <div><span className="k">{t('entry')}</span><span className="v">{L(e.entry)}</span></div>
        <div><span className="k">{t('when')}</span><span className="v">{L(e.when)}</span></div>
        <div><span className="k">{t('website')}</span><span className="v">{e.site}</span></div>
      </div>
      <div className="doc" style={{ marginTop: 20 }}>
        <section><h2>{t('eligibility')}</h2><ul>{e.eligibility.map((x, i) => <li key={i}>{L(x)}</li>)}</ul></section>
        <section><h2>{t('pattern')}</h2><ul>{e.pattern.map((x, i) => <li key={i}>{L(x)}</li>)}</ul></section>
        {e.tips.length > 0 && <section><h2>{t('tips')}</h2><ul>{e.tips.map((x, i) => <li key={i}>{L(x)}</li>)}</ul></section>}
        <p className="callout">{t('confirm')}</p>
      </div>
    </div>
  )
}

// ---------------- Colleges directory ----------------
export function Colleges() {
  const { t, L, lang } = useLang()
  useTitle(t('colleges'))
  const [sp, setSp] = useSearchParams()
  const tab = DIRECTORY.find((d) => d.id === sp.get('tab')) || DIRECTORY[0]
  const [q, setQ] = useState('')
  const [dist, setDist] = useState('')
  const districts = useMemo(() => [...new Set(tab.rows.map((r) => r[2]))].filter((d) => !/^All/.test(d)).sort(), [tab])
  const rows = tab.rows.filter((r) => (!dist || r[2] === dist || /^All/.test(r[2])) && (!q || (r[0] + ' ' + r[1]).toLowerCase().includes(q.toLowerCase())))
  const pick = (id) => { setSp({ tab: id }); setQ(''); setDist('') }
  const tabsRef = useRef(null)
  useEffect(() => { const el = tabsRef.current?.querySelector('.on'); if (el && tabsRef.current.scrollWidth > tabsRef.current.clientWidth) tabsRef.current.scrollLeft = el.offsetLeft - tabsRef.current.offsetLeft - 16 }, [tab.id])
  return (
    <div className="page wide">
      <div className="pagehead">
        <h1>{lang === 'te' ? 'పాఠశాలలు & కాలేజీలు – జిల్లా వారీగా' : 'Schools & colleges – district-wise'}</h1>
        <p>{lang === 'te' ? 'నవోదయ, గురుకుల, జూనియర్, ఇంజనీరింగ్, మెడికల్, నర్సింగ్, వ్యవసాయ, పాలిటెక్నిక్ – ఒక్కో విభాగం విడిగా.' : 'Navodaya, Gurukul, junior, engineering, medical, nursing, agriculture and polytechnic – each as its own report.'}</p>
      </div>
      <div className="tabs dirtabs" role="tablist" ref={tabsRef}>
        {DIRECTORY.map((d) => <button key={d.id} role="tab" aria-selected={d.id === tab.id} className={d.id === tab.id ? 'on' : ''} onClick={() => pick(d.id)}>{L(d.name)}{d.rows.length ? ` (${d.rows.length})` : ''}</button>)}
      </div>
      <p>{L(tab.intro)}</p>
      {tab.how && (
        <div className="panel" style={{ margin: '12px 0' }}>
          <h3 style={{ marginBottom: 8 }}>{t('howToFind')}</h3>
          <ol style={{ margin: 0, paddingLeft: '1.3em' }}>{tab.how.map((x, i) => <li key={i}>{L(x)}</li>)}</ol>
        </div>
      )}
      {tab.rows.length > 0 && (
        <>
          <div className="filters">
            <label className="sr" htmlFor="dir-q">{t('filter')}</label>
            <div className="searchbox" style={{ flex: 2 }}>{Icon.search}<input id="dir-q" value={q} onChange={(e) => setQ(e.target.value)} placeholder={t('filter')} /></div>
            <label className="sr" htmlFor="dir-d">{t('district')}</label>
            <select id="dir-d" className="select" value={dist} onChange={(e) => setDist(e.target.value)}>
              <option value="">{t('allDistricts')}</option>
              {districts.map((d) => <option key={d} value={d}>{d}</option>)}
            </select>
          </div>
          <p className="muted" style={{ fontSize: '.9rem' }}>{rows.length} {t('results')}</p>
          {rows.length === 0 ? <p className="callout">{t('noMatch')}</p> : (
            <div className="tblwrap">
              <table className="tbl">
                <thead><tr>{tab.cols.map((c) => <th key={c} scope="col">{L(COL_LABEL[c])}</th>)}</tr></thead>
                <tbody>{rows.map((r, i) => <tr key={i}>{tab.cols.map((c, j) => <td key={c} data-label={L(COL_LABEL[c])}>{r[j]}</td>)}</tr>)}</tbody>
              </table>
            </div>
          )}
        </>
      )}
      <p className="footer-note"><b>{t('source')}:</b> {tab.source}<br /><b>{t('website')}:</b> {tab.official}<br />{t('confirm')}</p>
    </div>
  )
}

// ---------------- Software courses ----------------
export function Software() {
  const { lang } = useLang()
  const { L } = useLang()
  useTitle('Software courses')
  return (
    <div className="page">
      <div className="pagehead">
        <h1>{lang === 'te' ? 'సాఫ్ట్‌వేర్ కోర్సులు – ఎంత సమయం, ఎంత ఖర్చు, ఏ ఉద్యోగం' : 'Software courses – time, cost and jobs'}</h1>
        <p>{lang === 'te' ? 'ప్రతి కోర్సుకు నేర్చుకోవాల్సిన దశలు, సుమారు ఫీజు, ఉద్యోగాలు. ఫీజులు, జీతాలు సుమారు అంచనాలు మాత్రమే (హైదరాబాద్, అక్టోబర్ 2026).' : 'Step-by-step roadmap, approximate fee and the jobs each course leads to. Fees and salaries are approximate (Hyderabad, October 2026).'}</p>
      </div>
      <ul className="list">
        {SOFTWARE.map((c) => (
          <li key={c.id}><Link to={`/software/${c.id}`}><span className="mark sky" /><span><span className="t">{c.name}</span><span className="s">{c.months} {lang === 'te' ? 'నెలలు' : 'months'} – {c.fee} – {L(c.summary)}</span></span><span className="go">{Icon.chev}</span></Link></li>
        ))}
      </ul>
      <SalaryNote />
      <div className="panel" style={{ marginTop: 22 }}>
        <h3 style={{ marginBottom: 6 }}>{lang === 'te' ? 'ఉచితంగా నేర్చుకోండి' : 'Learn for free first'}</h3>
        <ul style={{ margin: 0, paddingLeft: '1.2em' }}>{FREE_LEARNING.map((x) => <li key={x}>{x}</li>)}</ul>
      </div>
      <div className="callout" style={{ marginTop: 14 }}>{lang === 'te' ? '"100% ప్లేస్‌మెంట్ గ్యారంటీ" అనే మాటలు నమ్మకండి. డెమో క్లాస్ చూసి, పాత విద్యార్థులతో మాట్లాడి, ఫీజు రసీదు తీసుకున్నాకే చేరండి.' : 'Be careful with "100% placement guarantee" claims. Attend a demo class, talk to past students and get a fee receipt before joining.'}</div>
    </div>
  )
}

export function SoftwareCourse() {
  const { id } = useParams()
  const { L, lang, t } = useLang()
  const c = SOFTWARE.find((x) => x.id === id)
  useTitle(c?.name)
  if (!c) return <NotFound />
  return (
    <div className="page">
      <Crumb to="/software" label={t('software')} here={c.name} />
      <div className="headrow"><h1>{c.name}</h1><SaveButton item={{ url: `/software/${id}`, title: c.name }} /></div>
      <p className="muted" style={{ marginTop: 8 }}>{L(c.summary)}</p>
      <div className="factrow">
        <div><span className="k">{lang === 'te' ? 'వ్యవధి' : 'Duration'}</span><span className="v">{c.months} {lang === 'te' ? 'నెలలు' : 'months'}</span></div>
        <div><span className="k">{lang === 'te' ? 'సుమారు ఫీజు' : 'Approx fee'}</span><span className="v">{c.fee}</span></div>
        <div><span className="k">{lang === 'te' ? 'మొదటి జీతం (సుమారు)' : 'Starting salary (approx)'}</span><span className="v">{c.salary}</span><span className="k" style={{ marginTop: 4 }}>{t('salaryShort')}</span></div>
      </div>
      <div className="doc" style={{ marginTop: 20 }}>
        <section><h2>{lang === 'te' ? 'ఎవరు చేయవచ్చు' : 'Who can join'}</h2><p>{L(c.who)}</p></section>
        <section>
          <h2>{lang === 'te' ? 'నేర్చుకునే క్రమం (టైమ్‌లైన్)' : 'Learning roadmap (in order)'}</h2>
          <ol className="steps">{c.roadmap.map((x, i) => <li key={i}><span className="n">{i + 1}</span><span>{x}</span></li>)}</ol>
        </section>
        <section><h2>{lang === 'te' ? 'తర్వాత ఉద్యోగాలు' : 'Jobs after this course'}</h2><ul>{c.jobs.map((x) => <li key={x}>{x}</li>)}</ul><SalaryNote /></section>
        <p className="callout">{lang === 'te' ? 'ఉద్యోగానికి సర్టిఫికేట్ కంటే మీ ప్రాజెక్టులు (GitHub / పోర్ట్‌ఫోలియో) ముఖ్యం.' : 'For jobs, your projects (GitHub / portfolio) matter more than the certificate.'}</p>
      </div>
      <p><Link className="btn" to="/guidance">{t('guidance')}</Link></p>
    </div>
  )
}

// ---------------- Creative careers ----------------
export function Creative() {
  const { L, lang } = useLang()
  useTitle('Creative careers')
  return (
    <div className="page">
      <div className="pagehead">
        <h1>{lang === 'te' ? 'క్రియేటివ్ కెరీర్లు – వీడియో, ఫోటో, యానిమేషన్, మోడలింగ్' : 'Creative careers – video, photo, animation, modelling'}</h1>
        <p>{lang === 'te' ? '10వ తరగతి లేదా ఇంటర్ తర్వాత చేయగల కోర్సులు, సుమారు ఫీజు, ఉద్యోగాలు, సంస్థలు.' : 'Courses you can join after 10th or Inter, approximate fees, jobs and institutes.'}</p>
      </div>
      <ul className="list">
        {CREATIVE.map((c) => (
          <li key={c.id}><Link to={`/creative/${c.id}`}><span className="mark pink" /><span><span className="t">{L(c.name)}</span><span className="s">{L(c.after)} – {c.duration} – {c.fee}</span></span><span className="go">{Icon.chev}</span></Link></li>
        ))}
      </ul>
      <SalaryNote />
      <h2 className="section-title">{lang === 'te' ? 'సంస్థలు (ఉదాహరణలు)' : 'Institutes (examples)'}</h2>
      <div className="tblwrap"><table className="tbl">
        <thead><tr><th>{lang === 'te' ? 'సంస్థ' : 'Institute'}</th><th>{lang === 'te' ? 'ప్రదేశం' : 'Place'}</th><th>{lang === 'te' ? 'రకం' : 'Type'}</th><th>{lang === 'te' ? 'కోర్సులు' : 'Courses'}</th></tr></thead>
        <tbody>{CREATIVE_INSTITUTES.map((r) => <tr key={r[0]}>{r.map((c, j) => <td key={j} data-label={['Institute', 'Place', 'Type', 'Courses'][j]}>{c}</td>)}</tr>)}</tbody>
      </table></div>
      <p className="footer-note">{lang === 'te' ? 'ప్రైవేట్ సంస్థలు ఉదాహరణలు మాత్రమే – ఫీజు, గుర్తింపు, ప్లేస్‌మెంట్ వాదనలను మీరే సరిచూసుకోండి. మేము ఏ సంస్థనూ సిఫార్సు చేయడం లేదు.' : 'Private institutes are examples only – check fees, recognition and placement claims yourself. We do not endorse any institute.'}</p>
    </div>
  )
}

export function CreativeCourse() {
  const { id } = useParams()
  const { L, lang, t } = useLang()
  const c = CREATIVE.find((x) => x.id === id)
  useTitle(c ? L(c.name) : '')
  if (!c) return <NotFound />
  return (
    <div className="page">
      <Crumb to="/creative" label={t('creative')} here={L(c.name)} />
      <div className="headrow"><h1>{L(c.name)}</h1><SaveButton item={{ url: `/creative/${id}`, title: L(c.name) }} /></div>
      <div className="factrow">
        <div><span className="k">{lang === 'te' ? 'ఎప్పుడు చేరవచ్చు' : 'When to join'}</span><span className="v">{L(c.after)}</span></div>
        <div><span className="k">{lang === 'te' ? 'వ్యవధి' : 'Duration'}</span><span className="v">{c.duration}</span></div>
        <div><span className="k">{lang === 'te' ? 'సుమారు ఫీజు' : 'Approx fee'}</span><span className="v">{c.fee}</span></div>
      </div>
      <div className="doc" style={{ marginTop: 20 }}>
        <section><h2>{lang === 'te' ? 'ఏమి నేర్చుకుంటారు' : 'What you learn'}</h2><ol className="steps">{c.learn.map((x, i) => <li key={i}><span className="n">{i + 1}</span><span>{x}</span></li>)}</ol></section>
        <section><h2>{lang === 'te' ? 'ఉద్యోగాలు & సంపాదన' : 'Jobs & earnings'}</h2><ul>{c.jobs.map((x) => <li key={x}>{x}</li>)}</ul><p className="muted">{c.salary}</p><SalaryNote /></section>
        {c.warning && (
          <section>
            <h2>{lang === 'te' ? 'మోసాల హెచ్చరిక – ఇవి కనిపిస్తే దూరంగా ఉండండి' : 'Scam warning – walk away if you see these'}</h2>
            <div className="callout"><ul style={{ margin: 0 }}>{MODELLING_RED_FLAGS.map((x, i) => <li key={i}>{L(x)}</li>)}</ul></div>
            <p className="muted" style={{ marginTop: 8 }}>{lang === 'te' ? 'మోసం జరిగితే: సైబర్ క్రైమ్ 1930, మహిళా హెల్ప్‌లైన్ 181, అత్యవసరం 112.' : 'If cheated: Cyber crime 1930, Women helpline 181, Emergency 112.'}</p>
          </section>
        )}
      </div>
      <p><Link className="btn" to="/guidance">{t('guidance')}</Link> <Link className="btn alt" to="/creative">{lang === 'te' ? 'అన్ని క్రియేటివ్ కోర్సులు' : 'All creative courses'}</Link></p>
    </div>
  )
}

// ---------------- Personal guidance & booking ----------------
const STAGES = [
  ['Class 1–5', '1–5 తరగతులు'], ['Class 6–9', '6–9 తరగతులు'], ['Class 10', '10వ తరగతి'], ['Intermediate', 'ఇంటర్మీడియట్'],
  ['Polytechnic / ITI', 'పాలిటెక్నిక్ / ITI'], ['Degree / B.Tech', 'డిగ్రీ / B.Tech'], ['Graduate – job search', 'గ్రాడ్యుయేట్ – ఉద్యోగ అన్వేషణ'], ['Parent', 'తల్లిదండ్రులు'],
]
const INTERESTS = [
  ['Engineering & IT', 'ఇంజనీరింగ్ & IT'], ['Medicine & health', 'మెడిసిన్ & ఆరోగ్యం'], ['Commerce & CA', 'కామర్స్ & CA'], ['Govt jobs', 'ప్రభుత్వ ఉద్యోగాలు'],
  ['Study / work abroad', 'విదేశాల్లో చదువు / ఉద్యోగం'], ['Creative careers', 'క్రియేటివ్ కెరీర్లు'], ['Software courses', 'సాఫ్ట్‌వేర్ కోర్సులు'], ['Gurukul / Navodaya', 'గురుకుల / నవోదయ'],
]
const QUIZ_NAMES = { eng: ['MPC – Engineering & technology', 'MPC – ఇంజనీరింగ్ & టెక్నాలజీ'], med: ['BiPC – Medicine & health', 'BiPC – మెడిసిన్ & ఆరోగ్యం'], com: ['MEC / CEC – Commerce', 'MEC / CEC – కామర్స్'], arts: ['HEC – Civil services, law, teaching', 'HEC – సివిల్ సర్వీసెస్, లా, టీచింగ్'], skill: ['Polytechnic / ITI – skills', 'పాలిటెక్నిక్ / ITI – స్కిల్స్'] }
const QUIZ_URL = { eng: '/f/01_After_10th_Intermediate/MPC/After_12th_MPC', med: '/f/01_After_10th_Intermediate/BiPC/After_12th_BiPC', com: '/f/01_After_10th_Intermediate/MEC/After_12th_MEC', arts: '/f/01_After_10th_Intermediate/HEC/After_12th_HEC', skill: '/f/02_After_10th_Polytechnic_Diploma' }

export function Guidance() {
  const { lang, t } = useLang()
  const auth = useAuth()
  useTitle(t('guidance'))
  const tx = (en, te) => (lang === 'te' ? te : en)
  let quiz = null
  try { quiz = JSON.parse(localStorage.getItem('cot-quiz') || 'null') } catch { /* ignore */ }
  const [f, setF] = useState({ name: auth?.session && !auth.session.guest ? auth.session.name : '', stage: '', interests: [], date: '', slot: '', mode: 'Phone call', phone: '', msg: '' })
  const [err, setErr] = useState('')
  const [sent, setSent] = useState('')
  const set = (k, v) => setF({ ...f, [k]: v })
  const toggle = (v) => set('interests', f.interests.includes(v) ? f.interests.filter((x) => x !== v) : [...f.interests, v])
  const body = () => [
    'Career counselling request – Career of Telangana Students app', '',
    `Student name: ${f.name}`, `Stage: ${f.stage}`, `Interested in: ${f.interests.join(', ') || '-'}`,
    quiz ? `Stream quiz top match: ${QUIZ_NAMES[quiz[0]]?.[0]}` : '', `Preferred date: ${f.date || '-'}  Time: ${f.slot || '-'}`, `Session mode: ${f.mode}`,
    `Contact number: ${f.phone || '-'}`, '', `Message: ${f.msg || '-'}`,
  ].filter((x) => x !== '').join('\n')
  const valid = () => {
    if (!f.name.trim()) { setErr(tx('Enter the student name.', 'విద్యార్థి పేరు నమోదు చేయండి.')); return false }
    if (!f.stage) { setErr(tx('Choose the current class or stage.', 'ప్రస్తుత తరగతి / దశ ఎంచుకోండి.')); return false }
    setErr(''); return true
  }
  const subject = 'Career counselling request – ' + f.name
  const mail = `mailto:${CONFIG.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body())}`
  const gmail = `https://mail.google.com/mail/?view=cm&fs=1&to=${encodeURIComponent(CONFIG.email)}&su=${encodeURIComponent(subject)}&body=${encodeURIComponent(body())}`
  const opened = () => setSent(tx(`A new tab opened with your request to ${CONFIG.email}. Press Send there. If nothing opened, use "Copy request" and email it yourself.`, `${CONFIG.email} కు మీ అభ్యర్థనతో కొత్త ట్యాబ్ తెరుచుకుంది. అక్కడ Send నొక్కండి. ఏదీ తెరుచుకోకపోతే "అభ్యర్థన కాపీ" వాడి మీరే ఈమెయిల్ చేయండి.`))
  const sendGmail = () => { if (!valid()) return; const w = window.open(gmail, '_blank', 'noopener'); opened(); return w }
  const wa = CONFIG.whatsapp ? `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(body())}` : ''
  const copy = async () => { try { await navigator.clipboard.writeText(body()); setSent(tx('Request copied – paste it into email or WhatsApp.', 'అభ్యర్థన కాపీ అయింది – ఈమెయిల్ లేదా వాట్సాప్‌లో పేస్ట్ చేయండి.')) } catch { setSent(tx('Copy is blocked here – select the text above manually.', 'ఇక్కడ కాపీ కుదరదు – పై వివరాలను మీరే సెలెక్ట్ చేయండి.')) } }

  return (
    <div className="page">
      <div className="pagehead">
        <h1>{tx('Personal career guidance', 'వ్యక్తిగత కెరీర్ మార్గదర్శనం')}</h1>
        <p>{tx(`Talk one-to-one with the ${CONFIG.counsellorTitle}. Share your details – we reply by phone, WhatsApp or email.`, `${CONFIG.company} కెరీర్ కౌన్సెలింగ్ టీమ్‌తో నేరుగా మాట్లాడండి. మీ వివరాలు పంపండి – ఫోన్, వాట్సాప్ లేదా ఈమెయిల్ ద్వారా స్పందిస్తాం.`)}</p>
      </div>

      <section className="panel fit">
        <h2 style={{ fontSize: '1.2rem', marginBottom: 8 }}>{tx('Where you fit best', 'మీకు బాగా సరిపోయేది')}</h2>
        {quiz ? (
          <ol className="fitlist">
            {quiz.slice(0, 3).map((k, i) => <li key={k}><span className="n">{i + 1}</span><Link to={QUIZ_URL[k]}>{QUIZ_NAMES[k][lang === 'te' ? 1 : 0]}</Link></li>)}
          </ol>
        ) : <p style={{ margin: 0 }}>{tx('Take the 10-question stream quiz to see your best-fit paths here.', 'మీకు సరిపోయే దారులు ఇక్కడ చూడటానికి 10 ప్రశ్నల క్విజ్ రాయండి.')}</p>}
        <p style={{ margin: '10px 0 0' }}><Link className="chip" to="/quiz">{quiz ? tx('Retake the quiz', 'క్విజ్ మళ్లీ రాయండి') : tx('Take the quiz', 'క్విజ్ రాయండి')}</Link> <Link className="chip" to="/path">{t('path')}</Link></p>
      </section>

      <h2 className="section-title">{tx('Book a counselling session', 'కౌన్సెలింగ్ సెషన్ బుక్ చేయండి')}</h2>
      <form className="form" onSubmit={(e) => { e.preventDefault(); sendGmail() }} noValidate>
        <div className="field"><label htmlFor="g-name">{tx('Student name', 'విద్యార్థి పేరు')} *</label><input id="g-name" value={f.name} onChange={(e) => set('name', e.target.value)} autoComplete="name" /></div>
        <div className="field"><label htmlFor="g-stage">{tx('Current class / stage', 'ప్రస్తుత తరగతి / దశ')} *</label>
          <select id="g-stage" className="select" value={f.stage} onChange={(e) => set('stage', e.target.value)}>
            <option value="">{tx('Choose…', 'ఎంచుకోండి…')}</option>
            {STAGES.map(([en, te]) => <option key={en} value={en}>{lang === 'te' ? te : en}</option>)}
          </select></div>
        <fieldset className="field"><legend>{tx('Interested in', 'ఆసక్తి')}</legend>
          <div className="branches">{INTERESTS.map(([en, te]) => <button type="button" key={en} className={'chip' + (f.interests.includes(en) ? ' on' : '')} aria-pressed={f.interests.includes(en)} onClick={() => toggle(en)}>{lang === 'te' ? te : en}</button>)}</div>
        </fieldset>
        <div className="fieldrow">
          <div className="field"><label htmlFor="g-date">{tx('Preferred date', 'ఇష్టమైన తేదీ')}</label><input id="g-date" type="date" value={f.date} onChange={(e) => set('date', e.target.value)} /></div>
          <div className="field"><label htmlFor="g-slot">{tx('Preferred time', 'ఇష్టమైన సమయం')}</label>
            <select id="g-slot" className="select" value={f.slot} onChange={(e) => set('slot', e.target.value)}>
              <option value="">{tx('Any time', 'ఎప్పుడైనా')}</option><option>10:00 – 12:00</option><option>14:00 – 16:00</option><option>18:00 – 20:00</option>
            </select></div>
        </div>
        <div className="field"><label htmlFor="g-mode">{tx('Session mode', 'సెషన్ విధానం')}</label>
          <select id="g-mode" className="select" value={f.mode} onChange={(e) => set('mode', e.target.value)}>
            <option value="Phone call">{tx('Phone call', 'ఫోన్ కాల్')}</option><option value="WhatsApp call">{tx('WhatsApp call', 'వాట్సాప్ కాల్')}</option><option value="Video call">{tx('Video call', 'వీడియో కాల్')}</option>
          </select></div>
        <div className="field"><label htmlFor="g-phone">{tx('Parent / student phone (for call back)', 'తల్లిదండ్రులు / విద్యార్థి ఫోన్ (తిరిగి కాల్ కోసం)')}</label><input id="g-phone" type="tel" inputMode="tel" value={f.phone} onChange={(e) => set('phone', e.target.value)} autoComplete="tel" /></div>
        <div className="field"><label htmlFor="g-msg">{tx('Your question', 'మీ ప్రశ్న')}</label><textarea id="g-msg" rows="3" value={f.msg} onChange={(e) => set('msg', e.target.value)} /></div>
        {err && <p className="formerr" role="alert">{err}</p>}
        <div className="actions">
          <button type="submit" className="btn">{Icon.mail}{tx('Send via Gmail', 'Gmail ద్వారా పంపండి')}</button>
          <a className="btn alt" href={mail} target="_blank" rel="noopener" onClick={(e) => { if (!valid()) e.preventDefault(); else opened() }}>{Icon.mail}{tx('Other email app', 'ఇతర ఈమెయిల్ యాప్')}</a>
          {wa && <a className="btn alt" href={wa} target="_blank" rel="noopener" onClick={(e) => { if (!valid()) e.preventDefault() }}>{Icon.whatsapp}WhatsApp</a>}
          {CONFIG.phone && <a className="btn alt" href={`tel:${CONFIG.phone}`}>{Icon.phone}{tx('Call us', 'కాల్ చేయండి')}</a>}
          <button type="button" className="btn alt" onClick={() => { if (valid()) copy() }}>{tx('Copy request', 'అభ్యర్థన కాపీ')}</button>
        </div>
        {sent && <p className="formok" role="status">{sent}</p>}
      </form>
      <div className="panel" style={{ marginTop: 18 }}>
        <p style={{ margin: 0 }}><b>{tx('Email', 'ఈమెయిల్')}:</b> <span className="selectable">{CONFIG.email}</span></p>
        {CONFIG.phone && <p style={{ margin: '6px 0 0' }}><b>{tx('Phone', 'ఫోన్')}:</b> <span className="selectable">{CONFIG.phone}</span></p>}
        <p className="muted" style={{ margin: '8px 0 0', fontSize: '.88rem' }}>{tx('Gmail (or your email app) opens with the request filled in – press Send there and it reaches our team. Nothing is stored in this app.', 'Gmail (లేదా మీ ఈమెయిల్ యాప్) వివరాలతో తెరుచుకుంటుంది – అక్కడ Send నొక్కితే మా టీమ్‌కు చేరుతుంది. ఈ యాప్‌లో ఏదీ సేవ్ కాదు.')}</p>
      </div>
    </div>
  )
}

// ---------------- More (mobile menu) ----------------
export function More() {
  const { t } = useLang()
  const auth = useAuth()
  useTitle(t('more'))
  return (
    <div className="page">
      <div className="pagehead"><h1>{t('more')}</h1></div>
      <div style={{ marginBottom: 16 }}><LangSwitch /></div>
      <ul className="list">
        {NAV_ALL.filter(([to]) => to !== '/').map(([to, key, ic]) => (
          <li key={to}><Link to={to}><span className="navic">{Icon[ic]}</span><span className="t">{t(key)}</span><span className="go">{Icon.chev}</span></Link></li>
        ))}
        {auth?.session && <li><button onClick={() => auth.logout()}><span className="navic">{Icon.info}</span><span className="t">{t('signOut')}</span></button></li>}
      </ul>
      <p className="footer-note">{t('poweredBy')} – {CONFIG.site}</p>
    </div>
  )
}
