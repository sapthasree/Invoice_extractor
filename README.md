# Multimodal Invoice Extractor

A multimodal AI application that extracts information from invoice images and allows users to ask questions about the uploaded invoice using natural language.

## Overview

The Multimodal Invoice Extractor simplifies the process of understanding and querying information from invoices.

Users can upload an invoice image and interact with it through natural-language queries. The application processes the visual content of the invoice and generates responses based on the information available in the uploaded document.

This project demonstrates the use of multimodal AI for document understanding and question answering, with a focus on extracting meaningful information from visually structured documents such as invoices.

## Key Features

- Upload invoice images through a simple interface
- Process and understand information contained in invoice images
- Ask natural-language questions about the uploaded invoice
- Generate responses based on the contents of the invoice
- Extract information such as invoice numbers, dates, items, quantities, prices, taxes, and totals
- Provide an interactive document question-answering experience

## How It Works

```text
Upload Invoice Image
        |
        v
Image Processing
        |
        v
Multimodal AI Model
        |
        v
Understand Invoice Content
        |
        v
User Query
        |
        v
Generate Context-Based Response
```

### Workflow

1. The user uploads an invoice image.
2. The application processes the uploaded image.
3. The multimodal AI model analyzes the visual and textual information present in the invoice.
4. The user enters a question related to the invoice.
5. The application uses the invoice information to generate a relevant response.
6. The response is displayed through the application interface.

## Example Queries

After uploading an invoice, users can ask questions such as:

```text
What is the invoice number?

What is the total amount?

What is the invoice date?

Who is the vendor?

What items are included in the invoice?

What is the quantity of each item?

What is the total tax amount?

What is the price of a particular item?
```

## Technologies Used

- Python
- Streamlit
- Multimodal AI
- Image Processing
- Natural Language Processing
- Large Language Models

## Project Structure

```text
Invoice_extractor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .vscode/
```

### `app.py`

Contains the main application logic, including the user interface, invoice image handling, model interaction, and question-answering workflow.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `.gitignore`

Specifies files and directories that should not be committed to the repository.

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

## Configuration

If the application requires an API key for the multimodal AI model, create a `.env` file in the project directory and add the required credentials.

Example:

```env
API_KEY=your_api_key_here
```

Do not commit API keys or other sensitive credentials to the repository.

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser and provide an interface for uploading an invoice and asking questions about it.

## Use Cases

The application can be useful for:

- Automated invoice analysis
- Financial document processing
- Invoice information extraction
- Accounts payable workflows
- Document question answering
- Business document automation
- Reducing manual invoice review

## Project Objective

The main objective of this project is to explore how multimodal AI can be applied to real-world document processing tasks.

Invoices often contain a combination of text, tables, numbers, layouts, and visual elements. Traditional text-based approaches may not fully capture this information. This project demonstrates how multimodal AI can be used to understand invoice content and provide answers to user queries.

## Future Improvements

- Support for multiple invoice formats
- Batch invoice processing
- Structured JSON extraction
- Automatic invoice field validation
- Invoice comparison
- Export extracted information to CSV or Excel
- Support for PDF invoices
- Conversation history
- Improved handling of complex invoice layouts
- Integration with accounting and business systems

## Author

**Sapthasree N K**

GitHub: https://github.com/sapthasree

## Repository

https://github.com/sapthasree/Invoice_extractor
