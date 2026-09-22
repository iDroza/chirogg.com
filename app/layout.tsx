import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = {
 title: 'Chiro Growth Group | PPC & AI for Clinics',
 description: 'Google Ads, Meta campaigns, landing pages, and AI-assisted follow-up for med spas, chiropractors, and physical therapy clinics.',
};
export default function RootLayout({children}:Readonly<{children:React.ReactNode}>){return <html lang="en"><body>{children}</body></html>}
