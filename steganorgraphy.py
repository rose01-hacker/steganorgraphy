import cv2
import os
import string
import hashlib

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def embed_message(image, msg):
    m = 0
    n = 0
    z = 0
    for i in range(len(msg)):
        image[n, m, z] = ord(msg[i])
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3
    return image

def extract_message(image, msg_length):
    message = ""
    n = 0
    m = 0
    z = 0
    for i in range(msg_length):
        message += chr(image[n, m, z])
        n = (n + 1) % image.shape[0]
        m = (m + 1) % image.shape[1]
        z = (z + 1) % 3
    return message

def main():
    # Read the image
    image_path = "c:\\Users\\Administrator\\Downloads\\photo_1.jpg"
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image.")
        return

    # Get the secret message and password from the user
    msg = input("Enter the secret message: ")
    password = input("Enter the password: ")

    # Check if the message is too long for the image
    if len(msg) > image.shape[0] * image.shape[1] * 3:
        print("Error: The message is too long for the image.")
        return

    # Embed the message in the image
    image = embed_message(image, msg)

    # Save the image with the secret message
    cv2.imwrite("encryptedImage.jpg", image)

    # Open the encrypted image
    os.system("start encryptedImage.jpg")

    # Get the password for decryption
    pas = input("Enter the password for decryption: ")

    # Decrypt the message if the password is correct
    if get_hash(password) == get_hash(pas):
        message = extract_message(image, len(msg))
        print("Decrypted message:", message)
    else:
        print("You are not authorized")

if __name__ == "__main__":
    main()
