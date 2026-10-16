// Device-only demo accounts (no server yet). Passwords are stored as salted SHA-256 hashes in this browser.
// Replace with a real backend (Node + PostgreSQL, bcrypt, JWT) before storing any personal data.
import { createContext, useContext, useState } from 'react'

const USERS = 'cot-users-v1'
const SESSION = 'cot-session-v1'
const get = (k, d) => { try { return JSON.parse(localStorage.getItem(k)) ?? d } catch { return d } }
const put = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)) } catch { /* storage blocked */ } }

async function hash(password, salt) {
  const data = new TextEncoder().encode(`${salt}:${password}`)
  if (globalThis.crypto?.subtle) {
    const buf = await crypto.subtle.digest('SHA-256', data)
    return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('')
  }
  let h = 0; for (const b of data) h = (h * 31 + b) >>> 0
  return 'x' + h.toString(16)
}

// Built-in company demo login that works on every device (username: ggtech). Only the salted hash is kept here.
const BUILTIN = { ggtech: { name: 'GGTECH Demo', salt: 'ggtech-demo-2026', hash: '855f551723730203932919aa6311f2b5927f00a2a8533c664c708c64571e4256' } }

const AuthCtx = createContext(null)

export function AuthProvider({ children }) {
  const [session, setSession] = useState(() => get(SESSION, null))
  const save = (s) => { setSession(s); put(SESSION, s) }
  const api = {
    session,
    async register({ name, username, password }) {
      const users = get(USERS, {})
      const u = username.toLowerCase()
      if (users[u] || BUILTIN[u]) return 'errUserTaken'
      const salt = Math.random().toString(36).slice(2)
      users[u] = { name, salt, hash: await hash(password, salt), created: Date.now() }
      put(USERS, users)
      save({ username: u, name, guest: false })
      return null
    },
    async login({ username, password }) {
      const users = get(USERS, {})
      const rec = BUILTIN[username.toLowerCase()] || users[username.toLowerCase()]
      if (!rec || (await hash(password, rec.salt)) !== rec.hash) return 'errBadLogin'
      save({ username: username.toLowerCase(), name: rec.name, guest: false })
      return null
    },
    guest() { save({ username: 'guest', name: '', guest: true }) },
    logout() { setSession(null); try { localStorage.removeItem(SESSION) } catch { /* ignore */ } },
  }
  return <AuthCtx.Provider value={api}>{children}</AuthCtx.Provider>
}

export const useAuth = () => useContext(AuthCtx)
