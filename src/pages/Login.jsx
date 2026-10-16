import { useState } from 'react'
import { useLang } from '../i18n.jsx'
import { useAuth } from '../auth.jsx'
import { LangSwitch } from '../components/ui.jsx'
import { CONFIG } from '../config.js'

export default function Login() {
  const { t, lang } = useLang()
  const auth = useAuth()
  const [mode, setMode] = useState('login')
  const [f, setF] = useState({ name: '', username: '', password: '', confirm: '' })
  const [show, setShow] = useState(false)
  const [err, setErr] = useState('')
  const [busy, setBusy] = useState(false)
  const set = (k) => (e) => setF({ ...f, [k]: e.target.value })

  const submit = async (e) => {
    e.preventDefault()
    setErr('')
    if (!/^[A-Za-z0-9_]{3,20}$/.test(f.username)) return setErr(t('errUser'))
    if (f.password.length < 6) return setErr(t('errPwShort'))
    if (mode === 'register') {
      if (!f.name.trim()) return setErr(t('errName'))
      if (f.password !== f.confirm) return setErr(t('errPwMatch'))
    }
    setBusy(true)
    const code = mode === 'register' ? await auth.register({ name: f.name.trim(), username: f.username, password: f.password }) : await auth.login(f)
    setBusy(false)
    if (code) setErr(t(code))
  }

  return (
    <div className="login">
      <section className="login-brand" aria-hidden={false}>
        <div className="login-brand-in">
          <div className="brand"><img src={`${import.meta.env.BASE_URL}icons/icon-192.png`} alt="" width="44" height="44" /><span><b>{t('appName')}</b><small>{t('tagline')}</small></span></div>
          <h1>{lang === 'te' ? 'బడి నుండి కెరీర్ వరకు, ఒకే దారి.' : 'From school to career, one clear route.'}</h1>
          <p>{t('loginLead')}</p>
          <svg className="login-route" viewBox="0 0 320 120" aria-hidden="true">
            <path d="M16 100 C 90 100, 100 60, 160 58 S 250 20, 300 18" fill="none" stroke="#F2B705" strokeWidth="8" strokeLinecap="round" />
            <circle cx="16" cy="100" r="10" fill="#F5F6FA" stroke="#F2B705" strokeWidth="5" />
            <circle cx="160" cy="58" r="10" fill="#F5F6FA" stroke="#F2B705" strokeWidth="5" />
            <circle cx="300" cy="18" r="14" fill="#F2B705" />
          </svg>
          <ul className="login-points">
            <li>{lang === 'te' ? 'గురుకుల, నవోదయ నుండి ఇంజనీరింగ్, మెడిసిన్ వరకు' : 'Gurukul and Navodaya to engineering and medicine'}</li>
            <li>{lang === 'te' ? 'జిల్లా వారీ కాలేజీలు, ఉద్యోగాలు, విదేశీ అవకాశాలు' : 'District-wise colleges, jobs and abroad options'}</li>
            <li>{lang === 'te' ? 'తెలుగు & ఇంగ్లీష్ – ఆఫ్‌లైన్‌లోనూ పనిచేస్తుంది' : 'Telugu & English – works offline too'}</li>
          </ul>
          <p className="login-company">{t('poweredBy')}</p>
        </div>
      </section>

      <section className="login-form-wrap">
        <div className="login-top"><LangSwitch /></div>
        <form className="login-card" onSubmit={submit} noValidate>
          <h2>{mode === 'login' ? t('signIn') : t('createAccount')}</h2>
          {mode === 'register' && (
            <div className="field"><label htmlFor="l-name">{t('fullName')}</label><input id="l-name" value={f.name} onChange={set('name')} autoComplete="name" /></div>
          )}
          <div className="field"><label htmlFor="l-user">{t('username')}</label><input id="l-user" value={f.username} onChange={set('username')} autoComplete="username" autoCapitalize="none" spellCheck="false" /></div>
          <div className="field">
            <label htmlFor="l-pw">{t('password')}</label>
            <div className="pwrow">
              <input id="l-pw" type={show ? 'text' : 'password'} value={f.password} onChange={set('password')} autoComplete={mode === 'login' ? 'current-password' : 'new-password'} />
              <button type="button" className="pwtoggle" onClick={() => setShow(!show)} aria-pressed={show}>{show ? t('hidePw') : t('showPw')}</button>
            </div>
          </div>
          {mode === 'register' && (
            <div className="field"><label htmlFor="l-pw2">{t('confirmPassword')}</label><input id="l-pw2" type={show ? 'text' : 'password'} value={f.confirm} onChange={set('confirm')} autoComplete="new-password" /></div>
          )}
          {err && <p className="formerr" role="alert">{err}</p>}
          <button className="btn block" type="submit" disabled={busy}>{mode === 'login' ? t('signIn') : t('createAccount')}</button>
          <p className="login-switch">
            {mode === 'login' ? t('newHere') : t('haveAccount')}{' '}
            <button type="button" className="linkbtn" onClick={() => { setMode(mode === 'login' ? 'register' : 'login'); setErr('') }}>{mode === 'login' ? t('createAccount') : t('signIn')}</button>
          </p>
          <div className="divider"><span>{lang === 'te' ? 'లేదా' : 'or'}</span></div>
          <button type="button" className="btn alt block" onClick={() => auth.guest()}>{t('continueGuest')}</button>
          <p className="muted login-note">{t('deviceNote')}</p>
        </form>
        <p className="login-foot">© 2026 {CONFIG.company}, {CONFIG.site}</p>
      </section>
    </div>
  )
}
