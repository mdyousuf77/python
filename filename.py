#python program to accept filename from the user and print the extenson of that

filename=input('enter the filename:')
extension=filename.split(".")
print("The extension of the file is:" +repr(extension[-1]))
