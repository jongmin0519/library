#원격저장소 수정 

from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.today()
    age = today.year - birth_year
    
    # 생일 전이라면 나이에서 1을 뺍니다.
    if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
        age -= 1

    return age

if __name__ == "__main__":
    birth_year = int(input("생년(예: 1990)을 입력하세요: "))
    birth_month = int(input("생월(예: 1)을 입력하세요: "))
    birth_day = int(input("생일(예: 25)을 입력하세요: "))

    age = calculate_age(birth_year, birth_month, birth_day)
    print(f"만 나이는 {age}세 입니다.")
