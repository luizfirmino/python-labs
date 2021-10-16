#
# Luiz Filho
# 3/23/2021
# Module 6 Assignment
# 4. Write a Python function to create the HTML string with tags around the word(s). Sample function and result are shown below:
#
#add_html_tags('h1', 'My First Page')  
#<h1>My First Page</h1>
#
#add_html_tags('p', 'This is my first page.')  
#<p>This is my first page.</p>
#
#add_html_tags('h2', 'A secondary header.') 
#<h2>A secondary header.</h2>
#
#add_html_tags('p', 'Some more text.') 
#<p>Some more text.</p>

def add_html_tags(tag, value):
    return "<" + tag + ">" + value + "</" + tag + ">"

print(add_html_tags('h1', 'My First Page'))
print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
