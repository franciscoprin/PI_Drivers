import threading
from Graph import Graph
import time
import matplotlib.pyplot as plt
import json

class GraphThread (threading.Thread):
   def __init__(self, delay, points,semaphore):
      threading.Thread.__init__(self)
      self.points = points
      self.delay = delay
      self.semaphore = semaphore

   def run(self):
      g = Graph(plt)
      g.setAxis(0,300,0,100)
      while True:
         if self.points.size() > 3:
            print("GRAPH POINT: sending point")
            g.addPoint(self.points.dequeue())
            plt.pause(1)
         time.sleep(self.delay)


