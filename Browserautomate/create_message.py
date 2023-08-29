text_path="./message_text.txt"
def create_message(uploader_name):
    with open(text_path, "r") as file:
            element_text = file.read().strip()
        # delete eveything around the name
    uploader_name = uploader_name[13:-1]
    # delte lastname
    uploader_name = uploader_name.split(' ',1)[0]
    uploader_name = uploader_name + ",\n"
    full_text = "Hi "+uploader_name + element_text
    return full_text
