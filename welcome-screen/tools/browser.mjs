// Shared Playwright launcher for local visual checks.
// Usage from another script:  import { launch } from './browser.mjs'
import { createRequire } from 'node:module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('playwright');

// iPhone 17 Pro Max logical viewport (points). Real panel: 1320x2868 @ 3x.
export const IPHONE = { width: 440, height: 956, deviceScaleFactor: 2, isMobile: true, hasTouch: true };

export async function launch(opts = {}) {
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium',
    args: ['--no-sandbox', '--disable-gpu', '--font-render-hinting=none'],
    ...(proxy ? { proxy: { server: proxy } } : {}),
  });
  const context = await browser.newContext({
    viewport: opts.viewport || { width: 1280, height: 1100 },
    deviceScaleFactor: opts.deviceScaleFactor ?? 2,
    isMobile: opts.isMobile ?? false,
    hasTouch: opts.hasTouch ?? true,
    ignoreHTTPSErrors: true,
    reducedMotion: opts.reducedMotion || 'no-preference',
    colorScheme: opts.colorScheme || 'dark',
  });
  const page = await context.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') errors.push(m.type() + ': ' + m.text()); });
  page.on('requestfailed', r => errors.push('requestfailed: ' + r.url() + ' ' + (r.failure()?.errorText || '')));
  return { browser, context, page, errors, close: () => browser.close() };
}
