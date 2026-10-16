import { Link, useParams, useSearchParams } from 'react-router-dom'
import { useEffect, useMemo, useState } from 'react'
import MiniSearch from 'minisearch'
import { QRCodeSVG } from 'qrcode.react'
import { useTree, useAbroad, load, folderUrl, docUrl, crumbs, useSaved, toggleSaved } from '../data.js'
import { Icon, Loading, Problem, useTitle, useInstall } from '../components/ui.jsx'
import { useLang } from '../i18n.jsx'
import { CountryApps } from '../components/AbroadView.jsx'
import { NotFound } from './Browse.jsx'
import { SCHOOL_EXAMS } from '../content/schools.js'
import { SOFTWARE, CREATIVE } from '../content/courses.js'
import { DIRECTORY } from '../content/directory.js'

function extraDocs() {
  const out = []
  SCHOOL_EXAMS.forEach((e) => out.push({ id: 'school:' + e.id, t: e.name.en, f: '', c: 'school', x: [e.name.te, e.short.en, e.about.en, e.entry.en, 'class school entrance exam gurukul navodaya'].join(' ') }))
  SOFTWARE.forEach((c) => out.push({ id: 'sw:' + c.id, t: c.name, f: '', c: 'software', x: [c.summary.en, c.roadmap.join(' '), c.jobs.join(' '), 'software course IT training fee'].join(' ') }))
  CREATIVE.forEach((c) => out.push({ id: 'cr:' + c.id, t: c.name.en, f: '', c: 'creative', x: [c.name.te, c.learn.join(' '), c.jobs.join(' '), 'creative course after 10th'].join(' ') }))
  DIRECTORY.forEach((d) => d.rows.forEach((r, i) => out.push({ id: `col:${d.id}:${i}`, t: r[0], f: '', c: 'college', x: [r[1], r[2], r[3], r[4] || '', d.name.en, 'college school'].join(' ') })))
  return out
}

const GROUPS = [['Gulf', ['UAE', 'SAU', 'QAT', 'OMN', 'KWT', 'BHR']], ['English-speaking', ['GBR', 'USA', 'CAN', 'AUS', 'NZL', 'IRL']],
  ['Europe', ['DEU', 'NLD', 'FRA', 'SWE', 'POL']], ['Asia & others', ['SGP', 'JPN', 'MYS', 'HKG', 'KOR', 'MDV', 'MUS', 'ISR', 'AFR']], ['At sea', ['SEA', 'CRU']]]

export function Countries() {
  const { lang } = useLang()
  useTitle('Jobs abroad')
  const { data: ab, error } = useAbroad()
  if (error) return <Problem error={error} />
  if (!ab) return <Loading />
  const count = (code) => Object.values(ab.profiles).filter((p) => p.rows.some((r) => r[0] === code)).length
  return (
    <div className="page">
      <div className="pagehead"><h1>{lang === 'te' ? 'విదేశీ ఉద్యోగాలు' : 'Jobs abroad'}</h1><p>{lang === 'te' ? 'ప్రతి దేశానికి వీసా దారులు, జాబ్ యాప్స్, భాష, శాశ్వత నివాసం, భారత రాయబార కార్యాలయం. ప్రతి కోర్సులో దాని టాప్ 10 దేశాలు కూడా ఉన్నాయి.' : <>Visa routes, job apps, language, permanent stay and the Indian embassy for each country. Every course page also has its own top 10 countries.</>}</p></div>
      {GROUPS.map(([g, codes]) => (
        <section key={g}>
          <h2 className="section-title">{g}</h2>
          <ul className="list">
            {codes.map((c) => <li key={c}><Link to={`/countries/${c}`}><span className="mark sky" /><span><span className="t">{ab.countries[c].name}</span><span className="s">In the top 10 for {count(c)} professions</span></span><span className="go">{Icon.chev}</span></Link></li>)}
          </ul>
        </section>
      ))}
      <div className="callout leaf" style={{ marginTop: 22 }}>Before you trust any job offer, read <Link to="/d/08_Work_and_Study_Abroad_Guide/04_Safe_Emigration_and_Avoiding_Fraud">Safe emigration and fraud signs</Link>.</div>
    </div>
  )
}

