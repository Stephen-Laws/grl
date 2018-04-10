# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffer

import flatbuffers

class ftkMarker(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsftkMarker(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ftkMarker()
        x.Init(buf, n + offset)
        return x

    # ftkMarker
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ftkMarker
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # ftkMarker
    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ftkMarker
    def GeometryID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ftkMarker
    def GeometryPresenceMask(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ftkMarker
    def GeometryPresenceMaskAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # ftkMarker
    def GeometryPresenceMaskLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ftkMarker
    def Transform(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .Pose import Pose
            obj = Pose()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def ftkMarkerStart(builder): builder.StartObject(5)
def ftkMarkerAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def ftkMarkerAddID(builder, ID): builder.PrependUint32Slot(1, ID, 0)
def ftkMarkerAddGeometryID(builder, geometryID): builder.PrependUint32Slot(2, geometryID, 0)
def ftkMarkerAddGeometryPresenceMask(builder, geometryPresenceMask): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(geometryPresenceMask), 0)
def ftkMarkerStartGeometryPresenceMaskVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ftkMarkerAddTransform(builder, transform): builder.PrependStructSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(transform), 0)
def ftkMarkerEnd(builder): return builder.EndObject()
