import numpy as np

def convolve(image: np.ndarray, kernel: np.ndarray) -> np.ndarray: 
    """
    Convolve an image with a kernel assuming zero-padding of the image to handle the borders
        :param image: the image (either greyscale shape=(rows,cols) or colour shape=(rows,cols,channels))
        :type numpy.ndarray
        :param kernel: the kernel (shape=(kheight,kwidth); both dimensions odd)
        :type numpy.ndarray
    :returns the convolved image (of the same shape as the input image)
    :rtype numpy.ndarray
    """
    # Your code here. You'll need to vectorise your implementation to ensure it runs # at a reasonable speed.
    kernel = np.flip(kernel)
    rows, cols = image.shape[:2]
    trows, tcols = kernel.shape
    tr, tc = trows//2, tcols//2

    if image.ndim == 2:
        channels = 1
        pimage = np.pad(image, ((tr, tr), (tc, tc))) # padded image
    else:
        channels = 3
        pimage = np.pad(image, ((tr, tr), (tc, tc), (0, 0))) # padded image
 
    cimage = np.zeros(image.shape)
   
    for ch in range(channels): 
        for x in range(0, cols):
            for y in range(0, rows):
                if channels == 1:
                    cimage[y, x] = (kernel * pimage[y:y+trows, x:x+tcols]).sum()
                else:
                    cimage[y, x, ch] = (kernel * pimage[y:y+trows, x:x+tcols, ch]).sum()

    return cimage