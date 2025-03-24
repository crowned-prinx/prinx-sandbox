from utils.functions import compress


input_path = "/Users/crownedprince/Documents/my projects/sandbox/python-projects/FileHandling/projects/test-2"
output_path = "/Users/crownedprince/Documents/my projects/sandbox/python-projects/FileHandling/projects/test-2-out"
filename = "ompressed-v1"

def main():
    compress(input_path, output_path, filename)

if __name__ == "__main__":
    main()