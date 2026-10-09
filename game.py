#!/usr/bin/env python3
"""Offline keyboard emoji clicker, session-only progress."""
import curses,time
from ui import put,run
SUBJECT='🫪'
class Clicker:
 def __init__(self):self.points=0.;self.total=0.;self.power=1;self.workers=0
 def click(self):self.points+=self.power;self.total+=self.power
 def tick(self,dt):gain=self.workers*max(0,min(dt,1));self.points+=gain;self.total+=gain
 def cost(self,kind):return 10*2**(self.power-1) if kind==1 else 25*2**self.workers
 def buy(self,kind):
  if kind not in (1,2):return False
  cost=self.cost(kind)
  if self.points<cost:return False
  self.points-=cost
  if kind==1:self.power+=1
  else:self.workers+=1
  return True

def loop(s):
 s.timeout(80);g=Clicker();last=time.monotonic();message='';emoji=True
 while True:
  h,w=s.getmaxyx();key=s.getch();now=time.monotonic();g.tick(now-last);last=now
  if key in (27,ord('q')):return
  if key in (ord(' '),10,13):g.click();message='Click!'
  if key in (ord('1'),ord('2')):message='Upgrade bought.' if g.buy(key-ord('0')) else 'Not enough points.'
  if key==ord('f'):emoji=not emoji
  if key==ord('r'):g=Clicker();message='New session.'
  s.erase()
  if w<60 or h<20:
   put(s,2,1,'Resize to60x20. Esc/q exits.');s.refresh();continue
  put(s,0,1,'BLOATED FACE EMOJI CLICKER',curses.A_BOLD)
  put(s,2,2,'Points: '+str(int(g.points))+'   total earned: '+str(int(g.total)))
  put(s,4,2,'Click power: '+str(g.power)+'   auto per second: '+str(g.workers))
  face=SUBJECT if emoji else '( bloated face )'
  put(s,max(6,h//2-1),max(1,w//2-len(face)//2),face,curses.A_REVERSE)
  put(s,max(7,h//2+1),max(1,w//2-11),'SPACE / ENTER to click')
  put(s,h-7,2,'1: +1 click power, cost '+str(g.cost(1)))
  put(s,h-6,2,'2: +1 auto point/sec, cost '+str(g.cost(2)))
  put(s,h-4,2,message);put(s,h-3,2,'Emoji missing? F toggles text fallback. No save; quitting clears progress.')
  put(s,h-1,1,'Space/Enter click | 1/2 upgrades | F font fallback | R reset | Esc/q exit');s.refresh()
if __name__=='__main__':
 import sys
 if '--version' in sys.argv:print('1.0.0')
 else:raise SystemExit(run(loop))
