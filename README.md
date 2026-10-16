# Career of Telangana Students – Career Guide (React PWA)

A free, installable, offline-friendly career guide for Telangana students:
Intermediate groups, every degree after each group, Polytechnic, ITI, doctor specialisations,
nursing/pharmacy/allied health, govt & private jobs, **jobs abroad (top 10 countries + job apps)**,
scholarships and helplines.

- Runs on **port 5010**
- **PWA** – installable on Android, iPhone/iPad and Windows/Mac/Linux laptops; works offline after first visit
- 458 guides, 327 career folders, 265 courses with "Jobs abroad", 27 country guides, full-text search

## 1. Run on your laptop (Windows)
Needs **Node.js 20+** (https://nodejs.org).

```powershell
cd C:\Users\Goutham\Desktop\career_of_telangana
npm install
npm run build
npm run preview
```
Open **http://localhost:5010**  (for live editing use `npm run dev` – also port 5010).

## 2. Run with Docker (production)
```bash
docker compose up -d --build
```
Open http://SERVER-IP:5010 . Nginx config is in `nginx.conf` (SPA fallback + correct cache headers for the service worker).

Jenkins: the included `Jenkinsfile` builds the image and redeploys on every push.

## 3. IMPORTANT – HTTPS for installing on phones
Browsers allow "Install app" only on **https://** (or localhost). For students' phones, put the app behind your
Nginx reverse proxy with a domain and a free Let's Encrypt certificate, for example:

```nginx
server {
  server_name career.ggtech.info;
  location / { proxy_pass http://127.0.0.1:5010; proxy_set_header Host $host; }
  # certbot --nginx -d career.ggtech.info  (adds SSL automatically)
}
```

## 4. Install the app
- **Android (Chrome):** open the site → "Install app" (or menu ⋮ → Install app)
- **iPhone/iPad (Safari):** Share → Add to Home Screen
- **Laptop (Chrome/Edge):** install icon in the address bar
The in-app page **Install & share** shows these steps and a QR code for classrooms.

## 5. Update the content
All content comes from the Python generator in `data-generator/` (the same one that made the Word files).
```bash
pip install python-docx
cd data-generator
# edit the data files (e.g. deg_science.py, medical.py, abroad_prof.py, abroad_countries.py)
python export_json.py        # regenerates Word files in data-generator/output AND public/data/*.json
python test_all.py           # checks every Word file
cd .. && npm run build       # rebuild the app
```
Students get the update automatically the next time they open the app online.

## Project structure
```
src/            React app (pages, components, styles)
public/data/    all career content as JSON (tree, docs, abroad, search)
public/icons/   app icons (any + maskable + Apple)
data-generator/ Python scripts that produce the content
```
