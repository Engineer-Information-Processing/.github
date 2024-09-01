from datetime import datetime
import os

def calculate_d_day(target_date):
    today = datetime.now()
    target = datetime.strptime(target_date, "%Y-%m-%d")
    delta = target - today
    return delta.days

target_date = "2024-10-19"  # 목표 날짜 설정
d_day = calculate_d_day(target_date)

# 루트 디렉토리 기준으로 절대 경로 설정
root_dir = os.getenv('GITHUB_WORKSPACE', '')  # GitHub Actions의 루트 디렉토리 가져오기
readme_path = os.path.join(root_dir, ".github", "profile", "README.md")

with open(readme_path, "w") as f:
    f.write(f"# Engineer-Information-Processing\n\n## D-Day\n현재 목표일까지 남은 날짜는 {d_day}일입니다.")
