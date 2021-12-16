from aocutils import get_raw

from dataclasses import dataclass
from math import prod

OPERATORS = [sum, prod, min, max, None, lambda v: int(v[0] > v[1]), lambda v: int(v[0] < v[1]), lambda v: int(v[0] == v[1])]

def problem1():
    packet = parse_packets()
    return packet.sum_versions()

def problem2():
    packet = parse_packets()
    return packet.eval()

@dataclass
class Bits:
    bits: str

    def pop(self, num_bits):
        bits = self.bits[:num_bits]
        self.bits = self.bits[num_bits:]
        return bits

    def __bool__(self):
        return len(self.bits) > 0

@dataclass
class Packet:
    version: int
    packet_type: int
    value: int
    packets: list

    def sum_versions(self):
        if self.packet_type == 4:
            return self.version
        return sum(packet.sum_versions() for packet in self.packets) + self.version
    
    def eval(self):
        if self.packet_type == 4:
            return self.value
        else:
            return OPERATORS[self.packet_type]([packet.eval() for packet in self.packets])

def parse_packets():
    bits = Bits(''.join([f'{int(h, 16):0>4b}' for h in get_raw(16).strip()]))
    return get_packet(bits)

def get_packet(bits):
    version = int(bits.pop(3), 2)
    type = int(bits.pop(3), 2)
    if type == 4:
        return Packet(version, type, get_literal(bits), [])
    else:
        return Packet(version, type, 0, get_operator(bits))

def get_literal(bits):
    value = ''
    while bits.pop(1) == '1':
        value += bits.pop(4)
    value += bits.pop(4)
    return int(value, 2)

def get_operator(bits):
    if bits.pop(1) == '0':
        inner_bits = Bits(bits.pop(int(bits.pop(15), 2)))
        packets = []
        while inner_bits:
            packets.append(get_packet(inner_bits))
    else:
        num_packets = int(bits.pop(11), 2)
        packets = [get_packet(bits) for _ in range(num_packets)]
    return packets