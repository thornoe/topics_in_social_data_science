### Intro to Python for Data Science - a highly recommendable free course ###
https://www.datacamp.com/courses/intro-to-python-for-data-science

### Variables ###
var1 = [1, 2, 3, 4]
var2 = True
var3 = "Happy holiday"

# type
type(var1)

# length
len(var1)
len(var3)

# Convert var2 to an integer: out2
out2 = int(var2)

# Help
help(complex)
# also pull-up the list of options when writing a command, e.g.
# alt+i in atom (hydrogen inspector)
# shift+tab in a Jupyter Notebook

# Sorted
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse=1)

# Print out full_sorted
full_sorted

### String methods ###
place = "poolhouse"

# Print out the number of o's in place
place.count('o')
### List methods that don't change the list ###
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 18.0
areas.index(18)

# Print out how often 9.50 appears in areas
areas.count(9.5)

### List methods that changes the list ###
areas.append(24.5)
areas.append(15.45)
areas.reverse()
areas