export function CountryPage() {
  const { code } = useParams()
  const { data: ab } = useAbroad()
  const { data: tree } = useTree()
  const c = ab?.countries[code]
  useTitle(c?.name)
  const courses = useMemo(() => {
    if (!ab || !tree) return []
    const keys = Object.entries(ab.profiles).filter(([, p]) => p.rows.some((r) => r[0] === code)).map(([k]) => k)
    return keys.map((k) => ({ k, p: ab.profiles[k], rank: ab.profiles[k].rows.findIndex((r) => r[0] === code) + 1, folders: Object.values(tree.folders).filter((f) => f.abroad === k) }))
      .sort((a, b) => a.rank - b.rank)
  }, [ab, tree, code])
  if (!ab || !tree) return <Loading />
  if (!c) return <NotFound />
  return (
    <div className="page">
      <nav className="route"><Link to="/countries"><span className="dot" />Jobs abroad</Link><span className="seg" /><span className="stop here"><span className="dot" />{c.name}</span></nav>
      <div className="headrow"><h1>{c.name}</h1></div>
      <div className="doc" style={{ marginTop: 14 }}>
        <section><CountryApps c={c} sector={c.health ? 'health' : null} /></section>
        {c.edu && <section><h2>Teaching jobs</h2><ul>{c.edu.map((x) => <li key={x}>{x}</li>)}</ul></section>}
        {c.eng && <section><h2>Engineering registration</h2><ul>{c.eng.map((x) => <li key={x}>{x}</li>)}</ul></section>}
        <section>
          <h2>Courses that lead here</h2>
          <p className="muted">Rank shows this country's place in that profession's top 10.</p>
          <ul className="list">
            {courses.map(({ k, p, rank, folders }) => (
              <li key={k}><Link to={folders[0] ? folderUrl(folders[0].id) + '?tab=abroad' : '/explore'}><span className="mark" /><span><span className="t">{p.name}</span><span className="s">Rank {rank} of 10 – {p.rows[rank - 1][3]}</span></span><span className="go">{Icon.chev}</span></Link></li>
            ))}
          </ul>
        </section>
      </div>
    </div>
  )
}

let msPromise = null
function getIndex() {
  if (!msPromise) {
    msPromise = load('search').then((docs) => {
      const ms = new MiniSearch({ fields: ['t', 'x'], storeFields: ['t', 'f', 'c'], searchOptions: { boost: { t: 3 }, prefix: true, fuzzy: 0.2, combineWith: 'AND' } })
      ms.addAll(docs)
      ms.addAll(extraDocs())
      return ms
    })
  }
  return msPromise
}
const SUGGEST = ['MBBS', 'nursing UK', 'Group 2', 'ITI electrician Dubai', 'CA', 'polytechnic', 'scholarship', 'B.Tech CSE Germany', 'police constable', 'pharmacy']

