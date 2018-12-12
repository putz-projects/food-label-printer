from PIL import Image, ImageDraw, ImageFont
import datetime
import qrcode
import time
import subprocess

def print_label(kerberos, date):
    """Prints a food label given a kerberos string and a datetime object.
    """

    # Initialize image and fonts.
    img = Image.new('RGB', (500, 200), color='white')
    font_regular = ImageFont.truetype('Roboto-Regular.ttf', 46)
    font_light = ImageFont.truetype('Roboto-Regular.ttf', 36)
    font_italic = ImageFont.truetype('Roboto-Regular.ttf', 24)

    # Draw the text.
    draw = ImageDraw.Draw(img)
    draw.text((30, 20), kerberos, font=font_regular, fill=(0, 0, 0))
    draw.text((30, 90), date.strftime("%m/%d/%Y").lower(), font=font_light, fill=(0, 0, 0))
    draw.text((30, 140), date.strftime("%I:%M %p").lower(), font=font_italic, fill=(0, 0, 0))

    # Build a QR code.
    qr = qrcode.QRCode(box_size = 5, border=1)
    qr.add_data('\n'.join([kerberos, str(int(time.time()))]))
    qr.make(fit=True)
    qr = qr.make_image(fill_color='black', back_color='white')
    draw.bitmap((330, 30), qr, fill='black')
    
    # Render the image out.
    img.save('label.png')

    # Print it!
    subprocess.call(["lp", "-o", "fit-to-page", "-o", "orientation-requested=6", "label.png"])

if __name__ == '__main__':
    print_label("shreyask", datetime.datetime.now())
