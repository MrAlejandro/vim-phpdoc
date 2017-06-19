import vim
import re

def is_valid_php_file(filepath):
    return  str(filepath)[-4:] == '.php'

def get_argument_type(type_hint, default_value):
    arg_type = 'mixed' # for null and if no value at all

    if type_hint:
        if type_hint.lower() == 'array': # type hint array
            arg_type = 'array'
        else: # use specified class name as type
            arg_type = type_hint
    elif default_value:
        if "'" in default_value or '"' in default_value: # string passed as default value
            arg_type = 'string'
        elif default_value.lower() != 'null': # if not null then integer
            arg_type = 'integer'

    return arg_type

def get_doc_data(definition_line):
    args_data = []
    result = re.search(
        'function (?P<name>.+?)\((?P<args>.+?)?\)$',
        definition_line
    )

    args = result.group('args')

    if args:
        args = [arg.strip() for arg in args.split(',')]

        for arg in args:
            result = re.search(
                '(?P<type_hint>.+)?(?P<arg_name>\$.+?)(?P<def_val>\s?=\s?.+)?$',
                arg
            )

            type_hint = result.group('type_hint')
            arg_name = result.group('arg_name')
            default_value = result.group('def_val')

            if default_value:
                default_value = default_value.strip(' =')

            if type_hint:
                type_hint = type_hint.strip()

            args_data.append(
                {
                    'arg_name':arg_name.strip(),
                    'type':get_argument_type(type_hint, default_value)
                }
            )

    return args_data

def get_leading_spaces_qty(definition_line):
    return len(definition_line) - len(definition_line.lstrip())

def generate_doc_comment(doc_data, indent):
    comment = ''
    lines = [' ' * indent + '/**']

    for item in doc_data:
        lines.append(' ' * indent + ' * @param %s %s ' % (item['type'], item['arg_name']))

    lines.append(' ' * indent + ' */\n')

    return '\n'.join(lines)

try:
    active_buffer = vim.current.buffer
    active_buffer_name = active_buffer.name

    if is_valid_php_file(active_buffer_name):
        current_line = int(vim.current.range.start)

        with open(active_buffer_name, 'r') as handler:
            lines = handler.readlines()

            if len(lines) > current_line:
                definition_line = lines[current_line]
                doc_data = get_doc_data(definition_line)
                indent = get_leading_spaces_qty(definition_line)
                doc_comment = generate_doc_comment(doc_data, indent)

                if doc_comment:
                    with open(active_buffer_name + '.bak', 'w') as tmp_file:
                        i = 0

                        for line in lines:
                            if i == current_line:
                                tmp_file.write(doc_comment)

                            tmp_file.write(line)
                            i += 1

                        tmp_file.close()

            handler.close()
except:
    print('Error')
