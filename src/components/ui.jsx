import { Link, NavLink } from 'react-router-dom'
import { useEffect, useRef, useState } from 'react'
import { crumbs, folderUrl, niceHeading, headingTone, toggleSaved, useSaved } from '../data.js'
import { useLang } from '../i18n.jsx'
import { useAuth } from '../auth.jsx'

const P = { width: 24, height: 24, fill: 'none', stroke: 'currentColor', strokeWidth: 2, strokeLinecap: 'round', strokeLinejoin: 'round', 'aria-hidden': true, focusable: false }
export const Icon = {
  home: <svg viewBox="0 0 24 24" {...P}><path d="M3 11l9-7 9 7" /><path d="M5 10v10h14V10" /></svg>,
  explore: <svg viewBox="0 0 24 24" {...P}><path d="M3 7h6l2 2h10v10H3z" /></svg>,
  path: <svg viewBox="0 0 24 24" {...P}><circle cx="5" cy="19" r="2" /><circle cx="12" cy="12" r="2" /><circle cx="19" cy="5" r="2" /><path d="M6.5 17.5l4-4M13.5 10.5l4-4" /></svg>,
  search: <svg viewBox="0 0 24 24" {...P}><circle cx="11" cy="11" r="7" /><path d="M20 20l-4-4" /></svg>,
  saved: <svg viewBox="0 0 24 24" {...P}><path d="M6 3h12v18l-6-4-6 4z" /></svg>,
  globe: <svg viewBox="0 0 24 24" {...P}><circle cx="12" cy="12" r="9" /><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18" /></svg>,
  quiz: <svg viewBox="0 0 24 24" {...P}><circle cx="12" cy="12" r="9" /><path d="M9.5 9.5a2.5 2.5 0 015 0c0 1.7-2.5 2-2.5 4M12 17h.01" /></svg>,
  install: <svg viewBox="0 0 24 24" {...P}><path d="M12 3v12M7 10l5 5 5-5M4 21h16" /></svg>,
  info: <svg viewBox="0 0 24 24" {...P}><circle cx="12" cy="12" r="9" /><path d="M12 11v5M12 8h.01" /></svg>,
  school: <svg viewBox="0 0 24 24" {...P}><path d="M3 10l9-5 9 5-9 5z" /><path d="M7 12v5c3 2 7 2 10 0v-5" /></svg>,
  building: <svg viewBox="0 0 24 24" {...P}><path d="M4 21V8l8-4 8 4v13" /><path d="M9 21v-6h6v6M8 10h.01M12 10h.01M16 10h.01" /></svg>,
  code: <svg viewBox="0 0 24 24" {...P}><path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13 6l-2 12" /></svg>,
  camera: <svg viewBox="0 0 24 24" {...P}><rect x="3" y="7" width="13" height="11" rx="2" /><path d="M16 11l5-3v9l-5-3" /></svg>,
  chat: <svg viewBox="0 0 24 24" {...P}><path d="M4 5h16v11H9l-5 4z" /><path d="M8 10h8M8 13h5" /></svg>,
  menu: <svg viewBox="0 0 24 24" {...P}><path d="M4 7h16M4 12h16M4 17h16" /></svg>,
  mail: <svg viewBox="0 0 24 24" {...P}><rect x="3" y="5" width="18" height="14" rx="2" /><path d="M3 7l9 6 9-6" /></svg>,
  phone: <svg viewBox="0 0 24 24" {...P}><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z" /></svg>,
  whatsapp: <svg viewBox="0 0 24 24" {...P}><path d="M4 20l1.3-4A8 8 0 1112 20a8 8 0 01-4-1z" /><path d="M9 9.5c.5 2 2.5 4 4.5 4.5l1-1.2 1.6.8" /></svg>,
  chev: <svg viewBox="0 0 24 24" {...P} width="20" height="20"><path d="M9 6l6 6-6 6" /></svg>,
  down: <svg viewBox="0 0 24 24" {...P} width="20" height="20"><path d="M6 9l6 6 6-6" /></svg>,
}

export const NAV_ALL = [
  ['/', 'home', 'home'], ['/explore', 'explore', 'explore'], ['/schools', 'schools', 'school'], ['/colleges', 'colleges', 'building'],
  ['/software', 'software', 'code'], ['/creative', 'creative', 'camera'], ['/guidance', 'guidance', 'chat'], ['/countries', 'abroad', 'globe'],
  ['/path', 'path', 'path'], ['/quiz', 'quiz', 'quiz'], ['/search', 'search', 'search'], ['/saved', 'saved', 'saved'],
  ['/install', 'install', 'install'], ['/about', 'about', 'info'],
]
const BOTTOM = [['/', 'home', 'home'], ['/explore', 'explore', 'explore'], ['/colleges', 'colleges', 'building'], ['/guidance', 'counselShort', 'chat'], ['/more', 'more', 'menu']]

