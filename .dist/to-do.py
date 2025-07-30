class Task:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority
        
    def __str__(self):
        return f"{self.task}({self.priority})"
    
    def __repr__(self):
        return f"Task({self.task}, {self.priority})"
    
class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def delete_task(self, index):
        self.tasks.pop(index)
        
    def view_tasks(self):
        return [task for task in self.tasks]
    
if __name__ == "__main__":
    todolist = ToDoList()
    
    #todolist.add_task(Task("Task1", "High"))
    #todolist.add_task(Task("Task2", "Low"))
    #todolist.add_task(Task("Task3", "High"))
    #todolist.add_task(Task("Task4", "Medium"))
    
    #for task in todolist.view_tasks():
       # print(task)
        
    #todolist.delete_task(0)
    
    #print("")
    
    # print(task)
    
    condition = True
    while condition:
        print("====OPTIONS====")
        print("1) Add Task")
        print("2) Delete Task")
        print("3) View Task")
        print("4) Exit")
        
        choice = input("Enter a choice: ")
        match choice:
            case 1:
                task = input("Enter Task name: ")
                priority = input("Enter Task Priority: ")
                todolist.add_task(Task(task, priority))
            
            case 2:
                index = input("Enter Task index to delete: ")
                todolist.delete_task(index)
            
            case 3:
                print("\n")
                for task in todolist.view_tasks():
                    print(task)
            
            case 4:
                condition = False