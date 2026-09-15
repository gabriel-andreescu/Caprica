Scriptname StructMembers extends MemberBase

Struct Entry
    Int Parent
    Int Self
EndStruct

Int Function Read(Entry value)
    Return value.parent + value.SELF
EndFunction

Function Write(Entry value)
    value.PARENT = 3
    value.self = 4
EndFunction

Function Increment(Entry value)
    value.Parent += 1
    value.Self += 1
EndFunction

Int Function Inherited()
    Return Parent.GetValue()
EndFunction

Int Function Current()
    Return Self.GetValue()
EndFunction