function useOnline() {
  const [on, setOn] = useState(typeof navigator === 'undefined' ? true : navigator.onLine)
  useEffect(() => {
    const a = () => setOn(true), b = () => setOn(false)
    window.addEventListener('online', a); window.addEventListener('offline', b)
    return () => { window.removeEventListener('online', a); window.removeEventListener('offline', b) }
  }, [])
  return on
}

export function LangSwitch() {
  const { lang, setLang } = useLang()
  return (
    <div className="langswitch" role="group" aria-label="Language / భాష">
      <button className={lang === 'te' ? 'on' : ''} aria-pressed={lang === 'te'} onClick={() => setLang('te')} lang="te">తెలుగు</button>
      <button className={lang === 'en' ? 'on' : ''} aria-pressed={lang === 'en'} onClick={() => setLang('en')} lang="en">English</button>
    </div>
  )
}

function UserChip() {
  const auth = useAuth()
  const { t } = useLang()
  const [open, setOpen] = useState(false)
  if (!auth?.session) return null
  const s = auth.session
  const label = s.guest ? t('guest') : s.name || s.username
  return (
    <div className="userchip">
      <button className="iconbtn wide" onClick={() => setOpen(!open)} aria-expanded={open} aria-label={label}>
        <span className="avatar" aria-hidden="true">{(label[0] || 'G').toUpperCase()}</span><span className="uname">{label}</span>
      </button>
      {open && (
        <div className="usermenu" role="menu">
          <p className="muted" style={{ margin: '0 0 8px', fontSize: '.85rem' }}>{s.guest ? t('guest') : '@' + s.username}</p>
          <button role="menuitem" className="btn alt" onClick={() => { setOpen(false); auth.logout() }}>{t('signOut')}</button>
        </div>
      )}
    </div>
  )
}

export function Shell({ children }) {
  const online = useOnline()
  const { t } = useLang()
  return (
    <div className="shell">
      <header className="topbar">
        <div className="topbar-in">
          <Link to="/" className="brand" aria-label={t('appName')}>
            <img src={`${import.meta.env.BASE_URL}icons/icon-192.png`} alt="" width="36" height="36" />
            <span><b>{t('appName1')}<span className="brand2"> {t('appName2')}</span></b><small>{t('tagline')}</small></span>
          </Link>
          <span className="spacer" />
          <LangSwitch />
          <Link to="/search" className="iconbtn hide-sm" aria-label={t('search')}>{Icon.search}</Link>
          <UserChip />
        </div>
        <div className="ikat" aria-hidden="true" />
        {!online && <div className="offline" role="status">{t('offline')}</div>}
      </header>
      <div className="layout">
        <aside className="rail" aria-label="Main">
          <nav>
            {NAV_ALL.map(([to, key, ic]) => (
              <NavLink key={to} to={to} end={to === '/'}>{Icon[ic]}{t(key)}</NavLink>
            ))}
          </nav>
          <p className="railnote">{t('railNote')}</p>
          <p className="railbrand">{t('poweredBy')}</p>
        </aside>
        <main id="main">{children}</main>
      </div>
      <nav className="bottomnav" aria-label="Main">
        {BOTTOM.map(([to, key, ic]) => (
          <NavLink key={to} to={to} end={to === '/'}>{Icon[ic]}<span>{t(key)}</span></NavLink>
        ))}
      </nav>
    </div>
  )
}

export function RouteLine({ tree, folderId, tail }) {
  const { lang } = useLang()
  const list = crumbs(tree, folderId)
  const ref = useRef(null)
  useEffect(() => { if (ref.current) ref.current.scrollLeft = ref.current.scrollWidth }, [folderId, tail])
  return (
    <nav className="route" aria-label="Your path" ref={ref}>
      <Link to="/explore"><span className="dot" />{lang === 'te' ? 'మొదలు' : 'Start'}</Link>
      {list.map((f, i) => {
        const last = i === list.length - 1 && !tail
        return (
          <span key={f.id} style={{ display: 'contents' }}>
            <span className="seg" aria-hidden="true" />
            {last ? <span className="stop here" aria-current="page"><span className="dot" />{f.name}</span>
              : <Link to={folderUrl(f.id)}><span className="dot" />{f.name}</Link>}
          </span>
        )
      })}
      {tail && <><span className="seg" aria-hidden="true" /><span className="stop here" aria-current="page"><span className="dot" />{tail}</span></>}
    </nav>
  )
}

