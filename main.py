import selectors
import server

selector = selectors.DefaultSelector()
print('Hello')
def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ =='__main__':
    server.start(selector)
    event_loop()