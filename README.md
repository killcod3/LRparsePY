# LR Parse Python

The `lr` function is a versatile string parsing utility designed to extract substrings from a given input based on left and right delimiters. This Python function is inspired by a similar utility in C# and offers flexibility with its recursive and regular expression parsing capabilities.

## Features

- **Flexible Delimiters**: Specify any string as the left or right delimiter to frame the substring you wish to extract.
- **Recursive Parsing**: Enable recursive parsing to extract multiple substrings within the nested delimiters.
- **Regular Expression Support**: Leverage regular expressions for advanced parsing scenarios, allowing for pattern-based delimiter matching.
- **Error Handling**: Gracefully handles errors and edge cases, ensuring stability across a wide range of inputs.

## Usage

```python
def lr(input_str, left, right, recursive=False, use_regex=False):
    """
    Parses substrings from an input string based on left and right delimiters.

    :param input_str: The input string to parse.
    :param left: The left delimiter.
    :param right: The right delimiter.
    :param recursive: Enable recursive parsing within nested delimiters (default is False).
    :param use_regex: Use regular expressions for delimiters (default is False).
    :return: A list of extracted substrings.
    """
```

## Parameters
* input_str (str): The string to parse.
* left (str): The left delimiter. If empty, parsing starts from the beginning of the string.
* right (str): The right delimiter. If empty, parsing goes until the end of the string.
* recursive (bool): If True, performs recursive parsing within nested delimiters. Defaults to False.
* use_regex (bool): If True, treats left and right as regular expressions. Defaults to False.

## Returns
* list: A list of strings extracted from input_str based on the specified delimiters.

## Examples
Extracting a simple substring:

```python
result = lr("Hello [World]!", "[", "]")
# result: ['World']

```
Using recursive parsing:

```python
result = lr("Start <div>inner <span>text</span> more</div> end", "<div>", "</div>", recursive=True)
# result: ['inner <span>text</span> more']

```

## Dependencies
Python's re module for regular expression support.

##Notes
Ensure that the build_lr_pattern function is implemented and accessible within your project if you intend to use regular expressions.
