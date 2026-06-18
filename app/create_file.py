import sys
import os
from datetime import datetime


print(sys.argv)

if "-d" in sys.argv and "-f" in sys.argv:
    idx_d = sys.argv.index("-d")
    idx_f = sys.argv.index("-f")
    if idx_d < idx_f:
        dirs = sys.argv[idx_d + 1:idx_f]
        filename = sys.argv[idx_f + 1]
    else:
        dirs = sys.argv[idx_d + 1:]
        filename = sys.argv[idx_f + 1]

elif "-d" in sys.argv:
    dirs = sys.argv[sys.argv.index("-d") + 1:]
    filename = None

elif "-f" in sys.argv:
    dirs = []
    filename = sys.argv[sys.argv.index("-f") + 1]

else:
    dirs = []
    filename = sys.argv[-1]

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

filepath = None
if filename:
    if dirs:
        filepath = os.path.join(path, filename)
    else:
        filepath = filename

if filename:
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    if lines:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filepath, "a") as f:
            if os.path.getsize(filepath) > 0:
                f.write("\n")
            f.write(timestamp + "\n")
            for i, line in enumerate(lines, 1):
                f.write(f"{i} {line}\n")
