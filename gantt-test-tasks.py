import datetime
import gantt
import json



# create date from ordinal
def orddate(num): 
    return datetime.date.fromordinal(num)


class JTask():
    """Holds a task parsed from the json file
    """

    def __init__(self,pkg):
        self.start = orddate(pkg['Queue Position'])
        self.end = orddate(pkg['Last Required'])




dataFile = "/home/gabriel/University/Master/experiments/gantt-tests/gantt-py/Row1.json"

with open(dataFile) as fh:
    data = json.load(fh)

title = data['title']
for pkg in data['packages']:
    tasks.append(JTask(pkg))


print(orddate(2))

# Create some tasks
t1 = gantt.Task(name='task1',
                start=datetime.date(2014, 12, 27),
                duration=4 )
t2 = gantt.Task(name='task2',
                start=datetime.date(2014, 12, 28),
                depends_of=[t1],
                duration=6)
t7 = gantt.Task(name='tache7',
                start=datetime.date(2014, 12, 28),
                duration=5)
t3 = gantt.Task(name='tache3',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=[t1, t7, t2], )
t4 = gantt.Task(name='tache4',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=[t1, t7, t2],
                )
t5 = gantt.Task(name='tache5',
                start=datetime.date(2014, 12, 23),
                duration=3)
t6 = gantt.Task(name='tache6',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=t7, )
t8 = gantt.Task(name='tache8',
                start=datetime.date(2014, 12, 25),
                duration=4,
                depends_of=t7,
                )


# Create a project
p1 = gantt.Project(name='Projet 1')

# Add tasks to this project
p1.add_task(t1)
p1.add_task(t7)
p1.add_task(t2)
p1.add_task(t3)
p1.add_task(t5)
p1.add_task(t8)



# Create another project
p2 = gantt.Project(name='Projet 2', color='#FFFF40')

# Add tasks to this project
p2.add_task(t2)
p2.add_task(t4)


# Create another project
p = gantt.Project(name='Gantt')
# wich contains the first two projects
# and a single task
p.add_task(p1)
p.add_task(p2)
p.add_task(t6)



# Change font default
gantt.define_font_attributes(fill='black',
                             stroke='black',
                             stroke_width=0,
                             font_family="Verdana")



##########################$ MAKE DRAW ###############
p.make_svg_for_tasks(filename='test-full.svg', 
                     today=datetime.date(2014, 12, 31))
p.make_svg_for_tasks(filename='test_full2.svg',
                     today=datetime.date(2014, 11, 10))
##########################$ /MAKE DRAW ###############
