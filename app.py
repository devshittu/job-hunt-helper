import argparse
import csv


def load_templates_from_csv(csv_file):
    templates = {}
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            templates[row['Title']] = row['Message']
    return templates


def substitute_variables(template, variables):
    for variable, value in variables.items():
        placeholder = f"{{{{{variable}}}}}"
        template = template.replace(placeholder, str(value))
    return template


def main():
    """Main function to substitute variables in the email template."""
    parser = argparse.ArgumentParser(description='Email template variable substitution')
    parser.add_argument('--position', required=True, help='Position title')
    parser.add_argument('--company', required=True, help='Company name')
    parser.add_argument('--last-name', help='Contact\'s last name')
    parser.add_argument('--pronoun', choices=['Mr.', 'Ms.'], help='Contact\'s pronoun')
    parser.add_argument('--template', help='Template title')

    args = parser.parse_args()

    salutation = ''
    if args.last_name:
        salutation = f'Dear {args.last_name}:'
    elif args.pronoun:
        pronoun = args.pronoun if args.pronoun == 'Mr.' else 'Ms.'
        salutation = f'Dear {pronoun} {args.last_name}:'
    else:
        salutation = 'Dear Hiring Manager:'

    variables = {
        'PositionTitle': args.position,
        'CompanyName': args.company,
        'Salutation': salutation
    }

    templates = load_templates_from_csv('templates.csv')

    if args.template not in templates:
        print(f"Error: Template '{args.template}' not found.")
        return

    template = templates[args.template]

    substituted_template = substitute_variables(template, variables)
    print(substituted_template)


if __name__ == '__main__':
    main()
