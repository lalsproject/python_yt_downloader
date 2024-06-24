# Quart YouTube Video Info Fetcher

A simple web application built using Quart and PyTube to fetch YouTube video information, including the title, URL of the highest resolution stream, and thumbnail URL.

## Requirements

- Python 3.7+
- Quart
- PyTube

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/quart-youtube-fetcher.git
    cd quart-youtube-fetcher
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://0.0.0.0:5000/`.

3. Use the form to input a YouTube video URL and fetch its information.

## Code Explanation

- The application uses the Quart framework to create an asynchronous web server.
- The root route (`'/'`) renders the `index.html` template.
- The `/download` route accepts POST requests with a YouTube video URL, fetches the video information using PyTube, and returns the data in JSON format.

### `fetch_video_info(video_url)`

Fetches information for a given YouTube video URL:
- `video_url`: The URL of the YouTube video.
- Returns a dictionary containing the video title, highest resolution stream URL, and thumbnail URL.

### `download()`

Handles POST requests to the `/download` route:
- Extracts the video URL from the form data.
- Calls `fetch_video_info(video_url)` to fetch the video information.
- Returns the information as a JSON response.

## Example

Here is an example of how to use the application:
1. Open the application in your web browser.
2. Enter a YouTube video URL in the input field and submit the form.
3. The application will return a JSON response with the video title, URL of the highest resolution stream, and thumbnail URL.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
