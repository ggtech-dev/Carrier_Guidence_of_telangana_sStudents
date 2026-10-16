import { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import { useLang } from '../i18n.jsx'
import { BANNERS } from '../content/banners.js'

const ART = {
  school: <><path d="M20 58 L60 34 L100 58" /><path d="M28 54 V92 H92 V54" /><path d="M52 92 V72 H68 V92" /><path d="M60 34 V18 L76 23 L60 28" /></>,
  shield: <><path d="M60 16 L94 28 V56 C94 78 80 94 60 102 C40 94 26 78 26 56 V28 Z" /><path d="M44 58 L56 70 L78 46" /></>,
  gear: <><circle cx="60" cy="60" r="16" /><path d="M60 22 V34 M60 86 V98 M22 60 H34 M86 60 H98 M33 33 L42 42 M78 78 L87 87 M87 33 L78 42 M42 78 L33 87" /><circle cx="60" cy="60" r="30" /></>,
  book: <><path d="M60 34 C48 26 34 24 20 26 V90 C34 88 48 90 60 98 C72 90 86 88 100 90 V26 C86 24 72 26 60 34 Z" /><path d="M60 34 V98" /></>,
  pen: <><rect x="30" y="20" width="56" height="78" rx="6" /><path d="M42 40 H74 M42 54 H74 M42 68 H62" /><path d="M70 92 L96 58 L104 66 L78 100 L68 102 Z" /></>,
}

const today = () => new Date().toISOString().slice(0, 10)

export default function Banners() {
  const { L, lang } = useLang()
  const items = BANNERS.filter((b) => !b.until || b.until >= today())
  const track = useRef(null)
  const [idx, setIdx] = useState(0)
  const [paused, setPaused] = useState(false)
  const te = lang === 'te'

  const go = (i) => {
    const el = track.current
    if (!el) return
    const n = (i + items.length) % items.length
    el.scrollTo({ left: n * el.clientWidth, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' })
  }

  useEffect(() => {
    const el = track.current
    if (!el) return
    const onScroll = () => setIdx(Math.round(el.scrollLeft / Math.max(1, el.clientWidth)))
    el.addEventListener('scroll', onScroll, { passive: true })
    return () => el.removeEventListener('scroll', onScroll)
  }, [])

  useEffect(() => {
    if (paused || items.length < 2 || matchMedia('(prefers-reduced-motion: reduce)').matches) return
    const id = setInterval(() => { if (!document.hidden) go(idx + 1) }, 5500)
    return () => clearInterval(id)
  })

  if (!items.length) return null
  return (
    <section className="banners" aria-roledescription="carousel" aria-label={te ? 'రాబోయే పరీక్షలు' : 'Upcoming exams'}
      onMouseEnter={() => setPaused(true)} onMouseLeave={() => setPaused(false)}
      onFocus={() => setPaused(true)} onBlur={() => setPaused(false)} onTouchStart={() => setPaused(true)}>
      <div className="bn-track" ref={track}>
        {items.map((b, i) => (
          <article key={b.id} className={'bn tone-' + b.tone} role="group" aria-roledescription="slide" aria-label={`${i + 1} / ${items.length}`}>
            <div className="bn-body">
              <p className="bn-top">
                <span className="bn-tag">{L(b.tag)}</span>
                <span className={'bn-status ' + b.status}>{b.status === 'confirmed' ? (te ? 'అధికారిక తేదీ' : 'Official date') : (te ? 'అంచనా తేదీ' : 'Expected date')}</span>
              </p>
              <h2 className="bn-title">{L(b.title)}</h2>
              <p className="bn-date">{L(b.date)}</p>
              <p className="bn-note">{L(b.note)}</p>
              <Link className="bn-cta" to={b.link} tabIndex={i === idx ? 0 : -1}>{te ? 'వివరాలు చూడండి' : 'See details'}<span aria-hidden="true"> →</span></Link>
            </div>
            <div className="bn-art" aria-hidden="true">
              {b.image ? <img src={b.image} alt="" loading="lazy" /> : (
                <svg viewBox="0 0 120 120" width="120" height="120"><circle cx="60" cy="60" r="56" className="ring" /><g className="glyph">{ART[b.art] || ART.book}</g></svg>
              )}
            </div>
          </article>
        ))}
      </div>
      {items.length > 1 && (
        <div className="bn-ctrl">
          <button type="button" className="bn-arrow" onClick={() => go(idx - 1)} aria-label={te ? 'ముందటిది' : 'Previous'}>‹</button>
          <div className="bn-dots">
            {items.map((b, i) => <button type="button" key={b.id} className={i === idx ? 'on' : ''} aria-label={`${i + 1}: ${L(b.title)}`} aria-current={i === idx} onClick={() => go(i)} />)}
          </div>
          <button type="button" className="bn-arrow" onClick={() => go(idx + 1)} aria-label={te ? 'తర్వాతిది' : 'Next'}>›</button>
        </div>
      )}
      <p className="bn-disclaimer">{te ? 'తేదీలు 16 అక్టోబర్ 2026 నాటివి. దరఖాస్తుకు ముందు అధికారిక వెబ్‌సైట్‌లో సరిచూసుకోండి.' : 'Dates checked 16 October 2026. Always confirm on the official website before applying.'}</p>
    </section>
  )
}
