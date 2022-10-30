from pathlib import Path
from typing import Callable

from torch.utils.data import Dataset
from torchvision.datasets.folder import default_loader


class CarRacingDataset(Dataset):
    def __init__(self,
                 data_path: str,
                 split: str,
                 transform: Callable = None,
                 **kwargs):
        self.data_dir = Path(data_path)
        self.transforms = transform
        imgs = sorted(self.data_dir.glob("*.png"))
        self.imgs = imgs[:int(len(imgs) * 0.75)] if split == "train" else imgs[int(len(imgs) * 0.75):]
    
    def __len__(self):
        return len(self.imgs)
    
    def __getitem__(self, idx):
        img = default_loader(self.imgs[idx])
        
        if self.transforms is not None:
            img = self.transforms(img)
            
        return img, 0.0
