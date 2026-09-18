import qrcode

def generate_qr():
    # url
    url = input("Please enter URL: ")
    
    # create qr
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        
        # add url to qr
    qr.add_data(url)
    qr.make(fit=True)
        
        # create image of qr
    img = qr.make_image(fill_color="black",back_color="white")
        
        # save img of qr
    filename = "qrcode.png"
    img.save(filename)
        
        # print
    print(f"QRCode is generated as filename {filename}")
        
    # run function
if __name__ == "__main__":
    generate_qr()