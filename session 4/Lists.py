# apply some of list command
command_insert = "insert"
command_print = "print"
command_remove = "remove"
command_append = "append"
command_sort = "sort"
command_pop = "pop"
command_reverse = "reverse"
#intialize empty list
my_list = []
num_of_commands= int(input())
for i in range(num_of_commands):
       order = input().split()
       if order[0] == command_insert:
              my_list.insert(int(order[1]),int(order[2]))
       elif order[0] == command_print:
              print(my_list)
       elif order[0] == command_remove:
              my_list.remove(int(order[1]))
       elif order[0] == command_append:
              my_list.append(int(order[1]))              
       elif order[0] == command_pop:
              my_list.pop()
       elif order[0] == command_reverse:
              my_list.reverse()
       else :
              my_list.sort()
              
       
