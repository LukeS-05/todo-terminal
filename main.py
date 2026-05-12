with open("todo.txt", "r") as f:
    tasks = []
    for line in f:
        todo = line.replace("\n", "")
        tasks.append(todo)
    
for i in range(0, len(tasks)):
    print(f"{i+1} - {tasks[i]}")