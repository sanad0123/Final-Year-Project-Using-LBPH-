import numpy as np
import lbph_algo as la



def train_classifier():
    myObj = la.LBPHFaceRecognizer(1,8,8,8)
    myObj.train()
    # Save the array to a .npy file
    np.save('histograms.npy', myObj.histograms)
    np.save('labels.npy', myObj.labels)