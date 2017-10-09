#!/usr/bin/python
import config as config
from pytodoist import todoist
user = todoist.login(config.todoistapi['user'], config.todoistapi['password'])
projects = user.get_projects()
groceries_project = user.get_project('Courses')
groceries = groceries_project.get_tasks()
print "##### LISTE COURSES #####"
print "Nombre d'articles : "+str(len(groceries))
print "------------------------"
for item in groceries:
	print "[ ] "+item.content
print "------------------------"
