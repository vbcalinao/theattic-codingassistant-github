# Causal Language Model: Coding Assistant

This is an imported repository from https://huggingface.co/spaces/vbcalinao/theattic-clm-codingassistant

# Project Documentation

## Project Overview

This project is a simple FastAPI application that provides an API endpoint to make POST requests to a specified URL with a specified prompt. The application makes a POST request to the provided URL with the provided prompt and returns the response.

## Usage

You can interact with the API using FastAPI's automatic interactive API documentation at `https://vbcalinao-theattic-clm-codingassistant.hf.space/docs`.

To make a POST request to the `/api/generate` endpoint:

1. Click on the `/generate` endpoint in the API documentation.
2. Click the "Try it out" button.
3. Enter the `input_prompt` data in the appropriate fields.
4. Click the "Execute" button.

The API will make a POST request to the provided URL with the provided prompt and return the response.

## Responses (Example)

### Curl

```
curl -X 'POST' \
  'https://vbcalinao-theattic-clm-codingassistant.hf.space/api/generate?input_prompt=How%20to%20generate%20sinewave%20using%20matplotlib%3F' \
  -H 'accept: application/json' \
  -d ''
```
### Request URL
```
https://vbcalinao-theattic-clm-codingassistant.hf.space/api/generate?input_prompt=How%20to%20generate%20sinewave%20using%20matplotlib%3F
```


#### Request Body

```
{
  "text": "Here is an example of how to generate a sine wave using Matplotlib:\n```python\nimport matplotlib.pyplot as plt\n\n# Specify the number of cycles and amplitude of the sine wave\nnum_cycles = 10\namplitude = 5\n\n# Generate the sine wave\nx = np.linspace(0, 2 * np.pi, num_cycles * 1000, endpoint=False)\ny = amplitude * np.sin(x)\n\n# Plot the sine wave\nplt.plot(x, y)\nplt.xlabel('Angle')\nplt.ylabel('Amplitude')\nplt.title('Sine Wave')\nplt.show()\n```\n\nThis code uses the `matplotlib.pyplot` module to create a sine graph. The `num_cycles` and `amplitude` variables determine the number of cycles and the maximum height of the sine wave, respectively. The `np.linspace` function creates an array `x` of num_cycles * 1000 equally spaced values between 0 and 2*pi. The `np.sin` function generates the sine wave values for `y` based on the values of `x`. It then uses the `plt.plot` function to create a line plot of the sine wave. \n\nFinally, add labels and a title to the plot and display it using the `plt.show` function. You can customize the number of cycles, amplitude, and other parameters according to your requirements."
}
```

#### Response headers
```
 access-control-allow-credentials: true 
 access-control-allow-origin: * 
 content-length: 1144 
 content-type: application/json 
 date: Sun,24 Mar 2024 17:44:00 GMT 
 link: <https://huggingface.co/spaces/vbcalinao/theattic-clm-codingassistant>;rel="canonical" 
 server: uvicorn 
 x-proxied-host: http://10.19.34.113 
 x-proxied-path: /api/generate?input_prompt=How%20to%20generate%20sinewave%20using%20matplotlib%3F 
 x-request-id: bLQiCD
```

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
