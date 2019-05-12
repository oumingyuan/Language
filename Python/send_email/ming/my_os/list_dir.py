import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        # print(files)
        #
        # print(len(files))

        return files


file_list = file_name("C:\\Users\\oumin\\Desktop\\snow")


print(file_list)
print(len(file_list))
