import random
import sys

class TraceGen:

  def __init__(self, addr_width_p):
    self.addr_width_p = addr_width_p


  def send_read(self, addr):
    trace = "0001_"
    trace += self.get_bin_str(addr, self.addr_width_p)
    print(trace)

  def done(self):
    trace = "0011_"
    trace += self.get_bin_str(0, self.addr_width_p)
    print(trace)
  
  def get_bin_str(self, val, width):
    return format(val, "0" + str(width) + "b")

if __name__ == "__main__":
  tg=TraceGen(30)
  random.seed(sys.argv[1])
  # 1MB sequential read
  for i in range(1024*1024/32):
    tg.send_read(i<<5)

  tg.done()