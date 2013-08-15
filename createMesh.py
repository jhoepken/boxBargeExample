from os.path import join
from sys import argv, exit
import numpy as np

from PyFoam.RunDictionary.SolutionDirectory import SolutionDirectory

from Mesher import BlockMesh

origin = (0, 0, 0)
B = 0.3
T = 0.1
L = 0.9

p = 3.0*L

nCellsX = 15
nCellsY = 15
nCellsZ = 15

phi=np.radians(15.0)

case = SolutionDirectory(".",archive=None,paraviewLink=False)

#############################################
# Create points for each block individually #
#############################################

#v1 = [
def rot(v):
    R = np.array([1,0,0,0,np.cos(phi),-1*np.sin(phi),0,np.sin(phi), np.cos(phi)])
    R.shape = (3,3)
    if isinstance(v, list):
        vT = np.array(v)
    else:
        vT = v

    return [i for i in np.dot(R,vT)]

points1 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]-(0.5*B + p), origin[2]-(0.5*T + p)),
            (origin[0]-0.5*L, origin[1]-0.5*B, origin[2]-0.5*T)
        )
for i in [6,7]:
    points1[i] = rot(points1[i])
    points1[i-4][1] = points1[i][1]
    points1[i-2][2] = points1[i][2]

points2 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]-0.5*B, origin[2]-(0.5*T + p)),
            (origin[0]-0.5*L, origin[1]+0.5*B, origin[2]-0.5*T)
        )
for i in [4,5,6,7]:
    points2[i] = rot(points2[i])
    points2[i-4][1] = points2[i][1]

points3 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]+0.5*B, origin[2]-(0.5*T + p)),
            (origin[0]-0.5*L, origin[1]+(0.5*B + p), origin[2]-0.5*T)
        )
for i in [4,5]:
    points3[i] = rot(points3[i])
    points3[i-4][1] = points3[i][1]
    points3[i+2][2] = points3[i][2]

points4 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]-(0.5*B + p), origin[2]-0.5*T),
            (origin[0]-0.5*L, origin[1]-0.5*B, origin[2]+0.5*T)
        )
for i in [2,3,6,7]:
    points4[i] = rot(points4[i])
    points4[i-2][2] = points4[i][2]

points5 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]-0.5*B, origin[2]-0.5*T),
            (origin[0]-0.5*L, origin[1]+0.5*B, origin[2]+0.5*T)
        )
for i in range(0,8):
    points5[i] = rot(points5[i])

points6 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]+0.5*B, origin[2]-0.5*T),
            (origin[0]-0.5*L, origin[1]+(0.5*B + p), origin[2]+0.5*T)
        )
for i in [0,1,4,5]:
    points6[i] = rot(points6[i])
    points6[i+2][2] = points6[i][2]

points7 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]-(0.5*B + p), origin[2]+0.5*T),
            (origin[0]-0.5*L, origin[1]-0.5*B, origin[2]+(0.5*T+p))
        )
for i in [2,3]:
    points7[i] = rot(points7[i])
    points7[i+4][1] = points7[i][1]
    points7[i-2][2] = points7[i][2]

points8 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]-0.5*B, origin[2]+0.5*T),
            (origin[0]-0.5*L, origin[1]+0.5*B, origin[2]+(0.5*T+p))
        )
for i in [0,1,2,3]:
    points8[i] = rot(points8[i])
    points8[i+4][1] = points8[i][1]

points9 = BlockMesh.boundingBox(
            (origin[0]-(0.5*L + p), origin[1]+0.5*B, origin[2]+0.5*T),
            (origin[0]-0.5*L, origin[1]+(0.5*B + p), origin[2]+(0.5*T+p))
        )
for i in [0,1]:
    points9[i] = rot(points9[i])
    points9[i+2][2] = points9[i][2]
    points9[i+4][1] = points9[i][1]

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------

points10 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]-(0.5*B + p), origin[2]-(0.5*T + p)),
            (origin[0]+0.5*L, origin[1]-0.5*B, origin[2]-0.5*T)
        )
for i in [6,7]:
    points10[i] = rot(points10[i])
    points10[i-4][1] = points10[i][1]
    points10[i-2][2] = points10[i][2]

points11 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]-0.5*B, origin[2]-(0.5*T + p)),
            (origin[0]+0.5*L, origin[1]+0.5*B, origin[2]-0.5*T)
        )
for i in [4,5,6,7]:
    points11[i] = rot(points11[i])
    points11[i-4][1] = points11[i][1]

points12 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]+0.5*B, origin[2]-(0.5*T + p)),
            (origin[0]+0.5*L, origin[1]+(0.5*B + p), origin[2]-0.5*T)
        )
for i in [4,5]:
    points12[i] = rot(points12[i])
    points12[i-4][1] = points12[i][1]
    points12[i+2][2] = points12[i][2]

points13 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]-(0.5*B + p), origin[2]-0.5*T),
            (origin[0]+0.5*L, origin[1]-0.5*B, origin[2]+0.5*T)
        )
for i in [2,3,6,7]:
    points13[i] = rot(points13[i])
    points13[i-2][2] = points13[i][2]

points14 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]+0.5*B, origin[2]-0.5*T),
            (origin[0]+0.5*L, origin[1]+(0.5*B + p), origin[2]+0.5*T)
        )
for i in [0,1,4,5]:
    points14[i] = rot(points14[i])
    points14[i+2][2] = points14[i][2]

points15 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]-(0.5*B + p), origin[2]+0.5*T),
            (origin[0]+0.5*L, origin[1]-0.5*B, origin[2]+(0.5*T+p))
        )
