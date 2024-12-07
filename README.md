Here's the updated README with the complete installation and usage instructions:

### README.md

# Enhanced Security Vision

Enhanced Security Vision is a Python project that utilizes computer vision techniques to detect changes in intensity and faces in images captured from a webcam. It also enhances the detected faces using various image processing techniques.

## Requirements

To run this project, you need to have the following dependencies installed:

- `opencv-python`
- `numpy`

You can install these dependencies using the provided `requirements.txt` file.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/AdithyaSean/Enhanced-Security-Vision.git
cd Enhanced-Security-Vision
```

2. Create a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

## Usage

To run the main script, execute:

```sh
python src/main.py
```

This will start the webcam, detect changes in intensity, and process the images accordingly.

## Project Structure

- `src/main.py`: Main script to capture images from the webcam and process them.
- `src/segment.py`: Contains functions to detect faces and enhance them.
- `src/enhance.py`: Contains functions to enhance images.
- `src/night_vision.py`: Contains functions to apply night vision effects.

## License

This project is licensed under the MIT License.
```
