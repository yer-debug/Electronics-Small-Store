from electronics import Electronics
import utils
import config

def main():
    # create object
    r1 = Electronics("Resistor", config.DEFAULT_RESISTOR)
    c1 = Electronics("Capacitor", config.DEFAULT_CAPACITOR)
    l1 = Electronics("Inductor", config.DEFAULT_INDUCTOR)
    t1 = Electronics("Transistor", config.DEFAULT_TRANSISTOR)
    ic1 = Electronics("IC", config.DEFAULT_IC)

    print("---------Components------Value------")
    components = [r1, c1, l1, t1, ic1]
    utils.list_components(components)
    print("------------------------------------")


if __name__ == "__main__":
    main()
