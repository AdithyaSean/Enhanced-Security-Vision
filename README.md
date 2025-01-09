Here's the updated README with the complete installation and usage instructions:

### README.md

# Enhanced Security Vision

Enhanced Security Vision is a Python project that utilizes computer vision techniques to detect changes in intensity and faces in images captured from a webcam. It also enhances the detected faces using various image processing techniques like contrast enhancement and sharpening.

## Features

- Real-time webcam monitoring
- Intensity change detection
- Face detection and segmentation
- Image enhancement with night vision capabilities
- Automatic saving of original and enhanced images

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- A working webcam
- Git (for cloning the repository)

## Installation

1. Clone the repository:
```sh
git clone https://github.com/AdithyaSean/Enhanced-Security-Vision.git
cd Enhanced-Security-Vision
```

2. Create and activate a virtual environment:
```sh
# On Linux/macOS
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

## Project Structure

```
Enhanced-Security-Vision/
├── src/
│   ├── main.py          # Main script for webcam monitoring
│   ├── enhance.py       # Image enhancement functions
│   ├── segment.py       # Face detection and segmentation
│   └── night_vision.py  # Night vision enhancement
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Usage

1. Make sure your webcam is connected and working.

2. Run the main script:
```sh
python src/main.py
```

3. The program will:
   - Start your webcam
   - Monitor for intensity changes
   - Detect and enhance faces when changes are detected
   - Save processed images automatically

4. Press 'q' to quit the program

## Output Files

The program creates the following directories for storing processed images:
- `original/`: Contains original captured frames
- `segmented/`: Contains detected face segments
- `enhanced/`: Contains enhanced face images

## Troubleshooting

1. If the webcam doesn't start:
   - Check if another application is using the webcam
   - Verify webcam permissions
   - Try reconnecting the webcam

2. If face detection isn't working:
   - Ensure proper lighting conditions
   - Make sure faces are clearly visible
   - Try adjusting your distance from the camera

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
