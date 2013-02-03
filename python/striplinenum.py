infile = open("file.py","r")
outfile = open("file_new.py","w")
for eachline in infile:
    pos = eachline.find(".",0,len(eachline))
    newline = eachline[pos+1:-1]+'\n'
    print newline
    outfile.write(newline)
