INPUT_CODE_DELIMETER = '# ---end----'
MD_CONTENT_DELIMETER = '--------------------------------'

def main(solution, md):
    content = read_data(solution)
    old_md_content = read_data(md)
    result = convert_data(content, old_md_content)
    write_data(md, result)


def read_data(file_name):
    start_file = open(file_name, encoding='utf-8')
    content = start_file.read()
    start_file.close()
    return content

def convert_data(data, old_md_content):
    titles, source_code = data.split(INPUT_CODE_DELIMETER)
    title, description = prepare_md_titles(titles)
    new_md_code = prepare_md_format(title, description, source_code)
    new_md_link = prepare_md_link(title)
    return prepare_new_md_content(new_md_link, new_md_code, old_md_content)


def write_data(file_name, data):
    file = open(file_name, 'w', encoding='utf-8')
    file.write(data)
    file.close()


def prepare_md_titles(data):
    title = None
    description = None
    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description '):
            description = line.replace('# description ', '')
    return title, description


def prepare_md_format(title, description, source_code):
    template = """## {}

{}

```python
{}
```"""

    return template.format(title, description, source_code.lstrip())


def prepare_md_link(title):
    md_link = '-'.join(title.lower().split())
    template = '+ [{}](#{})'
    return template.format(title, md_link)


def prepare_new_md_content(new_md_link, new_md_code, old_md_content):
    if MD_CONTENT_DELIMETER not in old_md_content:
        result_md = f"{new_md_link}\n{MD_CONTENT_DELIMETER}\n\n{new_md_code}"
    else:
        old_md_link, old_md_code = old_md_content.split(MD_CONTENT_DELIMETER)
        result_md = f"{old_md_link}{new_md_link}\n{MD_CONTENT_DELIMETER}{old_md_code}\n\n{new_md_code}"
    return result_md


if __name__ == "__main__":
    main("python-course/task_1/input.py", 'python-course/task_1/out.md')

