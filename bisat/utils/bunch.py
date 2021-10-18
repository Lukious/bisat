def csv_reader(dir):
    datalist = []
    f = open(dir, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        datalist.append(int(str(line)[2]))
    f.close()
    return datalist
        
def search(dir):
        file_list = []
        files = os.listdir(dir)
        for file in files:
                # print(file)
                file_list.append(file)
        return file_list
    
def filetype_selector(file_list,file_type):
    selected_list = []
    for i in(range(len(file_list))):
        filename = file_list[i]
        if filename[-3:] == file_type:
            selected_list.append(filename)
    return selected_list

def list_to_csv(target_list,filename):
    with open(filename+'.csv','w',newline = '') as file:
        writer = csv.writer(file)
        for i in range(len(target_list)):
            writer.writerow(target_list[i])