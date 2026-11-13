concrete_strength_optimizer/
│
├── main.py                       # 메인 화면
├── requirements.txt              # 필요한 라이브러리 목록
├── README.md                     # 프로젝트 설명 및 실행 방법
│
├── data/
│   ├── concrete.csv              # 콘크리트 배합 및 압축강도 데이터
│   └── optimized_mix.csv         # 최적 배합 결과 저장
│
├── models/
│   ├── strength_model.pkl        # 학습된 압축강도 예측 모델
│   └── scaler.pkl                # 데이터 스케일러
│
├── pages/
│   ├── 1_데이터_탐색.py           # 데이터 확인 및 기초 통계
│   ├── 2_데이터_시각화.py         # 배합 재료와 압축강도 시각화
│   ├── 3_모델_학습.py             # 머신러닝 모델 학습 및 평가
│   ├── 4_압축강도_예측.py         # 사용자 입력 배합의 강도 예측
│   └── 5_최적_배합.py             # 목표 강도에 따른 최적 배합 도출
│
├── utils/
│   ├── __init__.py
│   ├── data_loader.py             # 데이터 불러오기 및 전처리
│   ├── preprocessing.py           # 결측치 및 이상치 처리
│   ├── model_utils.py             # 모델 학습 및 평가 함수
│   ├── prediction.py              # 압축강도 예측 함수
│   └── optimizer.py               # 최적 배합 탐색 알고리즘
│
└── assets/
    └── logo.png                   # 프로그램 로고
