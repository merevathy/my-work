# Face Detection System

This project implements a real-time face detection system using Python and OpenCV.

## Requirements

- Python 3.10+
- OpenCV (`opencv-python`)

## Setup

1.  Create a virtual environment:
    ```bash
    python -m venv my_face_det_env
    ```
2.  Activate the environment:
    - Windows: `my_face_det_env\Scripts\activate`
    - Mac/Linux: `source my_face_det_env/bin/activate`
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script:

```bash
python face_det.py
```

- A window will open showing the webcam feed.
- Detected faces will have a blue bounding box.
- The number of detected faces will be shown in green at the top right.
- Press `Esc` to exit.
