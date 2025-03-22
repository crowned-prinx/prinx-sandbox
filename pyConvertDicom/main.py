from utils.functions import convert_dcm


inputdir = '/Users/crownedprince/Documents/Kumamoto University/ISIS-LAB/dcm files/samples/'
outdir = '/Users/crownedprince/Documents/Kumamoto University/ISIS-LAB/dcm files/samples/images/'

def main():
    convert_dcm(inputdir, outdir, format="PNG")

if __name__ == "__main__":
    main()