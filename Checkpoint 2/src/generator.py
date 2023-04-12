import sys
import math

def generateSphere(radius, slice, stack, outputFile):
    triangles = []

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

            x = radius * math.sin(alpha1) * math.cos(beta) 
            y = radius * math.sin(beta)
            z = radius * math.cos(alpha1) * math.cos(beta)

            triangles.append((x,y,z))

            x = radius * math.sin(alpha) * math.cos(beta1) 
            y = radius * math.sin(beta1)
            z = radius * math.cos(alpha) * math.cos(beta1)

            triangles.append((x,y,z))

            x = radius * math.sin(alpha1) * math.cos(beta) 
            y = radius * math.sin(beta)
            z = radius * math.cos(alpha1) * math.cos(beta)

            triangles.append((x,y,z))

            x = radius * math.sin(alpha1) * math.cos(beta1) 
            y = radius * math.sin(beta1)
            z = radius * math.cos(alpha1) * math.cos(beta1)

            triangles.append((x,y,z))

            x = radius * math.sin(alpha) * math.cos(beta1) 
            y = radius * math.sin(beta1)
            z = radius * math.cos(alpha) * math.cos(beta1)

            triangles.append((x,y,z))

    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
                f.write('\n')

def generateBox(size, divisions, outputFile):
    step = size / divisions
    triangles = []

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
    
    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
                f.write('\n')

def generateCone(radius, height, slice, stack, outputFile):
    triangles = []

    slices = int(slice)
    stacks = int(stack)

    for j in range(stacks):
        for i in range(slices): 
            angle = 2 * math.pi / slices
            z = radius * math.cos(i * angle)
            x = radius * math.sin(i * angle)
            zz = radius * math.cos((i + 1) * angle)
            xx = radius * math.sin((i + 1) * angle)

            if j == 0:
                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))

                a = x * ((stacks - j) / stacks)
                b = height * j / stacks
                c = z * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                
                a = 0
                b = height * j / stacks
                c = 0

                triangles.append((a, b, c))

            angle2 = math.pi / slices

            if (j < stacks - 1):
                a = x * ((stacks - j) / stacks)
                b = height * j / stacks
                c = z * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                
                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                
                a = x * ((stacks - j - 1) / stacks)
                b = height * (j + 1) / stacks
                c = z * ((stacks - j - 1) / stacks)

                triangles.append((a, b, c))
                
                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))
                
                a = xx * ((stacks - j - 1) / stacks)
                b = height * (j + 1) / stacks
                c = zz * ((stacks - j - 1) / stacks)

                triangles.append((a, b, c))

                a = x * ((stacks - j - 1) / stacks)
                b = height * (j + 1) / stacks
                c = z * ((stacks - j - 1) / stacks)

                triangles.append((a, b, c))

            else:
                a = x * ((stacks - j) / stacks)
                b = height * j / stacks
                c = z * ((stacks - j) / stacks)

                triangles.append((a, b, c))

                a = xx * ((stacks - j) / stacks)
                b = height * j / stacks
                c = zz * ((stacks - j) / stacks)

                triangles.append((a, b, c))

                a = 0
                b = height
                c = 0

                triangles.append((a, b, c))

    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
                f.write('\n')

def generatePlane(size, divisions, outputFile):
    step = size / divisions
    triangles = []
    
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

    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
                f.write('\n')

def generateCylinder(radius, height, side, stack, outputFile):
   
    triangles = []
    sides = int(side)
    stacks = int(stack)

    for i in range(sides):
        angle = i * (2 * math.pi / sides)
        value = (i + 1) * (2 * math.pi / sides)

        # Top
        x = radius * math.sin(angle)
        y = height 
        z = radius * math.cos(angle)

        triangles.append((x,y,z))
 
        x = radius * math.sin(value)
        y = height 
        z = radius * math.cos(value)
        
        triangles.append((x,y,z))       

        x = 0
        y = height 
        z = 0

        triangles.append((x,y,z))

        for j in range(stacks):
            
            # Body
            x = radius * math.sin(angle)
            y = height  * (j / stacks)
            z = radius * math.cos(angle)

            triangles.append((x,y,z))
    
            x = radius * math.sin(value)
            y = height  * (j / stacks)
            z = radius * math.cos(value)
            
            triangles.append((x,y,z))       

            x = radius * math.sin(angle)
            y = height  * ((j + 1) / stacks)
            z = radius * math.cos(angle)

            triangles.append((x,y,z))


            x = radius * math.sin(angle)
            y = height * ((j + 1) / stacks)
            z = radius * math.cos(angle)

            triangles.append((x,y,z))
    
            x = radius * math.sin(value)
            y = height * (j / stacks)
            z = radius * math.cos(value)
            
            triangles.append((x,y,z))       

            x = radius * math.sin(value)
            y = height * ((j + 1) / stacks)
            z = radius * math.cos(value)

            triangles.append((x,y,z))
        
        # Bottom
        x = radius * math.sin(angle)
        y = 0 
        z = radius * math.cos(angle)

        triangles.append((x,y,z))
 
        x = 0
        y = 0
        z = 0

        triangles.append((x,y,z))
        
        x = radius * math.sin(value)
        y = 0 
        z = radius * math.cos(value)
        
        triangles.append((x,y,z))       
    
    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
                f.write('\n')

