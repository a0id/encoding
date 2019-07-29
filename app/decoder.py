class Decoder:
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one

    def decode(self, text):
        parsed_text = text.split(' ')

        binary = ''
        for key in parsed_text:
            if key == self.zero:
                binary += '0'
            elif key == self.one:
                binary += '1'

        decoded = bytes(binary).encode('ascii')
        return decoded