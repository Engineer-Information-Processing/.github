from datetime import datetime
import os

def calculate_d_day(target_date):
    today = datetime.now()
    target = datetime.strptime(target_date, "%Y-%m-%d")
    delta = target - today
    return delta.days

target_date = "2024-10-19"  # 목표 날짜 설정
d_day = calculate_d_day(target_date)

# 정확한 경로로 profile 디렉토리의 README.md 파일 업데이트
readme_path = os.path.join(".github", "profile", "README.md")
with open(readme_path, "w") as f:
    f.write(f"# D-Day: {d_day} days remaining\n")
