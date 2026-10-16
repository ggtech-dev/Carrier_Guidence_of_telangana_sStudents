// Data loading with in-memory cache. All files live in /public/data and are cached by the service worker.
import { useEffect, useState } from 'react'

const cache = new Map()

export function load(name) {
  if (!cache.has(name)) {
    const p = fetch(`${import.meta.env.BASE_URL}data/${name}.json`).then((r) => {
      if (!r.ok) throw new Error(`Could not load ${name} (${r.status})`)
      return r.json()
    })
    p.catch(() => cache.delete(name))
    cache.set(name, p)
  }
  return cache.get(name)
}

export function useData(name) {
  const [state, setState] = useState({ data: null, error: null })
  useEffect(() => {
    let alive = true
    if (!name) return
    setState({ data: null, error: null })
    load(name).then(
      (data) => alive && setState({ data, error: null }),
      (error) => alive && setState({ data: null, error })
    )
    return () => { alive = false }
  }, [name])
  return state
}

export function useTree() { return useData('tree') }
export function useAbroad() { return useData('abroad') }

export async function loadDoc(meta) {
  const chunk = await load(`docs-${meta.chunk}`)
  return chunk[meta.id]
}

// ---------- paths & names ----------
export const enc = (p) => p.split('/').map(encodeURIComponent).join('/')
export const folderUrl = (id) => `/f/${enc(id)}`
export const docUrl = (id) => `/d/${enc(id)}`

export function crumbs(tree, folderId) {
  const out = []
  let cur = folderId
  while (cur) {
    const f = tree.folders[cur]
    if (!f) break
    out.unshift(f)
    cur = f.parent
  }
  return out
}

// Friendly names for the top-level folders
export const ROOT_INFO = {
  '01_After_10th_Intermediate': { name: 'Intermediate (11th & 12th)', hint: 'MPC, BiPC, MEC, CEC, HEC and every degree after them', tone: 'indigo' },
  '02_After_10th_Polytechnic_Diploma': { name: 'Polytechnic diploma', hint: '3-year diplomas after 10th, ECET to B.Tech', tone: 'indigo' },
  '03_After_10th_ITI_Trades': { name: 'ITI trades', hint: '1–2 year skill courses and jobs', tone: 'indigo' },
  '04_After_10th_Other_Options': { name: 'Other options after 10th', hint: 'Open school, apprenticeship, skill courses', tone: 'indigo' },
  '05_After_10th_Govt_Jobs_Telangana': { name: 'Govt jobs after 10th', hint: 'GDS, MTS, GD Constable, Railways, Agniveer…', tone: 'leaf' },
  '06_After_Inter_Govt_Jobs': { name: 'Govt jobs after Inter', hint: 'Police, SSC CHSL, NDA, Agniveer…', tone: 'leaf' },
  '07_After_Degree_Govt_and_Private_Jobs': { name: 'Jobs after degree', hint: 'Group I–IV, UPSC, banks, SSC + private sectors', tone: 'leaf' },
  '08_Work_and_Study_Abroad_Guide': { name: 'Work & study abroad', hint: 'Country guides, language tests, safe emigration', tone: 'sky' },
  '09_Scholarships_and_Student_Support': { name: 'Scholarships & support', hint: 'ePASS, overseas scholarships, loans, helplines', tone: 'pink' },
}

export function niceHeading(h) {
  return h.replace(/^PRIVATE JOBS/, 'Private jobs').replace(/^GOVERNMENT JOBS/, 'Government jobs')
}

export function headingTone(h) {
  if (/^PRIVATE JOBS/.test(h)) return 'private'
  if (/^GOVERNMENT JOBS/.test(h)) return 'govt'
  return ''
}

// ---------- saved items (per device) ----------
const KEY = 'cot-saved-v1'
export function getSaved() {
  try { return JSON.parse(localStorage.getItem(KEY) || '[]') } catch { return [] }
}
export function setSaved(list) {
  try { localStorage.setItem(KEY, JSON.stringify(list)) } catch { /* storage unavailable */ }
  window.dispatchEvent(new Event('cot-saved'))
}
export function useSaved() {
  const [list, setList] = useState(getSaved)
  useEffect(() => {
    const on = () => setList(getSaved())
    window.addEventListener('cot-saved', on)
    window.addEventListener('storage', on)
    return () => { window.removeEventListener('cot-saved', on); window.removeEventListener('storage', on) }
  }, [])
  return list
}
export function toggleSaved(item) {
  const list = getSaved()
  const i = list.findIndex((x) => x.url === item.url)
  if (i >= 0) list.splice(i, 1)
  else list.unshift({ ...item, at: Date.now() })
  setSaved(list)
}
