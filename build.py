from os import listdir
from os.path import isfile, join, realpath, dirname
from sys import argv
from time import sleep

__version__ = '1'

def getBasePath():
    script_cwd = realpath(__file__)
    script_cwd = dirname(script_cwd)
    return script_cwd

def getFilesInPath(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def concatenateFiles(paths):
    concatFile = []
    for path in paths:
        with open(path, 'r') as file:
            concatFile.append(*file.readlines())
    return concatFile

def saveOutputFile(path, data, append = False):
    mode = 'w+'
    if append is True:
        mode = 'a+'
    with open(path, mode) as file:
        file.writelines(data)
    return True

def printSortedFiles(paths):
    print('Files will be concatenated in order: ')
    for i, file in enumerate(paths):
        print('{0} | {1}'.format(i, file))
    print('-------------------------------------')

def noNone(value, default):
    if value is not None:
        return value
    return default

def build():
    base_path = getBasePath()
    source_path = join(base_path, 'src')
    output_path = join(base_path, 'README.md')
    filesToConcatenate = getFilesInPath(source_path)
    sortedFiles = sorted(filesToConcatenate)
    sortedFiles = noNone(sortedFiles, [])
    printSortedFiles(sortedFiles)
    absolutePathedFiles = [join(source_path, file) for file in sortedFiles]
    fileBuilded = concatenateFiles(absolutePathedFiles)
    return saveOutputFile(output_path, fileBuilded)

def main():
    print('PAiP Web Developer Guide Builder v.{0}'.format(__version__))
    time_limiter = 10
    if 'cb' in argv:
        print('Starting Continuos Build Mode')
        print('-----------------------------')
        i = 1
        while True:
            print('Starting Build {0}'.format(i))
            build()
            i += 1
            print('Waiting {0} seconds for next build'.format(time_limiter))
            sleep(time_limiter)
    else:
        print('Starting Single Build Mode')
        print('--------------------------')
        build()

main()