export function Table({ h, r }) {
  return (
    <table className="tbl">
      <thead><tr>{h.map((x, i) => <th key={i} scope="col">{x}</th>)}</tr></thead>
      <tbody>{r.map((row, i) => <tr key={i}>{row.map((c, j) => <td key={j} data-label={h[j]}>{c}</td>)}</tr>)}</tbody>
    </table>
  )
}

function Blocks({ blocks }) {
  const out = []
  let ul = []
  const flush = (k) => { if (ul.length) { out.push(<ul key={'u' + k}>{ul.map((x, i) => <li key={i}>{x}</li>)}</ul>); ul = [] } }
  blocks.forEach((b, i) => {
    if (b.t === 'li') { ul.push(b.x); return }
    flush(i)
    if (b.t === 'p') out.push(<p key={i}>{b.x}</p>)
    else if (b.t === 'h2') out.push(<h3 key={i}>{b.x}</h3>)
    else if (b.t === 'table') out.push(<Table key={i} h={b.h} r={b.r} />)
  })
  flush('end')
  return out
}

export function SalaryNote({ style }) {
  const { t } = useLang()
  return <p className="salnote" role="note" style={style}><span aria-hidden="true">₹</span>{t('salaryNote')}</p>
}

const PAY_RE = /salar|LPA|per month|\/month|pay scale|pay level|per annum|\/yr|CTC|wage|stipend/i
const PAY_SKIP = /contains|folder structure|how to use|other documents|signs of a fake|scheme|stages|study circles/i
const hasPay = (sec) => !PAY_SKIP.test(sec.h) && PAY_RE.test(JSON.stringify(sec.b))

export function DocBody({ doc }) {
  const { lang, t } = useLang()
  return (
    <div className="doc">
      {lang === 'te' && <p className="callout" lang="te" style={{ marginBottom: 18 }}>{t('englishOnly')}</p>}
      {doc.s.map((sec, i) => (
        <section key={i} className={headingTone(sec.h)}>
          <h2>{niceHeading(sec.h)}</h2>
          <Blocks blocks={sec.b} />
          {hasPay(sec) && <SalaryNote />}
        </section>
      ))}
      <p className="note">Fees, seats, age limits, exam patterns and vacancies change every year. Always confirm with the latest official notification before applying.</p>
    </div>
  )
}

export function SaveButton({ item }) {
  const saved = useSaved()
  const { t } = useLang()
  const on = saved.some((x) => x.url === item.url)
  return (
    <button className={'savebtn' + (on ? ' on' : '')} onClick={() => toggleSaved(item)} aria-pressed={on}>
      <svg viewBox="0 0 24 24" width="18" height="18" fill={on ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth="2"><path d="M6 3h12v18l-6-4-6 4z" /></svg>
      {on ? t('savedBtn') : t('save')}
    </button>
  )
}

export function Loading() {
  return <div aria-busy="true" aria-label="Loading"><div className="skeleton" style={{ width: '60%', height: 34 }} /><div className="skeleton" /><div className="skeleton" style={{ width: '80%' }} /><div className="skeleton" style={{ width: '70%' }} /></div>
}

export function Problem({ error }) {
  return (
    <div className="callout">
      <p><b>This page could not load.</b> {String(error?.message || error)}</p>
      <p>Check your internet connection and reload. Pages you opened before work offline.</p>
    </div>
  )
}

export function useTitle(t) {
  useEffect(() => { document.title = t ? `${t} – Career of Telangana Students` : 'Career of Telangana Students' }, [t])
}

// ----- PWA install prompt -----
let deferred = null
const listeners = new Set()
if (typeof window !== 'undefined') {
  window.addEventListener('beforeinstallprompt', (e) => { e.preventDefault(); deferred = e; listeners.forEach((f) => f()) })
  window.addEventListener('appinstalled', () => { deferred = null; listeners.forEach((f) => f()) })
}
export function useInstall() {
  const [, force] = useState(0)
  useEffect(() => { const f = () => force((x) => x + 1); listeners.add(f); return () => listeners.delete(f) }, [])
  const standalone = typeof window !== 'undefined' && (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true)
  const ios = typeof navigator !== 'undefined' && /iphone|ipad|ipod/i.test(navigator.userAgent)
  return {
    canPrompt: !!deferred, standalone, ios,
    prompt: async () => { if (!deferred) return; deferred.prompt(); await deferred.userChoice; deferred = null; force((x) => x + 1) },
  }
}
