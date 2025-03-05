from Cipher.Caesar import ALPHABAT

class CaesarCipher :
    def __init__(self):
        self.alphabat= ALPHABAT
    
    def encrypt_text(self, text : str, key : int)-> str:
        alphabet_len=len(self.alphabat)
        text = text.upper
        encrypted_text=[]
        for i in text :
            i_index= self.alphabat.index(i)
            output_index=(i_index+ key) % alphabet_len
            output_i= self.alphabat[output_index]
            encrypted_text.append(output_i)
        return "".join(encrypted_text)
    def encrypt_text(self, text : str, key : int)-> str:
        alphabet_len=len(self.alphabat)
        text = text.upper
        decrypted_text=[]
        for i in text :
            i_index= self.alphabat.index(i)
            output_index=(i_index - key) % alphabet_len
            output_i= self.alphabat[output_index]
            decrypted_text.append(output_i)
        return "".join(decrypted_text)
    

