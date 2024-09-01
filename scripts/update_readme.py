from datetime import datetime

def calculate_d_day(target_date):
    today = datetime.now()
    target = datetime.strptime(target_date, "%Y-%m-%d")
    delta = target - today
    return delta.days

target_date = "2024-12-25"  # 목표 날짜 설정
d_day = calculate_d_day(target_date)

with open("README.md", "w") as f:
    f.write(f"# D-Day: {d_day} days remaining\n")
