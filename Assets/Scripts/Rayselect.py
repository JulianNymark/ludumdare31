import bge


def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner

    sens = cont.sensors['Ray']
    actu = cont.actuators['myActuator']

main()
