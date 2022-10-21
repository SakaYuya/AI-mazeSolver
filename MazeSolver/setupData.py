from mazeDrawing import read_file

def mapToPointNameConverter(matrix):
    converter = {}
    
    with open(r'GlobalCache.py', 'w') as fp:
        fp.write("")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)
                vertex = [i, j]
                converter[f'"{i}_{j}"'] = vertex
                with open(r'GlobalCache.py', 'a') as fp:
                    fp.write(f'global_start = ({i}, {j})\n\n')
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    with open(r'GlobalCache.py', 'a') as fp:
                        fp.write(f'global_end = ({i}, {j})\n\n')
            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    vertex = [i, j]
                    converter[f'"{i}_{j}"'] = vertex
                    with open(r'GlobalCache.py', 'a') as fp:
                        fp.write(f'global_end = ({i}, {j})\n\n')

                elif matrix[i][j]==' ':
                    vertex = [i, j]
                    converter[f'"{i}_{j}"'] = vertex
            else:
                pass

    with open(r'OtherCache.py', 'w') as fp:
        builder = ''
        for item in converter.keys():
            builder += f'\n\t{item} : {converter[item]},'
        
        fp.write("mapToPointNameConverter = {")
        fp.write(builder[:-1])
        fp.write("\n}\n\n")

def setupAdjacencyList(matrix):
    mapToPointNameConverter(matrix)
    from OtherCache import mapToPointNameConverter as mapConverter
    with open(r'GlobalCache.py', 'a') as fp:
        builder = ''
        for vertex in mapConverter.keys():
            x = mapConverter[vertex][0]
            y = mapConverter[vertex][1]
            
            up    = f'{x}_{y - 1}'
            down  = f'{x}_{y + 1}'
            left  = f'{x - 1}_{y}'
            right = f'{x + 1}_{y}'
            
            builder += f'\n\t"{vertex}" : {{'
            if (up in mapConverter): builder += f'\n\t\t"{up}" : {{"cost" : 1}},'
            if (down in mapConverter): builder += f'\n\t\t"{down}" : {{"cost" : 1}},'
            if (left in mapConverter): builder += f'\n\t\t"{left}" : {{"cost" : 1}},'
            if (right in mapConverter): builder += f'\n\t\t"{right}" : {{"cost" : 1}},'
            builder = builder if builder[-1] == '{' else builder[:-1]
            builder += f'\n\t}},'
        fp.write("adjacencyList = {")
        fp.write(builder[:-1])
        fp.write("\n}")      

def pointNameToPointConverter(pointName, delim):
    converter = str(pointName).split(delim)
    return {"x" : converter[0], "y" : converter[1]}

def pointToPointNameConverter(point):
    return f"{point[0]}_{point[1]}"
