from bs4 import BeautifulSoup

xml_file = "ex_1_invalid.xml"
with open(xml_file, "r", encoding="utf-8") as file:
    xml_content = file.read()
soup = BeautifulSoup(xml_content, "xml")


def validate_xml(soup):
    errors = []
    # Check for the presence of the <component> element and its attributes
    component = soup.migration.component
    if not component:
        errors.append("The <component> element is missing inside <migration>.")
    else:
        if not component.get("type"):
            errors.append(
                "The <component> element is missing the required attribute 'type'.")
        if not component.get("context"):
            errors.append(
                "The <component> element is missing the required attribute 'context'.")

    # Check the structure inside <role>
    role = component.role if component else None
    if not role:
        errors.append("The <role> element is missing inside <component>.")
    else:
        # Check elements inside <rules>
        include = role.rules.include if role.rules else None
        if not include:
            errors.append("The <include> element is missing inside <rules>.")
        else:
            pattern = include.objectSet.pattern if include.objectSet else None
            if not pattern:
                errors.append(
                    "The <pattern> element is missing inside <objectSet>.")
            else:
                if not pattern.get("type"):
                    errors.append(
                        "The <pattern> element is missing the required attribute 'type'.")

    return errors


# Validation
validation_errors = validate_xml(soup)
if validation_errors:
    print("The XML file failed validation:")
    for error in validation_errors:
        print(f"- {error}")
else:
    print("The XML file passed validation.")
