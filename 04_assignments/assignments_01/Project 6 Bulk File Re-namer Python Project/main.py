import os

def main():
    i = 0
    path = "F:/Codes/Python & AI/Q3/assignments/assignments/04_assignments/assignments_01/Project 6 Bulk File Re-namer Python Project/tester-folder/testing/" # / will be on end otherwise filenotfound error!
    for filename in os.listdir(path):
        my_dest = "file" + str(i) + ".txt"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()
