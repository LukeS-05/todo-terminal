version = "0.1.2"

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

print(f"✅ To-Do CLI v{version}")
while True:
    print("-"*90)
        
    for i in range(0, len(tasks)):
        print(f"{i+1} - {tasks[i]}")
        
    command = input(">> ")
    cmdlist = command.split("|")
    match cmdlist[0]:
        case "add" | "+":
            if len(cmdlist) < 2:
                print("Invalid arguments - Format - add | <task name>")
                continue
            todo = cmdlist[1]
            tasks.append(todo)
            writeToFile(tasks)
        case "mod" | "~":
            if len(cmdlist) < 3:
                print("Invalid arguments - Format - mod | <task number> | <new text>")
                continue
            try:
                todo = int(cmdlist[1])
            except ValueError:
                print("Invalid arguments - arg2 must be an integer")
            newtext = cmdlist[2]
            tasks[todo-1] = newtext
            writeToFile(tasks)
        case "swap":
            if len(cmdlist) < 3:
                print("Invalid arguments - Format - swap | <task number> | <task number>")
                continue
            try:
                swap1 = int(cmdlist[1]) -1
                swap2 = int(cmdlist[2]) -1
            except ValueError:
                print("Invalid arguments - arg2 and arg3 must be integers")
            
            tasks[swap1], tasks[swap2] = tasks[swap2], tasks[swap1]
            writeToFile(tasks)
        case "del" | "-":
            if len(cmdlist) < 2:
                print("Invalid arguments - Format - del | <task number>")
                continue
            try:
                todo = int(cmdlist[1])
            except ValueError:
                print("Invalid arguments - arg2 must be an integer")
            del tasks[todo-1]
            writeToFile(tasks)
        case "clear":
            confirm = input("Clearing your to-do list is a permanent action.\nType 'clear' to continue.")
            if confirm == "clear":
                tasks = []
                writeToFile(tasks)
                print("Successfully cleared todo list.")
            else:
                print("Cancelled")
        case "help" | "?":
            print("Coming soon")
        case "exit" | "x":
            raise SystemExit
