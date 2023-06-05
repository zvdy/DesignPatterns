class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject.request()")
        return "RealSubject.request()"
    

class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        print("Proxy.request()")
        return self._real_subject.request()
    

def main():
    proxy = Proxy()
    proxy.request()

