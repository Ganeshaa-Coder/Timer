import time

def format_time(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

def stopwatch():
    print("⏱️ Stopwatch Started")
    print("Press [Enter] to pause/resume. Type 'stop' and press [Enter] to end.\n")

    running = True
    start_time = time.time()
    paused_time = 0

    while True:
        user_input = input()
        if user_input.strip().lower() == "stop":
            break
        if running:
            paused_at = time.time()
            print("⏸️ Paused at:", format_time(paused_at - start_time - paused_time))
            running = False
        else:
            resumed_at = time.time()
            paused_time += resumed_at - paused_at
            print("▶️ Resumed")
            running = True

    end_time = time.time()
    total_time = end_time - start_time - paused_time
    print(f"\n✅ Stopwatch stopped. Total time: {format_time(total_time)}")

if __name__ == "__main__":
    stopwatch()
