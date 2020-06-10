import threading 
import time

class RepeatedTimer(object):
  def __init__(self, interval, function, *args, **kwargs):
    """The builder of the 'repeatedTime' class.
    
    The purpose of this class is to execute a "function" every x seconds put in the "interval" parameter.
    The execution of the function is non-blocking and allow other threads to execute at the same time.
    The constructor call the "run" function by itself so no need to call it when you create your 
    repeatedTime object.
    
    """
    self.a_time = None
    self.a_interval = interval
    self.a_function = function
    self.a_args = args
    self.a_kwargs = kwargs
    self.a_is_running = False
    self.a_next_call = time.time()
    self.start()

  def _run(self):
    self.a_is_running = False
    self.start()
    self.a_function(*self.a_args, **self.a_kwargs)

  def start(self):
    """No need to call this function with your object."""
    if not self.a_is_running:
      self.a_next_call += self.a_interval
      self.a_time = threading.Timer(self.a_next_call - time.time(), self._run)
      self.a_time.start()
      self.a_is_running = True

  def stop(self):
    """Use this function to stop your thread whenever."""
    self.a_time.cancel()
    self.a_is_running = False
