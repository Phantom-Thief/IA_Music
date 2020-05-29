import pynput
import time
from pynput.mouse import Button,Listener

def on_move(x,y):
    write_file_move(x,y)

def on_click(x,y,button,pressed):
    if pressed:
        write_file_clicked(x,y,button)
    if not pressed:
        #Stop Monitoring the mouse
        return False


def on_scroll(x,y,dx,dy):
    write_file_scrolled(x,y,dx,dy)



def write_file_move(x,y):
    with open("log_mouse.txt",'a') as f:
        f.write("Mouse moved to ({0}, {1}) \n".format(x, y))

def write_file_clicked(x,y,button):
    with open("log_mouse.txt",'a') as f:
        f.write('Mouse clicked at ({0}, {1}) with {2} \n'.format(x, y, button))

def write_file_scrolled(x,y,dx,dy):
    with open("log_mouse.txt",'a') as f:
        f.write('Mouse scrolled at ({0}, {1})({2}, {3}) \n'.format(x, y, dx, dy))



def mouseLogger():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

