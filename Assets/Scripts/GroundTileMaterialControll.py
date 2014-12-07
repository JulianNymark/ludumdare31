import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    statusSensor = cont.sensors['TileStatusSensor']

    tileStatus = statusSensor.value

    print(own.meshes.materials)
    
    if tileStatus == 0:
        own.meshes[0].materials[0] = "MAGround"
    

main()
