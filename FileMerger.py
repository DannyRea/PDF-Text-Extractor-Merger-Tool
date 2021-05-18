import os


def fileMerge():

    all_files = os.listdir(os.path.abspath('./'))
    print('\nAll files in current directory ' + str(all_files) + '\n')

    txtFiles = list(filter(lambda x: x[-4:] == '.txt', all_files))

    print("Text files in directory: " + str(txtFiles))

    filenames = txtFiles

    print("Merging files.....")

    with open('171 final notes.rtf', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())

    print("Merging complete!\n")
    os.system('pause')