def main(args):
      import pyqrcode
      text = args.get("text", "need generate QR code from texts ?, visit our qrcode app")
      code = pyqrcode.create(text)
      image_as_str = code.png_as_base64_str(scale=5)
      html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)
      html_img = '<img src=>'
      return {"headers": {'content-type': 'text/html; charset=UTF-8'}, "body": html_img}