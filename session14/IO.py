# fout = open('session14/output.txt', 'w')

# line1 = "How many roads must a man walk down\n"
# fout.write(line1)

# line2 = "Before you call him a man?\n"
# fout.write(line2)

# # When you are done writing, you should close the file.
# fout.close()
# # If you don’t close the file, 
# # it gets closed for you when the program ends.

# import os.path

# def sed(pattern, replace, source, dest):
#     """
#     Reads a source file and writes the destination file.
#     In each line, replaces pattern with replace.
#     pattern: string
#     replace: string
#     source: string filename
#     dest: string filename
#     """
#     content = open(source)
#     fout = open(dest, 'w')
#     for line in content:
#         if pattern in line:
#             a = line.replace(pattern, replace)
#             fout.write(a)
#         else:
#             fout.write(line)

# sed('Jude', 'Julie', 'session14/test.txt', 'session14/result.txt')


# import os
# cwd = os.getcwd() 
# # cwd stands for “current working directory”. 
# print(cwd)

# print(os.path.abspath('output.txt'))
# print(os.path.exists('output.txt'))
# print(os.path.isdir('output.txt'))
# print(os.path.isdir(cwd))
# print(os.path.isfile('output.txt'))
# print(os.listdir(cwd))

# def walk(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

# def walk2(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for root, dirs, files in os.walk(dirname):
#         for filename in files:
#             print(os.path.join(root, filename))

# try:    
#     fin = open('bad_file')
# except:
#     print('Something went wrong.')

# # The pickle module can translate almost any type of object into a string
# # suitable for storage in a database, and then translates strings back into objects.

# import pickle
# t = [1, 2, 3]
# print(pickle.dumps(t))

# t1 = [1, 2, 3]
# s = pickle.dumps(t1)
# t2 = pickle.loads(s)
# print(t2)

# print(t1 == t2)
# print(t1 is t2)

  
import wc
print(wc)
print(wc.linecount('session14/result.txt'))