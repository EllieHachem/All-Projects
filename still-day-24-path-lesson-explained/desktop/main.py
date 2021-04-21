#files dont just have names they also have pathes 
#on computers there is file and folders and files can live in folders
#and you can navigate(go through) serveral folders to get to a particular  file 
# the root is the main path of folder which is represented by /
#then the main path which is usually c and the path c contain folder that could contain folder and file and that folder in folder could contain files 
#directions are like how you worked in cordova projects same way forward slash / and this is called absolute file path always have / 

#relative file path = depend on the directory that we are  working from also like cordova as we choose the path like an example if we are working in folder that contains the file u want to use we just say /file_name_we_wanna_use.txt so that explains why data.txt was working 
#fine in same main.py and how game works cool stuff so the relative file path alwways depend on the working directory 
#if we wanna go up we use ../ = going up 1 parents file means going up by 1 folder 
#./ for same place or / or nothing since same location that is why ../ is one parent (this is relative that is why ./)
#go to windows press properites in a file you want to use and copy location (that is path file )
#usually windows uses \ and we should fix it to use / 
#each ../ means file file backward so ../../ means 2 folders up awesome to use in relative file path so that u dont repeat code again 
#absolute file path = always relative to the root of your computer
#in windowws in c drive and relative file path is relative to currenr  working directory it depend on ur stituation depend on you u can use both 


with open("data.txt") as cool:
    cool.read()
    print(cool)