import os;

def find_key(dictionary, originalValue):
    for key, value in dictionary.items():
        if value == originalValue:
            return [key]
        elif isinstance(value, dict):
            p = find_key(value, originalValue)
            if p:
                return [key] + p

def find_directory(fileStructure, arrayKeys):
    if arrayKeys is None:
        return fileStructure;
    tempDict = fileStructure;
    for key in arrayKeys:
        tempDict = tempDict[key];
    return tempDict;

def find_directory_size(fileStructure, onlyFiles = False):
    size = 0;
    for key, item in fileStructure.items():
        if (isinstance(item, dict)):
            if (not onlyFiles):
                size += find_directory_size(item);
        else:
            size += int(item);
    return size;

def find_directories(fileStructure):
    directories = [];
    for key, value in fileStructure.items():
        if (isinstance(value, dict)):
            directories.append(value);
            directories = directories + find_directories(value);
    return directories;

workingDirectoryName = "";
workingDirectory = {};
fileStructure = workingDirectory;
with open(os.path.join(os.path.dirname(__file__), '7.txt')) as f:
    for line in f:
        line = line.strip();
        if '$' in line:
            command = line[2:];
            if (command[0:2] == 'cd'):
                key = find_key(fileStructure, workingDirectory);
                if (command[3:] == '..'):
                    workingDirectory = find_directory(fileStructure, key[:-1]);
                    continue;

                workingDirectoryName = command[3:];
                workingDirectory[workingDirectoryName] = {};
                workingDirectory = workingDirectory[workingDirectoryName];
        else:
            if line[0:3] == 'dir':
                directoryName = line[4:];
                workingDirectory[directoryName] = {};
            else:
                size, fileName = line.split(' ');
                workingDirectory[fileName] = size;

availableSpace = 70000000;
neededSpace = 30000000;
usedSpace = 0;
usedSpaceBySmallerDirs = 0;
dirSizes = [];
for dir in find_directories(fileStructure):
    dirSize = find_directory_size(dir);
    dirSizes.append(dirSize);
    usedSpace += find_directory_size(dir, onlyFiles=True);
    if dirSize <= 100000:
        usedSpaceBySmallerDirs += dirSize;

print("part 1:");
print(usedSpaceBySmallerDirs);

print("used space:");
print(usedSpace);

emptySpace = availableSpace - usedSpace;

spaceToFreeUp = neededSpace - emptySpace;
print("space to free up:");
print(spaceToFreeUp);

directoryDeletionCandidates = [];
for dirSize in dirSizes:
    if (dirSize >= spaceToFreeUp):
        directoryDeletionCandidates.append(dirSize);

directoryDeletionCandidates.sort();
print(directoryDeletionCandidates[0]);
