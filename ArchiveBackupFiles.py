import os, time, sys, datetime, shutil

#create log file
current_datetime = datetime.datetime.now()
str_current_datetime = str(current_datetime)
filen = str_current_datetime.replace(" ","_")
filen2 = filen.replace(":","-")
filen3 = filen2.replace(".","-")
file_name = "C:\\ArchiveShared\\Logs\\"+filen3+"_archive.txt"
print(file_name)
file = open(file_name, 'w')
  
print("File created : ", file_name)
file.close()


today = datetime.datetime.now()
now = time.time()
count = 0
print(today)


#log start time
with open(file_name, 'a') as f:
    strnow = str(today)
    f.write(strnow)
    f.write('\n')

    
#crawl thru the directory and delete old files
for parent, dirnames, filenames in os.walk('//us2bak01/SQLData'):
        for file in filenames:
            try:
                if file.endswith(".bak") or file.endswith(".trn"):
                    if os.stat(os.path.join(parent,file)).st_mtime < now - (60 * 86400):
                        #create full path for file to be removed
                        x = parent+"/"+file
                        print(x)
                        #remove file if exists
                        if os.path.exists(x):
                            os.remove(x)
                            text = "File removed: "+x
                            with open(file_name, 'a') as f:
                                f.write(text)
                                f.write('\n')

                        else:
                            print("The file does not exist")

                        count += 1
                        print(count)
                    
            except:
                a = parent+"/"+file
                y = "The system cannot find the file specified:"+a
                print(y)
                with open(file_name, 'a') as f:
                    f.write(y)
                    f.write('\n')
                continue

                
#log end time                 
today = datetime.datetime.now()
print(today)
strtoday = str(today)
with open(file_name, 'a') as f:
    f.write(strtoday)
    f.write('\n')
