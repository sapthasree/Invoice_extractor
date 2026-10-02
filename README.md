# Multimodal Invoice Extractor

A Streamlit-based multimodal AI application that uses Google Gemini to analyze invoice images and answer user queries based on the uploaded invoice.

## Overview

The Multimodal Invoice Extractor allows users to upload an invoice image and ask questions about its contents using natural language.

The application uses the Gemini 2.5 Flash multimodal model to process the uploaded invoice image along with the user's question. Gemini analyzes the visual information in the invoice and generates a response based on the provided image.

This project demonstrates how multimodal generative AI can be used for document understanding and image-based question answering.

## Features

- Upload invoice images in JPG, JPEG, or PNG format
- Preview the uploaded invoice
- Ask natural-language questions about the invoice
- Analyze invoice images using Google Gemini
- Generate responses based on the uploaded invoice
- Simple and interactive Streamlit interface

## How It Works

```text
User
 |
 | Upload Invoice Image
 v
Streamlit Application
 |
 | Convert Image to Bytes
 v
Gemini 2.5 Flash
 |
 | Analyze Image + User Query
 v
Generated Response
 |
 v
Display Answer in Streamlit
```

### Workflow

1. The user enters a question in the input field.
2. The user uploads an invoice image.
3. The application reads the uploaded image and converts it into byte data.
4. The image data is passed to the Gemini 2.5 Flash multimodal model.
5. Gemini analyzes the invoice image along with the user's question.
6. The generated response is displayed in the Streamlit application.

## Example Queries

After uploading an invoice, users can ask questions such as:

```text
What is the invoice number?

What is the total amount?

What is the invoice date?

Who is the seller?

Who is the customer?

What items are listed in the invoice?

What is the price of each item?

What is the total tax?

What is the billing address?
```

The model generates answers based on the information visible in the uploaded invoice.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Gemini 2.5 Flash
- Google Generative AI Python SDK
- python-dotenv
- Pillow

## Project Structure

```text
Invoice_extractor/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### `app.py`

Contains the complete Streamlit application, including:

- Streamlit user interface
- Invoice image upload
- Image processing
- Gemini model configuration
- User query handling
- Response generation
- Display of the generated response

### `requirements.txt`

Contains the Python packages required to run the application.

### `.env`

Stores the Google Gemini API key used by the application.

Example:

```env
GOOGLE_API_KEY=your_google_api_key
```

The `.env` file should not be uploaded to GitHub.

### `.gitignore`

Used to prevent sensitive files such as `.env` and unnecessary local files from being committed to the repository.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sapthasree/Invoice_extractor.git
```

### 2. Navigate to the Project Directory

```bash
cd Invoice_extractor
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## API Key Configuration

The application requires a Google Gemini API key.

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key
```

The application loads the API key using `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()
```

The key is then used to configure the Gemini API:

```python
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
```

Do not expose or commit your API key to the repository.

## Running the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, open the Streamlit URL displayed in the terminal.

## Application Components

### Gemini Model

The project uses:

```python
model = genai.GenerativeModel('gemini-2.5-flash')
```

Gemini 2.5 Flash is used because it supports multimodal input, allowing the application to provide an invoice image together with a text query.

### Image Processing

The uploaded invoice is converted into byte data before being sent to Gemini:

```python
byte_data = uploaded_file.getvalue()
```

The application then creates an image object containing the MIME type and image data:

```python
img_parts = [
    {
        "mime_type": uploaded_file.type,
        "data": byte_data
    }
]
```

### Multimodal Question Answering

The application sends the invoice image and prompt to Gemini:

```python
response = model.generate_content([input, image[0], prompt])
```

This allows the model to consider both the invoice image and the user's query when generating the response.

## System Prompt

The application provides Gemini with the following instruction:

```text
You are an expert in understanding invoices. We will upload an image as invoice
and you'll have to answer any questions based on the uploaded invoice image.
```

This guides the model to focus its response on the information available in the uploaded invoice.

## Limitations

This project currently focuses on image-based invoice question answering.

Current limitations include:

- Supports invoice images rather than PDF documents
- Does not store extracted invoice information in a database
- Does not maintain conversation history
- Does not perform structured invoice data export
- Responses depend on the information visible in the uploaded image
- The application requires access to the Gemini API
- The quality of responses may depend on the image quality and invoice layout

## Future Improvements

Potential improvements include:

- Support for PDF invoices
- Structured extraction of invoice fields
- Export extracted data to CSV or Excel
- Conversation history
- Multiple invoice comparison
- Batch invoice processing
- Invoice validation
- Improved error handling
- Support for additional document formats
- Deployment as a public web application

## Project Objective

The objective of this project is to explore the practical use of multimodal generative AI for understanding real-world business documents.

By combining Streamlit with Google's Gemini multimodal model, the application provides a simple interface where users can upload an invoice and interact with its contents using natural-language questions.

## Author

**Sapthasree N K**

GitHub: https://github.com/sapthasree

https://github.com/sapthasree/Invoice_extractor
