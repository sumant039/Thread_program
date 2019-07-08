# Thread_program
Thread_program


It can temporarily be put on hold (also known as sleeping) while other threads are running - this is called yielding.
Starting a New Thread
To spawn another thread, you need to call the following method available in the thread module −
_thread.start_new_thread ( function, args[, kwargs] )


Creating Thread Using Threading Module

To implement a new thread using the threading module, you have to do the following −
Define a new subclass of the Thread class.
Override the __init__(self [,args]) method to add additional arguments.
Then, override the run(self [,args]) method to implement what the thread should do when started.
Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by invoking the start(),
which in turn calls the run() method.

Synchronizing Threads
The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to synchronize threads. 
A new lock is created by calling the Lock() method, which returns the new lock.
The acquire(blocking) method of the new lock object is used to force the threads to run synchronously. 
The optional blocking parameter enables you to control whether the thread waits to acquire the lock.
If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired and with a 1 if the lock was acquired. 
If blocking is set to 1, the thread blocks and wait for the lock to be released.
The release() method of the new lock object is used to release the lock when it is no longer required.


The Threading Module
The newer threading module included with Python 2.4 provides much more powerful,
 high-level support for threads than the thread module discussed in the previous section.
The threading module exposes all the methods of the thread module and provides some additional methods −
threading.activeCount() − Returns the number of thread objects that are active.
threading.currentThread() − Returns the number of thread objects in the caller's thread control.
threading.enumerate() − Returns a list of all thread objects that are currently active.
In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −
run() − The run() method is the entry point for a thread.
start() − The start() method starts a thread by calling the run method.
join([time]) − The join() waits for threads to terminate.
isAlive() − The isAlive() method checks whether a thread is still executing.
getName() − The getName() method returns the name of a thread.
setName() − The setName() method sets the name of a thread