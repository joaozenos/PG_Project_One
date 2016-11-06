import thread
import time
from Template import *
from graph import *
import popup

try:
    # Inicio do programa e das threads para rodar o grafico e a curva
    popup.start()
    thread.start_new_thread(main, ())
    thread.start_new_thread(graph, ())
except KeyboardInterrupt:
    thread.exit()

while 1:
    pass
