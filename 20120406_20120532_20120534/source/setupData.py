from imp import reload

def mapToPointNameConverter(matrix):
    converter = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=="S" or matrix[i][j]==" ":
                vertex = [i, j]
                converter[f'"{i}_{j}"'] = vertex

    with open('./OtherCache.py', 'w') as fp:
        builder = ''
        for item in converter.keys():
            builder += f'\n\t{item} : {converter[item]},'
        
        fp.write("mapToPointNameConverter = {")
        fp.write(builder[:-1])
        fp.write("\n}\n\n")

def setupAdjacencyList(matrix):
    with open('./GlobalCache.py', 'w') as fp:
        fp.write('')
    mapToPointNameConverter(matrix)

    import OtherCache
    reload(OtherCache)
    mapConverter = OtherCache.mapToPointNameConverter

    with open('./GlobalCache.py', 'a') as fp:
        builder = ''
        for vertex in mapConverter.keys():
            x = mapConverter[vertex][0]
            y = mapConverter[vertex][1]
            
            up    = f'{x - 1}_{y}'
            down  = f'{x + 1}_{y}'
            left  = f'{x}_{y - 1}'
            right = f'{x}_{y + 1}'
            
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
