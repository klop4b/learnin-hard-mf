



with socketserver.TCP((", PORT"), MyHandler) as httpd:
    print("it works")
    httpd.serve_forever()