#!/usr/bin/env python

#		Latex Table Maker v0.03
#
#	Use it however you want, don't tell me about it. There is a bug
#	in it however that causes hardrives to fail. Sometimes. It likely
#	won't happen to you.
#
#		To Use:
#	./latex_table.py table_filename [deliminator]
#
#	The deliminator functionality is currently disabled, because I use 
#	tabs in my tables and I can't figure out how to pass the tab character
#	from the command line. See line 35.
#
#	This was my first use of python, so some stuff is likely done wrong.
#
#	For instance, I have no idea why max_cols is too big.


import sys

# Expect the format to be
# ./latex_table.py table_filename delim
if len(sys.argv) != 3:
	exit(2)

# open the table to read
table = open(sys.argv[1], "r")
# make tex output file name
teX = sys.argv[1] + ".tex"
# open tex file to write
table_out = open(teX, "w")

# load deliminator of the table fields in the file
delim = '\t' #sys.argv[2]
#lines in the table
lines = 0
# columns in the table
cols = 0
max_cols = 0

# read through the file and get the number of lines and number of columns
for line in table:
	table_line = line.split(delim)
	lines += 1
	cols = len(table_line)
	if (cols > max_cols):
		max_cols = cols
# Get back to beginning of the table, now we'll read it
table.seek(0, 0)

#Write out the header for the table in LaTeX
table_out.write("\\begin{table}\n\\centering\n\\begin{tabular}{|")

#need number of columsn here
for i in range (1, max_cols):
	table_out.write("c")

# I don't know why max_cols is one too large, but it is.
table_out.write("|}\n\\hline\n\\multicolumn{%d" % (max_cols - 1) + "}{c}{Dummy Title}\\\\\n\\hline\n")

# now read the lines
for line in table:
	#parse the lines by the deliminator
	# this takes more lines in c
	table_line = line.split(delim)
	# write out the line of the file in the table
	for i in range (0,len(table_line) - 1):
		table_out.write(table_line[i] + " & ")

	#backup because we didn't need that last alignment character
	table_out.seek(-2, 1)
	
	#on to the next line!
	table_out.write('\\' + '\\' + ' \n')

# Last lines, tidying up. Go get ice cream!
table_out.write("\\hline\n\\end{tabular}\n\\caption{Dummy Caption. \\label{LBL}}\n\\end{table}")
