import os
from diagrams import Diagram, Cluster
from diagrams.onprem.client import Users
from diagrams.programming.framework import React
from diagrams.programming.language import Nodejs
from diagrams.onprem.database import PostgreSQL
from diagrams.custom import Custom  # Custom 아이콘 추가

# 현재 파일 위치 기반 상대 경로 설정
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SUPABASE_ICON = os.path.join(CURRENT_DIR, "assets/supabase.png")
SENTRY_ICON = os.path.join(CURRENT_DIR, "assets/sentry.png")
VERCEL_ANALYTICS_ICON = os.path.join(CURRENT_DIR, "assets/vercel.png")
GITHUB_ACTIONS_ICON = os.path.join(CURRENT_DIR, "assets/github_action.png")

# 다이어그램 전체 스타일 설정 (간격 조정)
graph_attrs = {
    "fontsize": "12",
    "splines": "polyline",  # 선을 직선으로 정리
    "ordering": "out",  # 노드가 한 방향으로 정렬되도록 설정
    "nodesep": "1.0",  # 노드 간 간격을 줄여서 압축적 레이아웃
    "ranksep": "1.2",  # 클러스터 간 세로 간격 조정
    "labelloc": "t",  # 타이틀을 위쪽에 정렬
    "labeljust": "c",  # 타이틀을 중앙 정렬
    "margin": "0.3",  # 전체적인 마진을 줄여서 모이게 설정
}

with Diagram("Zoofitter Architecture", show=True, graph_attr=graph_attrs):

    users = Users("React Native & Next.js Clients")

    with Cluster("프론트엔드", graph_attr={"pad": "1.0"}):
        nextjs = React("Next.js (Vercel)")
        rn = React("React Native (Expo)")
        analytics = Custom("Vercel Analytics", VERCEL_ANALYTICS_ICON)

    with Cluster("백엔드", graph_attr={"pad": "1.0"}):
        with Cluster("BFF - Next.js API Routes (Vercel)", graph_attr={"pad": "0.8"}):
            bff = Nodejs("Next.js API (Serverless)")

        with Cluster("서비스 백엔드 (Supabase)", graph_attr={"pad": "0.8"}):
            service_api = Nodejs("Supabase Edge Functions")
            db = PostgreSQL("PostgreSQL (Supabase)")
            storage = Custom("Supabase Storage", SUPABASE_ICON)
            auth = Custom("Supabase Auth", SUPABASE_ICON)

    with Cluster("배포 & 운영", graph_attr={"pad": "1.0"}):
        ci_cd = Custom("GitHub Actions", GITHUB_ACTIONS_ICON)
        sentry = Custom("Sentry (무료)", SENTRY_ICON)

    # 연결 관계 설정
    users >> nextjs
    users >> rn >> bff
    nextjs >> analytics
    bff >> service_api
    service_api >> [db, storage, auth]

    # 배포 & 운영 연결
    service_api >> ci_cd
    bff >> ci_cd
    sentry >> bff
