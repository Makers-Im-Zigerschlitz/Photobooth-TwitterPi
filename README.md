# Raspberry Pi Twitter Photo Booth

This is a Raspberry Pi application that allows users to take photos of themselves and post them on Twitter. Before uploading the image, a logo is added to the image.

## Features
- Take pictures with the click of a button
- Preview of the image before uploading
- Option to accept or reject the picture
- Post accepted pictures on Twitter with a predefined caption

## Prerequisites
This script requires the following Python packages:
- `RPi.GPIO`
- `picamera`
- `tweepy`
- `os`
- `time`
- `show_img`
- `pin_funcs`
- `sys`

Install them with `pip install <package-name>`.

## Setup
1. Connect the Raspberry Pi camera module and the button to the GPIO ports.
2. Insert your Twitter API keys and tokens into the respective variables at the top of the script:
```python
# Consumer keys and access tokens, used for OAuth
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
```
3. Run the script.

## Usage
1. Press the connected button to take a picture.
2. The application will start a countdown shown on the display before the picture is taken.
3. Once the picture is taken, it will be displayed for review.
4. If the picture is accepted, it will be posted on Twitter with the caption "Greetings from #Glarnermesse".

## License
This project is released under the MIT license.

## Support
If you encounter any issues or require further information, please raise an issue on the project's GitHub page.

## Contributing
We welcome all contributions. Please submit a pull request or create an issue for any changes you propose.

## Authors and Acknowledgments
This project is created by [your name or team] and all contributors who submit pull requests. Special thanks to the Raspberry Pi community for the resources provided.
