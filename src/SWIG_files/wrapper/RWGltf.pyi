from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *


class RWGltf_GltfPrimitiveMode(IntEnum):
	RWGltf_GltfPrimitiveMode_UNKNOWN: int = ...
	RWGltf_GltfPrimitiveMode_Points: int = ...
	RWGltf_GltfPrimitiveMode_Lines: int = ...
	RWGltf_GltfPrimitiveMode_LineLoop: int = ...
	RWGltf_GltfPrimitiveMode_LineStrip: int = ...
	RWGltf_GltfPrimitiveMode_Triangles: int = ...
	RWGltf_GltfPrimitiveMode_TriangleStrip: int = ...
	RWGltf_GltfPrimitiveMode_TriangleFan: int = ...
RWGltf_GltfPrimitiveMode_UNKNOWN = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_UNKNOWN
RWGltf_GltfPrimitiveMode_Points = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Points
RWGltf_GltfPrimitiveMode_Lines = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Lines
RWGltf_GltfPrimitiveMode_LineLoop = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineLoop
RWGltf_GltfPrimitiveMode_LineStrip = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_LineStrip
RWGltf_GltfPrimitiveMode_Triangles = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_Triangles
RWGltf_GltfPrimitiveMode_TriangleStrip = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleStrip
RWGltf_GltfPrimitiveMode_TriangleFan = RWGltf_GltfPrimitiveMode.RWGltf_GltfPrimitiveMode_TriangleFan

class RWGltf_GltfBufferViewTarget(IntEnum):
	RWGltf_GltfBufferViewTarget_UNKNOWN: int = ...
	RWGltf_GltfBufferViewTarget_ARRAY_BUFFER: int = ...
	RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER: int = ...
RWGltf_GltfBufferViewTarget_UNKNOWN = RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_UNKNOWN
RWGltf_GltfBufferViewTarget_ARRAY_BUFFER = RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ARRAY_BUFFER
RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER = RWGltf_GltfBufferViewTarget.RWGltf_GltfBufferViewTarget_ELEMENT_ARRAY_BUFFER

class RWGltf_GltfArrayType(IntEnum):
	RWGltf_GltfArrayType_UNKNOWN: int = ...
	RWGltf_GltfArrayType_Indices: int = ...
	RWGltf_GltfArrayType_Position: int = ...
	RWGltf_GltfArrayType_Normal: int = ...
	RWGltf_GltfArrayType_Color: int = ...
	RWGltf_GltfArrayType_TCoord0: int = ...
	RWGltf_GltfArrayType_TCoord1: int = ...
	RWGltf_GltfArrayType_Joint: int = ...
	RWGltf_GltfArrayType_Weight: int = ...
RWGltf_GltfArrayType_UNKNOWN = RWGltf_GltfArrayType.RWGltf_GltfArrayType_UNKNOWN
RWGltf_GltfArrayType_Indices = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Indices
RWGltf_GltfArrayType_Position = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Position
RWGltf_GltfArrayType_Normal = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Normal
RWGltf_GltfArrayType_Color = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Color
RWGltf_GltfArrayType_TCoord0 = RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord0
RWGltf_GltfArrayType_TCoord1 = RWGltf_GltfArrayType.RWGltf_GltfArrayType_TCoord1
RWGltf_GltfArrayType_Joint = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Joint
RWGltf_GltfArrayType_Weight = RWGltf_GltfArrayType.RWGltf_GltfArrayType_Weight

class RWGltf_GltfRootElement(IntEnum):
	RWGltf_GltfRootElement_Asset: int = ...
	RWGltf_GltfRootElement_Scenes: int = ...
	RWGltf_GltfRootElement_Scene: int = ...
	RWGltf_GltfRootElement_Nodes: int = ...
	RWGltf_GltfRootElement_Meshes: int = ...
	RWGltf_GltfRootElement_Accessors: int = ...
	RWGltf_GltfRootElement_BufferViews: int = ...
	RWGltf_GltfRootElement_Buffers: int = ...
	RWGltf_GltfRootElement_NB_MANDATORY: int = ...
	RWGltf_GltfRootElement_Animations: int = ...
	RWGltf_GltfRootElement_Materials: int = ...
	RWGltf_GltfRootElement_Programs: int = ...
	RWGltf_GltfRootElement_Samplers: int = ...
	RWGltf_GltfRootElement_Shaders: int = ...
	RWGltf_GltfRootElement_Skins: int = ...
	RWGltf_GltfRootElement_Techniques: int = ...
	RWGltf_GltfRootElement_Textures: int = ...
	RWGltf_GltfRootElement_Images: int = ...
	RWGltf_GltfRootElement_ExtensionsUsed: int = ...
	RWGltf_GltfRootElement_ExtensionsRequired: int = ...
	RWGltf_GltfRootElement_NB: int = ...