export function Search() {
  const { lang } = useLang()
  useTitle('Search')
  const [sp, setSp] = useSearchParams()
  const q = sp.get('q') || ''
  const [text, setText] = useState(q)
  const [ms, setMs] = useState(null)
  const [err, setErr] = useState(null)
  const { data: tree } = useTree()
  useEffect(() => { getIndex().then(setMs, setErr) }, [])
  useEffect(() => { setText(q) }, [q])
  const results = useMemo(() => {
    if (!ms || !q.trim()) return []
    let r = ms.search(q)
    if (r.length < 5) r = ms.search(q, { combineWith: 'OR' })
    return r.slice(0, 40)
  }, [ms, q])
  const link = (r) => {
    if (r.id.startsWith('abroad:')) return folderUrl(r.id.slice(7)) + '?tab=abroad'
    if (r.id.startsWith('country:')) return `/countries/${r.id.slice(8)}`
    if (r.id.startsWith('school:')) return `/schools/${r.id.slice(7)}`
    if (r.id.startsWith('sw:')) return `/software/${r.id.slice(3)}`
    if (r.id.startsWith('cr:')) return `/creative/${r.id.slice(3)}`
    if (r.id.startsWith('col:')) return `/colleges?tab=${r.id.split(':')[1]}`
    return docUrl(r.id)
  }
  const KIND = { country: 'Country guide', school: 'Class 1–10', software: 'Software course', creative: 'Creative career', college: 'College / school directory' }
  const where = (r) => !tree || !r.f ? (KIND[r.c] || '') : crumbs(tree, r.f).map((x) => x.name).slice(-3).join(' / ')
  return (
    <div className="page">
      <div className="pagehead"><h1>{lang === 'te' ? 'వెతకండి' : 'Search'}</h1></div>
      <form className="searchbox" role="search" onSubmit={(e) => { e.preventDefault(); setSp(text ? { q: text } : {}) }}>
        {Icon.search}
        <input autoFocus value={text} onChange={(e) => setText(e.target.value)} placeholder="Course, job, exam or country" aria-label="Search" />
        <button className="btn" type="submit">Search</button>
      </form>
      {err && <Problem error={err} />}
      {!q && <div style={{ marginTop: 18, display: 'flex', flexWrap: 'wrap', gap: 8 }}>{SUGGEST.map((s) => <button key={s} className="chip" onClick={() => setSp({ q: s })}>{s}</button>)}</div>}
      {q && !ms && !err && <Loading />}
      {q && ms && (
        <>
          <p className="muted" style={{ marginTop: 14 }}>{results.length ? `${results.length}${results.length === 40 ? '+' : ''} results for “${q}”` : `No results for “${q}”. Try a shorter word, like “nurse” or “Group”.`}</p>
          <ul className="list">
            {results.map((r) => <li key={r.id}><Link to={link(r)}><span className={'mark ' + (r.c === 'abroad' || r.c === 'country' ? 'sky' : '')} /><span><span className="t">{r.t}</span><span className="s">{where(r)}</span></span><span className="go">{Icon.chev}</span></Link></li>)}
          </ul>
        </>
      )}
    </div>
  )
}

