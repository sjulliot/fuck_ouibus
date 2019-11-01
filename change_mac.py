from os import system
from random import choice


def form_mac(v):
    return ':'.join(map(str, v))


def set_mac(new_address):
    system('sudo ifconfig wlo1 down')
    res = system('sudo ifconfig wlo1 hw ether {} 2> /dev/null'.format(new_address))
    system('sudo ifconfig wlo1 up')
    return res


def enjoy_internet():
    '''
    This function is intended to fuck Ouibus.
    '''
    random_values = [choice(range(10, 100)) for _ in range(6)]
    random_address = form_mac(random_values)
    return set_mac(random_address)


if __name__ == '__main__':
    res = enjoy_internet()
    while res:
        res = enjoy_internet()
    system('sudo service network-manager restart')