RWGltf_GltfRootElement_Asset = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Asset
RWGltf_GltfRootElement_Scenes = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scenes
RWGltf_GltfRootElement_Scene = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Scene
RWGltf_GltfRootElement_Nodes = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Nodes
RWGltf_GltfRootElement_Meshes = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Meshes
RWGltf_GltfRootElement_Accessors = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Accessors
RWGltf_GltfRootElement_BufferViews = RWGltf_GltfRootElement.RWGltf_GltfRootElement_BufferViews
RWGltf_GltfRootElement_Buffers = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Buffers
RWGltf_GltfRootElement_NB_MANDATORY = RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB_MANDATORY
RWGltf_GltfRootElement_Animations = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Animations
RWGltf_GltfRootElement_Materials = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Materials
RWGltf_GltfRootElement_Programs = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Programs
RWGltf_GltfRootElement_Samplers = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Samplers
RWGltf_GltfRootElement_Shaders = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Shaders
RWGltf_GltfRootElement_Skins = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Skins
RWGltf_GltfRootElement_Techniques = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Techniques
RWGltf_GltfRootElement_Textures = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Textures
RWGltf_GltfRootElement_Images = RWGltf_GltfRootElement.RWGltf_GltfRootElement_Images
RWGltf_GltfRootElement_ExtensionsUsed = RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsUsed
RWGltf_GltfRootElement_ExtensionsRequired = RWGltf_GltfRootElement.RWGltf_GltfRootElement_ExtensionsRequired
RWGltf_GltfRootElement_NB = RWGltf_GltfRootElement.RWGltf_GltfRootElement_NB

class RWGltf_GltfAccessorCompType(IntEnum):
	RWGltf_GltfAccessorCompType_UNKNOWN: int = ...
	RWGltf_GltfAccessorCompType_Int8: int = ...
	RWGltf_GltfAccessorCompType_UInt8: int = ...
	RWGltf_GltfAccessorCompType_Int16: int = ...
	RWGltf_GltfAccessorCompType_UInt16: int = ...
	RWGltf_GltfAccessorCompType_UInt32: int = ...
	RWGltf_GltfAccessorCompType_Float32: int = ...
RWGltf_GltfAccessorCompType_UNKNOWN = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UNKNOWN
RWGltf_GltfAccessorCompType_Int8 = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int8
RWGltf_GltfAccessorCompType_UInt8 = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt8
RWGltf_GltfAccessorCompType_Int16 = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Int16
RWGltf_GltfAccessorCompType_UInt16 = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt16
RWGltf_GltfAccessorCompType_UInt32 = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_UInt32
RWGltf_GltfAccessorCompType_Float32 = RWGltf_GltfAccessorCompType.RWGltf_GltfAccessorCompType_Float32

class RWGltf_GltfAccessorLayout(IntEnum):
	RWGltf_GltfAccessorLayout_UNKNOWN: int = ...
	RWGltf_GltfAccessorLayout_Scalar: int = ...
	RWGltf_GltfAccessorLayout_Vec2: int = ...
	RWGltf_GltfAccessorLayout_Vec3: int = ...
	RWGltf_GltfAccessorLayout_Vec4: int = ...
	RWGltf_GltfAccessorLayout_Mat2: int = ...
	RWGltf_GltfAccessorLayout_Mat3: int = ...
	RWGltf_GltfAccessorLayout_Mat4: int = ...
RWGltf_GltfAccessorLayout_UNKNOWN = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_UNKNOWN
RWGltf_GltfAccessorLayout_Scalar = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Scalar
RWGltf_GltfAccessorLayout_Vec2 = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec2
RWGltf_GltfAccessorLayout_Vec3 = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec3
RWGltf_GltfAccessorLayout_Vec4 = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Vec4
RWGltf_GltfAccessorLayout_Mat2 = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat2
RWGltf_GltfAccessorLayout_Mat3 = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat3
RWGltf_GltfAccessorLayout_Mat4 = RWGltf_GltfAccessorLayout.RWGltf_GltfAccessorLayout_Mat4

class RWGltf_GltfAccessor:
	def __init__(self) -> None: ...

class RWGltf_GltfBufferView:
	def __init__(self) -> None: ...

class RWGltf_GltfFace:
	pass

class RWGltf_GltfPrimArrayData:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theType: RWGltf_GltfArrayType) -> None: ...

class RWGltf_MaterialCommon(Standard_Transient):
	def __init__(self) -> None: ...

class RWGltf_MaterialMetallicRoughness(Standard_Transient):
	def __init__(self) -> None: ...

#classnotwrapped
class RWGltf_GltfSharedIStream: ...

#classnotwrapped
class RWGltf_TriangulationReader: ...

#classnotwrapped
class RWGltf_GltfLatePrimitiveArray: ...

#classnotwrapped
class RWGltf_PrimitiveArrayReader: ...

#classnotwrapped
class RWGltf_CafReader: ...

# harray1 classes
# harray2 classes
# hsequence classes

