
task_count = int(input(f'How many tasks do you want to list? \n Enter here : '))

my_tasks = []
for i in range(task_count):
    task = input(f'Enter task {i+1} : ')
    my_tasks.append(task)

print('Your TO-DO List: ')
for idx, task in enumerate(my_tasks):
    print(idx, task)