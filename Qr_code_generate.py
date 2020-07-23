import qrcode

class file:
    text = ""
    image = ""
    fileName = ""
    qr_code = ""
    qr_code_directory = "Qr_code_directory"
    
    """
        instantiate class text
        
        parameters:- takes only the text text, supplied from the user interface
        
    """
    def __init__(self, text, fileName):
        self.text = text
        self.fileName = fileName
    
    """
        function generate_code() takes care of:
            -generating our qr code
            -saving our image
        
    """
    def generate_code(self):
        self.qr_code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr_code.add_data(self.text, optimize=0)
        self.qr_code.make(fit=True)

        self.image = self.qr_code.make_image(fill_color="black", back_color="white")
        
        self.image.save(self.qr_code_directory + '/'+ self.fileName + '.png')
    
    def load_qrcode_image(self):
        qrcode_image = self.fileName + '.png'
        return qrcode_image
    
    
    
    
    
    
    
    