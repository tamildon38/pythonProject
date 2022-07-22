import threading
t=threading.current_thread()

print("current thread:",t)
print("Thread name:",t.name)
print("thread identifier:",t.ident)
print("is the thread alive:",t.is_alive())
t.name='Mythread'
print("after name change:",t.name)