for i in [2,3]:
    points15[i] = rot(points15[i])
    points15[i+4][1] = points15[i][1]
    points15[i-2][2] = points15[i][2]

points16 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]-0.5*B, origin[2]+0.5*T),
            (origin[0]+0.5*L, origin[1]+0.5*B, origin[2]+(0.5*T+p))
        )
for i in [0,1,2,3]:
    points16[i] = rot(points16[i])
    points16[i+4][1] = points16[i][1]

points17 = BlockMesh.boundingBox(
            (origin[0]-0.5*L, origin[1]+0.5*B, origin[2]+0.5*T),
            (origin[0]+0.5*L, origin[1]+(0.5*B + p), origin[2]+(0.5*T+p))
        )
for i in [0,1]:
    points17[i] = rot(points17[i])
    points17[i+2][2] = points17[i][2]
    points17[i+4][1] = points17[i][1]

# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------

points18 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]-(0.5*B + p), origin[2]-(0.5*T + p)),
            (origin[0]+0.5*L+p, origin[1]-0.5*B, origin[2]-0.5*T)
        )
for i in [6,7]:
    points18[i] = rot(points18[i])
    points18[i-4][1] = points18[i][1]
    points18[i-2][2] = points18[i][2]

points19 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]-0.5*B, origin[2]-(0.5*T + p)),
            (origin[0]+0.5*L+p, origin[1]+0.5*B, origin[2]-0.5*T)
        )
for i in [4,5,6,7]:
    points19[i] = rot(points19[i])
    points19[i-4][1] = points19[i][1]

points20 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]+0.5*B, origin[2]-(0.5*T + p)),
            (origin[0]+0.5*L+p, origin[1]+(0.5*B + p), origin[2]-0.5*T)
        )
for i in [4,5]:
    points20[i] = rot(points20[i])
    points20[i-4][1] = points20[i][1]
    points20[i+2][2] = points20[i][2]

points21 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]-(0.5*B + p), origin[2]-0.5*T),
            (origin[0]+0.5*L+p, origin[1]-0.5*B, origin[2]+0.5*T)
        )
for i in [2,3,6,7]:
    points21[i] = rot(points21[i])
    points21[i-2][2] = points21[i][2]

points22 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]-0.5*B, origin[2]-0.5*T),
            (origin[0]+0.5*L+p, origin[1]+0.5*B, origin[2]+0.5*T)
        )
for i in range(0,8):
    points22[i] = rot(points22[i])

points23 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]+0.5*B, origin[2]-0.5*T),
            (origin[0]+0.5*L+p, origin[1]+(0.5*B + p), origin[2]+0.5*T)
        )
for i in [0,1,4,5]:
    points23[i] = rot(points23[i])
    points23[i+2][2] = points23[i][2]

points24 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]-(0.5*B + p), origin[2]+0.5*T),
            (origin[0]+0.5*L+p, origin[1]-0.5*B, origin[2]+(0.5*T+p))
        )
for i in [2,3]:
    points24[i] = rot(points24[i])
    points24[i+4][1] = points24[i][1]
    points24[i-2][2] = points24[i][2]

points25 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]-0.5*B, origin[2]+0.5*T),
            (origin[0]+0.5*L+p, origin[1]+0.5*B, origin[2]+(0.5*T+p))
        )
for i in [0,1,2,3]:
    points25[i] = rot(points25[i])
    points25[i+4][1] = points25[i][1]

points26 = BlockMesh.boundingBox(
            (origin[0]+0.5*L, origin[1]+0.5*B, origin[2]+0.5*T),
            (origin[0]+0.5*L+p, origin[1]+(0.5*B + p), origin[2]+(0.5*T+p))
        )
for i in [0,1]:
    points26[i] = rot(points26[i])
    points26[i+2][2] = points26[i][2]
    points26[i+4][1] = points26[i][1]


blocks = []

for i in range(1,27):
    blocks.append(BlockMesh.block(globals()["points%i" %i], nodes=[nCellsX, nCellsY, nCellsZ], gradings=[1,1,1]))

blocks[0].adjustGrading(blocks[3],2)
blocks[6].adjustGrading(blocks[3],2)
blocks[0].adjustGrading(blocks[1],1)
blocks[2].adjustGrading(blocks[1],1)
blocks[0].adjustGrading(blocks[9],0)
blocks[17].adjustGrading(blocks[9],0)


hull = BlockMesh.patch("HULL", [
                        blocks[4].faces[1],
                        blocks[21].faces[0],
                        blocks[12].faces[3],
                        blocks[13].faces[2],
                        blocks[10].faces[5],
                        blocks[15].faces[4]
                        ], type='wall')
xmin = BlockMesh.patch("XMIN", [blocks[i].faces[0] for i in range(0,9)])
xmax = BlockMesh.patch("XMAX", [blocks[i].faces[1] for i in range(17,26)])
ymin = BlockMesh.patch("YMIN", [blocks[i].faces[2] for i in [0,3,6,9,12,14,17,20,23]])
ymax = BlockMesh.patch("YMAX", [blocks[i].faces[3] for i in [2,5,8,11,13,16,19,22,25]])
zmin = BlockMesh.patch("ZMIN", [blocks[i].faces[4] for i in [0,1,2,9,10,11,17,18,19]])
zmax = BlockMesh.patch("ZMAX", [blocks[i].faces[5] for i in [6,7,8,14,15,16,23,24,25]])

mesh = BlockMesh.blockMesh(case)
mesh.addBlocks(blocks)
mesh.addPatches([hull, xmin, xmax, ymin, ymax, zmin, zmax])
mesh.write()
