from time import sleep
from threading import Thread

answer = 0
def longtime_job(a,b):
    print('++JOB START')
    sleep(5)
    answer = a*b
    print(f'++JOB RESULT {answer}')

def main():
    a, b = 3, 4
    t = Thread(target=longtime_job, args=(a, b))
    t.start()
    print('**RUN MAIN LOGIC')
    #t.join()
    tmp = a+b
    final = answer + tmp
    print(f'MAIN RESULT {final}')

if __name__ == '__main__':
    main()