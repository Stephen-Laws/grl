# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffer

import flatbuffers

class EulerPoseParams(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEulerPoseParams(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EulerPoseParams()
        x.Init(buf, n + offset)
        return x

    # EulerPoseParams
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EulerPoseParams
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Vector3d import Vector3d
            obj = Vector3d()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # EulerPoseParams
    def Rotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .EulerRotation import EulerRotation
            obj = EulerRotation()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def EulerPoseParamsStart(builder): builder.StartObject(2)
def EulerPoseParamsAddPosition(builder, position): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def EulerPoseParamsAddRotation(builder, rotation): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(rotation), 0)
def EulerPoseParamsEnd(builder): return builder.EndObject()
