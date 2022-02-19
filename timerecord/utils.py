def handle_uploaded_file(file):
    with open("temp/image.jpg", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)