# Article Information Extractor

This Python script extracts title, abstract, and keywords from a given text.

## Description

The script provides functions to extract article information such as title, abstract, and keywords from a text input. It specifically looks for sections labeled "ABSTRACT" and "KEYWORDS" to extract the relevant information.

## Functions

### `extract_article_info(text)`

This function takes a text input and extracts the title, abstract, and keywords from it.

#### Parameters

- `text`: The text from which to extract the information.

#### Returns

- `title`: The title of the article.
- `abstract`: The abstract of the article.
- `keywords`: The keywords associated with the article.

### `generate_article_html(title, abstract, keywords)`

This function generates an HTML representation of the article information provided.

#### Parameters

- `title`: The title of the article.
- `abstract`: The abstract of the article.
- `keywords`: The keywords associated with the article.

#### Returns

- `html_output`: HTML representation of the article information.

## Example Usage

```python
text = """
# Insert your article text here
"""

title, abstract, keywords = extract_article_info(text)

# Print the extracted information
print("Title:", title)
print("Abstract:", abstract)
print("Keywords:", keywords)

# Example usage to generate HTML representation
html_output = generate_article_html(title, abstract, keywords)
print(html_output)
