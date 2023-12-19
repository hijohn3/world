from time import sleep
from threading import Thread

def longtime_job(a,b):
    print('++JOB START')
    sleep(5)
    print(f'++JOB RESULT {a*b}')

def main():
    a, b = 3, 4
    t = Thread(target=longtime_job, args=(a, b))
    #longtime_job(a, b)
    t.start()
    print('**RUN MAIN LOGIC')
    ret = a+b
    print(f'MAIN RESULT {ret}')

if __name__ == '__main__':
    main()