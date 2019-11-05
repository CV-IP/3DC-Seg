DAVIS_ROOT = '/globalwork/mahadevan/mywork/data/DAVIS17/DAVIS'
YOUTUBEVOS_ROOT = '/globalwork/data/youtube-vos/'
COCO_ROOT = '/globalwork/mahadevan/mywork/data/coco/'
network_models = {0:"RGMP", 1:"FeatureAgg3d", 2: "FeatureAgg3dMergeTemporal", 3: "FeatureAgg3dMulti",
                  4: "FeatureAgg3dMulti101", 5: "Resnet3d", 6: "Resnet3dPredictOne", 7: "Resnet3dMaskGuidance",
                  8: "SiamResnet3d", 9:"Resnet3dNonLocal", 10: "Resnet3dSimilarity", 11:"Resnet3dEmbeddingNetwork",
                  12: "Resnet3dSegmentEmbedding", 13: "Resnet3dSpatialEmbedding", 14: "Resnet3dEmbeddingMultiDecoder"}
#DAVIS_ROOT = '/disk2/data/DAVIS/'
PALETTE = [
  0, 0, 0,
  31, 119, 180,
  174, 199, 232,
  255, 127, 14,
  255, 187, 120,
  44, 160, 44,
  152, 223, 138,
  214, 39, 40,
  255, 152, 150,
  148, 103, 189,
  197, 176, 213,
  140, 86, 75,
  196, 156, 148,
  227, 119, 194,
  247, 182, 210,
  127, 127, 127,
  199, 199, 199,
  188, 189, 34,
  219, 219, 141,
  23, 190, 207,
  158, 218, 229
]


class font:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

