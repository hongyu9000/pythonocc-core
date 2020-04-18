from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class Image_Format(IntEnum):
	Image_Format_UNKNOWN: int = ...
	Image_Format_Gray: int = ...
	Image_Format_Alpha: int = ...
	Image_Format_RGB: int = ...
	Image_Format_BGR: int = ...
	Image_Format_RGB32: int = ...
	Image_Format_BGR32: int = ...
	Image_Format_RGBA: int = ...
	Image_Format_BGRA: int = ...
	Image_Format_GrayF: int = ...
	Image_Format_AlphaF: int = ...
	Image_Format_RGBF: int = ...
	Image_Format_BGRF: int = ...
	Image_Format_RGBAF: int = ...
	Image_Format_BGRAF: int = ...
Image_Format_UNKNOWN = Image_Format.Image_Format_UNKNOWN
Image_Format_Gray = Image_Format.Image_Format_Gray
Image_Format_Alpha = Image_Format.Image_Format_Alpha
Image_Format_RGB = Image_Format.Image_Format_RGB
Image_Format_BGR = Image_Format.Image_Format_BGR
Image_Format_RGB32 = Image_Format.Image_Format_RGB32
Image_Format_BGR32 = Image_Format.Image_Format_BGR32
Image_Format_RGBA = Image_Format.Image_Format_RGBA
Image_Format_BGRA = Image_Format.Image_Format_BGRA
Image_Format_GrayF = Image_Format.Image_Format_GrayF
Image_Format_AlphaF = Image_Format.Image_Format_AlphaF
Image_Format_RGBF = Image_Format.Image_Format_RGBF
Image_Format_BGRF = Image_Format.Image_Format_BGRF
Image_Format_RGBAF = Image_Format.Image_Format_RGBAF
Image_Format_BGRAF = Image_Format.Image_Format_BGRAF

#classnotwrapped
class Image_ColorRGB: ...

#classnotwrapped
class Image_ColorRGB32: ...

#classnotwrapped
class Image_ColorRGBA: ...

#classnotwrapped
class Image_ColorBGR: ...

#classnotwrapped
class Image_ColorBGR32: ...

#classnotwrapped
class Image_ColorBGRA: ...

#classnotwrapped
class Image_ColorRGBF: ...

#classnotwrapped
class Image_ColorBGRF: ...

#classnotwrapped
class Image_ColorRGBAF: ...

#classnotwrapped
class Image_ColorBGRAF: ...

#classnotwrapped
class Image_VideoParams: ...

#classnotwrapped
class Image_VideoRecorder: ...

#classnotwrapped
class Image_PixMapData: ...

#classnotwrapped
class Image_PixMapTypedData: ...

#classnotwrapped
class Image_PixMap: ...

#classnotwrapped
class Image_Texture: ...

#classnotwrapped
class Image_AlienPixMap: ...

#classnotwrapped
class Image_Diff: ...

# harray1 classes
# harray2 classes
# hsequence classes

