from json_converter import Converter
from json_converter_raw import ConverterRaw

def read_data(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content

def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

def main():
    data = read_data("python-course/task_2/input.csv")
    manual_converter = ConverterRaw(data)
    write_data("output1.json", manual_converter.to_json())

    import_converter = Converter(data)
    write_data("output2.json", import_converter.to_json())

if __name__ == "__main__":
    main()