export function Saved() {
  const { lang } = useLang()
  useTitle('Saved')
  const list = useSaved()
  return (
    <div className="page">
      <div className="pagehead"><h1>{lang === 'te' ? 'సేవ్ చేసినవి' : 'Saved'}</h1><p>{lang === 'te' ? 'ఈ పరికరంలో మీరు సేవ్ చేసిన కోర్సులు, గైడ్‌లు.' : 'Courses and guides you saved on this device.'}</p></div>
      {list.length === 0 ? (
        <div className="panel"><p style={{ margin: 0 }}>Nothing saved yet. Tap <b>Save</b> on any course to keep it here for later – it works offline too.</p><p style={{ margin: '12px 0 0' }}><Link className="btn" to="/explore">Explore courses</Link></p></div>
      ) : (
        <ul className="list">
          {list.map((x) => (
            <li key={x.url} style={{ display: 'flex', alignItems: 'center' }}>
              <Link to={x.url} style={{ flex: 1 }}><span className="mark" /><span className="t">{x.title}</span></Link>
              <button className="chip" onClick={() => toggleSaved(x)} aria-label={`Remove ${x.title}`}>Remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export function Install() {
  useTitle('Install & share')
  const inst = useInstall()
  const url = typeof window !== 'undefined' ? window.location.origin : ''
  const share = async () => { try { await navigator.share({ title: 'Career of Telangana Students', text: 'Free career guide for Telangana students', url }) } catch { /* cancelled */ } }
  return (
    <div className="page">
      <div className="pagehead"><h1>Install & share</h1><p>Install the guide like an app. It opens from your home screen and works without internet.</p></div>
      {inst.standalone ? <div className="callout leaf">The app is already installed on this device.</div> : inst.canPrompt ? <p><button className="btn yellow" onClick={inst.prompt}>Install app on this device</button></p> : null}
      <div className="doc" style={{ marginTop: 16 }}>
        <section><h2>Android phone (Chrome)</h2><ol style={{ paddingLeft: '1.3em' }}><li>Open this site in Chrome.</li><li>Tap <b>Install app</b> (or menu ⋮ then <b>Install app / Add to Home screen</b>).</li><li>Open “Career TG” from your home screen.</li></ol></section>
        <section><h2>iPhone or iPad (Safari)</h2><ol style={{ paddingLeft: '1.3em' }}><li>Open this site in Safari.</li><li>Tap the <b>Share</b> button (square with arrow).</li><li>Choose <b>Add to Home Screen</b>, then <b>Add</b>.</li></ol></section>
        <section><h2>Laptop or desktop (Chrome / Edge)</h2><ol style={{ paddingLeft: '1.3em' }}><li>Open this site.</li><li>Click the install icon at the right end of the address bar, or menu then <b>Install Career of Telangana</b>.</li><li>It opens in its own window, like any app.</li></ol></section>
        <section>
          <h2>Share with friends</h2>
          <p>Show this QR code in class – students scan it with their phone camera.</p>
          <div className="qr"><QRCodeSVG value={url} size={180} fgColor="#1E2A5A" /></div>
          <p style={{ marginTop: 10 }}><code>{url}</code></p>
          {typeof navigator !== 'undefined' && navigator.share && <button className="btn alt" onClick={share}>Share link</button>}
        </section>
      </div>
    </div>
  )
}

export function About() {
  useTitle('About & help')
  return (
    <div className="page">
      <div className="pagehead"><h1>About this guide</h1><p>A free, offline-friendly career guide for students in Telangana – from 10th class to jobs in India and abroad.</p></div>
      <div className="doc">
        <section><h2>What's inside</h2><ul>
          <li>Intermediate groups, every degree after each group, Polytechnic branches and ITI trades – with subjects and pass marks.</li>
          <li>Private jobs with starting salaries and government jobs with recruiters for every course.</li>
          <li>Doctor specialisations (MD, MS, DM, MCh), nursing, pharmacy, allied health and paramedical courses.</li>
          <li>Top 10 countries, job apps and step-by-step plans to work abroad for every course.</li>
          <li>Scholarships (ePASS, overseas up to ₹20 lakh), education loans, free coaching and helplines.</li></ul></section>
        <section><h2>Important</h2><div className="callout">Information was prepared in October 2026 from official and trusted public sources. Fees, seats, age limits, salaries, visa rules and exam patterns change often. Always confirm on the official website (TGBIE, TGCHE, KNRUHS, TGPSC, MHSRB, embassies) before you apply or pay any money.</div></section>
        <section><h2>Helplines</h2><ul>
          <li>Tele-MANAS (free mental-health support, 24x7): 14416</li><li>Emergency: 112</li><li>Women helpline: 181</li><li>Child helpline: 1098</li>
          <li>Cyber crime and online fraud: 1930</li><li>Indians abroad (MEA, 24x7): 1800 11 3090</li></ul></section>
        <section><h2>Official websites</h2><ul>
          <li>Intermediate: tgbie.cgg.gov.in</li><li>Degree admissions: dost.cgg.gov.in</li><li>Entrance exams: tgche.ac.in</li>
          <li>Polytechnic: sbtet.telangana.gov.in</li><li>Health courses: knruhs.telangana.gov.in</li>
          <li>State jobs: tspsc.gov.in, tgprb.in, mhsrb.telangana.gov.in</li><li>Central jobs: ssc.gov.in, upsc.gov.in</li>
          <li>Scholarships: telanganaepass.cgg.gov.in, scholarships.gov.in</li><li>Emigration: emigrate.gov.in</li></ul></section>
      </div>
    </div>
  )
}
