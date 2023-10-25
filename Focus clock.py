import time

def focus_timer(duration, break_duration):
    print("专注时间开始！")
    for remaining in range(duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        print(f"{minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
    
    print("\n专注时间结束。休息一下！")
    
    for remaining in range(break_duration, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        print(f"{minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)
    
    print("\n休息时间结束。继续下一个专注周期。")

if __name__ == "__main__":
    focus_duration = 25 * 60  # 25分钟专注时间（以秒为单位）
    break_duration = 5 * 60   # 5分钟休息时间（以秒为单位）
    focus_timer(focus_duration, break_duration)
