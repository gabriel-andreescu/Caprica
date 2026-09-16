Scriptname LocalScopes

Int Function Pick(Bool condition) Global
    If condition
        Int value = 7
        Return value
    EndIf
    String value = "9"
    Return value as Int
EndFunction
