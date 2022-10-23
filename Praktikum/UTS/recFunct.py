import pandas as pd
gpuData = pd.read_csv("gpuData.csv")


gpuDedicated = gpuData.copy().loc[gpuData['Integrated']=='No']

def filters(cat, x):
    # copy parameter category yang di filter ke variable output
    output = gpuDedicated[(gpuDedicated[cat]>x)].copy().head(10)
    print(output[["Name", cat]])

def gpuRec(x):
    # VRAM > 1GB
    if x == 1:
        filters("Memory(MB)", 1024)
    # VRAM > 4GB
    elif x == 2:
        filters("Memory(MB)", 4096)
    # Pixel Rate > 120 GPixel/s
    elif x == 3:
        filters("Pixel_Rate(GPixel/s)", 120)
    # VRAM > 3GB
    elif x == 4:
        filters("Memory(MB)", 3072)
    # VRAM > 2GB
    elif x == 5:
        filters("Memory(MB)", 2048)
    # VRAM > 1.5GB
    elif x == 6:
        filters("Memory(MB)", 1536)    
    # Pixel Rate > 100 GPixel/s
    elif x == 7:
        filters("Texture_Rate(GTexel/s)", 100)
