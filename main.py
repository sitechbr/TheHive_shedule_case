import schedule
import time


def job():
    print("I'm working...")
def job_day ():
    print("I'm working every day")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    schedule.every().minute.do(job)
    schedule.every().day.do(job_day)
    schedule.every().saturday.at("21:49").do(job_day)
    while True:
        schedule.run_pending()
        time.sleep(1)


