secs = int(input("Enter seconds: "))

hours = secs // 3600
minutes = secs // 60 % 60
seconds = secs % 60

print("%02d:%02d:%02d" % (hours, minutes, seconds))