from numpy import array, moveaxis, load
from PIL import Image
from torch import from_numpy
from torch.utils.data import Dataset


class SegmentationDataset(Dataset):
    def __init__(self, image_paths, mask_paths, size, num_classes, device):
        """
        Class extending the PyTorch Dataset class
        :param image_paths: list with paths to images
        :param mask_paths: list with paths to masks
        :param size: size to which the image is resized
        :param num_classes: number of classes to classify
        :param device: device on which the model is trained
        """
        self.image_paths = image_paths
        self.mask_paths = mask_paths
        self.size = size
        self.num_classes = num_classes
        self.device = device

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        # image = array(
                # Image.open(self.image_paths[idx]).resize((self.size, self.size),
                                                         # resample=Image.BILINEAR))
        image = load(self.image_paths[idx])
        image = image / 255
        # image = image[ : , : , :3]
        # mask = array(
                # Image.open(self.mask_paths[idx]).resize((self.size, self.size),
                                                        # resample=Image.NEAREST),
                # dtype='int')[:, :, 0]
        mask = load(self.mask_paths[idx])
        image = moveaxis(image, -1, 0)
        image = from_numpy(image).float().to(self.device)
        mask = moveaxis(mask, -1, 0)
        mask = from_numpy(mask).long().to(self.device)
        return image, mask