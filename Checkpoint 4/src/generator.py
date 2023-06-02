import sys
import math
import numpy as np

def generateSphere(radius, slice, stack, outputFile):
    triangles = []
    normals = []
    texcoords = []

    slices = int(slice)
    stacks = int(stack)
    
    for i in range(slices):
        alpha = i * (2 * math.pi / slices)
        alpha1 = (i + 1) * (2 * math.pi / slices)

        for j in range(int(-(stacks / 2)), int(stacks/2)):
            beta = j * (math.pi / stacks)
            beta1 = (j + 1) * (math.pi /stacks)

            x = radius * math.sin(alpha) * math.cos(beta) 
            y = radius * math.sin(beta)
            z = radius * math.cos(alpha) * math.cos(beta)

            triangles.append((x,y,z))

            norm = math.sqrt(x*x + y*y + z*z)
            normals.append((x/norm, y/norm, z/norm))

            x = radius * math.sin(alpha1) * math.cos(beta) 
            y = radius * math.sin(beta)
            z = radius * math.cos(alpha1) * math.cos(beta)

            triangles.append((x,y,z))
            
            norm = math.sqrt(x*x + y*y + z*z)
            normals.append((x/norm, y/norm, z/norm))

            x = radius * math.sin(alpha) * math.cos(beta1) 
            y = radius * math.sin(beta1)
            z = radius * math.cos(alpha) * math.cos(beta1)

            triangles.append((x,y,z))
            
            norm = math.sqrt(x*x + y*y + z*z)
            normals.append((x/norm, y/norm, z/norm))

            x = radius * math.sin(alpha1) * math.cos(beta) 
            y = radius * math.sin(beta)
            z = radius * math.cos(alpha1) * math.cos(beta)

            triangles.append((x,y,z))
            
            norm = math.sqrt(x*x + y*y + z*z)
            normals.append((x/norm, y/norm, z/norm))

            x = radius * math.sin(alpha1) * math.cos(beta1) 
            y = radius * math.sin(beta1)
            z = radius * math.cos(alpha1) * math.cos(beta1)

            triangles.append((x,y,z))
            
            norm = math.sqrt(x*x + y*y + z*z)
            normals.append((x/norm, y/norm, z/norm))

            x = radius * math.sin(alpha) * math.cos(beta1) 
            y = radius * math.sin(beta1)
            z = radius * math.cos(alpha) * math.cos(beta1)

            triangles.append((x,y,z))
            
            norm = math.sqrt(x*x + y*y + z*z)
            normals.append((x/norm, y/norm, z/norm))

            u = i / slices
            v = 1 - ((j + stacks / 2) / stacks)

            texcoords.append((u, v))
            texcoords.append(((i + 1) / slices, v))
            texcoords.append((u, 1 - ((j + 1 + stacks / 2) / stacks)))
            texcoords.append(((i + 1) / slices, v))
            texcoords.append(((i + 1) / slices, 1 - ((j + 1 + stacks / 2) / stacks)))
            texcoords.append((u, 1 - ((j + 1 + stacks / 2) / stacks)))

    with open(outputFile, 'w') as f:
        for i in range(0, len(triangles), 3):
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in triangles[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in normals[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in texcoords[j]) + '\n')

            f.write('\n')

