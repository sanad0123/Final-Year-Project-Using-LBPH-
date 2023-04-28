import numpy as np
import cv2
import os
from PIL import Image

def compute_lbph_histogram(img, radius, neighbors, grid_x, grid_y):
    #img = cv2.imread(img)
    # Convert the image to grayscale
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Compute the LBP image
    lbp = compute_lbp_image(img, radius, neighbors)

    # Compute the LBPH histogram
    histogram = compute_lbph_grid(lbp, grid_x, grid_y,neighbors)

    return histogram

def compute_lbph_histogramm(img, radius, neighbors, grid_x, grid_y):
    img = cv2.imread(img)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Compute the LBP image
    lbp = compute_lbp_image(gray, radius, neighbors)

    # Compute the LBPH histogram
    histogram = compute_lbph_grid(lbp, grid_x, grid_y,neighbors)

    return histogram

def compute_lbp_image(img, radius, neighbors):
    # Compute the LBP pattern for each pixel
    lbp = np.zeros_like(img)
    for i in range(radius, img.shape[0]-radius):
        for j in range(radius, img.shape[1]-radius):
            center = img[i,j]
            code = 0
            for n in range(neighbors):
                x = i + int(radius * np.cos(2*np.pi*n/neighbors))
                y = j - int(radius * np.sin(2*np.pi*n/neighbors))
                if img[x,y] > center:
                    code += 2**n
            lbp[i,j] = code

    return lbp

def compute_lbph_grid(lbp, grid_x, grid_y,neighbors):
    # Compute the LBPH histogram for each grid cell
    height, width = lbp.shape
    cell_x = int(width / grid_x)
    cell_y = int(height / grid_y)
    histogram = np.zeros(grid_x*grid_y*(2**neighbors))

    for i in range(grid_y):
        for j in range(grid_x):
            cell = lbp[i*cell_y:(i+1)*cell_y, j*cell_x:(j+1)*cell_x]
            hist, _ = np.histogram(cell, bins=2**neighbors, range=(0, 2**neighbors))
            histogram[i*grid_x*(2**neighbors) + j*(2**neighbors):i*grid_x*(2**neighbors) + (j+1)*(2**neighbors)] = hist

    return histogram

class LBPHFaceRecognizer:
    def __init__(self, radius, neighbors, grid_x, grid_y):
        self.radius = radius
        self.neighbors = neighbors
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.histograms = None
        self.labels = None

    def train(self):
        # Compute the LBPH histograms for each training image
        histograms = []
        ids = []
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir) ]
        for image in path :
            img = Image.open(image).convert('L') #Grayscale iamge
            imageNp = np.array(img,'uint8')
            cv2.imshow("Training data sets and enter e to exit",imageNp)
            cv2.waitKey(1) == 101 #value of e; enter e to exit
            histogram = compute_lbph_histogramm(image, self.radius, self.neighbors, self.grid_x, self.grid_y)
            histograms.append(histogram)
            id = int(os.path.split(image)[1].split('.')[1])
            print(id)
            ids.append(id)

        # Convert the histograms and labels to numpy arrays
        self.histograms = np.array(histograms)
        self.labels = np.array(ids)
        cv2.destroyAllWindows()

    def predict(self, img):
        # Compute the LBPH histogram for the input image
        histogram = compute_lbph_histogram(img, self.radius, self.neighbors, self.grid_x, self.grid_y)

        # Compute the L1 distance between the input histogram and each training histogram
        distances = np.sum(np.abs(self.histograms - histogram), axis=1)

        # Find the label of the training image with the smallest distance
        idx = np.argmin(distances)
        label = self.labels[idx]

        # Compute the confidence score as the inverse of the normalized distance
        max_distance = np.max(distances)
        if max_distance == 0:
            confidence = 1.0
        else:
            confidence = 1.0 - distances[idx] / max_distance

        return label, confidence

        #return label