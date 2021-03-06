# Copyright (c) Youngwan Lee (ETRI) All Rights Reserved.
from .config import add_vovnet_config
from .vovnet import build_vovnet_fpn_backbone, build_vovnet_backbone
from .mobilenet import build_mobilenetv2_fpn_backbone, build_mnv2_backbone
from .shufflenet import build_shufflenetv2_x0_5_fpn_backbone, build_shufflenetv2_x1_0_fpn_backbone, build_shufflenetv2_x1_5_fpn_backbone
from .mobilenet_flgc import build_mobilenetv2_flgc_fpn_backbone
from .shufflenet_flgc import build_shufflenetv2_x1_0_flgc_fpn_backbone
from .hardnet import build_hardnet68_fpn_backbone
from .hardnet39 import build_hardnet39ds_fpn_backbone