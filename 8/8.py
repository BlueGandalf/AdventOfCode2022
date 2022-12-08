import os;

# grid[row][column]

def getColumn(grid, x):
    column = [];
    for line in grid:
        column.append(line[x])
    return column;

def isVisible(grid, x, y):
    treeHeight = grid[y][x];
    if (x == 0 or y == 0 or x == (len(grid[y]) - 1) or y == (len(grid) - 1)):
        return True;

    isVisible = False;
    if (max(grid[y][:x]) < treeHeight or max(grid[y][x+1:]) < treeHeight):
        isVisible = True;
    elif (max(getColumn(grid, x)[:y]) < treeHeight or max(getColumn(grid, x)[y+1:]) < treeHeight):
        isVisible = True;

    return isVisible;

def howManyTreesLine(column, y):
    leftIndex = 0;
    rightIndex = 0;
    for i in range(len(column)):
        if (i < y and column[i] >= column[y]):
            leftIndex = i;
        elif (i > y and column[i] >= column[y]):
            rightIndex = i;
            break;

    leftScore = (y - leftIndex);
    if rightIndex != 0:
        rightScore = (rightIndex - y);
    else:
        rightScore = len(column) - 1 - y;

    return leftScore * rightScore;

def getScenicScore(grid, x, y):
    column = getColumn(grid, x);
    scenicScore = howManyTreesLine(grid[y], x) * howManyTreesLine(column, y);

    return scenicScore;

grid = [];
with open(os.path.join(os.path.dirname(__file__), '8.txt')) as f:
    y = 0;
    for line in f:
        grid.append([]);
        for digit in line.strip():
            grid[y].append(int(digit))
        y += 1;

visibleCount = 0;
hiddenCount = 0;
highestScenicScore = 0;
for line in grid:
    print(line);
    for x in range(len(line)):
        if (isVisible(grid, x, grid.index(line))):
            visibleCount += 1;
        else:
            hiddenCount += 1;
        scenicScore = getScenicScore(grid, x, grid.index(line));
        if (scenicScore > highestScenicScore):
            highestScenicScore = scenicScore;
        # print("digit: ");
        # print(line[x]);
        # print("scenicScore: ");
        # print(scenicScore);

print("visible:");
print(visibleCount);
print("hidden:");
print(hiddenCount);
print("scenicScore:");
print(highestScenicScore);

# print(howManyTreesLine([6, 5, 3, 3, 2], 3))
# print(howManyTreesLine([7, 1, 3, 4, 9], 2))
# print(howManyTreesLine([3, 3, 5, 4, 9], 2)) # 4
# print(howManyTreesLine([3, 5, 3, 5, 3], 3)) # 2