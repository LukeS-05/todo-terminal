version = "0.1.1"

def writeToFile(tasks):
    with open("todo.txt", "w") as f:
        for i in range(0, len(tasks)):
            f.write(f"{tasks[i]}\n")
     
# main code
with open("todo.txt", "r") as f:
        tasks = []
        for line in f:
            todo = line.replace("\n", "")
            tasks.append(todo)

print(f"To-Do CLI v{version}")
while True:
    print("-"*90)
        
    for i in range(0, len(tasks)):
        print(f"{i+1} - {tasks[i]}")
        
    command = input()
    cmdlist = command.split(" | ")
    match cmdlist[0]:
        case "add":
            if len(cmdlist) < 2:
                print("Invalid arguments - Format - add | <task name>")
                continue
            todo = cmdlist[1]
            tasks.append(todo)
            writeToFile(tasks)
        case "mod":
            if len(cmdlist) < 2:
                print("Invalid arguments - Format - mod | <task number> | <new text>")
                continue
            todo = int(cmdlist[1])
            newtext = cmdlist[2]
            tasks[todo-1] = newtext
            writeToFile(tasks)
        case "del":
            if len(cmdlist) < 2:
                print("Invalid arguments - Format - del | <task number>")
                continue
            todo = int(cmdlist[1])
            del tasks[todo-1]
            writeToFile(tasks)
        case "clear":
            tasks = []
            writeToFile(tasks)
        case "exit":
            raise SystemExit