def generateBox(size, divisions, outputFile):
    step = size / divisions
    ss = 1.0 / divisions

    triangles = []
    normals = []
    texcoords = []

    for i in range(int(divisions)):
        for j in range(int(divisions)):
            
            x1 = -size/2 + i*step
            z1 = -size/2 + j*step
            y1 = size/2

            x2 = -size/2 + (i+1)*step
            z2 = -size/2 + j*step
            y2 = size/2

            x3 = -size/2 + i*step
            z3 = -size/2 + (j+1)*step
            y3 = size/2

            x4 = -size/2 + (i+1)*step
            z4 = -size/2 + (j+1)*step
            y4 = size/2

            triangles.append([x3, y3, z3])
            triangles.append([x2, y2, z2])
            triangles.append([x1, y1, z1])
                
            triangles.append([x3, y3, z3])
            triangles.append([x4, y4, z4])
            triangles.append([x2, y2, z2])

            triangles.append([x3, -y3, z3])
            triangles.append([x1, -y1, z1])
            triangles.append([x2, -y2, z2])
            
            triangles.append([x3, -y3, z3])
            triangles.append([x2, -y2, z2])
            triangles.append([x4, -y4, z4])
              
            for _ in range(6):
                normals.append([0,1,0])
            
            for _ in range(6):
                normals.append([0,-1,0])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])
            texcoords.append([i*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([i*ss, i-(j*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])
            texcoords.append([(i+1)*ss, 1-((j+1)*ss)])

    for i in range(int(divisions)):
        for j in range(int(divisions)):
            
            x1 = -size/2 + i*step
            y1 = -size/2 + j*step
            z1 = size/2

            x2 = -size/2 + (i+1)*step
            y2 = -size/2 + j*step
            z2 = size/2

            x3 = -size/2 + i*step
            y3 = -size/2 + (j+1)*step
            z3 = size/2

            x4 = -size/2 + (i+1)*step
            y4 = -size/2 + (j+1)*step
            z4 = size/2

            triangles.append([x3, y3, -z3])
            triangles.append([x2, y2, -z2])
            triangles.append([x1, y1, -z1])
                
            triangles.append([x3, y3, -z3])
            triangles.append([x4, y4, -z4])
            triangles.append([x2, y2, -z2])

            triangles.append([x3, y3, z3])
            triangles.append([x1, y1, z1])
            triangles.append([x2, y2, z2])
            
            triangles.append([x3, y3, z3])
            triangles.append([x2, y2, z2])
            triangles.append([x4, y4, z4]) 

            for _ in range(6):
                normals.append([0,0,-1])

            for _ in range(6):
                normals.append([0,0,1])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])
            texcoords.append([i*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([i*ss, i-(j*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])
            texcoords.append([(i+1)*ss, 1-((j+1)*ss)])

    for i in range(int(divisions)):
        for j in range(int(divisions)):
            
            z1 = -size/2 + i*step
            y1 = -size/2 + j*step
            x1 = size/2

            z2 = -size/2 + (i+1)*step
            y2 = -size/2 + j*step
            x2 = size/2

            z3 = -size/2 + i*step
            y3 = -size/2 + (j+1)*step
            x3 = size/2

            z4 = -size/2 + (i+1)*step
            y4 = -size/2 + (j+1)*step
            x4 = size/2

            triangles.append([-x3, y3, z3])
            triangles.append([-x1, y1, z1])
            triangles.append([-x2, y2, z2])
                
            triangles.append([-x3, y3, z3])
            triangles.append([-x2, y2, z2])
            triangles.append([-x4, y4, z4])

            triangles.append([x3, y3, -z3])
            triangles.append([x1, y1, -z1])
            triangles.append([x2, y2, -z2])
                           
            triangles.append([x3, y3, -z3])
            triangles.append([x2, y2, -z2])
            triangles.append([x4, y4, -z4])
    
            for _ in range(6):
                normals.append([-1,0,0])

            for _ in range(6):
                normals.append([1,0,0])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])
            texcoords.append([i*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([i*ss, i-(j*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])

            texcoords.append([i*ss, 1-((j+1)*ss)])
            texcoords.append([(i+1)*ss, i-(j*ss)])
            texcoords.append([(i+1)*ss, 1-((j+1)*ss)])

    with open(outputFile, 'w') as f:
        for i in range(0, len(triangles), 3):
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in triangles[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in normals[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in texcoords[j]) + '\n')
                
            f.write('\n')

def generateCone(radius, height, slice, stack, outputFile):
    triangles = []
    normals = []
    texcoords = []

    slices = int(slice)
    stacks = int(stack)

    for j in range(stacks):
        for i in range(slices): 
            angle = 2 * math.pi / slices
            z = radius * math.cos(i * angle)
            x = radius * math.sin(i * angle)
            zz = radius * math.cos((i + 1) * angle)
            xx = radius * math.sin((i + 1) * angle)

            if (j < stacks):
                a = x * ((stacks - j) / stacks)
                b = height * j / stacks
                c = z * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                normals.append((x, math.cos(math.atan(height/radius)), z))
                texcoords.append((i / slices, 1 - (j / stacks)))
                
                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                normals.append((xx, math.cos(math.atan(height/radius)), zz))
                texcoords.append(((i + 1) / slices, 1 - (j / stacks)))
                
                a = x * ((stacks - j - 1) / stacks)
                b = height * (j + 1) / stacks
                c = z * ((stacks - j - 1) / stacks)

                triangles.append((a, b, c))
                normals.append((x, math.cos(math.atan(height/radius)), z))
                texcoords.append((i / slices, 1 - ((j + 1) / stacks)))
                
                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                normals.append((xx, math.cos(math.atan(height/radius)), zz))
                texcoords.append(((i + 1) / slices, 1 - (j / stacks)))
                
                a = xx * ((stacks - j - 1) / stacks)
                b = height * (j + 1) / stacks
                c = zz * ((stacks - j - 1) / stacks)

                triangles.append((a, b, c))
                normals.append((xx, math.cos(math.atan(height/radius)), zz))
                texcoords.append(((i + 1) / slices, 1 - ((j + 1) / stacks)))

                a = x * ((stacks - j - 1) / stacks)
                b = height * (j + 1) / stacks
                c = z * ((stacks - j - 1) / stacks)

                triangles.append((a, b, c))
                normals.append((x, math.cos(math.atan(height/radius)), z))
                texcoords.append((i / slices, 1 - ((j + 1) / stacks)))
                
            else:
                a = x * ((stacks - j) / stacks)
                b = height * j / stacks
                c = z * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                normals.append((x, radius, z))
                texcoords.append((i / slices, 1))

                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                normals.append((xx, radius, zz))
                texcoords.append(((i + 1) / slices, 1))

                a = 0
                b = height
                c = 0

                triangles.append((a, b, c))
                normals.append((0, -1, 0))
                texcoords.append((0.5, 0.5))

    with open(outputFile, 'w') as f:
        for i in range(0, len(triangles), 3):
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in triangles[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in normals[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in texcoords[j]) + '\n')

            f.write('\n')

def generatePlane(size, divisions, outputFile):
    step = size / divisions
    ss = 1.0 / divisions

    triangles = []
    normals = []
    texcoords = []

    for i in range(int(divisions)):
        for j in range(int(divisions)):
            x1 = -size/2 + i*step
            z1 = -size/2 + j*step
            y1 = 0

            x2 = -size/2 + (i+1)*step
            z2 = -size/2 + j*step
            y2 = 0

            x3 = -size/2 + i*step
            z3 = -size/2 + (j+1)*step
            y3 = 0

            x4 = -size/2 + (i+1)*step
            z4 = -size/2 + (j+1)*step
            y4 = 0

            triangles.append([x4, y4, z4])
            triangles.append([x2, y2, z2])
            triangles.append([x1, y1, z1])

            triangles.append([x3, y3, z3])
            triangles.append([x4, y4, z4])
            triangles.append([x1, y1, z1])

            triangles.append([x3, y3, z3])
            triangles.append([x1, y1, z1])
            triangles.append([x2, y2, z2])

            triangles.append([x3, y3, z3])
            triangles.append([x2, y2, z2])
            triangles.append([x4, y4, z4])

            texcoords.append([(i+1)*ss, (j+1)*ss])
            texcoords.append([(i+1)*ss, j*ss])
            texcoords.append([i*ss, j*ss])

            texcoords.append([i*ss, (j+1)*ss])
            texcoords.append([(i+1)*ss, (j+1)*ss])
            texcoords.append([i*ss, j*ss])

            texcoords.append([i*ss, (j+1)*ss])
            texcoords.append([i*ss, j*ss])
            texcoords.append([(i+1)*ss, j*ss])

            texcoords.append([i*ss, (j+1)*ss])
            texcoords.append([(i+1)*ss, j*ss])
            texcoords.append([(i+1)*ss, (j+1)*ss])

            for m in range(6):
                normals.append([0,1,0])

            for m in range(6):
                normals.append([0,-1,0])

    with open(outputFile, 'w') as f:
        for i in range(0, len(triangles), 3):
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in triangles[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in normals[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in texcoords[j]) + '\n')

            f.write('\n')

def generateCylinder(radius, height, side, stack, outputFile):
    triangles = []
    normals = []
    texcoords = []

    slides = int(side)
    stacks = int(stack)

    for i in range(slides):
        angle = i * (2 * math.pi / slides)
        value = (i + 1) * (2 * math.pi / slides)

        # Top
        x = radius * math.sin(angle)
        y = height 
        z = radius * math.cos(angle)

        triangles.append((x,y,z))
        normals.append((0,1,0))
        texcoords.append((0.5 + 0.5 * math.cos(angle), 0.5 - 0.5 * math.sin(angle)))
        
        x = radius * math.sin(value)
        y = height 
        z = radius * math.cos(value)
        
        triangles.append((x,y,z))       
        normals.append((0,1,0))
        texcoords.append((0.5 + 0.5 * math.cos(value), 0.5 - 0.5 * math.sin(value)))

        x = 0
        y = height 
        z = 0

        triangles.append((x,y,z))
        normals.append((0,1,0))
        texcoords.append((0.5, 0.5))

        for j in range(stacks):
            
            # Body
            x = radius * math.sin(angle)
            y = height  * (j / stacks)
            z = radius * math.cos(angle)

            triangles.append((x,y,z))
            normals.append((x, 0, z))
            texcoords.append((i / slides, j / stacks))
    
            x = radius * math.sin(value)
            y = height  * (j / stacks)
            z = radius * math.cos(value)
            
            triangles.append((x,y,z))
            normals.append((x, 0, z))
            texcoords.append(((i+1) / slides, j / stacks))       

            x = radius * math.sin(angle)
            y = height  * ((j + 1) / stacks)
            z = radius * math.cos(angle)

            triangles.append((x,y,z))
            normals.append((x, 0, z))
            texcoords.append((i / slides, j / stacks))


            x = radius * math.sin(angle)
            y = height * ((j + 1) / stacks)
            z = radius * math.cos(angle)

            triangles.append((x,y,z))
            normals.append((x, 0, z))
            texcoords.append((i / slides, (j+1) / stacks))
    
            x = radius * math.sin(value)
            y = height * (j / stacks)
            z = radius * math.cos(value)
            
            triangles.append((x,y,z))
            normals.append((x, 0, z))    
            texcoords.append(((i+1) / slides, j / stacks))       

            x = radius * math.sin(value)
            y = height * ((j + 1) / stacks)
            z = radius * math.cos(value)

            triangles.append((x,y,z))
            normals.append((x, 0, z))
            texcoords.append((i / slides, (j+1) / stacks))
        
        # Bottom
        x = radius * math.sin(angle)
        y = 0 
        z = radius * math.cos(angle)

        triangles.append((x,y,z))
        normals.append((0,-1,0))
        texcoords.append((0.5 + 0.5 * math.cos(angle), 0.5 - 0.5 * math.sin(angle)))
 
        x = 0
        y = 0
        z = 0

        triangles.append((x,y,z))
        normals.append((0,-1,0))
        texcoords.append((0.5, 0.5))
        
        x = radius * math.sin(value)
        y = 0 
        z = radius * math.cos(value)
        
        triangles.append((x,y,z))       
        normals.append((0,-1,0))
        texcoords.append((0.5 + 0.5 * math.cos(value), 0.5 - 0.5 * math.sin(value)))
    
    with open(outputFile, 'w') as f:
        for i in range(0, len(triangles), 3):
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in triangles[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in normals[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in texcoords[j]) + '\n')

            f.write('\n')

def generateTorus(outerRadius, innerRadius, slide, stack, outputFile):
    triangles = []
    normals = []
    texcoords = []

    slides = int(slide)
    stacks = int(stack)
    
    for i in range(slides):
        alpha = i * (2 * math.pi / slides)
        cosalpha = math.cos(alpha)
        sinalpha = math.sin(alpha)
        
        for j in range(stacks):
            beta = j * (2 * math.pi / stacks)
            cosbeta = math.cos(beta)
            sinbeta = math.sin(beta)
            
            x = (outerRadius + innerRadius * cosbeta) * cosalpha
            y = innerRadius * sinbeta
            z = (outerRadius + innerRadius * cosbeta) * sinalpha
            
            triangles.append((x, y, z))
            
            nextalpha = (alpha + 2 * math.pi / slides) % (2 * math.pi)
            nextCosalpha = math.cos(nextalpha)
            nextSinalpha = math.sin(nextalpha)
            
            nextbeta = (beta + 2 * math.pi / stacks) % (2 * math.pi)
            nextCosbeta = math.cos(nextbeta)
            nextSinbeta = math.sin(nextbeta)
            
            nextX = (outerRadius + innerRadius * nextCosbeta) * cosalpha
            nextY = innerRadius * nextSinbeta
            nextZ = (outerRadius + innerRadius * nextCosbeta) * sinalpha
            
            triangles.append((nextX, nextY, nextZ))
            
            nextX = (outerRadius + innerRadius * cosbeta) * nextCosalpha
            nextY = innerRadius * sinbeta
            nextZ = (outerRadius + innerRadius * cosbeta) * nextSinalpha

            triangles.append((nextX, nextY, nextZ))
            
            triangles.append((nextX, nextY, nextZ))
            
            nextX = (outerRadius + innerRadius * nextCosbeta) * cosalpha
            nextY = innerRadius * nextSinbeta
            nextZ = (outerRadius + innerRadius * nextCosbeta) * sinalpha
            
            triangles.append((nextX, nextY, nextZ))

            nextX = (outerRadius + innerRadius * nextCosbeta) * nextCosalpha
            nextY = innerRadius * nextSinbeta
            nextZ = (outerRadius + innerRadius * nextCosbeta) * nextSinalpha
            
            triangles.append((nextX, nextY, nextZ))
    
    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
                f.write('\n')

def generateBezier(inputFile, tess, outputFile):
    with open(inputFile, 'r') as f:
        numPatches = int(f.readline())
        patches = []
        for i in range(numPatches):
            indices = [int(x) for x in f.readline().split(',')]
            patches.append(indices)

        numControlPoints = int(f.readline())
        controlPoints = []
        for i in range(numControlPoints):
            point = [float(x) for x in f.readline().split(',')]
            controlPoints.append(point)

    tessellation = int(tess)

    triangles = []
    normals = []
    texcoords = []

    def calculatePoint(u, v,arr):
        m = np.array([[-1, 3, -3, 1],
                    [3, -6, 3, 0],
                    [-3, 3, 0, 0],
                    [1, 0, 0, 0]])

        pos = np.zeros(3)

        for i in range(3):
            P = np.array([[arr[0][i], arr[1][i], arr[2][i], arr[3][i]],
                        [arr[4][i], arr[5][i], arr[6][i], arr[7][i]],
                        [arr[8][i], arr[9][i], arr[10][i], arr[11][i]],
                        [arr[12][i], arr[13][i], arr[14][i], arr[15][i]]])

            U = np.array([u*u*u, u*u, u, 1])
            V = np.array([[v*v*v], 
                        [v*v], 
                        [v], 
                        [1]])

            pos[i] = np.dot(np.dot(np.dot(np.dot(U,m),P),m), V)

        return pos
    
    delta = 1.0/tessellation
    for patch in patches:
        arr=[]
        for p in patch:
            arr.append(controlPoints[p])
        for i in range(tessellation):
            for j in range(tessellation):
                u = i * delta
                v = j * delta
                A = calculatePoint(u, v, arr)
                B = calculatePoint(u, v+delta, arr)
                C = calculatePoint(u+delta, v, arr)
                D = calculatePoint(u+delta, v+delta, arr)

                normal = np.cross(B - A, C - A) # normal entre os pontos A B C
                magnitude = np.linalg.norm(normal) # Tamanho do vetor normal
                if magnitude < 1e-6: # ver se é perto de zero pra não dar problemas com a divisão
                    continue
                
                normal /= magnitude

                triangles.append(B)
                normals.append(normal)
                texcoords.append((u, v + delta))

                triangles.append(C)
                normals.append(normal)
                texcoords.append((u + delta, v))

                triangles.append(A)
                normals.append(normal)
                texcoords.append((u, v))

                triangles.append(B)
                normals.append(normal)
                texcoords.append((u, v + delta))

                triangles.append(D)
                normals.append(normal)
                texcoords.append((u + delta, v + delta))

                triangles.append(C)
                normals.append(normal)
                texcoords.append((u + delta, v))
                
    with open(outputFile, 'w') as f:
        for i in range(0, len(triangles), 3):
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in triangles[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in normals[j]) + '\n')
            for j in range(i, i+3):
                f.write(' '.join(str(x) for x in texcoords[j]) + '\n')

            f.write('\n')

shapes = {
    'sphere': {
        'func': generateSphere,
        'args': ['radius', 'slices', 'stack', 'outputFile']
    },
    'box': {
        'func': generateBox,
        'args': ['size', 'divisions' 'outputFile']
    },
    'cone': {
        'func': generateCone,
        'args': ['radius', 'height', 'slices', 'stack', 'outputFile']
    },
    'plane': {
        'func': generatePlane,
        'args': ['x', 'z', 'outputFile']
    },
    'cylinder':{
        'func': generateCylinder,
        'args': ['radius', 'height', 'slides', 'stacks', 'outputFile']
    },
    'torus': {
        'func': generateTorus,
        'args': ['outerRadius', 'innerRadius', 'side', 'ring', 'outputFile']
    },
    'patch':{
        'func': generateBezier,
        'args': ['inputFile', 'tess', 'outputFile']
    }
}

if len(sys.argv) < 4:
    print('Usage: generator.py <shape> <arg1> <arg2> ... <outputFile>')
    sys.exit(1)

shapeName = sys.argv[1]
if shapeName not in shapes:
    print(f'Invalid shape name: {shapeName}')
    sys.exit(1)

args = sys.argv[2:-1]
outputFile = sys.argv[-1]

shapeArgs = []
for arg in args:
    try:
        shapeArgs.append(float(arg))
    except ValueError:
        shapeArgs.append(arg)

shapeArgs.append(outputFile)

shapeFunc = shapes[shapeName]['func']
shapeFunc(*shapeArgs)

print(f'Successfully generated {shapeName} in file {outputFile}')