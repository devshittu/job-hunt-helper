# Cover Letter Template Variable Substitution

This script allows you to substitute variables in an email template to generate personalized email messages. It can be useful when sending out bulk emails or automating the process of creating customized email content.

## Usage

1. Ensure that you have Python installed on your system (Python 3.6 or higher).
2. Install the required dependencies by running the following command:
```bash
$ pip install argparse
```
3. Prepare the CSV file containing the email templates. Each template should be defined with a title and a corresponding message that includes placeholders for the variables to be substituted.
4. Run the script with the necessary command-line arguments to specify the template and the values for the variables.

Example usage:
```bash
$ python email_template_substitution.py --template templates.csv --position "Full-stack Software Developer" --company "ABC Company" --last-name "Smith"
```



Available command-line arguments:
- `--template` (required): Path to the CSV file containing the email templates.
- `--position` (required): Position title for the email.
- `--company` (required): Company name for the email.
- `--last-name`: Last name of the contact (optional).
- `--pronoun`: Pronoun of the contact (optional). Valid values: "Mr." or "Ms."

5. The script will generate the personalized email message by substituting the variables in the template and display it on the console.

## CSV File Format

The CSV file should have the following format:

```csv
Title,Message
Template 1,Template 1 message...
Template 2,Template 2 message...
...
```


Each row represents a template, where:
- `Title`: A unique title for the template.
- `Message`: The email message content with placeholders for the variables enclosed in double curly braces (e.g., `{{VariableName}}`).

You can add as many templates as needed in the CSV file.

## Example

An example CSV file `templates.csv` has been provided as a starting point. You can modify it to create your own templates or add additional templates as required.

## Dependencies

This script depends on the `argparse` module, which is used for parsing command-line arguments. It can be installed using pip as mentioned in the installation steps.

## License

This project is licensed under the [MIT License](LICENSE).


Feel free to modify the template and the arguments to suit your needs.

