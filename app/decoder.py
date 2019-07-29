import binascii

class Decoder:
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one

    def decode(self, text):
        try:
            parsed_text = text.split(' ')
    
            binary = ''
            for key in parsed_text:
                if key == self.zero:
                    binary += '0'
                elif key == self.one:
                    binary += '1'
            
            n = int(binary, 2)
            decoded = binascii.unhexlify('%x' % n)
            
            clean_decoded = str(decoded)[2:][:-1]
            
            return clean_decoded
        
        except Exception:
            return "Something didn't work"
