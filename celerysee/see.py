import sys
import time
from datetime import datetime

def _rewrite_line(s):
    sys.stdout.write('\r')
    sys.stdout.write(s)
    sys.stdout.write('\n')
    sys.stdout.flush()
def _print(s, current_count):
    """Returns number of lines printed"""
    _rewrite_line(s)
    return current_count + 1
def _inspect(inspect, lines_to_clear):
    """Returns number of lines written."""
    back_str = '\033[F' * lines_to_clear
    sys.stdout.write(back_str)
    line_count = 0
    # List active tasks
    active = inspect.active()
    line_count = _print('Active', line_count)
    for k, v in active.items():
        line_count = _print('{} - {}'.format(k, len(v)), line_count)
    # List scheduled tasks
    scheduled = inspect.scheduled()
    line_count = _print('Scheduled', line_count)
    for k, v in scheduled.items():
        line_count = _print('{} - {}'.format(k, len(v)), line_count)
    line_count = _print(datetime.now().isoformat(), line_count)
    return line_count
def see(celery_app):
    inspect = celery_app.control.inspect()
    try:
        lines_written = 0
        while True:
            lines_written = _inspect(inspect, lines_written)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
