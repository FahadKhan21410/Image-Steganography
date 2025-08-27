# Image-Steganography
A simple Python tool to embed secret text messages inside images using the Least Significant Bit (LSB) technique and extract them later.

## Features
* Embed a text message inside an image without noticeable visual change.
* Extract the hidden text message from the encoded image.
* Uses LSB encoding to store data in image pixels.
* Works with common image formats (e.g., PNG, BMP).
* Command-line interface for easy interaction.

## Dev Stack
* Python
* Pillow (PIL) Library

## Requirements
* Python 3.x
* Pillow (PIL Fork) library
Install the dependency: 
  * `pip install pillow`
* Clone repository (bash: git clone https://github.com/username/project.git) or Download as ZIP

## How It Works
* Each pixel in an image has RGB values (Red, Green, Blue).
* The script replaces the least significant bit (LSB) of these color values with bits from the message.
* When decoding, it reads these bits and reconstructs the original message.

## Project Structure
* steganography.py   # Main Python script
* README.md          # Documentation

## Note
* This implementation does not encrypt the message. Anyone with the script can extract it. 
* For better security, consider adding encryption before embedding (future enhancement).

## Demo
* https://youtu.be/NeeTGMyCRhU (How the script works)

## Disclaimer
This project is for educational purposes only. Do not use it for illegal activities.

## License
* This project is licensed under the MIT License - see the [([LICENSE](https://github.com/FahadKhan21410/Image-Steganography/blob/main/LICENSE))] file for details.



  
