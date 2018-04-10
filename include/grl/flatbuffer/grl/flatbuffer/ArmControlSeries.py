# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffer

import flatbuffers

class ArmControlSeries(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsArmControlSeries(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArmControlSeries()
        x.Init(buf, n + offset)
        return x

    # ArmControlSeries
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArmControlSeries
    def States(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ArmControlState import ArmControlState
            obj = ArmControlState()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ArmControlSeries
    def StatesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArmControlSeriesStart(builder): builder.StartObject(1)
def ArmControlSeriesAddStates(builder, states): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(states), 0)
def ArmControlSeriesStartStatesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArmControlSeriesEnd(builder): return builder.EndObject()