def generateTorus(outerRadius, innerRadius, side, ring, outputFile):
    triangles = []
    sides = int(side)
    rings = int(ring)
    
    for i in range(sides):
        theta = i * (2 * math.pi / sides)
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta)
        
        for j in range(rings):
            phi = j * (2 * math.pi / rings)
            cosPhi = math.cos(phi)
            sinPhi = math.sin(phi)
            
            x = (outerRadius + innerRadius * cosPhi) * cosTheta
            y = innerRadius * sinPhi
            z = (outerRadius + innerRadius * cosPhi) * sinTheta
            
            triangles.append((x, y, z))
            
            nextTheta = (theta + 2 * math.pi / sides) % (2 * math.pi)
            nextCosTheta = math.cos(nextTheta)
            nextSinTheta = math.sin(nextTheta)
            
            nextPhi = (phi + 2 * math.pi / rings) % (2 * math.pi)
            nextCosPhi = math.cos(nextPhi)
            nextSinPhi = math.sin(nextPhi)
            
            nextX = (outerRadius + innerRadius * nextCosPhi) * nextCosTheta
            nextY = innerRadius * nextSinPhi
            nextZ = (outerRadius + innerRadius * nextCosPhi) * nextSinTheta
            
            triangles.append((nextX, nextY, nextZ))
            
            nextPhi = phi + 2 * math.pi / rings
            nextCosPhi = math.cos(nextPhi)
            nextSinPhi = math.sin(nextPhi)
            
            nextX = (outerRadius + innerRadius * nextCosPhi) * cosTheta
            nextY = innerRadius * nextSinPhi
            nextZ = (outerRadius + innerRadius * nextCosPhi) * sinTheta
            
            triangles.append((nextX, nextY, nextZ))
            
            x = (outerRadius + innerRadius * cosPhi) * cosTheta
            y = innerRadius * sinPhi
            z = (outerRadius + innerRadius * cosPhi) * sinTheta
            
            triangles.append((x, y, z))
            
            nextPhi = phi + 2 * math.pi / rings
            nextCosPhi = math.cos(nextPhi)
            nextSinPhi = math.sin(nextPhi)
            
            nextX = (outerRadius + innerRadius * nextCosPhi) * nextCosTheta
            nextY = innerRadius * nextSinPhi
            nextZ = (outerRadius + innerRadius * nextCosPhi) * nextSinTheta
            
            triangles.append((nextX, nextY, nextZ))
            
            nextTheta = (theta + 2 * math.pi / sides) % (2 * math.pi)
            nextCosTheta = math.cos(nextTheta)
            nextSinTheta = math.sin(nextTheta)
            
            nextX = (outerRadius + innerRadius * nextCosPhi) * nextCosTheta
            nextY = innerRadius * nextSinPhi
            nextZ = (outerRadius + innerRadius * nextCosPhi) * nextSinTheta
            
            triangles.append((nextX, nextY, nextZ))
    
    with open(outputFile, 'w') as f:
        for i, l in enumerate(triangles):
            f.write(' '.join(str(x) for x in l) + '\n')
            if (i+1) % 3 == 0:
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
        'args': ['radius', 'height', 'sides', 'stacks', 'outputFile']
    },
    'torus': {
        'func': generateTorus,
        'args': ['outerRadius', 'innerRadius', 'side', 'ring', 'outputFile']
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

shapeFunc = shapes[shapeName]['func']
shapeArgs = [float(arg) for arg in args] + [outputFile]
shapeFunc(*shapeArgs)

print(f'Successfully generated {shapeName} in file {outputFile}')

