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
            z = radius * math.cos(alpha1) * math.cos(beta1)

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

def generateCone(radius, height, slices, stacks, outputFile):
    vertices = []

    angle_increment = 2 * math.pi / slices
    height_increment = height / stacks

    for i in range(int(stacks) + 1):
        z = i * height_increment
        radius_stack = radius * (stacks - i) / stacks

        for j in range(int(slices)):
            angle = j * angle_increment
            x = radius_stack * math.cos(angle)
            y = radius_stack * math.sin(angle)
            vertices.append([x, y, z])

    triangles = []
    for i in range(int(stacks)):
        for j in range(int(slices)):
            current_stack_idx = i * slices + j
            next_stack_idx = current_stack_idx + slices

            v1_idx = current_stack_idx
            v2_idx = (j + 1) % slices + current_stack_idx
            v3_idx = (j + 1) % slices + next_stack_idx
            v4_idx = current_stack_idx + next_stack_idx

            triangles.append([v1_idx, v2_idx, v3_idx])
            triangles.append([v1_idx, v3_idx, v4_idx])

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

            triangles.append([x3, y3, z3])
            triangles.append([x2, y2, z2])
            triangles.append([x1, y1, z1])
                
            triangles.append([x3, y3, z3])
            triangles.append([x4, y4, z4])
            triangles.append([x2, y2, z2])


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

