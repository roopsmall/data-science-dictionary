# script to generate index.html from the dictionary terms in terms.txt


terms = 'terms.txt'     # file where the dictionary items are stored
previous_letter = ''    # previous letter in iteration over list of dictionary items
index_html = []         # ordered list of all the html for index.html
split_letter = 'M'      # letter at which to split the table into a second column


with open(terms) as f:  # get all dictionary items into list
    terms_list = f.read().splitlines()


terms_list.sort()       # order the list
for each in terms_list: # generate html for each item in the list of dictionary terms
    letter = each[0].upper()
    if letter != previous_letter:
        if letter == split_letter:  # split content into second column
            index_html.append('</table></td><td class="left_and_right_columns"><table>')
        index_html.append('<tr><td class="header_td"><b><a name="'+letter+'">'+letter+'</a></b></td></tr>')
    if '~' in each:
	acronym, root = each.split('~')
	index_html.append('<tr><td><a href="'+root.replace(' ','-')+'.html'+'">'+acronym+'</a></td></tr>')
    else:    
	index_html.append('<tr><td><a href="'+each.replace(' ','-')+'.html'+'">'+each+'</a></td></tr>')
    previous_letter = each[0].upper()


# html for top component of index.html
html_head = """
<html>
<head>
<link rel="stylesheet" href="stylesheet.css" type="text/css">
<meta name="description" content="dictionary of data science terms">
<meta name="keywords" content="data science, dictionary">
</head>
<body>
<table id="main">
<tr><td colspan="2"><h1>Dictionary of Data Science Terms</h1></td></tr>
<tr><td colspan="2"><hr><a href="#A">A</a> <a href="#B">B</a> <a href="#C">C</a> <a href="#D">D</a> 
<a href="#E">E</a> <a href="#F">F</a> <a href="#G">G</a> <a href="#H">H</a> <a href="#I">I</a> 
<a href="#J">J</a> <a href="#K">K</a> <a href="#L">L</a> <a href="#M">M</a> <a href="#N">N</a> 
<a href="#O">O</a> <a href="#P">P</a> <a href="#Q">Q</a> <a href="#R">R</a> <a href="#S">S</a> 
<a href="#T">T</a> <a href="#U">U</a> <a href="#V">V</a> <a href="#W">W</a> <a href="#X">X</a> 
<a href="#Y">Y</a> <a href="#Z">Z</a><br><hr> </td></tr>
<tr><td class="left_and_right_columns"><table>
"""


# html for base component of index.html
html_base = """
</td></tr>
</table>
</body><html>
"""


index_html = [html_head] + index_html + [html_base]  # combine everything in right order
with open('index.html','w') as f:
	for html in index_html:                      # output index.html
    		print >>f, html
