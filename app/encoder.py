import binascii

class Encoder:
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one
    
    def encode(self, text):
        binary = bin(int(binascii.hexlify(bytes(text, 'utf8')), 16))
        
        encoded_array = [ ]
        for i in range(len(binary)):
            if binary[i] == '0':
                encoded_array.append(self.zero)
            elif binary[i] == '1':
                encoded_array.append(self.one)

        encoded = ''

        for key in encoded_array:
            encoded += key + ' '

        return encoded