import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

// Career of Telangana Students – runs on port 5010 (dev and preview)
export default defineConfig({
  base: process.env.VITE_ARTIFACT === '1' ? './' : '/',
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg', 'icons/apple-touch-icon.png', 'icons/favicon-64.png'],
      manifest: {
        id: '/',
        name: 'Career of Telangana Students',
        short_name: 'TG Students Career',
        description: 'Courses after 10th, Inter and degree, govt and private jobs, abroad jobs and scholarships for Telangana students.',
        lang: 'en-IN',
        start_url: '/',
        scope: '/',
        display: 'standalone',
        orientation: 'any',
        background_color: '#F5F6FA',
        theme_color: '#1E2A5A',
        categories: ['education'],
        icons: [
          { src: '/icons/icon-192.png', sizes: '192x192', type: 'image/png', purpose: 'any' },
          { src: '/icons/icon-512.png', sizes: '512x512', type: 'image/png', purpose: 'any' },
          { src: '/icons/maskable-192.png', sizes: '192x192', type: 'image/png', purpose: 'maskable' },
          { src: '/icons/maskable-512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' }
        ],
        shortcuts: [
          { name: 'Find my path', url: '/path', icons: [{ src: '/icons/icon-192.png', sizes: '192x192' }] },
          { name: 'Search', url: '/search', icons: [{ src: '/icons/icon-192.png', sizes: '192x192' }] },
          { name: 'Jobs abroad', url: '/countries', icons: [{ src: '/icons/icon-192.png', sizes: '192x192' }] }
        ]
      },
      workbox: {
        // cache the whole app + all career data so it works fully offline after first visit
        globPatterns: ['**/*.{js,css,html,svg,png,woff2,json}'],
        maximumFileSizeToCacheInBytes: 4 * 1024 * 1024,
        navigateFallback: '/index.html',
        cleanupOutdatedCaches: true
      }
    })
  ],
  server: { port: 5010, strictPort: true, host: true },
  preview: { port: 5010, strictPort: true, host: true },
  build: { chunkSizeWarningLimit: 900 }
})
