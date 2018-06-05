#with allows you to open files without having to gracefully exiting.

with open('/etc/passwd','r') as f:
    for line in f:
        print(line)