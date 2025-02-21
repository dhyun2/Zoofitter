# **🚀 Zoofitter Tech Stack**

## **🎨 Frontend**

🎯 **Zoofitter의 프론트엔드는 모바일 및 웹을 지원하는 풀스택 애플리케이션으로 구성됩니다.**

- 🖥 **프레임워크:** Next.js
- 📱 **모바일 앱:** React Native
- ⚡ **번들러:** Vite, Turbopack
- 📦 **패키지 매니저:** pnpm
- 📂 **모노레포 관리:** Turborepo
- 🎨 **UI 라이브러리:** Tailwind CSS, shadcn/ui
- 🔄 **상태 관리:** TanStack Query + Zustand
- 🧪 **테스팅:**
  - ✅ **유닛 테스트:** Jest + Testing Library
  - 🔍 **E2E 테스트:** Detox (React Native), Playwright

## **🛠 Backend (BFF + 서비스 API)**

🔗 **Zoofitter는 BFF와 서비스 백엔드를 분리하여 효율적인 API 구조를 제공합니다.**

### **1️⃣ BFF (Frontend-Facing API)**

- ⚙ **프레임워크:** Next.js API Routes (Vercel Serverless Functions)
- 🔗 **API 방식:** REST API + GraphQL + tRPC
- 🚀 **캐싱:** Vercel Edge Caching 활용
- 🎯 **호출 대상:** Supabase Edge Functions API
- 🔐 **인증:** Supabase Auth(JWT)

### **2️⃣ 서비스 백엔드 (Supabase 기반)**

- 🗄 **DB:** PostgreSQL(Supabase)
- 🔗 **API 방식:** Supabase Edge Functions
- 🛠 **데이터 처리:** Prisma + Supabase SQL
- ⚡ **실시간 처리:** Supabase Realtime 활용
- 📂 **파일 저장:** Supabase Storage
- 🔐 **인증 & 보안:** Supabase Auth

## **🗄 Database & Caching**

- 🛢 **데이터베이스:** Supabase (PostgreSQL)
- 🚀 **캐싱:**Vercel Edge Caching + storage 

## **☁ Deployment & Infrastructure**

- 🚀 **서버 배포:**
  - **BFF** → Vercel Serverless Functions
  - **서비스 백엔드** → Supabase Edge Functions
  - **프론트엔드** → Vercel
- 🔄 **CI/CD:**
  - GitHub Actions + Vercel

## **📊 Monitoring & Logging**

- 📈 **웹 성능 모니터링:** Vercel Analytics
- 🔎 **API 모니터링:** Supabase Logs
- 🚨 **에러 트래킹:** Sentry
- 📝 **로그 관리:** Supabase Query Performance Logs
- ⚡ **실시간 데이터 처리:** Supabase Realtime


