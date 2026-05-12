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

while True:
    print("To do list")
        
    for i in range(0, len(tasks)):
        print(f"{i+1} - {tasks[i]}")
        
    command = input()
    if command.startswith("add"):
        todo = input()
        tasks.append(todo)
        writeToFile(tasks)

    elif command.startswith("del"):
        todo = int(input())
        tasks.remove(tasks[todo-1])
        writeToFile(tasks)
        
    elif command.startswith("exit"):
        raise SystemExit
